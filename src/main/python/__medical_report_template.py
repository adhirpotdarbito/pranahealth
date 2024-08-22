import json
from collections import OrderedDict
from __report_json_config import *

class MedicalReportTemplate(object):
    def __init__(self):
        self.file_path = ""
        self.param_annot = OrderedDict()
        self.paramters = []
        self.parsed_output = OrderedDict() 

    def loadMetaData(self):
        #get path of the json file and read the file
        with open(self.file_path) as file:
            self.profile = json.load(file)
        self.parameters = self.profile.get("parameters")
        for i in range(len(self.parameters)):
            self.param_annot[self.parameters[i].get("parameter_name")] = self.parameters[i].get("medical_annotation") 
        return self.profile

    def getParameters(self):
        return [param for param in self.param_annot.keys()]

    def getAnnotations(self, parameter_name):
        return self.param_annot.get(parameter_name,[])
  
    def getParsedData(self, file_name, gender, password):
        return self.parsed_output     
