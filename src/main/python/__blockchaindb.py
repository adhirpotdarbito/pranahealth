import os

class BlockchainDb(object):
    """
        A wrapper class for blockchain bd
    """ 
    def __init__(self):
        self.userdata = None
        self.result_data = []
        self.user_public_key = None
        self.user_private_key = None
        self.bdb = None
        
    def connect(self):
        return self.bdb   

    def disconnect(self):
        self.bdb = None 

    def storeData(self, user_data, data, user_public_key, user_private_key):
        """
            store data in bigchaindb
        """
        self.user_data = user_data
        self.data = data
        self.user_public_key = user_public_key
        self.user_private_key = user_private_key
        return None
 
    def getByUserAndType(self, user_email, data_type, start_time="00000000", end_time="30001231"):
        """
           get data by type e.g. bodyparams, lifesyle habit
        """
        return self.result_data

