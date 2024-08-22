import json
from collections import OrderedDict
from __medical_report_parser import *
from __medical_report_template import *


class KidneyProfile(MedicalReportTemplate):
    """
        A class for kidney profile
    """
    def __init__(self):
        try:
            super(KidneyProfile, self).__init__() 
            self.file_path = json_file_data.get("medical_parser_detail","")[2].get("file_name","")
            self.blood_urea = None
            self.creatinine = None
            self.uric_acid = None
            self.bun_creat_ratio = None 
            self.category_id = ""
            self.category_name = ""
            self.version_number = ""
            self.blood_urea_unit = ""
            self.blood_urea_medical_annot = []
            self.blood_urea_range_male = ""
            self.blood_urea_range_female = ""
            self.blood_urea_low_male = ""
            self.blood_urea_fair_male = ""
            self.blood_urea_moderate_male = ""
            self.blood_urea_high_male = ""
            self.blood_urea_low_female = ""
            self.blood_urea_fair_female = ""
            self.blood_urea_moderate_female = ""
            self.blood_urea_high_female = ""
            self.blood_urea_function = ""
            self.creat_unit = ""
            self.creat_medical_annot = []
            self.creat_range_male = ""
            self.creat_range_female = ""
            self.creat_low_male = ""
            self.creat_fair_male = ""
            self.creat_moderate_male = ""
            self.creat_high_male = ""
            self.creat_low_female = ""
            self.creat_fair_female = ""
            self.creat_moderate_female = ""
            self.creat_high_female = ""
            self.creat_func = ""
            self.uric_acid_unit = ""
            self.uric_acid_medical_annot = []
            self.uric_acid_range_male = ""
            self.uric_acid_range_female = ""
            self.uric_acid_low_male = ""
            self.uric_acid_fair_male = ""
            self.uric_acid_moderate_male = ""
            self.uric_acid_high_male = ""
            self.uric_acid_low_female = ""
            self.uric_acid_fair_female = ""
            self.uric_acid_moderate_female = ""
            self.uric_acid_high_female = ""
            self.uric_acid_func = ""
            self.bun_creat_ratio_unit = ""
            self.bun_creat_ratio_medical_annot = []
            self.bun_creat_ratio_range_male = ""
            self.bun_creat_ratio_range_female = ""
            self.bun_creat_ratio_low_male = ""
            self.bun_creat_ratio_fair_male = ""
            self.bun_creat_ratio_moderate_male = ""
            self.bun_creat_ratio_high_male = ""
            self.bun_creat_ratio_low_female = ""
            self.bun_creat_ratio_fair_female = ""
            self.bun_creat_ratio_moderate_female = ""
            self.bun_creat_ratio_high_female = ""
            self.bun_creat_ratio_func = ""
            self.bun_output = OrderedDict()
            self.creatinine_output = OrderedDict()
            self.uric_acid_output = OrderedDict()
            self.bun_creat_output = OrderedDict()
        except Exception as err:
            print err

    def loadMetaData(self):
        super(KidneyProfile, self).loadMetaData()
        self.setCategoryid()
        self.setCategoryName()
        self.setVersionNumber()
        self.setBloodUreaUnit()
        self.setBloodUreaMedicalAnotation()
        self.setBloodUreaRangeMale()
        self.setBloodUreaRangeFemale()
        self.setBloodUreaLowValueMale()
        self.setBloodUreaFairValueMale()
        self.setBloodUreaHighValueMale()
        self.setBloodUreaModerateValueMale()
        self.setBloodUreaLowValueFemale()
        self.setBloodUreaFairValueFemale()
        self.setBloodUreaHighValueFemale()
        self.setBloodUreaModerateValueFemale()
        self.setBloodUreaFunction()
        self.setCreatinineMedicalAnnotations()
        self.setCreatinineUnit()
        self.setCreatinineRangeMale()
        self.setCreatinineRangeFemale()
        self.setCreatinineLowValueMale()
        self.setCreatinineFairValueMale()
        self.setCreatinineModerateValueMale()
        self.setCreatinineHighValueMale()
        self.setCreatinineLowValueFemale()
        self.setCreatinineFairValueFemale()
        self.setCreatinineModerateValueFemale()
        self.setCreatinineHighValueFemale()
        self.setCreatininesFunction()
        self.setUricAcidUnit()
        self.setUricAcidMedicalAnnotations()
        self.setUricAcidRangeMale()
        self.setUricAcidRangeFemale()
        self.setUricAcidLowValueMale()
        self.setUricAcidFairValueMale()
        self.setUricAcidModerateValueMale()
        self.setUricAcidHighValueMale()
        self.setUricAcidLowValueFemale()
        self.setUricAcidFairValueFemale()
        self.setUricAcidModerateValueFemale()
        self.setUricAcidHighValueFemale()
        self.setUricAcidFunction()
        self.setBunCreatMedicalAnnotations()
        self.setBunCreatUnit()
        self.setBunCreatRangeMale()
        self.setBunCreatRangeFemale()
        self.setBunCreatLowValueMale()
        self.setBunCreatFairValueMale()
        self.setBunCreatModerateValueMale()
        self.setBunCreatHighValueMale()
        self.setBunCreatLowValueFemale()
        self.setBunCreatFairValueFemale()
        self.setBunCreatModerateValueFemale()
        self.setBunCreatHighValueFemale()
        self.setBunCreatFunction()
  
    def getParameters(self):
        return super(KidneyProfile, self).getParameters()

    def getAnnotations(self, parameter_name):
        return super(KidneyProfile, self).getAnnotations(parameter_name)


    def getParsedData(self, file_name, gender, password=""):
        report_parse = ReportParser(file_name, password)
        report_parse.reportList()
        parameter_name = self.getParameters()
        med_annot_bun = self.getAnnotations(parameter_name[0])
        med_annot_creatinine = self.getAnnotations(parameter_name[1])
        med_annot_uric_acid = self.getAnnotations(parameter_name[2])
        med_annot_bun_creat = self.getAnnotations(parameter_name[3])
        report_parse.parseBloodUreaNitrogen(med_annot_bun)
        report_parse.parseCreatinine(med_annot_creatinine)
        report_parse.parseUricAcid(med_annot_uric_acid)
        report_parse.parseBunCreatRatio(med_annot_bun_creat)
        medical_report_dict = report_parse.getMedicalParsedData()
        # set actual values from medical report
        bun_value = medical_report_dict.get("blood_urea",None)
        creatinine_value = medical_report_dict.get("creatinine",None)
        uric_acid_value = medical_report_dict.get("uric_acid",None)
        bun_creat_value = medical_report_dict.get("bun_creat_ratio",None)
        self.setBloodUreaValue(bun_value)
        self.setCreatinineValue(creatinine_value)
        self.setUricAcidValue(uric_acid_value)
        self.setBunCreatValue(bun_creat_value)
        self.bun_output["reading_value"] = str(self.getBloodUreaValue())
        self.bun_output["reading_unit"] = self.getBloodUreaUnit()
        self.bun_output["range_male"] = self.getBloodUreaRangeMale()
        self.bun_output["range_female"] = self.getBloodUreaRangeFemale()
        self.creatinine_output["reading_value"] = str(self.getCreatinineValue())
        self.creatinine_output["reading_unit"] = self.getCreatinineUnit()
        self.creatinine_output["range_male"] = self.getCreatinineRangeMale()
        self.creatinine_output["range_female"] = self.getCreatinineRangeFemale()
        self.uric_acid_output["reading_value"] = str(self.getUricAcidValue())
        self.uric_acid_output["reading_unit"] = self.getUricAcidUnit()
        self.uric_acid_output["range_male"] = self.getUricAcidRangeMale()
        self.uric_acid_output["range_female"] = self.getUricAcidRangeFemale()
        self.bun_creat_output["reading_value"] = str(self.getBunCreatValue())
        self.bun_creat_output["reading_unit"] = self.getBunCreatUnit()
        self.bun_creat_output["range_male"] = self.getBunCreatRangeMale()
        self.bun_creat_output["range_female"] = self.getBunCreatRangeFemale()
        if gender == "Female":
            self.bun_output["low_fair_moderate_high"] = [self.getBloodUreaLowValueFemale(), self.getBloodUreaFairValueFemale(), self.getBloodUreaModerateValueFemale(), self.getBloodUreaHighValueFemale()]
            if self.getBloodUreaValue() <= float(self.getBloodUreaLowValueFemale().split("-")[1]):
                self.bun_output["risk"] = Low
            if self.getBloodUreaValue() >= float(self.getBloodUreaFairValueFemale().split("-")[0]) and self.getBloodUreaValue() <= float(self.getBloodUreaFairValueFemale().split("-")[1]):
                self.bun_output["risk"] = Fair
            if self.getBloodUreaValue() >= float(self.getBloodUreaModerateValueFemale().split("-")[0]) and self.getBloodUreaValue() <= float(self.getBloodUreaModerateValueFemale().split("-")[1]):
                self.bun_output["risk"] = Moderate
            if self.getBloodUreaValue() > float(self.getBloodUreaHighValueFemale()):
                self.bun_output["risk"] = High
            if self.getBloodUreaValue() == None:
                self.bun_output["risk"] = n_a
            self.parsed_output["blood_urea_nitrogen"] = self.bun_output

            self.creatinine_output["low_fair_moderate_high"] = [self.getCreatinineLowValueFemale(), self.getCreatinineFairValueFemale(), self.getCreatinineModerateValueFemale(), self.getCreatinineHighValueFemale()]
            if self.getCreatinineValue() <= float(self.getCreatinineLowValueFemale().split("-")[1]):
                self.creatinine_output["risk"] = Low
            if self.getCreatinineValue() >= float(self.getCreatinineFairValueFemale().split("-")[0]) and self.getCreatinineValue() <= float(self.getCreatinineFairValueFemale().split("-")[1]):
                self.creatinine_output["risk"] = Fair
            if self.getCreatinineValue() >= float(self.getCreatinineModerateValueFemale().split("-")[0]) and self.getCreatinineValue() <= float(self.getCreatinineModerateValueFemale().split("-")[1]):
                self.creatinine_output["risk"] = Moderate
            if self.getCreatinineValue() > float(self.getCreatinineHighValueFemale()):
                self.creatinine_output["risk"] = High
            if self.getCreatinineValue() == None:
                self.creatinine_output["risk"] = n_a
            self.parsed_output["creatinine"] = self.creatinine_output
    
            self.uric_acid_output["low_fair_moderate_high"] = [self.getUricAcidLowValueFemale(), self.getUricAcidFairValueFemale(), self.getUricAcidModerateValueFemale(), self.getUricAcidHighValueFemale()]
            if self.getUricAcidValue() <= float(self.getUricAcidLowValueFemale().split("-")[1]):
                self.uric_acid_output["risk"] = Low
            if self.getUricAcidValue() >= float(self.getUricAcidFairValueFemale().split("-")[0]) and self.getUricAcidValue() <= float(self.getUricAcidFairValueFemale().split("-")[1]):
                self.uric_acid_output["risk"] = Fair
            if self.getUricAcidValue() >= float(self.getUricAcidModerateValueFemale().split("-")[0]) and self.getUricAcidValue() <= float(self.getUricAcidModerateValueFemale().split("-")[1]):
                self.uric_acid_output["risk"] = Moderate
            if self.getUricAcidValue() > float(self.getUricAcidHighValueFemale()):
                self.uric_acid_output["risk"] = High
            if self.getUricAcidValue() == None:
                self.uric_acid_output["risk"] = n_a
            self.parsed_output["uric_acid"] = self.uric_acid_output

            self.bun_creat_output["low_fair_moderate_high"] = [self.getBunCreatLowValueFemale(), self.getBunCreatFairValueFemale(), self.getBunCreatModerateValueFemale(), self.getBunCreatHighValueFemale()]
            if self.getBunCreatValue() <= float(self.getBunCreatLowValueFemale().split("-")[1]):
                self.bun_creat_output["risk"] = Low
            if self.getBunCreatValue() >= float(self.getBunCreatFairValueFemale().split("-")[0]) and self.getBunCreatValue() <= float(self.getBunCreatFairValueFemale().split("-")[1]):
                self.bun_creat_output["risk"] = Fair
            if self.getBunCreatValue() >= float(self.getBunCreatModerateValueFemale().split("-")[0]) and self.getBunCreatValue() <= float(self.getBunCreatModerateValueFemale().split("-")[1]):
                self.bun_creat_output["risk"] = Moderate
            if self.getBunCreatValue() > float(self.getBunCreatHighValueFemale()):
                self.bun_creat_output["risk"] = High
            if self.getBunCreatValue() == None:
                self.bun_creat_output["risk"] = n_a
            self.parsed_output["bun_creat_ratio"] = self.bun_creat_output
        else:
            self.bun_output["low_fair_moderate_high"] = [self.getBloodUreaLowValueMale(), self.getBloodUreaFairValueMale(), self.getBloodUreaModerateValueMale(), self.getBloodUreaHighValueMale()]
            if self.getBloodUreaValue() <= float(self.getBloodUreaLowValueMale().split("-")[1]):
                self.bun_output["risk"] = Low
            if self.getBloodUreaValue() >= float(self.getBloodUreaFairValueMale().split("-")[0]) and self.getBloodUreaValue() <= float(self.getBloodUreaFairValueMale().split("-")[1]):
                self.bun_output["risk"] = Fair
            if self.getBloodUreaValue() >= float(self.getBloodUreaModerateValueMale().split("-")[0]) and self.getBloodUreaValue() <= float(self.getBloodUreaModerateValueMale().split("-")[1]):
                self.bun_output["risk"] = Moderate
            if self.getBloodUreaValue() > float(self.getBloodUreaHighValueMale()):
                self.bun_output["risk"] = High
            if self.getBloodUreaValue() == None:
                self.bun_output["risk"] = n_a
            self.parsed_output["blood_urea_nitrogen"] = self.bun_output

            self.creatinine_output["low_fair_moderate_high"] = [self.getCreatinineLowValueMale(), self.getCreatinineFairValueMale(), self.getCreatinineModerateValueMale(), self.getCreatinineHighValueMale()]
            if self.getCreatinineValue() <= float(self.getCreatinineLowValueMale().split("-")[1]):
                self.creatinine_output["risk"] = Low
            elif self.getCreatinineValue() >= float(self.getCreatinineFairValueMale().split("-")[0]) and self.getCreatinineValue() <= float(self.getCreatinineFairValueMale().split("-")[1]):
                self.creatinine_output["risk"] = Fair
            if self.getCreatinineValue() >= float(self.getCreatinineModerateValueMale().split("-")[0]) and self.getCreatinineValue() <= float(self.getCreatinineModerateValueMale().split("-")[1]):
                self.creatinine_output["risk"] = Moderate
            if self.getCreatinineValue() > float(self.getCreatinineHighValueMale()):
                self.creatinine_output["risk"] = High
            if self.getCreatinineValue() == None:
                self.creatinine_output["risk"] = n_a
            self.parsed_output["creatinine"] = self.creatinine_output
    
            self.uric_acid_output["low_fair_moderate_high"] = [self.getUricAcidLowValueMale(), self.getUricAcidFairValueMale(), self.getUricAcidModerateValueMale(), self.getUricAcidHighValueMale()]
            if self.getUricAcidValue() <= float(self.getUricAcidLowValueMale().split("-")[1]):
                self.uric_acid_output["risk"] = Low
            if self.getUricAcidValue() >= float(self.getUricAcidFairValueMale().split("-")[0]) and self.getUricAcidValue() <= float(self.getUricAcidFairValueMale().split("-")[1]):
                self.uric_acid_output["risk"] = Fair
            if self.getUricAcidValue() >= float(self.getUricAcidModerateValueMale().split("-")[0]) and self.getUricAcidValue() <= float(self.getUricAcidModerateValueMale().split("-")[1]):
                self.uric_acid_output["risk"] = Moderate
            if self.getUricAcidValue() > float(self.getUricAcidHighValueMale()):
                self.uric_acid_output["risk"] = High
            if self.getUricAcidValue() == None:
                self.uric_acid_output["risk"] = n_a
            self.parsed_output["uric_acid"] = self.uric_acid_output

            self.bun_creat_output["low_fair_moderate_high"] = [self.getBunCreatLowValueMale(), self.getBunCreatFairValueMale(), self.getBunCreatModerateValueMale(), self.getBunCreatHighValueMale()]
            if self.getBunCreatValue() <= float(self.getBunCreatLowValueMale().split("-")[1]):
                self.bun_creat_output["risk"] = Low
            if self.getBunCreatValue() >= float(self.getBunCreatFairValueMale().split("-")[0]) and self.getBunCreatValue() <= float(self.getBunCreatFairValueMale().split("-")[1]):
                self.bun_creat_output["risk"] = Fair
            if self.getBunCreatValue() >= float(self.getBunCreatModerateValueMale().split("-")[0]) and self.getBunCreatValue() <= float(self.getBunCreatModerateValueMale().split("-")[1]):
                self.bun_creat_output["risk"] = Moderate
            if self.getBunCreatValue() > float(self.getBunCreatHighValueMale()):
                self.bun_creat_output["risk"] = High
            if self.getBunCreatValue() == None:
                self.bun_creat_output["risk"] = n_a
            self.parsed_output["bun_creat_ratio"] = self.bun_creat_output
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
        self.version_number = self.profile.get("version_number")
	
    # Function sets blood urea actual value
    def setBloodUreaValue(self, blood_urea): 
        self.blood_urea = blood_urea

    # Function sets unit of Glucose Fasting
    def setBloodUreaUnit(self):
        self.blood_urea_unit = self.parameters[0].get('value_meta_data',[])[0].get('unit',"")

    # Function sets list of medical annotations for blood urea
    def setBloodUreaMedicalAnotation(self):
        self.blood_urea_medical_annot =  self.parameters[0].get('medical_annotation',[])

    # Function sets range of values for blood urea for male  
    def setBloodUreaRangeMale(self):
        self.blood_urea_range_male =  self.parameters[0].get('value_meta_data',[])[0].get('range',"")
 
    # Function sets range of values for blood urea for female  
    def setBloodUreaRangeFemale(self):
        self.blood_urea_range_female =  self.parameters[0].get('value_meta_data',[])[1].get('range',"")

    # Function sets low risk values range for blood urea
    def setBloodUreaLowValueMale(self):
        self.blood_urea_low_male =  self.parameters[0].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for blood urea
    def setBloodUreaFairValueMale(self):
        self.blood_urea_fair_male = self.parameters[0].get('value_meta_data',[])[0].get('fair_value',"")

    # Function sets moderate risk values range for blood urea
    def setBloodUreaModerateValueMale(self):
        self.blood_urea_moderate_male = self.parameters[0].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for blood urea
    def setBloodUreaHighValueMale(self):
        self.blood_urea_high_male =  self.parameters[0].get('value_meta_data',[])[0].get('high_value',"")[1:]

    # Function sets low risk values range for blood urea
    def setBloodUreaLowValueFemale(self):
        self.blood_urea_low_female =  self.parameters[0].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for blood urea
    def setBloodUreaFairValueFemale(self):
        self.blood_urea_fair_female = self.parameters[0].get('value_meta_data',[])[1].get('fair_value',"")

    # Function sets moderate risk values range for blood urea
    def setBloodUreaModerateValueFemale(self):
        self.blood_urea_moderate_female = self.parameters[0].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for blood urea
    def setBloodUreaHighValueFemale(self):
        self.blood_urea_high_female =  self.parameters[0].get('value_meta_data',[])[1].get('high_value',"")[1:]


    # Function sets function name to parse blood urea value from medical reports
    def setBloodUreaFunction(self):
        self.blood_urea_function =  self.parameters[0].get("value_function",{}).get("function_name","")

    # Function sets creatine
    def setCreatinineValue(self, creat):
        self.creatinine = creat
 
    # Function sets list of medical annotations for glucose post prandial
    def setCreatinineMedicalAnnotations(self):
        self.creat_medical_annot =  self.parameters[1].get('medical_annotation',[])

    # Function sets unit of creatinine
    def setCreatinineUnit(self):
        self.creat_unit =  self.parameters[1].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for creatinine for male
    def setCreatinineRangeMale(self):
        self.creat_range_male =  self.parameters[1].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for creatinine for female
    def setCreatinineRangeFemale(self):
        self.creat_range_female =  self.parameters[1].get('value_meta_data',[])[1].get('range',"") 

    # Function sets low risk values range for creatinine
    def setCreatinineLowValueMale(self):
        self.creat_low_male = self.parameters[1].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for creatinine
    def setCreatinineFairValueMale(self):
        self.creat_fair_male = self.parameters[1].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function retuns moderate risk value ranges for creatinine
    def setCreatinineModerateValueMale(self):
        self.creat_moderate_male = self.parameters[1].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk value ranges for creatinine
    def setCreatinineHighValueMale(self):
        self.creat_high_male = self.parameters[1].get('value_meta_data',[])[0].get('high_value',"")[1:]

    # Function sets low risk values range for creatinine
    def setCreatinineLowValueFemale(self):
        self.creat_low_female = self.parameters[1].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for creatinine
    def setCreatinineFairValueFemale(self):
        self.creat_fair_female = self.parameters[1].get('value_meta_data',[])[1].get('fair_value',"")

    # Function retuns moderate risk value ranges for creatinine
    def setCreatinineModerateValueFemale(self):
        self.creat_moderate_female = self.parameters[1].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk value ranges for creatinine
    def setCreatinineHighValueFemale(self):
        self.creat_high_female = self.parameters[1].get('value_meta_data',[])[1].get('high_value',"")[1:]

    # Function sets function name to parse creatinine value from medical report
    def setCreatininesFunction(self):
        self.creat_func = self.parameters[1].get("value_function",{}).get("function_name","")
   
    # Function sets uric acid actual value
    def setUricAcidValue(self, uric_acid):
        self.uric_acid = uric_acid
           
    # Function sets list of medical annotations for uric acid
    def setUricAcidMedicalAnnotations(self):
        self.uric_acid_medical_annot = self.parameters[2].get('medical_annotation',[])

    # Function sets unit of uric acid
    def setUricAcidUnit(self):
        self.uric_acid_unit = self.parameters[2].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for uric acid for male
    def setUricAcidRangeMale(self):
        self.uric_acid_range_male = self.parameters[2].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for uric acid for female
    def setUricAcidRangeFemale(self):
        self.uric_acid_range_female = self.parameters[2].get('value_meta_data',[])[1].get('range',"") 
    
    # Function sets low risk values range for uric acid
    def setUricAcidLowValueMale(self):
        self.uric_acid_low_male = self.parameters[2].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for uric acid
    def setUricAcidFairValueMale(self):
        self.uric_acid_fair_male = self.parameters[2].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function sets moderate risk values range for uric acid
    def setUricAcidModerateValueMale(self):
        self.uric_acid_moderate_male = self.parameters[2].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for uric acid
    def setUricAcidHighValueMale(self):
        self.uric_acid_high_male = self.parameters[2].get('value_meta_data',[])[0].get('high_value',"")[1:]
       # Function sets low risk values range for uric acid

    def setUricAcidLowValueFemale(self):
        self.uric_acid_low_female = self.parameters[2].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for uric acid
    def setUricAcidFairValueFemale(self):
        self.uric_acid_fair_female = self.parameters[2].get('value_meta_data',[])[1].get('fair_value',"")
    
    # Function sets moderate risk values range for uric acid
    def setUricAcidModerateValueFemale(self):
        self.uric_acid_moderate_female =  self.parameters[2].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for uric acid
    def setUricAcidHighValueFemale(self):
        self.uric_acid_high_female = self.parameters[2].get('value_meta_data',[])[1].get('high_value',"")[1:]
    
    # Function sets function name for parsing uric acid value from medical reports
    def setUricAcidFunction(self):
        self.uric_acid_func =  self.parameters[2].get("value_function",{}).get("function_name","")

    # Function sets bun/creatinine ratio actual value
    def setBunCreatValue(self,bun_creat):
        self.bun_creat_ratio = bun_creat
    
    # Function sets list of medical annottions for bun/creatinine ratio
    def setBunCreatMedicalAnnotations(self):
        self.bun_creat_ratio_medical_annot = self.parameters[3].get('medical_annotation',[])

    # Function sets unit of bun/creatinine ratio
    def setBunCreatUnit(self):
        self.bun_creat_ratio_unit = self.parameters[3].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for bun/creatinine ratio for male
    def setBunCreatRangeMale(self):
        self.bun_creat_ratio_range_male = self.parameters[3].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for bun/creatinine ratio for female
    def setBunCreatRangeFemale(self):
        self.bun_creat_ratio_range_female = self.parameters[3].get('value_meta_data',[])[1].get('range',"") 
    
    # Function sets low risk values range for bun/creatinine ratio
    def setBunCreatLowValueMale(self):
        self.bun_creat_ratio_low_male = self.parameters[3].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for bun/creatinine ratio
    def setBunCreatFairValueMale(self):
        self.bun_creat_ratio_fair_male = self.parameters[3].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function sets moderate risk values range for bun/creatinine ratio
    def setBunCreatModerateValueMale(self):
        self.bun_creat_ratio_moderate_male = self.parameters[3].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for bun/creatinine ratio
    def setBunCreatHighValueMale(self):
        self.bun_creat_ratio_high_male = self.parameters[3].get('value_meta_data',[])[0].get('high_value',"")[1:]
  
    # Function sets low risk values range for bun/creatinine ratio
    def setBunCreatLowValueFemale(self):
        self.bun_creat_ratio_low_female = self.parameters[3].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for bun/creatinine ratio
    def setBunCreatFairValueFemale(self):
        self.bun_creat_ratio_fair_female = self.parameters[3].get('value_meta_data',[])[1].get('fair_value',"")
    
    # Function sets moderate risk values range for bun/creatinine ratio
    def setBunCreatModerateValueFemale(self):
        self.bun_creat_ratio_moderate_female = self.parameters[3].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for bun/creatinine ratio
    def setBunCreatHighValueFemale(self):
        self.bun_creat_ratio_high_female = self.parameters[3].get('value_meta_data',[])[1].get('high_value',"")[1:] 
 
    # Function sets function name for parsing bun/creatinine ratio value from medical reports
    def setBunCreatFunction(self):
        self.bun_creat_ratio_func = self.parameters[3].get("value_function",{}).get("function_name","")


    # Fuction returns category id
    def getCategoryid(self):
        return self.category_id 

    # Function returns category name
    def getCategoryName(self):
        return self.category_name 

    # Function returns Version number
    def getVersionNumber(self):
        return self.version_number 
	
    # Function returns blood urea actual value
    def getBloodUreaValue(self): 
        return self.blood_urea 
    # Function returns unit of Glucose Fasting
    def getBloodUreaUnit(self):
        return self.blood_urea_unit 
 
    # Function returns list of medical annotations for blood urea
    def getBloodUreaMedicalAnotation(self):
        return self.blood_urea_medical_annot 

    # Function returns range of values for blood urea for male  
    def getBloodUreaRangeMale(self):
        return self.blood_urea_range_male
 
    # Function returns range of values for blood urea for female  
    def getBloodUreaRangeFemale(self):
        return self.blood_urea_range_female 

    # Function returns low risk values range for blood urea
    def getBloodUreaLowValueMale(self):
        return self.blood_urea_low_male

    # Function returns fair risk values range for blood urea
    def getBloodUreaFairValueMale(self):
        return self.blood_urea_fair_male

    # Function returns moderate risk values range for blood urea
    def getBloodUreaModerateValueMale(self):
        return self.blood_urea_moderate_male

    # Function returns high risk values range for blood urea
    def getBloodUreaHighValueMale(self):
        return self.blood_urea_high_male

    # Function returns low risk values range for blood urea
    def getBloodUreaLowValueFemale(self):
        return self.blood_urea_low_female

    # Function returns fair risk values range for blood urea
    def getBloodUreaFairValueFemale(self):
        return self.blood_urea_fair_female

    # Function returns moderate risk values range for blood urea
    def getBloodUreaModerateValueFemale(self):
        return self.blood_urea_moderate_female

    # Function returns high risk values range for blood urea
    def getBloodUreaHighValueFemale(self):
        return self.blood_urea_high_female

    # Function returns function name to parse blood urea value from medical reports
    def getBloodUreaFunction(self):
        return self.blood_urea_function 

    # Function returns creatine
    def getCreatinineValue(self):
        return self.creatinine
 
    # Function returns list of medical annotations for glucose post prandial
    def getCreatinineMedicalAnnotations(self):
        return self.creat_medical_annot

    # Function returns unit of creatinine
    def getCreatinineUnit(self):
        return self.creat_unit

    # Function returns range of values for creatinine for male
    def getCreatinineRangeMale(self):
        return self.creat_range_male

    # Function returns range of values for creatinine for female
    def getCreatinineRangeFemale(self):
        return self.creat_range_female 

    # Function returns low risk values range for creatinine
    def getCreatinineLowValueMale(self):
        return self.creat_low_male 

    # Function returns fair risk values range for creatinine
    def getCreatinineFairValueMale(self):
        return self.creat_fair_male
    
    # Function retuns moderate risk value ranges for creatinine
    def getCreatinineModerateValueMale(self):
        return self.creat_moderate_male 

    # Function returns high risk value ranges for creatinine
    def getCreatinineHighValueMale(self):
        return self.creat_high_male 

    # Function returns low risk values range for creatinine
    def getCreatinineLowValueFemale(self):
        return self.creat_low_female 

    # Function returns fair risk values range for creatinine
    def getCreatinineFairValueFemale(self):
        return self.creat_fair_female
    
    # Function retuns moderate risk value ranges for creatinine
    def getCreatinineModerateValueFemale(self):
        return self.creat_moderate_female 

    # Function returns high risk value ranges for creatinine
    def getCreatinineHighValueFemale(self):
        return self.creat_high_female 

    # Function returns function name to parse creatinine value from medical report
    def getCreatininesFunction(self):
        return self.creat_func
   
    # Function returns uric acid actual value
    def getUricAcidValue(self):
        return self.uric_acid
           
    # Function returns list of medical annotations for uric acid
    def getUricAcidMedicalAnnotations(self):
        return self.uric_acid_medical_annot

    # Function returns unit of uric acid
    def getUricAcidUnit(self):
        return self.uric_acid_unit

    # Function returns range of values for uric acid for male
    def getUricAcidRangeMale(self):
        return self.uric_acid_range_male 

    # Function returns range of values for uric acid for female
    def getUricAcidRangeFemale(self):
        return self.uric_acid_range_female
    
    # Function returns low risk values range for uric acid
    def getUricAcidLowValueMale(self):
        return self.uric_acid_low_male

    # Function returns fair risk values range for uric acid
    def getUricAcidFairValueMale(self):
        return self.uric_acid_fair_male 
    
    # Function returns moderate risk values range for uric acid
    def getUricAcidModerateValueMale(self):
        return self.uric_acid_moderate_male 

    # Function returns high risk values range for uric acid
    def getUricAcidHighValueMale(self):
        return self.uric_acid_high_male 

    # Function returns low risk values range for uric acid
    def getUricAcidLowValueFemale(self):
        return self.uric_acid_low_female

    # Function returns fair risk values range for uric acid
    def getUricAcidFairValueFemale(self):
        return self.uric_acid_fair_female 
    
    # Function returns moderate risk values range for uric acid
    def getUricAcidModerateValueFemale(self):
        return self.uric_acid_moderate_female 

    # Function returns high risk values range for uric acid
    def getUricAcidHighValueFemale(self):
        return self.uric_acid_high_female 
 
    # Function returns function name for parsing uric acid value from medical reports
    def getUricAcidFunction(self):
        return self.uric_acid_func

    # Function returns bun/creatinine ratio actual value
    def getBunCreatValue(self):
        return self.bun_creat_ratio
    
    # Function returns list of medical annottions for bun/creatinine ratio
    def getBunCreatMedicalAnnotations(self):
        return self.bun_creat_ratio_medical_annot

    # Function returns unit of bun/creatinine ratio
    def getBunCreatUnit(self):
        return self.bun_creat_ratio_unit

    # Function returns range of values for bun/creatinine ratio for male
    def getBunCreatRangeMale(self):
        return self.bun_creat_ratio_range_male

    # Function returns range of values for bun/creatinine ratio for female
    def getBunCreatRangeFemale(self):
        return self.bun_creat_ratio_range_female
    
    # Function returns low risk values range for bun/creatinine ratio
    def getBunCreatLowValueMale(self):
        return self.bun_creat_ratio_low_male

    # Function returns fair risk values range for bun/creatinine ratio
    def getBunCreatFairValueMale(self):
        return self.bun_creat_ratio_fair_male 
    
    # Function returns moderate risk values range for bun/creatinine ratio
    def getBunCreatModerateValueMale(self):
        return self.bun_creat_ratio_moderate_male 

    # Function returns high risk values range for bun/creatinine ratio
    def getBunCreatHighValueMale(self):
        return self.bun_creat_ratio_high_male

     # Function returns low risk values range for bun/creatinine ratio
    def getBunCreatLowValueFemale(self):
        return self.bun_creat_ratio_low_female

    # Function returns fair risk values range for bun/creatinine ratio
    def getBunCreatFairValueFemale(self):
        return self.bun_creat_ratio_fair_female 
    
    # Function returns moderate risk values range for bun/creatinine ratio
    def getBunCreatModerateValueFemale(self):
        return self.bun_creat_ratio_moderate_female 

    # Function returns high risk values range for bun/creatinine ratio
    def getBunCreatHighValueFemale(self):
        return self.bun_creat_ratio_high_female

    # Function returns function name for parsing bun/creatinine ratio value from medical reports
    def getBunCreatFunction(self):
        return self.bun_creat_ratio_func

#Instantiate the class
#kidney_profile = KidneyProfile()

#call loadMetaData Function 
#kidney_profile.loadMetaData()

#call getParsedData function to get parsed output values
#kidney_parsed_value = kidney_profile.getParsedData("/home/isana/383713-619691-wZ5JNvLI.pdf")
#print json.dumps({"kidney_parsed_values" : kidney_parsed_value}, indent = 4)

