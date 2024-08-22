import json
from collections import OrderedDict
from __config import *
from __medical_report_parser import *
from __medical_report_template import *

class VitaminsProfile(MedicalReportTemplate):
    """
        A class for vitamin profile:
    """
    def __init__(self):
        try:
            super(VitaminsProfile, self).__init__()
            self.file_path = json_file_data.get("medical_parser_detail","")[5].get("file_name","")
            self.vitamin_b12 = None
            self.vitamin_d = None
            self.category_id = "" 
            self.category_name = ""
            self.version_number = ""
            self.vitamin_b12_unit = ""
            self.vitamin_b12_medical_annot = []
            self.vitamin_b12_range_male = ""
            self.vitamin_b12_range_female = ""
            self.vitamin_b12_low_male = ""
            self.vitamin_b12_fair_male = ""
            self.vitamin_b12_moderate_male = ""
            self.vitamin_b12_high_male = ""
            self.vitamin_b12_low_female = ""
            self.vitamin_b12_fair_female = ""
            self.vitamin_b12_moderate_female = ""
            self.vitamin_b12_high_female = ""
            self.vitamin_b12_func = ""
            self.vitamin_d_unit = ""
            self.vitamin_d_medical_annot = []
            self.vitamin_d_range_male = ""
            self.vitamin_d_range_female = ""
            self.vitamin_d_low_male = ""
            self.vitamin_d_fair_male = ""
            self.vitamin_d_moderate_male = ""
            self.vitamin_d_high_male = ""
            self.vitamin_d_low_female = ""
            self.vitamin_d_fair_female = ""
            self.vitamin_d_moderate_female = ""
            self.vitamin_d_high_female = ""
            self.vitamin_d_func = ""
            self.vitamin_b12_output = OrderedDict()
            self.vitamin_d_output = OrderedDict()
        except Exception as err:
            print err

    def loadMetaData(self):
        super(VitaminsProfile, self).loadMetaData()
        self.setCategoryid()
        self.setCategoryName()
        self.setVersionNumber()
        self.setVitaminB12Unit()
        self.setVitaminB12MedicalAnotation()
        self.setVitaminB12RangeMale()
        self.setVitaminB12RangeFemale()
        self.setVitaminB12LowValueMale()
        self.setVitaminB12FairValueMale()
        self.setVitaminB12ModerateValueMale()
        self.setVitaminB12HighValueMale()
        self.setVitaminB12LowValueFemale()
        self.setVitaminB12FairValueFemale()
        self.setVitaminB12ModerateValueFemale()
        self.setVitaminB12HighValueFemale()
        self.setVitaminB12Function()
        self.setVitaminDUnit()
        self.setVitaminDMedicalAnnotations()
        self.setVitaminDRangeMale()
        self.setVitaminDRangeFemale()
        self.setVitaminDLowValueMale()
        self.setVitaminDFairValueMale()
        self.setVitaminDModerateValueMale()
        self.setVitaminDHighValueMale()
        self.setVitaminDLowValueFemale()
        self.setVitaminDFairValueFemale()
        self.setVitaminDModerateValueFemale()
        self.setVitaminDHighValueFemale()
        self.setVitaminDFunction()

    def getAnnotations(self, parameter_name):
        return super(VitaminsProfile, self).getAnnotations(parameter_name)

    def getParsedData(self, file_name, gender, password=""):
        report_parse = ReportParser(file_name, password)
        report_parse.reportList()
        parameter_name = self.getParameters()
        med_annot_vita_b12 = self.getAnnotations(parameter_name[0])
        med_annot_vita_d = self.getAnnotations(parameter_name[1])
        vita_b12 = parameter_name[0]
        report_parse.parseMedicalParameter(med_annot_vita_b12, vita_b12)
        vita_d = parameter_name[1]
        report_parse.parseMedicalParameter(med_annot_vita_d, vita_d)
        medical_report_dict = report_parse.getMedicalParsedData()
        vita_b12_value = medical_report_dict.get(vita_b12,None)
        vita_d_value = medical_report_dict.get(vita_d,None)
        self.setVitaminB12Value(vita_b12_value)
        self.setVitaminDValue(vita_d_value)
        self.vitamin_b12_output["reading_value"] = str(self.getVitaminB12Value())
        self.vitamin_b12_output["reading_unit"] = self.getVitaminB12Unit()
        self.vitamin_b12_output["range_male"] = self.getVitaminB12RangeMale()
        self.vitamin_b12_output["range_female"] = self.getVitaminB12RangeFemale()
        self.vitamin_d_output["reading_value"] = str(self.getVitaminDValue())
        self.vitamin_d_output["reading_unit"] = self.getVitaminDUnit()
        self.vitamin_d_output["range_male"] = self.getVitaminDRangeMale()
        self.vitamin_d_output["range_female"] = self.getVitaminDRangeFemale()
        if gender == "Female":
            self.vitamin_b12_output["low_fair_moderate_high"] = [self.getVitaminB12LowValueFemale(), self.getVitaminB12FairValueFemale(), self.getVitaminB12ModerateValueFemale(), self.getVitaminB12HighValueFemale()]
            if self.getVitaminB12Value() >= float(self.getVitaminB12LowValueFemale().split("-")[0]) and self.getVitaminB12Value() <= float(self.getVitaminB12LowValueFemale().split("-")[1]):
                self.vitamin_b12_output["risk"] = Low
            if self.getVitaminB12Value() >= float(self.getVitaminB12FairValueFemale().split("-")[0]) and self.getVitaminB12Value() <= float(self.getVitaminB12FairValueFemale().split("-")[1]):
                self.vitamin_b12_output["risk"] = Low
            if self.getVitaminB12Value() >= float(self.getVitaminB12ModerateValueFemale().split("-")[0]) and self.getVitaminB12Value() <= float(self.getVitaminB12ModerateValueFemale().split("-")[1]):
                self.vitamin_b12_output["risk"] = Low
            if self.getVitaminB12Value() < float(self.getVitaminB12HighValueFemale()) or self.getVitaminB12Value() > float(self.getVitaminB12LowValueFemale().split("-")[1]):
                self.vitamin_b12_output["risk"] = High
            if self.getVitaminB12Value() == None:
                self.vitamin_b12_output["risk"] = n_a
            self.parsed_output["vitamin_b12"] = self.vitamin_b12_output

            self.vitamin_d_output["low_fair_moderate_high"] = [self.getVitaminDLowValueFemale(), self.getVitaminDFairValueFemale(), self.getVitaminDModerateValueFemale(), self.getVitaminDHighValueFemale()]
            if self.getVitaminDValue() >= float(self.getVitaminDLowValueFemale().split("-")[0]) and self.getVitaminDValue() <= float(self.getVitaminDLowValueFemale().split("-")[1]):
                self.vitamin_d_output["risk"] = Low
            if self.getVitaminDValue() >= float(self.getVitaminDFairValueFemale().split("-")[0]) and self.getVitaminDValue() <= float(self.getVitaminDFairValueFemale().split("-")[1]):
                self.vitamin_d_output["risk"] = Low
            if self.getVitaminDValue() >= float(self.getVitaminDModerateValueFemale().split("-")[0]) and self.getVitaminDValue() <= float(self.getVitaminDModerateValueFemale().split("-")[1]):
                self.vitamin_d_output["risk"] = Low
            if self.getVitaminDValue() < float(self.getVitaminDHighValueFemale()) or self.getVitaminDValue() > float(self.getVitaminDLowValueFemale().split("-")[1]):
                self.vitamin_d_output["risk"] = High
            if self.getVitaminDValue() == None:
                self.vitamin_d_output["risk"] = n_a
            self.parsed_output["vitamin_d"] = self.vitamin_d_output

        else:
            self.vitamin_b12_output["low_fair_moderate_high"] = [self.getVitaminB12LowValueMale(), self.getVitaminB12FairValueMale(), self.getVitaminB12ModerateValueMale(), self.getVitaminB12HighValueMale()]
            if self.getVitaminB12Value() >= float(self.getVitaminB12LowValueMale().split("-")[0]) and self.getVitaminB12Value() <= float(self.getVitaminB12LowValueMale().split("-")[1]):
                self.vitamin_b12_output["risk"] = Low
            if self.getVitaminB12Value() >= float(self.getVitaminB12FairValueMale().split("-")[0]) and self.getVitaminB12Value() <= float(self.getVitaminB12FairValueMale().split("-")[1]):
                self.vitamin_b12_output["risk"] = Low
            if self.getVitaminB12Value() >= float(self.getVitaminB12ModerateValueMale().split("-")[0]) and self.getVitaminB12Value() <= float(self.getVitaminB12ModerateValueMale().split("-")[1]):
                self.vitamin_b12_output["risk"] = Low
            if self.getVitaminB12Value() < float(self.getVitaminB12HighValueMale()) or self.getVitaminB12Value() > float(self.getVitaminB12LowValueMale().split("-")[1]):
                self.vitamin_b12_output["risk"] = High
            if self.getVitaminB12Value() == None:
                self.vitamin_b12_output["risk"] = n_a
            self.parsed_output["vitamin_b12"] = self.vitamin_b12_output

            self.vitamin_d_output["low_fair_moderate_high"] = [self.getVitaminDLowValueMale(), self.getVitaminDFairValueMale(), self.getVitaminDModerateValueMale(), self.getVitaminDHighValueMale()]
            if self.getVitaminDValue() >= float(self.getVitaminDLowValueMale().split("-")[0]) and self.getVitaminDValue() <= float(self.getVitaminDLowValueMale().split("-")[1]):
                self.vitamin_d_output["risk"] = Low
            if self.getVitaminDValue() >= float(self.getVitaminDFairValueMale().split("-")[0]) and self.getVitaminDValue() <= float(self.getVitaminDFairValueMale().split("-")[1]):
                self.vitamin_d_output["risk"] = Low
            if self.getVitaminDValue() >= float(self.getVitaminDModerateValueMale().split("-")[0]) and self.getVitaminDValue() <= float(self.getVitaminDModerateValueMale().split("-")[1]):
                self.vitamin_d_output["risk"] = Low
            if self.getVitaminDValue() < float(self.getVitaminDHighValueMale()) or self.getVitaminDValue() > float(self.getVitaminDLowValueMale().split("-")[1]):
                self.vitamin_d_output["risk"] = High 
            if self.getVitaminDValue() == None:
                self.vitamin_d_output["risk"] = n_a
            self.parsed_output["vitamin_d"] = self.vitamin_d_output
            
        if os.path.exists(report_parse.output):
            os.remove(report_parse.output)
        return self.parsed_output




    # Fuction sets category id
    def setCategoryid(self):
        self.category_id = self.profile.get("category_id","")

    # Function sets category name
    def setCategoryName(self):
        self.category_name = self.profile.get("category_name","")

    # Function sets Version number
    def setVersionNumber(self):
        self.version_number = self.profile.get("version_number","")

    # Function to sets vitamin_b12 actual value
    def setVitaminB12Value(self, vitamin_b12):
        self.vitamin_b12 = vitamin_b12

    # Function sets unit of vitamin_b12
    def setVitaminB12Unit(self):
        self.vitamin_b12_unit = self.parameters[0].get('value_meta_data',[])[0].get('unit',"")

    # Function sets list of medical annotations for vitamin_b12
    def setVitaminB12MedicalAnotation(self):
        self.vitamin_b12_medical_annot = self.parameters[0].get('medical_annotation',[])

    # Function sets range of values for vitamin_b12 for male  
    def setVitaminB12RangeMale(self):
        self.vitamin_b12_range_male = self.parameters[0].get('value_meta_data',[])[0].get('range',"")

    # Function sets range of values for vitamin_b12 for female  
    def setVitaminB12RangeFemale(self):
        self.vitamin_b12_range_female = self.parameters[0].get('value_meta_data',[])[1].get('range',"")

    # Function sets low risk values range for vitamin_b12
    def setVitaminB12LowValueMale(self):
        self.vitamin_b12_low_male = self.parameters[0].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for vitamin_b12
    def setVitaminB12FairValueMale(self):
        self.vitamin_b12_fair_male = self.parameters[0].get('value_meta_data',[])[0].get('fair_value',"")

    # Function sets moderate risk values range for vitamin_b12
    def setVitaminB12ModerateValueMale(self):
        self.vitamin_b12_moderate_male = self.parameters[0].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for vitamin_b12
    def setVitaminB12HighValueMale(self):
        self.vitamin_b12_high_male = self.parameters[0].get('value_meta_data',[])[0].get('high_value',"")[1:]

    # Function sets low risk values range for vitamin_b12
    def setVitaminB12LowValueFemale(self):
        self.vitamin_b12_low_female = self.parameters[0].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for vitamin_b12
    def setVitaminB12FairValueFemale(self):
        self.vitamin_b12_fair_female = self.parameters[0].get('value_meta_data',[])[1].get('fair_value',"")

    # Function sets moderate risk values range for vitamin_b12
    def setVitaminB12ModerateValueFemale(self):
        self.vitamin_b12_moderate_female = self.parameters[0].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for vitamin_b12
    def setVitaminB12HighValueFemale(self):
        self.vitamin_b12_high_female = self.parameters[0].get('value_meta_data',[])[1].get('high_value',"")[1:]

    # Function sets function name to parse vitamin_b12 value from medical reports
    def setVitaminB12Function(self):
        self.vitamin_b12_func = self.parameters[0].get("value_function",{}).get("function_name","")

    # Function to sets vitamin d actual value
    def setVitaminDValue(self,vitamin_d):
        self.vitamin_d = vitamin_d

    # Function sets list of medical annotations for vitamin d
    def setVitaminDMedicalAnnotations(self):
        self.vitamin_d_medical_annot = self.parameters[1].get('medical_annotation',[])

    # Function sets unit of vitamin d
    def setVitaminDUnit(self):
        self.vitamin_d_unit = self.parameters[1].get('value_meta_data',[])[0].get('unit',"")

    # Function sets range of values for vitamin d for male
    def setVitaminDRangeMale(self):
        self.vitamin_d_range_male = self.parameters[1].get('value_meta_data',[])[0].get('range',"")

    # Function sets range of values for vitamin d for female
    def setVitaminDRangeFemale(self):
        self.vitamin_d_range_female = self.parameters[1].get('value_meta_data',[])[1].get('range',"")

    # Function sets low risk values range for vitamin d
    def setVitaminDLowValueMale(self):
        self.vitamin_d_low_male = self.parameters[1].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for vitamin d
    def setVitaminDFairValueMale(self):
        self.vitamin_d_fair_male = self.parameters[1].get('value_meta_data',[])[0].get('fair_value',"")

    # Function retuns moderate risk value ranges for vitamin d
    def setVitaminDModerateValueMale(self):
        self.vitamin_d_moderate_male = self.parameters[1].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk value ranges for vitamin d
    def setVitaminDHighValueMale(self):
        self.vitamin_d_high_male = self.parameters[1].get('value_meta_data',[])[0].get('high_value',"")[1:]

    # Function sets low risk values range for vitamin d
    def setVitaminDLowValueFemale(self):
        self.vitamin_d_low_female = self.parameters[1].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for vitamin d
    def setVitaminDFairValueFemale(self):
        self.vitamin_d_fair_female = self.parameters[1].get('value_meta_data',[])[1].get('fair_value',"")

    # Function retuns moderate risk value ranges for vitamin d
    def setVitaminDModerateValueFemale(self):
        self.vitamin_d_moderate_female = self.parameters[1].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk value ranges for vitamin d
    def setVitaminDHighValueFemale(self):
        self.vitamin_d_high_female = self.parameters[1].get('value_meta_data',[])[1].get('high_value',"")[1:]

    # Function sets function name vitamin d value from medical report
    def setVitaminDFunction(self):
        self.vitamin_d_func = self.parameters[1].get("value_function",{}).get("function_name","")
     
    # Fuction returns category id
    def getCategoryid(self):
        return self.category_id

    # Function returns category name
    def getCategoryName(self):
        return self.category_name

    # Function returns Version number
    def getVersionNumber(self):
        return self.version_number

    # Function to get vitamin_b12 actual value
    def getVitaminB12Value(self):
        return self.vitamin_b12

    # Function returns unit of vitamin_b12
    def getVitaminB12Unit(self):
        return self.vitamin_b12_unit

    # Function returns list of medical annotations for vitamin_b12
    def getVitaminB12MedicalAnotation(self):
        return self.vitamin_b12_medical_annot

    # Function returns range of values for vitamin_b12 for male  
    def getVitaminB12RangeMale(self):
        return self.vitamin_b12_range_male

    # Function returns range of values for vitamin_b12 for female  
    def getVitaminB12RangeFemale(self):
        return self.vitamin_b12_range_female

    # Function returns low risk values range for vitamin_b12
    def getVitaminB12LowValueMale(self):
        return self.vitamin_b12_low_male

    # Function returns fair risk values range for vitamin_b12
    def getVitaminB12FairValueMale(self):
        return self.vitamin_b12_fair_male

    # Function returns moderate risk values range for vitamin_b12
    def getVitaminB12ModerateValueMale(self):
        return self.vitamin_b12_moderate_male

    # Function returns high risk values range for vitamin_b12
    def getVitaminB12HighValueMale(self):
        return self.vitamin_b12_high_male

    # Function returns low risk values range for vitamin_b12
    def getVitaminB12LowValueFemale(self):
        return self.vitamin_b12_low_female

    # Function returns fair risk values range for vitamin_b12
    def getVitaminB12FairValueFemale(self):
        return self.vitamin_b12_fair_female

    # Function returns moderate risk values range for vitamin_b12
    def getVitaminB12ModerateValueFemale(self):
        return self.vitamin_b12_moderate_female

    # Function returns high risk values range for vitamin_b12
    def getVitaminB12HighValueFemale(self):
        return self.vitamin_b12_high_female

    # Function returns function name to parse vitamin_b12 value from medical reports
    def getVitaminB12Function(self):
        return self.vitamin_b12_func

    # Function to get vitamin d actual value
    def getVitaminDValue(self):
        return self.vitamin_d

    # Function returns list of medical annotations for vitamin d
    def getVitaminDMedicalAnnotations(self):
        return self.vitamin_d_medical_annot

    # Function returns unit of vitamin d
    def getVitaminDUnit(self):
        return self.vitamin_d_unit

    # Function returns range of values for vitamin d for male
    def getVitaminDRangeMale(self):
        return self.vitamin_d_range_male

    # Function returns range of values for vitamin d for female
    def getVitaminDRangeFemale(self):
        return self.vitamin_d_range_female

    # Function returns low risk values range for vitamin d
    def getVitaminDLowValueMale(self):
        return self.vitamin_d_low_male

    # Function returns fair risk values range for vitamin d
    def getVitaminDFairValueMale(self):
        return self.vitamin_d_fair_male

    # Function retuns moderate risk value ranges for vitamin d
    def getVitaminDModerateValueMale(self):
        return self.vitamin_d_moderate_male

    # Function returns high risk value ranges for vitamin d
    def getVitaminDHighValueMale(self):
        return self.vitamin_d_high_male

    # Function returns low risk values range for vitamin d
    def getVitaminDLowValueFemale(self):
        return self.vitamin_d_low_female

    # Function returns fair risk values range for vitamin d
    def getVitaminDFairValueFemale(self):
        return self.vitamin_d_fair_female

    # Function retuns moderate risk value ranges for vitamin d
    def getVitaminDModerateValueFemale(self):
        return self.vitamin_d_moderate_female

    # Function returns high risk value ranges for vitamin d
    def getVitaminDHighValueFemale(self):
        return self.vitamin_d_high_female

    # Function returns function name to parse vitamin d value from medical report
    def getVitaminDFunction(self):
        return self.vitamin_d_func


