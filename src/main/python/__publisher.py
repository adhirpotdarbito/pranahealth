import json
import datetime
from collections import OrderedDict
from __user_queue_data import *
from __message_queue import *
from __message import *
from __db_config import *

class PublishData(QueueData):
    def __init__(self):
        super(PublishData, self).__init__()
        self.message = {}
        self.user_data = {}

    def publishUserData(self, user_data, message_data, parameter_type, private_key, public_key):
        super(PublishData, self).publishUserData(user_data, message_data, parameter_type, private_key, public_key) 
        #message_queue = MessageQueue() 
        message = Message()
        message.setTimeStamp(datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"))
        message.setMessageText(message_data)
        message.setUserId(user_data.get("user_id",""))
        message.setUserName(user_data.get("name", ""))
        message.setUserEmailId(user_data.get("email_id",""))
        message.setUserPhoneNumber(user_data.get("user_phone_number",""))
        message.setPrivateKey(private_key)
        message.setPublicKey(public_key)
        message.setParameterType(parameter_type) 
        message.setOpcode("write")
        self.message["user_id"] = message.getUserId()
        self.message["user_name"] = message.getUserName()
        self.message["user_email_id"] = message.getUserEmailId()
        self.message["user_phone_number"] = message.getUserPhoneNumber()
        self.message["timestamp"] = message.getTimeStamp()
        self.message["parameter_type"] = message.getUserParameterType()
        self.message["private_key"] = message.getPrivateKey()
        self.message["public_key"] = message.getPublicKey()
        self.message["message"] = message.getMessageText()
        #self.message["opcode"] = message.getOpcode()
        module = __import__(getAtmanConfigParamValue("MESSAGE_QUEUE_FILE_NAME"))
        message_queue = getattr(module, getAtmanConfigParamValue("MESSAGE_QUEUE_CLASS"))()
        message_queue.connectServer()
        message_queue.publishData(json.dumps(self.message))

    def getUserData(self, user_id):
        cursor = db.cursor()
        query = "SELECT id, name, email, contact FROM users WHERE id=%d"%(int(user_id))
        cursor.execute(query)
        user_data = cursor.fetchone()
        self.user_data["user_id"] = user_data[0]
        self.user_data["name"] = user_data[1]
        self.user_data["email_id"] = user_data[2]
        self.user_data["user_phone_number"] = user_data[3]
        return self.user_data

    def getUserKey(self):
        keys = OrderedDict()
        cursor = db.cursor()
        query = "SELECT private_key, public_key FROM user_keys WHERE id=%d"%(int(user_id))
        cursor.execute(query)
        key_pair = cursor.fetchone()
        keys["private_key"] = key_pair[0]
        keys["public_key"] = key_pair[1]
        return keys
         

if __name__ == "__main__":  
    pd = PublishData()
    init_db()
    db = get_db() 
    if len(sys.argv) < 3:
        print ("python __publisher.py <user_id> <parameter_type>") 
    else:
        user_id = sys.argv[1]
        parameter_type = sys.argv[2]
        user_data = pd.getUserData(user_id)
        key_pair = pd.getUserKey()
        private_key = key_pair.get("private_key") 
        public_key = key_pair.get("public_key")   
        message_data = {"height":"150", "weight":67, "bod":"19740504", "waist":"86.36", "hip_size":"86", "bmi":"29", "waist_hip_ratio":"0.98","waist_height_ratio":"0.57","ideal_body_weight":"50", "ideal_height":"165.1"}
        pd.publishUserData(user_data, message_data, parameter_type, private_key, public_key)
        
