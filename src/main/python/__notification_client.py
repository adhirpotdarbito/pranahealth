import json
import sys
from datetime import datetime
from collections import OrderedDict
from __notification_message import *
from __user_queue_data import *
from __config import *
from __notification_utils import *

class NotificationClient(QueueData):
    def __init__(self):
        super(NotificationClient, self).__init__()
        self.message = {}

    def publishNotification(self, notification_type, target):
        super(NotificationClient, self).publishNotification(notification_type, target)
        notification = NotificationMessage()
        notification.setNotificationType(notification_type)
        notification.setNotificationCategory(GROUP_NOTIFICATION)
        notification.setMessageTemplate("")
        notification.setMessageTemplateParameters("")
        self.message["notification_category"] = notification.getNotificationCategory()
        self.message["message_template"] = notification.getMessageTemplate()
        self.message["message_template_parameter"] = notification.getMessageTemplateParameters()
        if target == DIETITIAN:
            target_list = getTargetAudience(DIETITION_ACL)
        else:
            target_list = getTargetAudience(USER_ACL)
        notification.setTargetAudience(target_list)    
        #self.message["patientEmail"] = notification.getTargetAudience()
        self.message["patientEmail"] = ["viveksallu156@gmail.com"]
        self.message["patient_whatsapp"] = ["9993602730", "7020748154"]
        module = __import__(getAtmanConfigParamValue("MESSAGE_QUEUE_FILE_NAME"))
        message_queue = getattr(module, getAtmanConfigParamValue("MESSAGE_QUEUE_CLASS"))()
        message_queue.connectServer()
        message_queue.publishData(json.dumps({"parameter_type":notification.getNotificationType(), "message":self.message}))


if __name__=="__main__":
    notification_client = NotificationClient() 
    try:
        if len(sys.argv) < 2:
            print ("try")
            print ("python __notification_client.py <role>")
        else:
            target = sys.argv[1]
            notification_client.publishNotification(GENERAL_REMINDER, target)
    except Exception as err:
        print (err)   
