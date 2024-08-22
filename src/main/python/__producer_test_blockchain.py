import json
import random
import datetime
from collections import OrderedDict
from __user_queue_data import *
from __message_queue import *
from __message import *
from __config import *


class PublishData(QueueData):
    def __init__(self):
        super(PublishData, self).__init__()
        self.message = {}
        self.user_data = {}

    def publishUserData(self, message_data, parameter_type):
        super(PublishData, self).publishUserData(message_data, parameter_type)
        message_queue = MessageQueue() 
        message = Message()
        message.setMessageText(message_data)
        #message.setParameterType(parameter_type)
        #self.message["opcode"] = message.getOpcode()
        #self.message["parameter_type"] = message.getUserParameterType()
        #self.message["message"] = message.getMessageText()
        module = __import__(getAtmanConfigParamValue("MESSAGE_QUEUE_FILE_NAME"))
        message_queue = getattr(module, getAtmanConfigParamValue("MESSAGE_QUEUE_CLASS"))()
        message_queue.connectServer()
        message_queue.publishData(json.dumps(message_data))

if __name__ == "__main__":
    pd = PublishData()
    message_data = {"public_key":"MC0wCAYDK2VkCgEBAyEApnPbIE35\/LTBpdITDiD+FYG4Ykl56hERwSeW0aVB1z8=","wellness_info":"","user_name":"Anish Potdar","private_key":"MC8CAQAwCAYDK2VkCgEBBCDccQdd4DnnhgSDk9nB+P3Bm4k6UFRbG1xbtBGUve7yCA==","wellness_name":"Adhir Potdar","message":{"id":153,"diabetes":"1","cardiac":"none","hypertension":"none","obesity":"none","asthma":"none","depression":"none","thyroid":"none","cancer":"none"},"opcode":"write","user_email_id":"anish.potdar@isanasystems.com","user_phone_number":"9822309574","user_id":153,"admin_id":2,"wellness_type":"Dietitian","parameter_type":"User Family History","wellness_email_id":"adhirpotdar@gmail.com","timestamp": datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")}
    random_param = random.choice(["depression", "cardiac", "cancer", "hypertension", "diabetes", "obesity", "asthma", "thyroid"])
    message_data["message"][random_param] = random.randint(0,1) 
    print message_data
    pd.publishUserData(message_data, "User Family History")
     

