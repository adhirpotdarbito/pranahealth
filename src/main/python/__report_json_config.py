import json

class FileConfig():
    """
        A class to read json file and return json data
    """
    def __init__(self):
        file_path = '/opt/atman/config/__medical_report_parser.json'
        with open(file_path,'rb') as file:
            self.config = json.load(file)
    
    def getJsonData(self):
        return self.config

file_instance = FileConfig()
json_file_data = file_instance.getJsonData()
