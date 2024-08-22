import json
from collections import OrderedDict
from __notification_message import *
from __user_queue_data import *
from __notification_utils import *
from copy import deepcopy
from __config import *



class NotificationDietitian(QueueData): 
    def __init__(self):
        super(NotificationDietitian, self).__init__()
        self.message = {}

    def publishNotification(self, notification_type):
        super(NotificationDietitian, self).__init__()
        notification = NotificationMessage()
        notification.setNotificationType(notification_type)
        notification.setNotificationCategory(SCHEDULED_NOTIFICATION)
        message_template = getDietitonPatientAppointment() 
        notification.setMessageTemplate(message_template)
        target = []
        notification.setTargetAudience(target)
        template_parameters_list = []
        for message in message_template:
            template_parameter = {}
            template_parameter["dietitian_mail"] = message.get("dietitian_email", "")
            template_parameter["patient_data"] = tuple(message.get("patient_data", {}))
            template_parameter["dietitian_contact"] = message.get("dietitian_number", "")
            template_parameter["wellness_name"] = message.get("dietitian_name", "")
            template_parameters_list.append(template_parameter)
        notification.setMessageTemplateParameters(template_parameters_list)
        self.message["notification_category"] = notification.getNotificationCategory()
        self.message["message_template"] = notification.getMessageTemplate()
        self.message["message_template_parameter"] = notification.getMessageTemplateParameters()
        self.message["patientEmail"] = notification.getTargetAudience()
        module = __import__(getAtmanConfigParamValue("MESSAGE_QUEUE_FILE_NAME"))
        message_queue = getattr(module, getAtmanConfigParamValue("MESSAGE_QUEUE_CLASS"))()
        message_queue.connectServer()
        message_queue.publishData(json.dumps({"parameter_type":notification.getNotificationType(), "message":self.message}))


if __name__=="__main__":
    notification_appointent = NotificationDietitian()
    notification_type = APPOINTMENT_REMINDER_DIETITIAN 
    notification_appointent.publishNotification(notification_type)

