from __notification_utils import *
from datetime import datetime, timedelta
import os
import logging

def send_mail_attach(to_address, reply_to, subject, body, file_name_list):
    try:
        msg = MIMEMultipart()
        # storing the senders email address   
        msg['From'] = email_name
        msg['Subject'] = subject
        if reply_to is not None:
            msg['Cc'] = reply_to
            msg.add_header('reply-to',reply_to)
            to_address = to_address + [reply_to]
        # string to store the body of the mail 
        # attach the body with the msg instance 
        msg.attach(MIMEText(body, 'plain'))
        if len(file_name_list) != 0: 
            for file_name in file_name_list:
                if file_name is not None and os.path.isfile(file_name) == True:
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
        logging.info("Email send successfully")
        server.quit()
    except Exception as e:
        logging.info("Error sending mail - "+e)
        pass


if __name__ == "__main__":
    logging.basicConfig(filename='/var/log/atman/send_daily_email.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.getLogger()
    patient_register = createCsvPatientRegister()
    dietitian_register = createCsvDietitianRegister()
    appointments = createCsvAppointments()
    invites = createCsvInvites()
    if invites == []:
        file_name_invites = None
        logging.info("No Csv file created for today invites")
    else:
        file_name_invites = "/opt/atman/bin/invites_"+datetime.now().strftime("%d-%m-%Y")+".csv"
        logging.info("Created csv file for today's invites: " + file_name_invites)
    if appointments == []:
        file_name_appointments = None
        logging.info("No Csv file created for today appointments")
    else:
        file_name_appointments = "/opt/atman/bin/appointments_"+datetime.now().strftime("%d-%m-%Y")+".csv"
        logging.info("Created csv file for today's appointments: " + file_name_appointments)
    if patient_register == []:
        file_name_patients = None
        logging.info("No Csv file created for today patient registration")
    else:
        file_name_patients = "/opt/atman/bin/patient_register_"+datetime.now().strftime("%d-%m-%Y")+".csv"
        logging.info("Created csv file for today's patient registeration: " + file_name_patients)

    if dietitian_register == []:
        file_name_dietitian = None
        logging.info("No Csv file created for today dietitian registration")
    else:
        file_name_dietitian = "/opt/atman/bin/dietitian_register_"+datetime.now().strftime("%d-%m-%Y")+".csv" 
        logging.info("Created csv file for today's dietitian registeration: " + file_name_dietitian)
   
    file_name_blockchain = "/opt/atman/bin/blockchain_info_"+datetime.today().strftime("%Y%m%d")+".csv"
    file_name_list = [file_name_blockchain, file_name_appointments, file_name_patients, file_name_dietitian, file_name_invites] 
    logging.info("Files to be send: "+ str(file_name_list))
    subject = "Blockchain - Patient Data Insertion, Appointments, Patients, Dietitian registration, Invites for " + datetime.today().strftime("%d-%m-%Y")
    body = "Hi, \n\nKindly PFA the blockchain patient data insertion, appointments, patients, invites and dietitian registration for " + datetime.today().strftime("%d-%m-%Y") + ".\n\nThanks,\nTeam Pranacare." 
    #body_not_updated = "Hi, \n\nNo Blockchain Insertion or Update for "+(datetime.today() - timedelta(days=1)).strftime("%d-%m-%Y")+". \n\nThanks,\nTeam Pranacare."
    to_addr = ["vivek.vishwakarma@isanasystems.com", "pankaj.nirale@isanasystems.com", "adhir.potdar@isanasystems.com", "indraneel.bobde@isanasystems.com"]
    send_mail_attach(to_addr, None, subject, body, file_name_list)
    logging.info("=============================================================================================")

