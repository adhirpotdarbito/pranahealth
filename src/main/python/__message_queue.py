import sys

class MessageQueue(object):
    def __init__(self):
        self.host = None
        self.port = None
        self.connection = None      
        self.channel = None
  
    def connectServer(self):
        return None

    def disconnectServer(self):
        return None

    def createChannel(self):
        return None
    
    def publishData(self, data):
        return None

    def consumeData(self):
        return None
 


