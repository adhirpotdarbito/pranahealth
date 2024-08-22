import logging
import smtplib
import time
import base64
import os
import boto3
import calendar
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime,timedelta
from __config import *
from __db_config import *
import csv


init_db()
db = get_db()

# Function to send mail
def send_mail(to_address, reply_to, subject, body, file_name=None, parameter=None):
    try:
        msg = MIMEMultipart()
        # storing the senders email address   
        msg['From'] = email_name
        msg['Subject'] = subject
        if parameter is not None:
            msg['Cc'] = reply_to
            to_address = to_address + [reply_to]
        if reply_to is not None:
            #msg['Cc'] = reply_to
            msg.add_header('reply-to',reply_to)
            #to_address = to_address + [reply_to]
        # string to store the body of the mail 
        # attach the body with the msg instance 
        if body.find("<br>") >= 1 or body.find("<a href") >= 1:
            msg.attach(MIMEText(body, 'html'))
        else:
            msg.attach(MIMEText(body, 'plain'))
        if file_name is not None:
            filename = file_name
            attachment = open(filename, "rb")
            # instance of MIMEBase and named as p 
            p = MIMEBase('application', 'octet-stream')
            # To change the payload into encoded form 
            p.set_payload((attachment).read())
            # encode into base64 
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(filename))
            # attach the instance 'p' to instance 'msg' 
            msg.attach(p)
        # creates SMTP session 
        server = smtplib.SMTP(email_host, email_port)
        # start TLS for security 
        server.starttls()
        # Authentication 
        server.login(email_name, email_password)
        # Converts the Multipart msg into a string 
        text = msg.as_string()
        # sending the mail 
        server.sendmail(email_name, to_address, text)
        print("Email send successfully")
        server.quit()
    except Exception as e:
        logging.info("Error in sending mail - " + e)
        print e
        pass



def upload_file_to_s3(file_path, dietitian_email, patient_email, notification_type):
    AWS_ACCESS_KEY_ID = getAtmanConfigParamValue("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = getAtmanConfigParamValue("AWS_SECRET_ACCESS_KEY")
    AWS_BUCKET_NAME = getAtmanConfigParamValue("AWS_BUCKET_NAME")
    if file_path is None:
        raise ValueError("Please enter a valid and complete file path")

    session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY,)
    s3 = session.resource('s3')
    data = open(os.path.normpath(file_path), 'rb')
    if notification_type == "food_prescription":
        file_basename = "images/Food_Prescription/"+dietitian_email+"/"+patient_email+"/"+os.path.basename(file_path).replace(' ','')
    elif notification_type == "pathology_prescription":
        file_basename = "images/Pathology_Prescription/"+dietitian_email+"/"+patient_email+"/"+os.path.basename(file_path).replace(' ','')
    else:
        file_basename = "images/Biochemical/"+dietitian_email+"/"+patient_email+"/"+os.path.basename(file_path).replace(' ','')
    s3.Bucket(AWS_BUCKET_NAME).put_object(Key=file_basename, Body=data, ContentType="application/pdf")
    #print ("uploaded to s3")
    url = "https://%s.s3-ap-southeast-1.amazonaws.com/%s" % (AWS_BUCKET_NAME, file_basename)
    return url

def getWellnessContact(email):
    cursor = db.cursor()  
    query = "SELECT contact FROM users WHERE email='%s'"%(email)
    cursor.execute(query)
    get_contact = cursor.fetchone()[0]
    return get_contact
    
def convertFileToBase64(file_path):
    with open(file_path, "rb") as f:
        _file = f.read() 
        encoded_string = base64.b64encode(_file)
        return encoded_string

def getPatientId(email):
    patient_id_list = []
    for mail_id in email:
        cursor = db.cursor()
        query = "SELECT id FROM users where email='%s'"%(mail_id)
        cursor.execute(query)
        get_id = cursor.fetchone()[0]
        patient_id_list.append(get_id)
    return patient_id_list

def getAdminArea(db, admin_id, date, time_slot):
    admin_slot_list = []
    admin_area = None
    admin_city = None
    cursor = db.cursor()
    query = "SELECT start_time, end_time, start_date, end_date, admin_available_days, area, city FROM admin_time_granularity WHERE admin_id=%d"%(int(admin_id))
    cursor.execute(query)
    get_data = cursor.fetchone()
    day_new = datetime.strptime(str(date), '%Y%m%d').weekday()
    _day_new = calendar.day_name[day_new]
    while get_data is not None:
        admin_data_dict = {}
        admin_data_dict["start_time"] = get_data[0]
        admin_data_dict["end_time"] = get_data[1]  
        admin_data_dict["start_date"] = get_data[2]  
        admin_data_dict["end_date"] = get_data[3]  
        admin_data_dict["days"] = get_data[4]  
        admin_data_dict["area"] = get_data[5]  
        admin_data_dict["city"] = get_data[6]  
        admin_slot_list.append(admin_data_dict)
        get_data = cursor.fetchone()
    for admin_slot in admin_slot_list:
        if int(date) >= int(admin_slot.get("start_date")) and int(date) <= int(admin_slot.get("end_date")):
            if time_slot >= admin_slot.get("start_time") and time_slot <= admin_slot.get("end_time"):
               available_days = admin_slot.get("days", None) 
               if available_days not in [None, "", " "]:
                   if _day_new in available_days.split(","):
                       #print _day_new
                       admin_area = admin_slot.get("area", None)
                       admin_city = admin_slot.get("city", None) 
                       break
               else:
                   admin_area = None
                   admin_city = admin_slot.get("city", None)
    if (admin_area != None and admin_city != None) or (admin_area != "" and admin_city != ""):
        query_2 = "SELECT address FROM admin_areas WHERE admin_id=%d and area = '%s' and city = '%s' and country = 'India'"%(int(admin_id), admin_area, admin_city)
        cursor = db.cursor()
        cursor.execute(query_2)
        get_data = cursor.fetchone()
        if get_data == None:
            _get_data = None
        else:
            _get_data = get_data[0]
        return _get_data, admin_area, admin_city
    else:
        return None, admin_area, admin_city
    
def insertNotificationActivity(admin_id, patient_id, notification, notification_type, text):
    try:
        cursor = db.cursor()
        query = "INSERT INTO notification_activity_log(admin_id, patient_id, notification, notification_type, text) VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(query,(int(admin_id), int(patient_id), str(notification), str(notification_type), text))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    

def getTargetAudience(role):
    # get table data
    query = "SELECT email FROM users where role='%s'"%(role)
    cursor = db.cursor()
    cursor.execute(query)
    get_email = cursor.fetchone()
    list_aud = []
    while get_email is not None:
        list_aud.append(get_email[0])
        get_email = cursor.fetchone()
    close_db()
    return list_aud


def getPatientFirstAppointment():
    patient_data_list = []
    template_data = []
    query = "SELECT patient_id, admin_id FROM patient_appointments WHERE status='booked' AND date=%d GROUP BY patient_id HAVING COUNT(date)=1"%(int((datetime.now() - timedelta(days=7)).strftime("%Y%m%d")))
    cursor = db.cursor()
    cursor.execute(query) 
    get_data = cursor.fetchone()
    while get_data is not None:  
        patient_data_dict = {}
        patient_data_dict["patient_id"] = get_data[0]
        patient_data_dict["admin_id"] = get_data[1]
        patient_data_list.append(patient_data_dict)
        get_data = cursor.fetchone()
    for i in range(len(patient_data_list)):
        patient_id = patient_data_list[i].get("patient_id")  
        admin_id = patient_data_list[i].get("admin_id")
        query_1 = "SELECT name, email, contact from users WHERE id=%d"%(int(patient_id))  
        cursor.execute(query_1)
        get_patient_data = cursor.fetchone()
        patient_name = get_patient_data[0]
        patient_email = get_patient_data[1]
        patient_whatsapp = get_patient_data[2]
        query_2 = "SELECT name, email, contact from users WHERE id=%d"%(int(admin_id))  
        cursor.execute(query_2)
        get_admin_data = cursor.fetchone()
        admin_name = get_admin_data[0]
        admin_email = get_admin_data[1]
        admin_contact = get_admin_data[2]
        template = {"admin_name":admin_name, "admin_email":admin_email, "admin_contact":admin_contact, "patient_name":patient_name, "patient_email":patient_email, "patient_whatsapp":patient_whatsapp, "admin_id":admin_id, "patient_id":patient_id}
        template_data.append(template)
    close_db()
    return template_data 
    

def getPatientAppointment():
    # get table data
    patient_app = []
    template_data = []
    cursor = db.cursor()
    query = "select admin_id, patient_id, date, time_slot, meeting_url FROM patient_appointments WHERE date=%d AND status='booked'"%(int(datetime.now().strftime("%Y%m%d")))
    cursor.execute(query)
    get_app = cursor.fetchone()
    while get_app is not None:
        patient_app.append(get_app)
        get_app = cursor.fetchone()
    if len(patient_app) == 0:
        return template_data 
    for i in range(len(patient_app)):
        admin_id = patient_app[i][0]
        patient_id = patient_app[i][1]
        query = "select name, email, contact from users where id=%d"%(admin_id)
        query_1 = "select name, email, contact from users where id=%d"%(patient_id)
        cursor.execute(query)
        get_name = cursor.fetchone()
        admin_name = get_name[0]
        admin_email = get_name[1]
        admin_number = get_name[2]
        cursor.execute(query_1)
        get_name = cursor.fetchone()
        patient_name = get_name[0]
        patient_email = get_name[1]
        patient_whatsapp = get_name[2]
        template = {"admin_name" : admin_name, "admin_email" : admin_email, "patient_name": patient_name, "patient_email": patient_email, "time_slot": patient_app[i][3], "date": patient_app[i][2], "meeting_url": patient_app[i][4], "patient_whatsapp" : patient_whatsapp, "admin_id" : admin_id, "patient_id" : patient_id, "admin_contact":admin_number}
        template_data.append(template)
    close_db()
    return template_data

def getPatientAppointmentHourly():
    # get table data
    patient_app = []
    template_data = []
    cursor = db.cursor()
    time_str = time.strftime("%H%M", time.localtime())
    query = "select admin_id, patient_id, date, time_slot FROM patient_appointments WHERE date=%d AND status='booked' AND time_slot BETWEEN '%s' AND '%s'"%(int((datetime.now().strftime("%Y%m%d"))), str(int(time_str)+100), str(int(time_str)+159))
    cursor.execute(query)
    get_app = cursor.fetchone()
    while get_app is not None:
        patient_app.append(get_app)
        get_app = cursor.fetchone()
    if len(patient_app) == 0:
        return template_data
    for i in range(len(patient_app)):
        admin_id = patient_app[i][0]
        patient_id = patient_app[i][1]
        query = "select name, email from users where id=%d"%(admin_id)
        query_1 = "select name, email, contact from users where id=%d"%(patient_id)
        cursor.execute(query)
        get_name = cursor.fetchone()
        admin_name = get_name[0]
        admin_email = get_name[1]
        cursor.execute(query_1)
        get_name = cursor.fetchone()
        patient_name = get_name[0]
        patient_email = get_name[1]
        patient_whatsapp = get_name[2]
        template = {"admin_name" : admin_name, "admin_email" : admin_email, "patient_name": patient_name, "patient_email": patient_email, "time_slot": patient_app[i][3], "date": patient_app[i][2], "patient_whatsapp":patient_whatsapp, "admin_id":admin_id, "patient_id":patient_id}
        template_data.append(template)
    close_db()
    return template_data


def getDietitonAppointmentList():
    patient_app = []
    cursor = db.cursor()
    query = "SELECT DISTINCT(admin_id), u.email, u.contact, u.name FROM users u, patient_appointments p WHERE u.id=p.admin_id AND u.role in ('DIETITION_ACL', 'DIETITION_MIN_ROLE') AND p.date=%d"%(int(datetime.now().strftime("%Y%m%d"))) 
    cursor.execute(query)
    get_data = cursor.fetchone()
    while get_data is not None:
        patient_app.append(get_data)
        get_data = cursor.fetchone()
    return patient_app
        
                                     
def getDietitonPatientAppointment():
    diet_list = getDietitonAppointmentList()
    template_data = []
    if len(diet_list) == 0: 
        return template_data
    for i in range(len(diet_list)):
        patient_data = []
        admin_id = diet_list[i][0]         
        email = diet_list[i][1]
        number = diet_list[i][2]
        name = diet_list[i][3]
        query = "select u.name, p.time_slot, u.contact, u.email from users u, patient_appointments p where u.id=p.patient_id and p.admin_id=%d and p.date=%d and p.status='booked' order by p.time_slot"%(admin_id, int(datetime.now().strftime("%Y%m%d")))
        cursor = db.cursor()
        cursor.execute(query)
        get_data = cursor.fetchone()
        while get_data is not None:
            patient_name = get_data[0]
            if get_data[0] == None:
                patient_name = get_data[2]
                if patient_name == None:
                    patient_name = get_data[3]
            get_data_list = list(get_data)
            get_data_list[0] = patient_name
            get_data = tuple(get_data_list)
            patient_data.append(get_data[0:2]) 
            get_data = cursor.fetchone()
        template = {"dietitian_email" : email, "patient_data" : patient_data, "dietitian_number": number, "dietitian_name": name} 
        template_data.append(template)
    return template_data        
      

def deleteAppointment():
    try:
        query = "DELETE FROM patient_appointments WHERE status='requested' and date=%d"%(int((datetime.now() + timedelta(days=1)).strftime("%Y%m%d"))) 
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()
        if db.commit() is not None:
            print ("Requested Appointed Deleted")
    except Exception as err:
        #print err
        db.rollback()

def createCsvBlockchainInfo(file_name, wellness_id, patient_id, asset, mode, timestamp):
    try:
        file_exists = os.path.isfile(file_name)
        with open(file_name, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=["Dietition Name", "Patient", "Asset Name","Date Time", "Mode"])
            if not file_exists:
                writer.writeheader()
            fields = {"Dietition Name" : wellness_id, "Patient": "patient_"+str(patient_id), "Asset Name":asset, "Date Time": timestamp, "Mode":mode}
            logging.info(fields)
            logging.info(file_name)
            logging.info("Writing rows- wellness_name: "+ wellness_id + ", asset name "+asset+" and mode: "+mode)
            writer.writerow(fields)
            logging.info("Wrote rows Successful")
    except Exception as err:
        logging.info(err)
        logging.info("Wrote rows Unsuccessful")
        print err

def createCsvPatientRegister():
    try:
        query = "SELECT u.name, a.patient_id, a.admin_id, a.patient_type, u.gender, a.timestamp FROM users u, admin_patient_mapping a WHERE u.id = a.patient_id AND a.timestamp BETWEEN '%s' AND '%s'"%((datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d 18:30:00"), datetime.now().strftime("%Y-%m-%d 18:30:00"))
        #query = "SELECT u.name, a.patient_id, a.admin_id, a.patient_type,u.gender, a.timestamp FROM users u, admin_patient_mapping a WHERE u.id = a.patient_id AND a.timestamp BETWEEN '2020-01-01 00:00:00' AND '2020-01-01 23:59:59'"
        cursor = db.cursor()
        cursor.execute(query)
        get_data =cursor.fetchone()
        patient_register_list = []
        while get_data is not None:
            admin_id = get_data[2]
            query = "SELECT name from users where id=%d"%(admin_id)
            cursor_1 = db.cursor()
            cursor_1.execute(query)
            get_name = cursor_1.fetchone()[0]
            patient_register_dict = {"admin_name":get_name,"patient_id": str(get_data[1]), "patient_category":get_data[3], "patient_gender":get_data[4], "date":get_data[5].strftime("%Y%m%d %H:%M:%S")}
            patient_register_list.append(patient_register_dict)
            get_data = cursor.fetchone()      

        if patient_register_list == []:
            return patient_register_list

        for patient_register in patient_register_list:
            file_name = "/opt/atman/bin/patient_register_"+datetime.now().strftime("%d-%m-%Y")+".csv"
            file_exists = os.path.isfile(file_name)
            with open(file_name, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, delimiter=',',fieldnames=["Dietitan Name", "Patient", "Patient Category","Patient Gender","Date"])
                if not file_exists: 
                    writer.writeheader()
                fields = {"Dietitan Name":patient_register.get("admin_name", ""), "Patient":"patient_" + patient_register.get("patient_id",""), "Patient Category": patient_register.get("patient_category",""), "Patient Gender": patient_register.get("patient_gender",""), "Date":patient_register.get("date", "")} 
                logging.info("Writing rows to patient registration csv file- wellness_name: "+ patient_register.get("admin_name", "")  + ", patient id: "+"patient_" + patient_register.get("patient_id","")+", patient_gender: "+ patient_register.get("patient_gender","") +", date: "+ patient_register.get("date", ""))
                writer.writerow(fields)
                logging.info("Wrote Csv Successfully")
        return 0
    except Exception as err:
        logging.info("Wrote Csv Unsuccessful")
        print(err)
        logging.info(err)

def createCsvDietitianRegister():
    try:
        query = "SELECT name, email, city, gender, timestamp FROM users WHERE role in ('DIETITION_ACL', 'DIETITION_MIN_ROLE') and timestamp BETWEEN '%s' AND '%s'"%((datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d 18:30:00"), datetime.now().strftime("%Y-%m-%d 18:30:00"))
        cursor = db.cursor()
        cursor.execute(query)
        get_data = cursor.fetchone()
        dietitian_register_list = []
        while get_data is not None:
            dietitian_register_dict = {"dietitian_name":get_data[0], "dietitian_email":get_data[1], "city":get_data[2], "gender": get_data[3], "date":get_data[4]}
            dietitian_register_list.append(dietitian_register_dict)
            get_data = cursor.fetchone()

        if len(dietitian_register_list) == 0:
           return dietitian_register_list 

        for dietitian_register in dietitian_register_list:
            file_name = "/opt/atman/bin/dietitian_register_"+datetime.now().strftime("%d-%m-%Y")+".csv"
            file_exists = os.path.isfile(file_name)
            with open(file_name, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, delimiter=',',fieldnames=["Dietitan Name", "Email", "City","Gender","Date"])
                if not file_exists:
                    writer.writeheader()
                fields = {"Dietitan Name":dietitian_register.get("dietitian_name",""), "Email":dietitian_register.get("dietitian_email",""), "City":dietitian_register.get("city",""), "Gender":dietitian_register.get("gender",""), "Date":dietitian_register.get("date","")}   
                logging.info("Writing rows to dieitian registartion csv file- wellness_name: "+ dietitian_register.get("dietitian_name","")+ ", wellness_email: "+dietitian_register.get("dietitian_email","") + ", city: " + dietitian_register.get("city","") + ", gender: " + dietitian_register.get("gender","") + ", date: "+ str(dietitian_register.get("date","")))
                writer.writerow(fields)
                logging.info("Wrote csv successfully")

        return 0
    except Exception as err:
        logging.info("Wrote Csv Unsuccessful")
        print (err)        
        logging.info(err)

def createCsvAppointments():
    try:
        query = "SELECT a.admin_id, u.id, u.email, u.contact, a.date, a.time_slot, a.status FROM users u, patient_appointments a WHERE last_reminder_timestamp BETWEEN '%s' AND '%s' and u.id=a.patient_id"%((datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d 18:30:00"), datetime.now().strftime("%Y-%m-%d 18:30:00"))
        cursor = db.cursor()
        cursor.execute(query)
        get_data = cursor.fetchone()
        appointments_list = []
        while get_data is not None:
            admin_id = get_data[0]
            query = "SELECT name from users where id=%d"%(int(admin_id))
            cursor_1 = db.cursor()
            cursor_1.execute(query)
            get_name = cursor_1.fetchone()[0]
            appointment_dict = {"patient_id":get_data[1], "admin_name":get_name, "date":get_data[4], "time_slot":get_data[5], "status":get_data[6]} 
            appointments_list.append(appointment_dict)
            get_data = cursor.fetchone()

        if len(appointments_list) == 0:
            return appointments_list

        for appointments in appointments_list:
            file_name = "/opt/atman/bin/appointments_"+datetime.now().strftime("%d-%m-%Y")+".csv"

            file_exists = os.path.isfile(file_name)
            with open(file_name, 'a') as csvfile:
                logging.info("Appending to file: " + file_name)
                writer = csv.DictWriter(csvfile, delimiter=',',fieldnames=["Patient", "Dietitian Name", "Appointment Date", "Time Slot", "Status"])
                if not file_exists:
                    writer.writeheader()
                fields = {"Patient":"patient_" + str(appointments.get("patient_id", "")), "Dietitian Name":appointments.get("admin_name",""), "Appointment Date":appointments.get("date",""), "Time Slot": appointments.get("time_slot",""), "Status":appointments.get("status","")}
                logging.info("Writing rows daily appointment csv file- patient: "+ str(appointments.get("patient_id", ""))  + ",dietitan: " + appointments.get("admin_name","") + ",date: "+ str(appointments.get("date","")) + ", time slot: " + appointments.get("time_slot","") + ",status: "+appointments.get("status",""))
                writer.writerow(fields)
                logging.info("Wrote Csv Successfully")

        return 0 
    except Exception as err:
        logging.info("Wrote Csv Unsuccessful")
        print err

def createCsvInvites():
    try:
        query = "select wei.admin_id, u.name, u.role, wei.member_name, wei.member_type, wei.invite_status, wei.timestamp, wei.member_details from wellness_expert_invitation wei, users u where wei.admin_id = u.id and wei.timestamp BETWEEN '%s' AND '%s'"%((datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d 18:30:00"), datetime.now().strftime("%Y-%m-%d 18:30:00"))
        cursor = db.cursor()
        cursor.execute(query)
        get_data = cursor.fetchone()
        invites_list = []
        while get_data is not None:
            member_details = json.loads(unicode(get_data[7], errors='ignore'))
            invite_dict = {"expert_name":get_data[1], "member_name":get_data[3], "member_type":get_data[4], "invite_status":get_data[5], "member_contact":member_details.get("contact", ""), "member_email":member_details.get("email", ""), "member_city":member_details.get("city", ""), "member_gender":member_details.get("gender", "")}
            invites_list.append(invite_dict)
            get_data = cursor.fetchone()

        if len(invites_list) == 0:
            return invites_list

        file_name = "/opt/atman/bin/invites_"+datetime.now().strftime("%d-%m-%Y")+".csv"
        logging.info("Writing to CSV file: " + file_name)

        keys = invites_list[0].keys()
        with open(file_name, 'wb') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys, delimiter=',')
            writer.writeheader()
            writer.writerows(invites_list)
            logging.info("Wrote Csv Successfully")

        return 0 
    except Exception as err:
        logging.info("Wrote Csv Unsuccessful")
        print err

def getDailyPatientAppointmentTemplate():
    try:
        query = "select note_tag, note_json, note_param_json,type from notification_templates where template_name='Appointment Reminder'"
        cursor = db.cursor()
        cursor.execute(query)       
        get_data = cursor.fetchone()
        appointment_reminder_template = []
        while get_data is not None:
            appointment_template_dict = {"message_type": get_data[3], "messageJson": get_data[1], "paramJson" : get_data[2]} 
            appointment_reminder_template.append(appointment_template_dict)
            get_data = cursor.fetchone()
        return appointment_reminder_template
    except Exception as err:
        print err



def insertAuditTrail(user_id, user_role, session_id, access_type, parameters, message):
    try:
        cursor = db.cursor()
        query = 'INSERT INTO user_access_audit_trail(user_id, user_role, session_id, access_type, parameters, message) VALUES(%s, %s, %s, %s, %s, %s)'
        cursor.execute(query, (int(user_id), user_role, session_id, access_type, parameters, message)) 
        db.commit()
    except Exception as err:
        print ("Error in insertAuditTrail " + err)
        db.rollback()
