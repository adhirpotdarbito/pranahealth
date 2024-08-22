from __config import *
import sys


if __name__ == "__main__":
    try:
        if len(sys.argv) < 3:
            print ("python __start_blockchain_db.py <user_email> <parameter_type>")
        else:
            user_email = sys.argv[1]
            parameter_type = sys.argv[2]
            module = __import__(getAtmanConfigParamValue("BLOCKCHAIN_FILE_NAME"))
            blockchain = getattr(module, getAtmanConfigParamValue("BLOCKCHAIN_CLASS"))()
            blockchain.connect()
            blockchain.getByUserAndType(user_email, parameter_type, start_time="00000000", end_time="30001231")
    except Exception as err:
        print (err)
        print ("python __start_blockchain_db.py <user_email> <parameter_type>")
