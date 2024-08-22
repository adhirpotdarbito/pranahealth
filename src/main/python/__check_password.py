import PyPDF2
import sys
import os
import json

# Functions will return Password if pdf file requires password
def isPasswordRequired(file_name, dump = True):
    """
        Function to check whether report pdf requires password, and return True
    """
    if file_name.endswith("pdf"):
        checkPassword = PyPDF2.PdfFileReader(file_name, strict=False)
        if checkPassword.isEncrypted:
            if dump == True:
                print json.dumps({"check_password" : "required"}) 
            return True
        else:
            if dump == True:
                print json.dumps({"check_password" : "not required"})
            return False
    else:
        if dump == True: 
            print json.dumps({"check_password" : "not required"})        
        return False

file_name = sys.argv[1]
isPasswordRequired(file_name)
