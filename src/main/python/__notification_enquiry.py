import json
from __config import *
from __notification_utils import *
from __user_queue_data import *
from __notification_message import *


class NotificationEnquiry(QueueData):
    def __init__(self):
        super(NotificationEnquiry, self).__init__()
        self.message = {}
        init_db()
        db = get_db()
    
    def publishNotification(self, notification_type): 
        super(NotificationEnquiry, self).__init__()
        notification = NotificationMessage()
        notification.setNotificationType(notification_type)
        notification.setNotificationCategory(SCHEDULED_NOTIFICATION)
        message_template = getPatientFirstAppointment()
        notification.setMessageTemplate(message_template)
        self.message["notification_category"] = notification.getNotificationCategory()
        self.message["message_template"] = notification.getMessageTemplate()
        module = __import__(getAtmanConfigParamValue("MESSAGE_QUEUE_FILE_NAME"))
        message_queue = getattr(module, getAtmanConfigParamValue("MESSAGE_QUEUE_CLASS"))()
        message_queue.connectServer()
        message_queue.publishData(json.dumps({"parameter_type":notification.getNotificationType(), "message":self.message}))
         
    

 
if __name__=="__main__":
    notification_enquiry = NotificationEnquiry()
    notification_type = PATIENT_ENQUIRY 
    notification_enquiry.publishNotification(notification_type)

      
