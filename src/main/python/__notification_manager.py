'''
  
    Copyright (C) 2018-2020 Isana Systems India Private Limited

    This source code is owned and maintained by Isana Systems India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of Isana Systems India Private Limited.

'''

import logging
from __message_queue import *
import urllib
from __user_queue_data import *
from __config import *
from __notification_manager import *
from __notification_utils import *
from __whatsapp_config import *

class NotificationManager(QueueData):
    def __init__(self):
        super(NotificationManager, self).__init__()
        subject = None
        body = None
        return None
 
    def callback(self, ch, method, properties, body):
        print (body)
        self.processingFunction(body)

    def processingFunction(self, message_recieved):
        # create notification 
        try:
            logging.basicConfig(filename='/var/log/atman/notification_appointment.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
            logging.getLogger()
            message_notification = {}
            logging.info("Message Received in function: " + message_recieved)
            notification_type = json.loads(message_recieved).get("parameter_type", "") 
            logging.info("Notification Type in function: " + notification_type)
            message_recieved_dict = json.loads(message_recieved).get("message", {}) 
            message_template = message_recieved_dict.get("message_template", [])
            message_template_parameters = message_recieved_dict.get("message_template_parameter", [])
            template_file = getJsonTemplate()
            token_file = getTokenTemplate()
            instance_id = token_file.get("instance_id_pranacare", "")
            token = token_file.get("token_pranacare", "")
            header, url, data =  getSendMessageTemplate(template_file)
            _header = json.loads(header)
            _url = url%(instance_id, token)
            notification_whatsapp = getAtmanConfigParamValue("NOTIFICATION_WHATSAPP")
            notification_email = getAtmanConfigParamValue("NOTIFICATION_EMAIL")
            _message_recieved = json.loads(message_recieved)
            message_type = _message_recieved.get("message", {}).get("messageType", "")
            deleteAppointment()
            if notification_type in [USER_REGISTER, CHANGE_MAIL, APPOINTMENT_BOOKED_PATIENT, APPOINTMENT_BOOKED_DIETITIAN, APPOINTMENT_REQUESTED_CONFIRMED, APPOINTMENT_REQUESTED_BOOKED, APPOINTMENT_REQUESTED_DIET, APPOINTMENT_REQUESTED_PATIENT, APPOINTMENT_UPDATED, APPOINTMENT_REMINDER_MAIL, APPOINTMENT_BOOKED_CANCELLED_PATIENT, APPOINTMENT_BOOKED_CANCELLED_DIET, APPOINTMENT_REQUESTED_CANCELLED_PATIENT,APPOINTMENT_REQUESTED_CANCELLED_DIET, ANONYMOUS_TOKEN, FORGET_PASSWORD, APPOINTMENT_COMPLETED, CREATE_USER_WELLNESS]:
                _message_recieved = json.loads(message_recieved)
                user_email_id = [json.loads(message_recieved).get("user_email_id","")]
                user_number = json.loads(message_recieved).get("user_phone_number", "")
                wellness_email_id = json.loads(message_recieved).get("wellness_email_id","") 
                wellness_number = json.loads(message_recieved).get("wellness_phone_number","")
                admin_id = json.loads(message_recieved).get("admin_id", 0)
                patient_id = json.loads(message_recieved).get("user_id", 0)
                _notification = notification_type
                message_type = _message_recieved.get("message", {}).get("messageType", "")
                if wellness_number == None:
                    wellness_number = "" 
                if notification_email == "1" and message_type == "email":
                    patient_name = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##patient_name##$$", "")
                    wellness_type = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##wellness_type##$$", "")
                    clinic_address = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##clinic_address##$$", "")
                    if patient_name == None:
                        patient_name = "User"
                    wellness_name = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##wellness_name##$$", "")
                    appointment_date = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##appointment_date##$$", "")
                    appointment_time = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##appointment_time##$$", "")
                    admin_link = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##admin_link##$$", "")
                    wellness_email = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##wellness_email##$$","")
                    message_body = str(json.loads(_message_recieved.get("message", {}).get("messageJson", {})).get("message", "")).replace("$$##patient_name##$$", patient_name).replace("$$##appointment_date##$$", appointment_date).replace("$$##appointment_time##$$", appointment_time).replace("$$##wellness_name##$$", wellness_name).replace("$$##user_email##$$", user_email_id[0]).replace("$$##admin_link##$$", admin_link).replace("$$##clinic_address##$$", clinic_address).replace("$$##admin_id##$$", str(admin_id)).replace("$$##wellness_type##$$", wellness_type).replace("$$##wellness_email##$$", wellness_email)
                    message_subject = str(json.loads(_message_recieved.get("message", {}).get("messageJson", {})).get("subject", "")).replace("$$##wellness_name##$$", wellness_name)
                    if notification_type in [APPOINTMENT_BOOKED_PATIENT, APPOINTMENT_BOOKED_DIETITIAN, APPOINTMENT_REQUESTED_BOOKED, APPOINTMENT_REMINDER_MAIL, APPOINTMENT_REQUESTED_CONFIRMED, APPOINTMENT_REQUESTED_DIET, APPOINTMENT_REQUESTED_PATIENT]:
                        map_link = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##map_link##$$", "")
                        clinic_address = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##clinic_address##$$", "")
                        message_body = str(json.loads(_message_recieved.get("message", {}).get("messageJson", {})).get("message", "")).replace("$$##patient_name##$$", patient_name).replace("$$##appointment_date##$$", appointment_date).replace("$$##appointment_time##$$", appointment_time).replace("$$##clinic_address##$$", clinic_address).replace("$$##map_link##$$", map_link).replace("$$##wellness_name##$$", wellness_name).replace("$$##admin_link##$$", admin_link)
                        message_subject = str(json.loads(_message_recieved.get("message", {}).get("messageJson", {})).get("subject", "")).replace("$$##wellness_name##$$", wellness_name)
                    if notification_type in [ANONYMOUS_TOKEN, FORGET_PASSWORD]:
                        otp_number = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##otp_number##$$", "")
                        message_body = str(json.loads(_message_recieved.get("message", {}).get("messageJson", {})).get("message", "")).replace("$$##otp_number##$$", otp_number).replace("$$##patient_name##$$", patient_name)
                        message_subject = str(json.loads(_message_recieved.get("message", {}).get("messageJson", {})).get("subject", "")).replace("$$##wellness_name##$$", wellness_name)
                    if notification_type in [CHANGE_MAIL, USER_REGISTER, APPOINTMENT_COMPLETED, CREATE_USER_WELLNESS]:
                        send_mail(user_email_id, wellness_email_id, message_subject, message_body, parameter=notification_type) 
                    else:
                        send_mail(user_email_id, wellness_email_id, message_subject, message_body)
                        insertNotificationActivity(admin_id, patient_id, _notification, "email", message_subject + "\n\n" + message_body)
                        logging.info(notification_type + ": Email send to " + str(user_email_id))
                if notification_whatsapp == "1" and message_type == "whatsapp":
                    patient_name = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##patient_name##$$", "")
                    wellness_type = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##wellness_type##$$", "")
                    if patient_name == None:
                        patient_name = "User"
                    wellness_name = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##wellness_name##$$", "")
                    appointment_date = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##appointment_date##$$", "")
                    appointment_time = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##appointment_time##$$", "")
                    admin_link = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##admin_link##$$", "")
                    clinic_address = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##clinic_address##$$", "")
                    wellness_email = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##wellness_email##$$","")
                    message_body_whatsapp = str(json.loads(_message_recieved.get("message", {}).get("messageJson", {})).get("message", "")).replace("$$##patient_name##$$", patient_name).replace("$$##appointment_date##$$", appointment_date).replace("$$##appointment_time##$$",appointment_time).replace("$$##wellness_name##$$", wellness_name).replace("$$##wellness_number##$$", wellness_number).replace("$$##admin_link##$$", admin_link).replace("$$##user_email##$$", user_email_id[0]).replace("$$##clinic_address##$$", clinic_address).replace("$$##admin_id##$$", str(admin_id)).replace("$$##wellness_type##$$",wellness_type).replace("$$##wellness_email##$$", wellness_email)
                    if notification_type in [APPOINTMENT_BOOKED_PATIENT, APPOINTMENT_BOOKED_DIETITIAN, APPOINTMENT_REQUESTED_BOOKED, APPOINTMENT_REMINDER_MAIL, APPOINTMENT_REQUESTED_CONFIRMED, APPOINTMENT_REQUESTED_DIET, APPOINTMENT_REQUESTED_PATIENT]:
                        map_link = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##map_link##$$", "")
                        clinic_address = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##clinic_address##$$", "")
                        message_body_whatsapp = str(json.loads(_message_recieved.get("message", {}).get("messageJson", '')).get("message", "")).replace("$$##patient_name##$$", patient_name).replace("$$##wellness_name##$$", wellness_name).replace("$$##appointment_date##$$", appointment_date).replace("$$##appointment_time##$$", appointment_time).replace("$$##clinic_address##$$", clinic_address).replace("$$##map_link##$$", map_link).replace("$$##wellness_number##$$", wellness_number).replace("$$##admin_link##$$", admin_link)
                    if notification_type in [ANONYMOUS_TOKEN, FORGET_PASSWORD]:
                        otp_number = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##otp_number##$$", "")
                        message_body_whatsapp = str(json.loads(_message_recieved.get("message", {}).get("messageJson", {})).get("message", "")).replace("$$##otp_number##$$", otp_number).replace("$$##patient_name##$$", patient_name)
                    if user_number not in [None, "NULL", "", " "] and wellness_number not in [None, "NULL", "", " "]:
                        if len(user_number) == 10:
                            user_number = "91"+ user_number
                        _data = data%(user_number, message_body_whatsapp.replace("&", "%26"))
                        logging.info(notification_type + ": Whatsapp sending to " + str(user_number))
                        sentMessage(_data, _url, _header)
                        insertNotificationActivity(admin_id, patient_id, _notification, "whatsapp", message_body_whatsapp)
                        #if notification_type == USER_REGISTER:
                           #header, url, data = getSendContactTemplate(template_file)
                           #_header = json.loads(header)
                           #_url = url%(instance_id, token) 
                           #_data = data%(user_number)
                           #sentMessage(_data, _url, _header)
                    
            if notification_type == GENERAL_REMINDER:
                dietitian_mail = json.loads(message_recieved).get("user_email_id", None) 
                target = message_recieved_dict.get("patientEmail", [])
                #subject = getPranaEmailParameters("SUBJECT_GENERAL_REMINDER")
                #body = getPranaEmailParameters("BODY_GENERAL_REMINDER")
                subject = message_recieved_dict.get("subject", "")
                body = message_recieved_dict.get("message").replace("&", "%26")
                target_whatsapp = message_recieved_dict.get("patientPhone", [])
                patient_id_lists = getPatientId(target) 
                admin_id = json.loads(message_recieved).get("admin_id", 0)
                wellness_number = json.loads(message_recieved).get("wellness_phone_number", "")
                _notification = notification_type
                if wellness_number == None:
                    wellness_number = ""
                if notification_email == "1":
                    send_mail(target, dietitian_mail, subject, body) 
                    logging.info(notification_type + ": Email send to " + str(target))
                    for patient_id in patient_id_lists: 
                        insertNotificationActivity(admin_id, patient_id, _notification, "email", subject + "\n\n" + body)
                if notification_whatsapp == "1":
                    body = body + "\n\nNote: This is a system generated messages, please DO NOT REPLY to this number. In case on any queries please contact your Wellness Expert on " + wellness_number + "." 
                    for number in target_whatsapp:
                        if number not in [None, "NULL", "", " "] and wellness_number not in [None, "NULL", "", " "]:
                            if len(number) == 10: 
                                number = "91"+number
                            _data = data%(number, body)
                            logging.info(notification_type + ": Whatsapp sending to " + str(number))
                            sentMessage(_data, _url, _header)
                    for patient_id in patient_id_lists:
                        insertNotificationActivity(admin_id, patient_id, _notification, "whatsapp", body)

            if notification_type == APPOINTMENT_REMINDER:
                target = message_recieved_dict.get("patientEmail", [])
                location = "https://www.google.com/maps/dir/?api=1&origin=&destination="
                if len(message_template_parameters) == 0:
                    return 0
                for parameter in message_template_parameters:
                    patient_name = parameter.get("patient_name", None)
                    if patient_name == None:
                        patient_name = "User"
                    admin_name = parameter.get("dietitian_name")
                    dietitian_mail = parameter.get("dietitian_mail")
                    admin_id = parameter.get("admin_id", 0)
                    time_slot = parameter.get("time")
                    date = str(parameter.get("date"))
                    admin_address = parameter.get("admin_address")
                    area = parameter.get("area")
                    city = parameter.get("city")
                    meeting_url = parameter.get("meeting_url")
                    if admin_address == None:
                        admin_address = ""
                    if area == None:
                        area = ""
                    if city == None:
                        city = ""
                    if meeting_url == None or meeting_url == "":
                        _area = area+", "+city
                    else:
                        _area = meeting_url
                    date_new = datetime.strptime(date, '%Y%m%d').strftime("%d-%b-%Y")
                    time = parameter.get("time")[:2] + ":" + parameter.get("time")[2:]
                    time_new = datetime.strptime(time, "%H:%M")
                    wellness_number = parameter.get("wellness_number","")
                    if wellness_number == None: 
                        wellness_number = "" 
                    admin_link = admin_name+" https://wellness.pranacare.co.in/ALL/ALL/"+ str(admin_id)
                    appointment_template = message_recieved_dict.get("notification_template")
                    for template in appointment_template:
                        if template.get("message_type") == 'email':
                            body_email = json.loads(template.get("messageJson", {})).get("message", {})
                            subject_email = json.loads(template.get("messageJson", {})).get("subject", {})
                        if template.get("message_type") == 'whatsapp':
                            body_whatsapp = json.loads(template.get("messageJson", {})).get("message", {}) 
                    if admin_address not in [None, ""]:
                        admin_address = admin_address.replace(" ","%2B")
                        google_location = location + admin_address
                        subject = subject_email.replace("$$##wellness_name##$$", admin_name)                                    
                        body_mail = body_email.replace("$$##patient_name##$$", patient_name).replace("$$##appointment_date##$$", date_new).replace("$$##appointment_time##$$", time_new.strftime("%I:%M %p")).replace("$$##clinic_address##$$", _area).replace("$$##map_link##$$", google_location).replace("$$##wellness_name##$$", admin_name).replace("$$##admin_link##$$", admin_link)
                        body_wh = body_whatsapp.replace("$$##patient_name##$$", patient_name).replace("$$##appointment_date##$$", date_new).replace("$$##appointment_time##$$",
time_new.strftime("%I:%M %p")).replace("$$##wellness_name##$$", admin_name).replace("$$##clinic_address##$$", _area).replace("$$##map_link##$$", google_location).replace("$$##wellness_number##$$", wellness_number).replace("$$##admin_link##$$", admin_link)
                    else:
                        subject = subject_email.replace("$$##wellness_name##$$", admin_name)                                    
                        body_mail = body_email.replace("$$##patient_name##$$", patient_name).replace("$$##appointment_date##$$", date_new).replace("$$##appointment_time##$$", time_new.strftime("%I:%M %p")).replace("$$##wellness_name##$$", admin_name).replace("$$##clinic_address##$$", _area).replace("$$##map_link##$$", "").replace("$$##admin_link##$$", admin_link)
                        body_wh = body_whatsapp.replace("$$##patient_name##$$",patient_name).replace("$$##appointment_date##$$", date_new).replace("$$##appointment_time##$$", time_new.strftime("%I:%M %p")).replace("$$##wellness_name##$$",admin_name).replace("$$##wellness_number##$$", wellness_number).replace("$$##clinic_address##$$", _area).replace("$$##map_link##$$", "").replace("$$##admin_link##$$", admin_link)
                    email = [parameter.get("patient_mail")]
                    number = parameter.get("patient_whatsapp")
                    patient_id = parameter.get("patient_id", 0)
                    _notification = notification_type
                    if notification_email == "1":
                        send_mail(email, dietitian_mail, subject, body_mail)
                        logging.info(notification_type + ": Email send to " + str(email))
                        insertNotificationActivity(admin_id, patient_id, _notification, "email", subject + "\n\n" + body_mail)
                    if notification_whatsapp == "1":
                        if number not in [None, "NULL", "", " "] and wellness_number not in [None, "NULL", "", " "]:
                            if len(number) == 10:
                                number = "91"+number
                            _data = data%(number, body_wh.replace("&", "%26"))                    
                            logging.info(notification_type + ": Whatsapp sending to " + str(number))
                            sentMessage(_data, _url, _header)
                            insertNotificationActivity(admin_id, patient_id, _notification, "whatsapp", body_wh)
                    print ("Appointment Notification sent to Patients - " + patient_name  + ": " + datetime.now().strftime("%d-%b-%Y %H:%M"))

            if notification_type == APPOINTMENT_REMINDER_DIETITIAN:
                subject = getPranaEmailParameters("SUBJECT_APPOINTMENT_DIETITIAN") + " " + datetime.now().strftime("%d-%b-%Y")
                admin_id = json.loads(message_recieved).get("admin_id", 0)
                patient_id = json.loads(message_recieved).get("user_id", 0)
                _notification = notification_type
                if len(message_template_parameters) == 0:
                    return 0
                for message in message_template_parameters:
                    i = 1
                    dietitian_email = [message.get("dietitian_mail")] 
                    dietitian_number = message.get("dietitian_contact")
                    dietitian_name = message.get("wellness_name")
                    string = ""
                    for key, value in message.get("patient_data"): 
                        time = value[:2] + ":" + value[2:]
                        time_new = datetime.strptime(time, "%H:%M").strftime("%I:%M %p")
                        string += str(i) + ". " +  key + ", at time:- " + time_new + "\n"
                        i+=1 
                    body = getPranaEmailParameters("BODY_DIETITIAN_REMINDER")%(dietitian_name, datetime.now().strftime("%d-%b-%Y"), string)
                    body_whatsapp = getPranaEmailParameters("BODY_DIETITIAN_REMINDER_WHATSAPP")%(dietitian_name, datetime.now().strftime("%d-%b-%Y"), string) 
                    if notification_email == "1":
                        send_mail(dietitian_email, None, subject, body)
                        logging.info(notification_type + ": Email send to " + str(dietitian_email))
                    if notification_whatsapp == "1":
                        if dietitian_number not in [None, "NULL", "", " "]:
                            if len(dietitian_number) == 10:
                                dietitian_number = "91"+dietitian_number
                                _data = data%(dietitian_number, body_whatsapp)
                                logging.info(notification_type + ": Whatsapp sending to " + str(dietitian_number))
                                sentMessage(_data, _url, _header)

            if notification_type == FOOD_PRESCRIPTION or notification_type == PATHOLOGY_PRESCRIPTION or notification_type == NOTIFICATION_BIOCHEMICAL or notification_type == CUSTOM_FORM_DATA:
                user_email_id = [json.loads(message_recieved).get("user_email_id","")]
                wellness_email_id = json.loads(message_recieved).get("wellness_email_id","")
                admin_id = json.loads(message_recieved).get("admin_id", 0)
                patient_id = json.loads(message_recieved).get("user_id", 0)
                user_number = json.loads(message_recieved).get("user_phone_number", "")
                _notification = notification_type
                _message_recieved = json.loads(message_recieved)
                patient_name = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##patient_name##$$", "")
                wellness_name = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##wellness_name##$$", "")
                wellness_number = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##wellness_number##$$", "")
                admin_link = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##admin_link##$$", "")
                section_name = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##section_name##$$", "")
                subsection_name = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##sub_section_name##$$", "")

                if wellness_number == None:
                    wellness_number = ""

                if _message_recieved.get("message", {}).get("messageType", "") == "email":
                    if notification_type == CUSTOM_FORM_DATA:
                        message_body = str(json.loads(_message_recieved.get("message", {}).get("messageJson", '')).get("message", "")).replace("$$##patient_name##$$", patient_name).replace("$$##wellness_name##$$", wellness_name).replace("$$##wellness_number##$$", wellness_number).replace("$$##admin_link##$$", admin_link).replace("$$##section_name##$$", section_name).replace("$$##sub_section_name##$$", subsection_name)
                        message_subject = json.loads(_message_recieved.get("message", {}).get("messageJson", '')).get("subject", "").replace("$$##wellness_name##$$", wellness_name).replace("$$##section_name##$$", section_name).replace("$$##sub_section_name##$$", subsection_name)
                    else:
                        message_body = str(json.loads(_message_recieved.get("message", {}).get("messageJson", '')).get("message", "")).replace("$$##patient_name##$$", patient_name).replace("$$##wellness_name##$$", wellness_name).replace("$$##wellness_number##$$", wellness_number).replace("$$##admin_link##$$", admin_link)
                        message_subject = json.loads(_message_recieved.get("message", {}).get("messageJson", '')).get("subject", "").replace("$$##wellness_name##$$", wellness_name)

                    flag = _message_recieved.get("message", {}).get("fileData", {}).get("flag", "")
                    file_path = _message_recieved.get("message", {}).get("fileData", {}).get("filepath", "")
                    if flag == flag_email:
                        if notification_email == "1":
                            send_mail(user_email_id, wellness_email_id, message_subject, message_body, file_name = file_path, parameter = notification_type)
                            logging.info(notification_type + ": Email send to " + str(user_email_id))
                            insertNotificationActivity(admin_id, patient_id, _notification, "email", message_subject + "\n\n" + message_body)
                if _message_recieved.get("message", {}).get("messageType", "") == "whatsapp": 
                    if notification_type == CUSTOM_FORM_DATA:
                        message_body = str(json.loads(_message_recieved.get("message", {}).get("messageJson", '')).get("message", "")).replace("$$##patient_name##$$", patient_name).replace("$$##wellness_name##$$", wellness_name).replace("$$##wellness_number##$$", wellness_number).replace("$$##admin_link##$$", admin_link).replace("$$##section_name##$$", section_name).replace("$$##sub_section_name##$$", subsection_name)
                    else:
                        message_body = str(json.loads(_message_recieved.get("message", {}).get("messageJson", '')).get("message", "")).replace("$$##patient_name##$$", patient_name).replace("$$##wellness_name##$$", wellness_name).replace("$$##wellness_number##$$", wellness_number).replace("$$##admin_link##$$", admin_link)

                    flag = _message_recieved.get("message", {}).get("fileData", {}).get("flag", "")
                    file_path = _message_recieved.get("message", {}).get("fileData", {}).get("filepath", "")
                    file_name = os.path.basename(file_path)
                    if flag == flag_whatsapp:
                        if notification_whatsapp == "1":
                            file_link = upload_file_to_s3(file_path, wellness_email_id, user_email_id[0], notification_type)
                            if user_number not in [None, "NULL", "", " "] and wellness_number not in [None, "NULL", "", " "]:
                                if len(user_number) == 10:
                                    user_number = "91"+user_number
                                    message_whatsapp = message_body
                                    _data = data%(user_number, message_whatsapp)
                                    sentMessage(_data, _url, _header)
                                    header, url, data = getSendFileTemplate(template_file) 
                                    _header = json.loads(header)
                                    _url = url%(instance_id, token)
                                    _data = data%(user_number, file_link, file_name, file_name)
                                    logging.info(notification_type + ": Whatsapp sending to " + str(user_number))
                                    sentMessage(_data, _url, _header)
                                    insertNotificationActivity(admin_id, patient_id, _notification, "whatsapp", message_whatsapp)
        
            if notification_type == PATIENT_ENQUIRY:            
                patient_appointment_data = message_recieved_dict.get("message_template", [])
                subject = getPranaEmailParameters("SUBJECT_PATIENT_ENQUIRY")
                if patient_appointment_data != []:
                    for _data in patient_appointment_data:
                        patient_name = _data.get("patient_name", "")
                        patient_email = [_data.get("patient_email", "")]
                        patient_contact = _data.get("patient_whatsapp", "") 
                        wellness_name = _data.get("admin_name","")
                        wellness_email = _data.get("admin_email", "")
                        wellness_contact = _data.get("admin_contact", "")
                        body = getPranaEmailParameters("BODY_PATIENT_ENQUIRY")%(patient_name, wellness_name)
                        if notification_email == "1":
                            send_mail(patient_email, wellness_email, subject, body)
                            logging.info(notification_type + ": Email send to " + str(patient_email))
                        if notification_whatsapp == "1":
                            if patient_contact not in [None, "NULL", "", " "]:
                                if len(patient_contact) == 10:
                                    patient_contact = "91"+patient_contact
                                _data = data%(patient_contact, body)                    
                                logging.info(notification_type + ": Whatsapp sending to " + str(patient_contact))
                                sentMessage(_data, _url, _header)
                        print ("Appointment Enquiry Notification sent to Patient - " + patient_name  + ": " + datetime.now().strftime("%d-%b-%Y %H:%M"))

            if notification_type in [PATIENT_REFER, PATIENT_REFER_ADMIN, PATIENT_REFER_MEMBER, WELLNESS_INVITATION, COLLABORATION_CONFIRM]:
                user_email_id = [json.loads(message_recieved).get("user_email_id","")]
                wellness_email_id = json.loads(message_recieved).get("wellness_email_id","")
                admin_id = json.loads(message_recieved).get("admin_id", 0)
                patient_id = json.loads(message_recieved).get("user_id", 0)
                member_id = json.loads(message_recieved).get("member_id", 0)
                user_number = json.loads(message_recieved).get("user_phone_number", "")
                wellness_number = json.loads(message_recieved).get("wellness_phone_number", "")
                _notification = notification_type
                patient_name = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##patient_name##$$", "")
                patient_number = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##patient_number##$$", "")
                wellness_name = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##wellness_name##$$", "")
                admin_name = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##admin_name##$$", "")
                member_name = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##member_name##$$", "")
                member_type = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##member_type##$$", "")
                wellness_type = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##wellness_type##$$", "")
                member_link = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##member_link##$$", "")
                admin_link = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##admin_link##$$", "")
                member_number = _message_recieved.get("message", {}).get("paramJson", {}).get("$$##member_number##$$", "")
                invite_id = str(_message_recieved.get("message", {}).get("paramJson", {}).get("$$##invite_id##$$", ""))
                if wellness_number == None:
                    wellness_number = ""
                if notification_email == "1" and message_type == "email":
                    message_body = str(json.loads(_message_recieved.get("message", {}).get("messageJson", {})).get("message", "")).replace("$$##patient_name##$$", patient_name).replace("$$##member_name##$$", member_name).replace("$$##wellness_name##$$", wellness_name).replace("$$##member_type##$$", member_type).replace("$$##member_number##$$", member_number).replace("$$##member_link##$$", member_link).replace("$$##wellness_type##$$", wellness_type).replace("$$##patient_number##$$", patient_number).replace("$$##invite_id##$$", invite_id).replace("$$##admin_name##$$", admin_name)
                    message_subject = str(json.loads(_message_recieved.get("message", {}).get("messageJson", {})).get("subject", "")).replace("$$##wellness_name##$$", wellness_name).replace("$$##member_type##$$",member_type).replace("$$##wellness_type##$$", wellness_type).replace("$$##member_name##$$", member_name).replace("$$##patient_name##$$", patient_name).replace("$$##admin_name##$$", admin_name)
                    if notification_type == WELLNESS_INVITATION:
                        member_email = json.loads(_message_recieved.get("message", {}).get("memberDetails", {})).get("email", "") 
                        send_mail(member_email, wellness_email_id, message_subject, message_body)
                        insertNotificationActivity(admin_id, patient_id, _notification, "email", message_subject + "\n\n" + message_body)
                        logging.info(notification_type + ": Email send to " + str(member_email))
                      
                    if  notification_type in [PATIENT_REFER, COLLABORATION_CONFIRM]:
                        send_mail(user_email_id, wellness_email_id, message_subject, message_body)
                        insertNotificationActivity(admin_id, patient_id, _notification, "email", message_subject + "\n\n" + message_body)
                        logging.info(notification_type + ": Email send to " + str(user_email_id))
                    elif notification_type == PATIENT_REFER_ADMIN:
                        send_mail(wellness_email_id, None, message_subject, message_body)
                        insertNotificationActivity(admin_id, patient_id, _notification, "email", message_subject + "\n\n" + message_body)
                        logging.info(notification_type + ": Email send to " + str(wellness_email_id))
                    elif notification_type == PATIENT_REFER_MEMBER:
                        send_mail(user_email_id, None, message_subject, message_body)
                        insertNotificationActivity(admin_id, patient_id, _notification, "email", message_subject + "\n\n" + message_body)
                        logging.info(notification_type + ": Email send to " + str(user_email_id))
                        

                if notification_whatsapp == "1" and message_type == "whatsapp":
                    message_body_whatsapp = str(json.loads(_message_recieved.get("message", {}).get("messageJson", {})).get("message", "")).replace("$$##patient_name##$$", patient_name).replace("$$##member_name##$$", member_name).replace("$$##wellness_name##$$", wellness_name).replace("$$##member_type##$$", member_type).replace("$$##member_number##$$", member_number).replace("$$##admin_link##$$", admin_link).replace("$$##member_link##$$", member_link).replace("$$##member_number##$$", member_number).replace("$$##wellness_type##$$", wellness_type).replace("$$##patient_number##$$", patient_number).replace("$$##invite_id##$$", invite_id).replace("$$##admin_name##$$", admin_name)
                    if notification_type == WELLNESS_INVITATION:
                        member_contact = json.loads(_message_recieved.get("message", {}).get("memberDetails", {})).get("contact", )
                        if member_contact not in [None, "NULL", "", " "]:
                            if len(member_contact) == 10:
                                member_contact = "91" + member_contact
                            _data = data%(member_contact, message_body_whatsapp.replace("&", "%26"))
                            logging.info(notification_type + ": whatsapp sending to " + str(member_contact))
                            sentMessage(_data, _url, _header)
                            insertNotificationActivity(admin_id, patient_id, _notification, "whatsapp", message_body_whatsapp)

                    if notification_type in [PATIENT_REFER, COLLABORATION_CONFIRM]:
                        if user_number not in [None, "NULL", "", " "] and wellness_number not in [None, "NULL", "", " "]:
                            if len(user_number) == 10:
                                user_number = "91"+ user_number
                            _data = data%(user_number, message_body_whatsapp.replace("&", "%26"))
                            logging.info(notification_type + ": Whatsapp sending to " + str(user_number))
                            sentMessage(_data, _url, _header)
                            insertNotificationActivity(admin_id, patient_id, _notification, "whatsapp", message_body_whatsapp)
                    elif notification_type == PATIENT_REFER_ADMIN:
                        if user_number not in [None, "NULL", "", " "] and wellness_number not in [None, "NULL", "", " "]:
                            if len(user_number) == 10:
                                user_number = "91"+ user_number
                            _data = data%(user_number, message_body_whatsapp.replace("&", "%26"))
                            logging.info(notification_type + ": Whatsapp sending to " + str(user_number))
                            sentMessage(_data, _url, _header)
                            insertNotificationActivity(admin_id, patient_id, _notification, "whatsapp", message_body_whatsapp)
                    elif notification_type == PATIENT_REFER_MEMBER:
                        if user_number not in [None, "NULL", "", " "] and wellness_number not in [None, "NULL", "", " "]:
                            if len(user_number) == 10:
                                user_number = "91"+ user_number
                            _data = data%(user_number, message_body_whatsapp.replace("&", "%26"))
                            logging.info(notification_type + ": Whatsapp sending to " + str(user_number))
                            sentMessage(_data, _url, _header)
                            insertNotificationActivity(admin_id, patient_id, _notification, "whatsapp", message_body_whatsapp)

            if notification_type in [USER_AUDIT_TRAIL_LOGIN, USER_AUDIT_TRAIL_LOGOUT, USER_AUDIT_TRAIL_FORGOT_PASSWORD_TOKEN, USER_AUDIT_TRAIL_OTP_GENERATION, USER_AUDIT_TRAIL_FORGOT_PASSWORD_VERIFY, USER_AUDIT_TRAIL_OTP_VERIFICATION, USER_AUDIT_TRAIL_USER_UPDATE, DIET_AUDIT_TRAIL_LOGIN]:
               _message_recieved = json.loads(message_recieved)
               user_id = int(_message_recieved.get("message", {}).get("user_id", 0))
               user_role = _message_recieved.get("message", {}).get("user_role", "")
               status_message = _message_recieved.get("message", {}).get("message", "")
               parameter = _message_recieved.get("message", {}).get("parameters", "") 
               session_id = _message_recieved.get("message", {}).get("session_id", "")
               if session_id == None:
                   session_id = ""
               access_type = _message_recieved.get("message", {}).get("access_type", "")
               logging.info("Inserting Audit Trail for " + access_type + " in to database for user_id " + str(user_id))
               if user_id != 0:
                   insertAuditTrail(user_id, user_role, session_id, access_type, json.dumps(parameter), status_message)  
               logging.info("Inserted Audit Trail for " + access_type + " Successfully.")
        except Exception as err:
            logging.info(err)
            print (err)
         
    def consumeUserData(self):
        super(NotificationManager, self).consumeUserData()
        # call module name and message queue object from config file.
        module = __import__(getAtmanConfigParamValue("MESSAGE_QUEUE_FILE_NAME"))
        message_queue = getattr(module, getAtmanConfigParamValue("MESSAGE_QUEUE_CLASS"))()
        message_queue.connectServer()
        message_queue.createChannel()
        callback = self.callback
        message_queue.consumeData(callback, queue_name_notification)
    

if __name__ == "__main__":
    send_notification = NotificationManager()
    send_notification.consumeUserData()  
 
