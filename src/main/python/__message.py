class Message():
    """A class for defining message""" 
    def __init__(self):
        self.timestamp = None
        self.message_text = None
        self.user_email_id = None
        self.user_id = None
        self.admin_id = None
        self.user_name = None
        self.user_phone_number = None
        self.parameter_type = None
        self.opcode = None
        self.private_key = None
        self.public_key = None

    # setter functions
    def setTimeStamp(self, timestamp):
        self.timestamp = timestamp

    def setMessageText(self, message_text):
        self.message_text = message_text 
  
    def setUserEmailId(self, email_id):
        self.user_email_id = email_id

    def setUserId(self, user_id):
        self.user_id = user_id

    def setAdminId(self, admin_id):
        self.admin_id = admin_id

    def setUserName(self,user_name):
        self.user_name = user_name
 
    def setUserPhoneNumber(self, phone_number):
        self.user_phone_number = phone_number

    def setParameterType(self, parameter_type):
        self.parameter_type = parameter_type

    def setOpcode(self, opcode):
        self.opcode = opcode

    def setPrivateKey(self, key):
        self.private_key = key        
    
    def setPublicKey(self, key):
        self.public_key = key
 
    # getter functions
    def getTimeStamp(self):
        return self.timestamp

    def getMessageText(self):
        return self.message_text

    def getUserEmailId(self):
        return self.user_email_id

    def getUserId(self):
        return self.user_id

    def getAdminId(self):
        return self.admin_id

    def getUserName(self):
        return self.user_name

    def getUserPhoneNumber(self):
        return self.user_phone_number

    def getUserParameterType(self):
        return self.parameter_type

    def getOpcode(self):
        return self.opcode     

    def getPrivateKey(self):
        return self.private_key

    def getPublicKey(self):
        return self.public_key
