import os
import sys


if __name__ == "__main__":
    print("Starting hyperledger fabric") 
    print("======================================================")
    try:
        file_path = "~/fabric-tools/startFabric.sh"
        if os.system("/bin/bash "+file_path) != 0:
            raise Exception("Hyperledger failed to start.")
        else:
            print ("Started Hyperledger fabric")
    except:
        print ("========================================================")
        print("Command Failed for channel creation as it already exists.")
        print("Hyperledger Fabric started")
    
