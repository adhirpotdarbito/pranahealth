import sys
import json
from pymongo import MongoClient
from bigchaindb_driver import BigchainDB
import datetime
from __config import *
from __blockchaindb import *


class BigchainDb(BlockchainDb):
    """
        A class for storing and retrieving data in bigchaindb
    """
    def __init__(self): 
        # call constructor of the base class
        super(BigchainDb, self).__init__()
        self.client = MongoClient(mongodb_connect)
        self.db = self.client.bigchain 
         
    def connect(self):
        # call connectBlockchaindb function of the base class
        super(BigchainDb, self).connect()
        self.bdb = BigchainDB(bigchain_connect)
        return self.bdb
    
    def disconnect(self):
        super(BigchainDb, self).disconnect()
         
    def storeData(self, user_data, data, user_public_key, user_private_key):
        # user_data is "asset data" and data is "metadata" in bigchaindb 
        # call storeData function of the base class
        super(BigchainDb, self).storeData(user_data, data, user_public_key, user_private_key)
        try:
            # get user_email and data_type from user_data
            user_email = self.user_data.get("data","").get("user","").get("user_email","") 
            data_type = self.user_data.get("data","").get("type","")
            asset_query = self.db.assets.find_one({"$and" : [{"data.user.user_email" : user_email}, {"data.type":data_type}]})
            # if asset not found create it first time else append data to the metadata
            if asset_query == None:
                transaction = self.bdb.transactions.prepare(operation='CREATE', signers=self.user_public_key, asset=self.user_data, metadata=self.data)
                signed_tx = self.bdb.transactions.fulfill(transaction, private_keys=self.user_private_key)
                create_transaction = self.bdb.transactions.send_commit(signed_tx)
                if (signed_tx == create_transaction):
                    print ("Transaction successfully created and stored")
            else:
                # get the id of the asset
                tx_id = asset_query["id"]
                # retrieve transaction for the asset
                creation_tx = self.bdb.transactions.retrieve(tx_id)        
                #print  (creation_tx)
                # get trnsaction id for the trasaction of the asset
                asset_id = creation_tx['id']
                # append asset transaction id to the tx_ids list
                tx_ids = [asset_id]
                # get all transactions id for the asset
                query = self.db.transactions.find({"asset.id":asset_id},{"id":1,"_id":0})
                # append to the tx_ids list
                for ids in query:
                    tx_ids.append(ids["id"])
                transfer_asset = {'id': asset_id}
                output_index = 0
                output = creation_tx['outputs'][output_index]
                # transfer_input should contain the last transfer transaction id for the asset from the list
                transfer_input = {
                 'fulfillment': output['condition']['details'],
                 'fulfills': {
                 'output_index': output_index,
                 'transaction_id': tx_ids[-1],
                 },
                 'owners_before': output['public_keys'],
                 }
                prepared_transfer_tx = self.bdb.transactions.prepare(operation='TRANSFER', asset=transfer_asset, inputs=transfer_input, recipients=(self.user_public_key,), metadata=self.data)
                fulfilled_transfer_tx = self.bdb.transactions.fulfill(prepared_transfer_tx, private_keys=self.user_private_key) 
                sent_transfer_tx = self.bdb.transactions.send_commit(fulfilled_transfer_tx) 
                if (sent_transfer_tx == fulfilled_transfer_tx):
                    print ("Transaction appended successfully")
        except Exception as err:
            print ("transaction not successful",err)
  
 
    def getByUserAndType(self, user_email, data_type, start_time, end_time):
        # user param may be email and data type 
        # call getByUserId function of the base class
        super(BigchainDb, self).getByUserAndType(user_email, data_type, start_time, end_time)
        #user_email = self.user_data.get("data","").get("user","").get("user_email","") 
        #data_type = self.user_data.get("data","").get("type","")
        try:
            asset_query = self.db.assets.find_one({"$and" : [{"data.user.user_email" : user_email}, {"data.type":data_type}]},{"_id":0})
            asset_id = asset_query["id"]
            self.result_data.append(self.db.assets.find_one({"id":asset_id},{"_id":0,"id":0})["data"])
            tx_ids = [asset_id]
            query = self.db.transactions.find({"asset.id":asset_id},{"id":1,"_id":0})
            start_time = start_time + " 00:00:00"
            end_time = end_time + " 00:00:00"
            for ids in query:
                tx_ids.append(ids["id"])
            for tx_id in tx_ids:
                query_txid = self.db.metadata.find_one({"$and" : [{"id":tx_id}, {"metadata.timestamp":{"$gte":start_time ,"$lt":end_time}}]},{"_id":0,"id":0})
                if query_txid is not None:
                    self.result_data.append(query_txid["metadata"])
            print (json.dumps({"user_data" : self.result_data}, indent=4))
            return self.result_data
        except Exception as err:
            self.result_data = {}
            #print (err)
            return self.result_data


