import json
import datetime
from collections import OrderedDict
from __user_queue_data import *
from __message_queue import *
from __message import *
from __config import *


class ConsumeData(QueueData):
    def __init__(self):
        super(ConsumeData, self).__init__()
        return None

    def callback(self, ch, method, properties, body):
        print (body)
        self.processingFunction(body)

    def processingFunction(self, message_recieved):
        module = __import__(getAtmanConfigParamValue("BLOCKCHAIN_FILE_NAME"))
        blockchain = getattr(module, getAtmanConfigParamValue("BLOCKCHAIN_CLASS"))()
        blockchain.connect()
        data = {}
        user = OrderedDict()
        user_data = {}
        data_meta = OrderedDict()
        message_recieved = json.loads(message_recieved)
        if message_recieved.get("parameter_type") == "User Misc Data":
            misc_keys = message_recieved.get("message", {}).get("miscData", {})
            misc_keys = json.loads(misc_keys).keys()
            for misc in misc_keys:
                data["timestamp"] = message_recieved.get("timestamp", "")
                user["user_id"] = message_recieved.get("user_id", "")
                user["user_name"] = message_recieved.get("user_name", "")
                user["user_email"] = message_recieved.get("user_email_id", "")
                user["user_phone"] = message_recieved.get("user_phone_number", "")
                data["type"] = misc
                data["user"] = user
                user_data["data"] = data
                data_meta["timestamp"] = message_recieved.get("timestamp", "")
                data_meta[misc] = json.loads(message_recieved.get("message", {}).get("miscData", {})).get(misc, "")
                private_key = message_recieved.get("private_key","")
                public_key = message_recieved.get("public_key","")
                blockchain.storeData(user_data, data_meta, public_key, private_key)
                data = {}
                user = OrderedDict()
                user_data = {}
                data_meta = OrderedDict()
        else:       
            user["user_id"] = message_recieved.get("user_id", "")
            user["user_name"] = message_recieved.get("user_name", "")
            user["user_email"] = message_recieved.get("user_email_id", "")
            user["user_phone"] = message_recieved.get("user_phone_number", "")
            data["timestamp"] = message_recieved.get("timestamp", "")
            data["type"] = message_recieved.get("parameter_type", "")
            data["user"] = user
            user_data["data"] = data
            data_meta["timestamp"] = message_recieved.get("timestamp", "")
            data_meta[message_recieved.get("parameter_type")] = message_recieved.get("message", {})
            private_key = message_recieved.get("private_key","")
            public_key = message_recieved.get("public_key","")
            blockchain.storeData(user_data, data_meta, public_key, private_key)

    def consumeUserData(self):
        # call module name and message queue object from config file.
        super(ConsumeData, self).consumeUserData() 
        module = __import__(getAtmanConfigParamValue("MESSAGE_QUEUE_FILE_NAME"))
        message_queue = getattr(module, getAtmanConfigParamValue("MESSAGE_QUEUE_CLASS"))()
        message_queue.connectServer()
        message_queue.createChannel()
        callback = self.callback
        message_queue.consumeData(callback, queue_name_blockchain) 

       
