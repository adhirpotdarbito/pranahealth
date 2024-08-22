import json
import time
from collections import OrderedDict
from __notification_message import *
from __user_queue_data import *
from __notification_utils import *
from __config import *

class NotificationAppointment(QueueData):
    def __init__(self):
        super(NotificationAppointment, self).__init__()
        self.message = {}
        init_db()
        db = get_db()
        self.db = db

    def publishNotification(self, notification_type):
        super(NotificationAppointment, self).publishNotification(notification_type)
        notification = NotificationMessage()
        notification.setNotificationType(notification_type)
        notification.setNotificationCategory(SCHEDULED_NOTIFICATION)
        #if datetime.now().strftime("%H%M") == "0000":
        message_template = getPatientAppointment()
        #else:
        #    message_template = getPatientAppointmentHourly()
        notification.setMessageTemplate(message_template)
        template_parameter = []
        template_dict = {}
        target = []
        for template in message_template:
            template_dict["dietitian_name"] = template.get("admin_name")
            template_dict["dietitian_mail"] = template.get("admin_email")                
            template_dict["patient_name"] = template.get("patient_name")                
            template_dict["patient_mail"] = template.get("patient_email")                
            template_dict["date"] = template.get("date")
            template_dict["time"] = template.get("time_slot")
            template_dict["meeting_url"] = template.get("meeting_url")
            template_dict["patient_whatsapp"] = template.get("patient_whatsapp")
            template_dict["admin_id"] = template.get("admin_id")
            template_dict["patient_id"] = template.get("patient_id")
            template_dict["wellness_number"] = template.get("admin_contact")
            admin_id = template.get("admin_id")
            date = template.get("date")
            time_slot = template.get("time_slot")
            admin_address, area, city = getAdminArea(db, admin_id, date, time_slot)
            template_dict["admin_address"] = admin_address
            template_dict["area"] = area
            template_dict["city"] = city
            template_parameter.append(template_dict)
            target.append(template.get("patient_email"))
            template_dict = {}
        notification.setMessageTemplateParameters(template_parameter)
        notification.setTargetAudience(target)
        self.message["notification_category"] = notification.getNotificationCategory()
        self.message["message_template"] = notification.getMessageTemplate()
        self.message["message_template_parameter"] = notification.getMessageTemplateParameters()
        self.message["patientEmail"] = notification.getTargetAudience()
        self.message["notification_template"] = getDailyPatientAppointmentTemplate() 
        print self.message
        module = __import__(getAtmanConfigParamValue("MESSAGE_QUEUE_FILE_NAME"))
        message_queue = getattr(module, getAtmanConfigParamValue("MESSAGE_QUEUE_CLASS"))()
        message_queue.connectServer()
        message_queue.publishData(json.dumps({"parameter_type":notification.getNotificationType(), "message":self.message}))
        
        
    
if __name__=="__main__":
    notification_appointent = NotificationAppointment()
    notification_type = APPOINTMENT_REMINDER 
    notification_appointent.publishNotification(notification_type)


