import json
from collections import OrderedDict
from __config import *
from __medical_report_parser import *
from __medical_report_template import *

class DiabetesProfile(MedicalReportTemplate):
    """
        A class for diabetes profile:
    """
    def __init__(self):
        try:
            super(DiabetesProfile, self).__init__()
            self.file_path = json_file_data.get("medical_parser_detail","")[0].get("file_name","")
            self.glucose_fasting = None
            self.glucose_pp = None
            self.hbA1c = None
            self.mpg = None
            self.fasting_insulin = None
            self.category_id = "" 
            self.category_name = ""
            self.version_number = ""
            self.glucose_fast_unit = ""
            self.glucose_fast_medical_annot = []
            self.glucose_fast_range_male = ""
            self.glucose_fast_range_female = ""
            self.glucose_fast_low_male = ""
            self.glucose_fast_fair_male = ""
            self.glucose_fast_moderate_male = ""
            self.glucose_fast_high_male = ""
            self.glucose_fast_low_female = ""
            self.glucose_fast_fair_female = ""
            self.glucose_fast_moderate_female = ""
            self.glucose_fast_high_female = ""
            self.glucose_fast_func = ""
            self.glucose_pp_unit = ""
            self.glucose_pp_medical_annot = []
            self.glucose_pp_range_male = ""
            self.glucose_pp_range_female = ""
            self.glucose_pp_low_male = ""
            self.glucose_pp_fair_male = ""
            self.glucose_pp_moderate_male = ""
            self.glucose_pp_high_male = ""
            self.glucose_pp_low_female = ""
            self.glucose_pp_fair_female = ""
            self.glucose_pp_moderate_female = ""
            self.glucose_pp_high_female = ""
            self.glucose_pp_func = ""
            self.hba1c_unit = ""
            self.hba1c_medical_annot = []
            self.hba1c_range_male = ""
            self.hba1c_range_female = ""
            self.hba1c_low_male = ""
            self.hba1c_fair_male = ""
            self.hba1c_moderate_male = ""
            self.hba1c_high_male = ""
            self.hba1c_low_female = ""
            self.hba1c_fair_female = ""
            self.hba1c_moderate_female = ""
            self.hba1c_high_female = ""
            self.hba1c_func = ""
            self.mpg_unit = ""
            self.mpg_medical_annot = []
            self.mpg_range_male = ""
            self.mpg_range_female = ""
            self.mpg_low_male = ""
            self.mpg_fair_male = ""
            self.mpg_moderate_male = ""
            self.mpg_high_male = ""
            self.mpg_low_female = ""
            self.mpg_fair_female = ""
            self.mpg_moderate_female = ""
            self.mpg_high_female = ""
            self.mpg_func = ""
            self.fasting_insulin_unit = ""
            self.fasting_insulin_medical_annot = []
            self.fasting_insulin_range_male = ""
            self.fasting_insulin_range_female = ""
            self.fasting_insulin_low_male = ""
            self.fasting_insulin_fair_male = ""
            self.fasting_insulin_moderate_male = ""
            self.fasting_insulin_high_male = ""
            self.fasting_insulin_low_female = ""
            self.fasting_insulin_fair_female = ""
            self.fasting_insulin_moderate_female = ""
            self.fasting_insulin_high_female = ""
            self.fasting_insulin_func = ""
            self.gluc_fast_output = OrderedDict()
            self.gluc_pp_output = OrderedDict()
            self.hba1c_output = OrderedDict()
            self.mpg_output = OrderedDict()
            self.fasting_insulin_output = OrderedDict()
        except Exception as err:
            print err

    def loadMetaData(self):
        super(DiabetesProfile, self).loadMetaData()    
        self.setCategoryid()
        self.setCategoryName()
        self.setVersionNumber()
        self.setGlucoseFastingUnit()
        self.setGlucoseFastingMedicalAnotation()
        self.setGlucoseFastingRangeMale()
        self.setGlucoseFastingRangeFemale()
        self.setGlucoseFastingLowValueMale()
        self.setGlucoseFastingFairValueMale()
        self.setGlucoseFastingModerateValueMale()
        self.setGlucoseFastingHighValueMale()
        self.setGlucoseFastingLowValueFemale()
        self.setGlucoseFastingFairValueFemale()
        self.setGlucoseFastingModerateValueFemale()
        self.setGlucoseFastingHighValueFemale()
        self.setGlucoseFastingFunction()
        self.setGlucosePostprandialUnit()
        self.setGlucosePostprandialMedicalAnnotations()
        self.setGlucosePostprandialRangeMale()
        self.setGlucosePostprandialRangeFemale()
        self.setGlucosePostprandialLowValueMale()
        self.setGlucosePostprandialFairValueMale()
        self.setGlucosePostprandialModerateValueMale()
        self.setGlucosePostprandialHighValueMale()
        self.setGlucosePostprandialLowValueFemale()
        self.setGlucosePostprandialFairValueFemale()
        self.setGlucosePostprandialModerateValueFemale()
        self.setGlucosePostprandialHighValueFemale()
        self.setGlucosePostprandialFunction()
        self.setHemoglobinA1cMedicalAnnotations()
        self.setHemoglobinA1cUnit()
        self.setHemoglobinA1cRangeMale()
        self.setHemoglobinA1cRangeFemale()
        self.setHemoglobinA1cLowValueMale()
        self.setHemoglobinA1cFairValueMale()
        self.setHemoglobinA1cModerateValueMale()
        self.setHemoglobinA1cHighValueMale()
        self.setHemoglobinA1cLowValueFemale()
        self.setHemoglobinA1cFairValueFemale()
        self.setHemoglobinA1cModerateValueFemale()
        self.setHemoglobinA1cHighValueFemale()
        self.setHemoglobinA1cFunction()
        self.setMpgMedicalAnnotations()
        self.setMpgUnit()
        self.setMpgRangeMale()
        self.setMpgRangeFemale()
        self.setMpgLowValueMale()
        self.setMpgFairValueMale()
        self.setMpgModerateValueMale()
        self.setMpgHighValueMale()
        self.setMpgLowValueFemale()
        self.setMpgFairValueFemale()
        self.setMpgModerateValueFemale()
        self.setMpgHighValueFemale()
        self.setMpgFunction()
        self.setFastingInsulinMedicalAnnotations()
        self.setFastingInsulinUnit()
        self.setFastingInsulinRangeMale()
        self.setFastingInsulinRangeFemale()
        self.setFastingInsulinLowValueMale()
        self.setFastingInsulinFairValueMale()
        self.setFastingInsulinModerateValueMale()
        self.setFastingInsulinHighValueMale()
        self.setFastingInsulinLowValueFemale()
        self.setFastingInsulinFairValueFemale()
        self.setFastingInsulinModerateValueFemale()
        self.setFastingInsulinHighValueFemale()
        self.setFastingInsulinFunction()
 
    def getParameters(self):
        return super(DiabetesProfile, self).getParameters()

    def getAnnotations(self, parameter_name):
        return super(DiabetesProfile, self).getAnnotations(parameter_name)       

    def getParsedData(self, file_name, gender, password=""):
        report_parse = ReportParser(file_name, password)
        report_parse.reportList()
        parameter_name = self.getParameters()
        med_annot_gluc_fast = self.getAnnotations(parameter_name[0])
        med_annot_gluc_pp = self.getAnnotations(parameter_name[1])
        med_annot_hba1c = self.getAnnotations(parameter_name[2])
        med_annot_mpg = self.getAnnotations(parameter_name[3]) 
        med_annot_fast_ins = self.getAnnotations(parameter_name[4])
        gluc_fast = parameter_name[0]
        report_parse.parseMedicalParameter(med_annot_gluc_fast, gluc_fast)
        gluc_pp = parameter_name[1]
        report_parse.parseMedicalParameter(med_annot_gluc_pp, gluc_pp)
        hba1_c = parameter_name[2]
        report_parse.parseMedicalParameter(med_annot_hba1c, hba1_c)
        mpg = parameter_name[3]
        report_parse.parseMedicalParameter(med_annot_mpg, mpg)
        fast_ins = parameter_name[4]
        report_parse.parseMedicalParameter(med_annot_fast_ins, fast_ins)
        medical_report_dict = report_parse.getMedicalParsedData()
        # set actual values from medical report
        gluc_fast_value = medical_report_dict.get(gluc_fast,None)
        gluc_pp_value = medical_report_dict.get(gluc_pp,None)
        hba1c_value = medical_report_dict.get(hba1_c,None)
        mpg_value = medical_report_dict.get(mpg,None)
        fast_insul_value = medical_report_dict.get(fast_ins, None)
        self.setGlucoseFastingValue(gluc_fast_value)
        self.setGlucosePostprandialValue(gluc_pp_value)
        self.setHemoglobinA1cValue(hba1c_value)
        self.setMpgValue(mpg_value)
        self.setFastingInsulinValue(fast_insul_value)
        self.gluc_fast_output["reading_value"] = str(self.getGlucoseFastingValue())
        self.gluc_fast_output["reading_unit"] = self.getGlucoseFastingUnit()
        self.gluc_fast_output["range_male"] = self.getGlucoseFastingRangeMale()
        self.gluc_fast_output["range_female"] = self.getGlucoseFastingRangeFemale()
        self.gluc_pp_output["reading_value"] = str(self.getGlucosePostprandialValue())
        self.gluc_pp_output["reading_unit"] = self.getGlucosePostprandialUnit()
        self.gluc_pp_output["range_male"] = self.getGlucosePostprandialRangeMale()
        self.gluc_pp_output["range_female"] = self.getGlucosePostprandialRangeFemale()
        self.hba1c_output["reading_value"] = str(self.getHemoglobinA1cValue())
        self.hba1c_output["reading_unit"] = self.getHemoglobinA1cUnit()
        self.hba1c_output["range_male"] = self.getHemoglobinA1cRangeMale()
        self.hba1c_output["range_female"] = self.getHemoglobinA1cRangeFemale()
        self.mpg_output["reading_value"] = str(self.getMpgValue())
        self.mpg_output["reading_unit"] = self.getMpgUnit()
        self.mpg_output["range_male"] = self.getMpgRangeMale()
        self.mpg_output["range_female"] = self.getMpgRangeFemale()
        self.fasting_insulin_output["reading_value"] = str(self.getFastingInsulinValue())
        self.fasting_insulin_output["reading_unit"] = self.getFastingInsulinUnit()
        self.fasting_insulin_output["range_male"] = self.getFastingInsulinRangeMale()
        self.fasting_insulin_output["range_female"] = self.getFastingInsulinRangeFemale()

        if gender == "Female":
            self.gluc_fast_output["low_fair_moderate_high"] = [self.getGlucoseFastingLowValueFemale(), self.getGlucoseFastingFairValueFemale(), self.getGlucoseFastingModerateValueFemale(), self.getGlucoseFastingHighValueFemale()]
            if self.getGlucoseFastingValue() <= float(self.getGlucoseFastingLowValueFemale().split("-")[1]): 
                self.gluc_fast_output["risk"] = Low
            if self.getGlucoseFastingValue() >= float(self.getGlucoseFastingFairValueFemale().split("-")[0]) and self.getGlucoseFastingValue() <= float(self.getGlucoseFastingFairValueFemale().split("-")[1]): 
                self.gluc_fast_output["risk"] = Fair
            if self.getGlucoseFastingValue() >= float(self.getGlucoseFastingModerateValueFemale().split("-")[0]) and self.getGlucoseFastingValue() <= float(self.getGlucoseFastingModerateValueFemale().split("-")[1]): 
                self.gluc_fast_output["risk"] = Moderate
            if self.getGlucoseFastingValue() > float(self.getGlucoseFastingHighValueFemale()): 
                self.gluc_fast_output["risk"] = High
            if self.getGlucoseFastingValue() == None:
                self.gluc_fast_output["risk"] = n_a
            self.parsed_output["glucose_fasting"] = self.gluc_fast_output

            self.gluc_pp_output["low_fair_moderate_high"] = [self.getGlucosePostprandialLowValueFemale(), self.getGlucosePostprandialFairValueFemale(), self.getGlucosePostprandialModerateValueFemale(), self.getGlucosePostprandialHighValueFemale()]
            if self.getGlucosePostprandialValue() <= float(self.getGlucosePostprandialLowValueFemale().split("-")[1]):  
                self.gluc_pp_output["risk"] = Low
            if self.getGlucosePostprandialValue() >= float(self.getGlucosePostprandialFairValueFemale().split("-")[0]) and self.getGlucosePostprandialValue() <= float(self.getGlucosePostprandialFairValueFemale().split("-")[1]): 
                self.gluc_pp_output["risk"] = Fair
            if self.getGlucosePostprandialValue() >= float(self.getGlucosePostprandialModerateValueFemale().split("-")[0]) and self.getGlucosePostprandialValue() <= float(self.getGlucosePostprandialModerateValueFemale().split("-")[1]): 
                self.gluc_pp_output["risk"] = Moderate
            if self.getGlucosePostprandialValue() > float(self.getGlucosePostprandialHighValueFemale()): 
                self.gluc_pp_output["risk"] = High
            if self.getGlucosePostprandialValue() == None:
                self.gluc_pp_output["risk"] = n_a
            self.parsed_output["glucose_postprandial"] = self.gluc_pp_output
            
            self.hba1c_output["low_fair_moderate_high"] = [self.getHemoglobinA1cLowValueFemale(), self.getHemoglobinA1cFairValueFemale(), self.getHemoglobinA1cModerateValueFemale(), self.getHemoglobinA1cHighValueFemale()]
            if self.getHemoglobinA1cValue() <= float(self.getHemoglobinA1cLowValueFemale().split("-")[1]):  
                self.hba1c_output["risk"] = Low
            if self.getHemoglobinA1cValue() >= float(self.getHemoglobinA1cFairValueFemale().split("-")[0]) and self.getHemoglobinA1cValue() <= float(self.getHemoglobinA1cFairValueFemale().split("-")[1]): 
                self.hba1c_output["risk"] = Fair
            if self.getHemoglobinA1cValue() >= float(self.getHemoglobinA1cModerateValueFemale().split("-")[0]) and self.getHemoglobinA1cValue() <= float(self.getHemoglobinA1cModerateValueFemale().split("-")[1]): 
                self.hba1c_output["risk"] = Moderate
            if self.getHemoglobinA1cValue() > float(self.getHemoglobinA1cHighValueFemale()): 
                self.hba1c_output["risk"] = High
            if self.getHemoglobinA1cValue() == None:
                self.hba1c_output["risk"] = n_a
            self.parsed_output["hemoglobin_a1c"] = self.hba1c_output

            self.mpg_output["low_fair_moderate_high"] = [self.getMpgLowValueFemale(), self.getMpgFairValueFemale(), self.getMpgModerateValueFemale(), self.getMpgHighValueFemale()]
            if self.getMpgValue() <= float(self.getMpgLowValueFemale().split("-")[1]):  
                self.mpg_output["risk"] = Low
            if self.getMpgValue() >= float(self.getMpgFairValueFemale().split("-")[0]) and self.getMpgValue() <= float(self.getMpgFairValueFemale().split("-")[1]): 
                self.mpg_output["risk"] = Fair
            if self.getMpgValue() >= float(self.getMpgModerateValueFemale().split("-")[0]) and self.getMpgValue() <= float(self.getMpgModerateValueFemale().split("-")[1]): 
                self.mpg_output["risk"] = Moderate
            if self.getMpgValue() > float(self.getMpgHighValueFemale()): 
                self.mpg_output["risk"] = High
            if self.getMpgValue() == None:
                self.mpg_output["risk"] = n_a
            self.parsed_output["mean_plasma_glucose"] = self.mpg_output

            self.fasting_insulin_output["low_fair_moderate_high"] = [self.getFastingInsulinLowValueFemale(), self.getFastingInsulinFairValueFemale(), self.getFastingInsulinModerateValueFemale(), self.getFastingInsulinHighValueFemale()]
            if self.getFastingInsulinValue() <= float(self.getFastingInsulinLowValueFemale().split("-")[1]):
                self.fasting_insulin_output["risk"] = Low
            if self.getFastingInsulinValue() >= float(self.getFastingInsulinFairValueFemale().split("-")[0]) and self.getFastingInsulinValue() <= float(self.getMpgFFastingInsulinValueFemale().split("-")[1]):
                self.fasting_insulin_output["risk"] = Fair
            if self.getFastingInsulinValue() >= float(self.getFastingInsulinModerateValueFemale().split("-")[0]) and self.getFastingInsulinValue() <= float(self.getFastingInsulinModerateValueFemale().split("-")[1]):
                self.fasting_insulin_output["risk"] = Moderate
            if self.getFastingInsulinValue() > float(self.getFastingInsulinHighValueFemale()):
                self.fasting_insulin_output["risk"] = High
            if self.getFastingInsulinValue() == None:
                self.fasting_insulin_output["risk"] = n_a
            self.parsed_output["fasting_insulin"] = self.fasting_insulin_output

        else:
            self.gluc_fast_output["low_fair_moderate_high"] = [self.getGlucoseFastingLowValueMale(), self.getGlucoseFastingFairValueMale(), self.getGlucoseFastingModerateValueMale(), self.getGlucoseFastingHighValueMale()]
            if self.getGlucoseFastingValue() <= float(self.getGlucoseFastingLowValueMale().split("-")[1]): 
                self.gluc_fast_output["risk"] = Low
            if self.getGlucoseFastingValue() >= float(self.getGlucoseFastingFairValueMale().split("-")[0]) and self.getGlucoseFastingValue() <= float(self.getGlucoseFastingFairValueMale().split("-")[1]): 
                self.gluc_fast_output["risk"] = Fair
            if self.getGlucoseFastingValue() >= float(self.getGlucoseFastingModerateValueMale().split("-")[0]) and self.getGlucoseFastingValue() <= float(self.getGlucoseFastingModerateValueMale().split("-")[1]): 
                self.gluc_fast_output["risk"] = Moderate
            if self.getGlucoseFastingValue() > float(self.getGlucoseFastingHighValueMale()): 
                self.gluc_fast_output["risk"] = High
            if self.getGlucoseFastingValue() == None:
                self.gluc_fast_output["risk"] = n_a
            self.parsed_output["glucose_fasting"] = self.gluc_fast_output

            self.gluc_pp_output["low_fair_moderate_high"] = [self.getGlucosePostprandialLowValueMale(), self.getGlucosePostprandialFairValueMale(), self.getGlucosePostprandialModerateValueMale(), self.getGlucosePostprandialHighValueMale()]
            if self.getGlucosePostprandialValue() <= float(self.getGlucosePostprandialLowValueMale().split("-")[1]):  
                self.gluc_pp_output["risk"] = Low
            if self.getGlucosePostprandialValue() >= float(self.getGlucosePostprandialFairValueMale().split("-")[0]) and self.getGlucosePostprandialValue() <= float(self.getGlucosePostprandialFairValueMale().split("-")[1]): 
                self.gluc_pp_output["risk"] = Fair
            if self.getGlucosePostprandialValue() >= float(self.getGlucosePostprandialModerateValueMale().split("-")[0]) and self.getGlucosePostprandialValue() <= float(self.getGlucosePostprandialModerateValueMale().split("-")[1]): 
                self.gluc_pp_output["risk"] = Moderate
            if self.getGlucosePostprandialValue() > float(self.getGlucosePostprandialHighValueMale()): 
                self.gluc_pp_output["risk"] = High
            if self.getGlucosePostprandialValue() == None:
                self.gluc_pp_output["risk"] = n_a
            self.parsed_output["glucose_postprandial"] = self.gluc_pp_output
            
            self.hba1c_output["low_fair_moderate_high"] = [self.getHemoglobinA1cLowValueMale(), self.getHemoglobinA1cFairValueMale(), self.getHemoglobinA1cModerateValueMale(), self.getHemoglobinA1cHighValueMale()]
            if self.getHemoglobinA1cValue() <= float(self.getHemoglobinA1cLowValueMale().split("-")[1]):  
                self.hba1c_output["risk"] = Low
            if self.getHemoglobinA1cValue() >= float(self.getHemoglobinA1cFairValueMale().split("-")[0]) and self.getHemoglobinA1cValue() <= float(self.getHemoglobinA1cFairValueMale().split("-")[1]): 
                self.hba1c_output["risk"] = Fair
            if self.getHemoglobinA1cValue() >= float(self.getHemoglobinA1cModerateValueMale().split("-")[0]) and self.getHemoglobinA1cValue() <= float(self.getHemoglobinA1cModerateValueMale().split("-")[1]): 
                self.hba1c_output["risk"] = Moderate
            if self.getHemoglobinA1cValue() > float(self.getHemoglobinA1cHighValueMale()): 
                self.hba1c_output["risk"] = High
            if self.getHemoglobinA1cValue() == None:
                self.hba1c_output["risk"] = n_a
            self.parsed_output["hemoglobin_a1c"] = self.hba1c_output

            self.mpg_output["low_fair_moderate_high"] = [self.getMpgLowValueMale(), self.getMpgFairValueMale(), self.getMpgModerateValueMale(), self.getMpgHighValueMale()]
            if self.getMpgValue() <= float(self.getMpgLowValueMale().split("-")[1]):  
                self.mpg_output["risk"] = Low
            if self.getMpgValue() >= float(self.getMpgFairValueMale().split("-")[0]) and self.getMpgValue() <= float(self.getMpgFairValueMale().split("-")[1]): 
                self.mpg_output["risk"] = Fair
            if self.getMpgValue() >= float(self.getMpgModerateValueMale().split("-")[0]) and self.getMpgValue() <= float(self.getMpgModerateValueMale().split("-")[1]): 
                self.mpg_output["risk"] = Moderate
            if self.getMpgValue() > float(self.getMpgHighValueMale()): 
                self.mpg_output["risk"] = High
            if self.getMpgValue() == None:
                self.mpg_output["risk"] = n_a
            self.parsed_output["mean_plasma_glucose"] = self.mpg_output

            self.fasting_insulin_output["low_fair_moderate_high"] = [self.getFastingInsulinLowValueMale(), self.getFastingInsulinFairValueMale(), self.getFastingInsulinModerateValueMale(), self.getFastingInsulinHighValueMale()]
            if self.getFastingInsulinValue() <= float(self.getFastingInsulinLowValueMale().split("-")[1]):
                self.fasting_insulin_output["risk"] = Low
            if self.getFastingInsulinValue() >= float(self.getFastingInsulinFairValueMale().split("-")[0]) and self.getFastingInsulinValue() <= float(self.getFastingInsulinFairValueMale().split("-")[1]):
                self.fasting_insulin_output["risk"] = Fair
            if self.getFastingInsulinValue() >= float(self.getFastingInsulinModerateValueMale().split("-")[0]) and self.getFastingInsulinValue() <= float(self.getFastingInsulinModerateValueMale().split("-")[1]):
                self.fasting_insulin_output["risk"] = Moderate
            if self.getFastingInsulinValue() > float(self.getFastingInsulinHighValueMale()):
                self.fasting_insulin_output["risk"] = High
            if self.getFastingInsulinValue() == None:
                self.fasting_insulin_output["risk"] = n_a
            self.parsed_output["fasting_insulin"] = self.fasting_insulin_output

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
        
    # Function to sets glucose fasting actual value
    def setGlucoseFastingValue(self, glucose_fasting):
        self.glucose_fasting = glucose_fasting

    # Function sets unit of Glucose Fasting
    def setGlucoseFastingUnit(self):
        self.glucose_fast_unit = self.parameters[0].get('value_meta_data',[])[0].get('unit',"")
 
    # Function sets list of medical annotations for glucose fasting
    def setGlucoseFastingMedicalAnotation(self):
        self.glucose_fast_medical_annot = self.parameters[0].get('medical_annotation',[])
 
    # Function sets range of values for glucose fasting for male  
    def setGlucoseFastingRangeMale(self):
        self.glucose_fast_range_male = self.parameters[0].get('value_meta_data',[])[0].get('range',"")
    
    # Function sets range of values for glucose fasting for female  
    def setGlucoseFastingRangeFemale(self):
        self.glucose_fast_range_female = self.parameters[0].get('value_meta_data',[])[1].get('range',"")
                  
    # Function sets low risk values range for glucose fasting
    def setGlucoseFastingLowValueMale(self):
        self.glucose_fast_low_male = self.parameters[0].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for glucose fasting
    def setGlucoseFastingFairValueMale(self):
        self.glucose_fast_fair_male = self.parameters[0].get('value_meta_data',[])[0].get('fair_value',"")
   
    # Function sets moderate risk values range for glucose fasting
    def setGlucoseFastingModerateValueMale(self):
        self.glucose_fast_moderate_male = self.parameters[0].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for glucose fasting
    def setGlucoseFastingHighValueMale(self):
        self.glucose_fast_high_male = self.parameters[0].get('value_meta_data',[])[0].get('high_value',"")[1:]

    # Function sets low risk values range for glucose fasting
    def setGlucoseFastingLowValueFemale(self):
        self.glucose_fast_low_female = self.parameters[0].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for glucose fasting
    def setGlucoseFastingFairValueFemale(self):
        self.glucose_fast_fair_female = self.parameters[0].get('value_meta_data',[])[1].get('fair_value',"")
   
    # Function sets moderate risk values range for glucose fasting
    def setGlucoseFastingModerateValueFemale(self):
        self.glucose_fast_moderate_female = self.parameters[0].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for glucose fasting
    def setGlucoseFastingHighValueFemale(self):
        self.glucose_fast_high_female = self.parameters[0].get('value_meta_data',[])[1].get('high_value',"")[1:]

    # Function sets function name to parse glucose fasting value from medical reports
    def setGlucoseFastingFunction(self):
        self.glucose_fast_func = self.parameters[0].get("value_function",{}).get("function_name","")

    # Function to sets glucose fasting actual value
    def setGlucosePostprandialValue(self,glucose_pp):
        self.glucose_pp = glucose_pp

    # Function sets list of medical annotations for glucose post prandial
    def setGlucosePostprandialMedicalAnnotations(self):
        self.glucose_pp_medical_annot = self.parameters[1].get('medical_annotation',[])

    # Function sets unit of glucose post prandial
    def setGlucosePostprandialUnit(self):
        self.glucose_pp_unit = self.parameters[1].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for glucose postprandial for male
    def setGlucosePostprandialRangeMale(self):
        self.glucose_pp_range_male = self.parameters[1].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for glucose postprandial for female
    def setGlucosePostprandialRangeFemale(self):
        self.glucose_pp_range_female = self.parameters[1].get('value_meta_data',[])[1].get('range',"") 

    # Function sets low risk values range for glucose postprandial
    def setGlucosePostprandialLowValueMale(self):
        self.glucose_pp_low_male = self.parameters[1].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for glucose postprandial
    def setGlucosePostprandialFairValueMale(self):
        self.glucose_pp_fair_male = self.parameters[1].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function retuns moderate risk value ranges for glucose postprandial
    def setGlucosePostprandialModerateValueMale(self):
        self.glucose_pp_moderate_male = self.parameters[1].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk value ranges for glucose postprandial
    def setGlucosePostprandialHighValueMale(self):
        self.glucose_pp_high_male = self.parameters[1].get('value_meta_data',[])[0].get('high_value',"")[1:]

    # Function sets low risk values range for glucose postprandial
    def setGlucosePostprandialLowValueFemale(self):
        self.glucose_pp_low_female = self.parameters[1].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for glucose postprandial
    def setGlucosePostprandialFairValueFemale(self):
        self.glucose_pp_fair_female = self.parameters[1].get('value_meta_data',[])[1].get('fair_value',"")
    
    # Function retuns moderate risk value ranges for glucose postprandial
    def setGlucosePostprandialModerateValueFemale(self):
        self.glucose_pp_moderate_female = self.parameters[1].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk value ranges for glucose postprandial
    def setGlucosePostprandialHighValueFemale(self):
        self.glucose_pp_high_female = self.parameters[1].get('value_meta_data',[])[1].get('high_value',"")[1:]

    # Function sets function name to parse HbA1c value from medical report
    def setGlucosePostprandialFunction(self):
        self.glucose_pp_func = self.parameters[1].get("value_function",{}).get("function_name","")
    
    # Function sets list of medical annotations for HbA1c
    def setHemoglobinA1cMedicalAnnotations(self):
        self.hba1c_medical_annot = self.parameters[2].get('medical_annotation',[])

    # Function sets actual value of HbA1c
    def setHemoglobinA1cValue(self, hbA1c):
        self.hbA1c = hbA1c

    # Function sets unit of HbA1c
    def setHemoglobinA1cUnit(self):
        self.hba1c_unit = self.parameters[2].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for HbA1c for male
    def setHemoglobinA1cRangeMale(self):
        self.hba1c_range_male = self.parameters[2].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for HbA1c for female
    def setHemoglobinA1cRangeFemale(self):
        self.hba1c_range_female = self.parameters[2].get('value_meta_data',[])[1].get('range',"") 
    
    # Function sets low risk values range for HbA1c
    def setHemoglobinA1cLowValueMale(self):
        self.hba1c_low_male = self.parameters[2].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for HbA1c
    def setHemoglobinA1cFairValueMale(self):
        self.hba1c_fair_male = self.parameters[2].get('value_meta_data',[])[0].get('fair_value',"")
   
    # Function sets moderate risk values range for HbA1c
    def setHemoglobinA1cModerateValueMale(self):
        self.hba1c_moderate_male = self.parameters[2].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for HbA1c
    def setHemoglobinA1cHighValueMale(self):
        self.hba1c_high_male = self.parameters[2].get('value_meta_data',[])[0].get('high_value',"")[1:]
  
    # Function sets low risk values range for HbA1c
    def setHemoglobinA1cLowValueFemale(self):
        self.hba1c_low_female = self.parameters[2].get('value_meta_data',[])[1].get('low_value',"")
 
    # Function sets fair risk values range for HbA1c
    def setHemoglobinA1cFairValueFemale(self):
        self.hba1c_fair_female = self.parameters[2].get('value_meta_data',[])[1].get('fair_value',"")
   
    # Function sets moderate risk values range for HbA1c
    def setHemoglobinA1cModerateValueFemale(self):
        self.hba1c_moderate_female = self.parameters[2].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for HbA1c
    def setHemoglobinA1cHighValueFemale(self):
        self.hba1c_high_female = self.parameters[2].get('value_meta_data',[])[1].get('high_value',"")[1:]
 
    # Function sets function name for parsing HbA1c value from medical reports
    def setHemoglobinA1cFunction(self):
        self.hba1c_func = self.parameters[2].get("value_function",{}).get("function_name","")

    # Function sets actual value for mpg from medical report
    def setMpgValue(self, mpg):
        self.mpg = mpg

    # Function sets list of medical annotations for mpg
    def setMpgMedicalAnnotations(self):
        self.mpg_medical_annot = self.parameters[3].get('medical_annotation',[])

    # Function sets unit of mpg
    def setMpgUnit(self):
        self.mpg_unit = self.parameters[3].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for Mpg(mean plasma glucose) for male
    def setMpgRangeMale(self):
        self.mpg_range_male = self.parameters[3].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for Mpg for female
    def setMpgRangeFemale(self):
        self.mpg_range_female = self.parameters[3].get('value_meta_data',[])[1].get('range',"") 
    
    # Function sets low risk values range for Mpg
    def setMpgLowValueMale(self):
        self.mpg_low_male = self.parameters[3].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for Mpg
    def setMpgFairValueMale(self):
        self.mpg_fair_male = self.parameters[3].get('value_meta_data',[])[0].get('fair_value',"")
   
    # Function sets moderate risk values range for Mpg
    def setMpgModerateValueMale(self):
        self.mpg_moderate_male = self.parameters[3].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for Mpg
    def setMpgHighValueMale(self):
        self.mpg_high_male = self.parameters[3].get('value_meta_data',[])[0].get('high_value',"")[1:]
   
    # Function sets low risk values range for Mpg
    def setMpgLowValueFemale(self):
        self.mpg_low_female = self.parameters[3].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for Mpg
    def setMpgFairValueFemale(self):
        self.mpg_fair_female = self.parameters[3].get('value_meta_data',[])[1].get('fair_value',"")
   
    # Function sets moderate risk values range for Mpg
    def setMpgModerateValueFemale(self):
        self.mpg_moderate_female = self.parameters[3].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for Mpg
    def setMpgHighValueFemale(self):
        self.mpg_high_female = self.parameters[3].get('value_meta_data',[])[1].get('high_value',"")[1:]
 
    # Function sets function name for parsing Mpg value from medical reports
    def setMpgFunction(self):
        self.mpg_func = self.parameters[3].get("value_function",{}).get("function_name","")

    # Function sets actual value for mpg from medical report
    def setFastingInsulinValue(self, fast_insulin):
        self.fasting_insulin = fast_insulin

    # Function sets list of medical annotations for mpg
    def setFastingInsulinMedicalAnnotations(self):
        self.fasting_insulin_medical_annot = self.parameters[4].get('medical_annotation',[])

    # Function sets unit of mpg
    def setFastingInsulinUnit(self):
        self.fasting_insulin_unit = self.parameters[4].get('value_meta_data',[])[0].get('unit',"")

    # Function sets range of values for Mpg(mean plasma glucose) for male
    def setFastingInsulinRangeMale(self):
        self.fasting_insulin_range_male = self.parameters[4].get('value_meta_data',[])[0].get('range',"")

    # Function sets range of values for Mpg for female
    def setFastingInsulinRangeFemale(self):
        self.fasting_insulin_range_female = self.parameters[4].get('value_meta_data',[])[1].get('range',"")

    # Function sets low risk values range for Mpg
    def setFastingInsulinLowValueMale(self):
        self.fasting_insulin_low_male = self.parameters[4].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for Mpg
    def setFastingInsulinFairValueMale(self):
        self.fasting_insulin_fair_male = self.parameters[4].get('value_meta_data',[])[0].get('fair_value',"")

    # Function sets moderate risk values range for Mpg
    def setFastingInsulinModerateValueMale(self):
        self.fasting_insulin_moderate_male = self.parameters[4].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for Mpg
    def setFastingInsulinHighValueMale(self):
        self.fasting_insulin_high_male = self.parameters[4].get('value_meta_data',[])[0].get('high_value',"")[1:]

    # Function sets low risk values range for Mpg
    def setFastingInsulinLowValueFemale(self):
        self.fasting_insulin_low_female = self.parameters[4].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for Mpg
    def setFastingInsulinFairValueFemale(self):
        self.fasting_insulin_fair_female = self.parameters[4].get('value_meta_data',[])[1].get('fair_value',"")

    # Function sets moderate risk values range for Mpg
    def setFastingInsulinModerateValueFemale(self):
        self.fasting_insulin_moderate_female = self.parameters[4].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for Mpg
    def setFastingInsulinHighValueFemale(self):
        self.fasting_insulin_high_female = self.parameters[4].get('value_meta_data',[])[1].get('high_value',"")[1:]

    # Function sets function name for parsing Mpg value from medical reports
    def setFastingInsulinFunction(self):
        self.fasting_insulin_func = self.parameters[4].get("value_function",{}).get("function_name","")

    # Fuction returns category id
    def getCategoryid(self):
        return self.category_id 

    # Function returns category name
    def getCategoryName(self):
        return self.category_name

    # Function returns Version number
    def getVersionNumber(self):
        return self.version_number
        
    # Function to get glucose fasting actual value
    def getGlucoseFastingValue(self):
        return self.glucose_fasting

    # Function returns unit of Glucose Fasting
    def getGlucoseFastingUnit(self):
        return self.glucose_fast_unit
 
    # Function returns list of medical annotations for glucose fasting
    def getGlucoseFastingMedicalAnotation(self):
        return self.glucose_fast_medical_annot
 
    # Function returns range of values for glucose fasting for male  
    def getGlucoseFastingRangeMale(self):
        return self.glucose_fast_range_male
    
    # Function returns range of values for glucose fasting for female  
    def getGlucoseFastingRangeFemale(self):
        return self.glucose_fast_range_female 
                  
    # Function returns low risk values range for glucose fasting
    def getGlucoseFastingLowValueMale(self):
        return self.glucose_fast_low_male

    # Function returns fair risk values range for glucose fasting
    def getGlucoseFastingFairValueMale(self):
        return self.glucose_fast_fair_male
   
    # Function returns moderate risk values range for glucose fasting
    def getGlucoseFastingModerateValueMale(self):
        return self.glucose_fast_moderate_male

    # Function returns high risk values range for glucose fasting
    def getGlucoseFastingHighValueMale(self):
        return self.glucose_fast_high_male 

    # Function returns low risk values range for glucose fasting
    def getGlucoseFastingLowValueFemale(self):
        return self.glucose_fast_low_female

    # Function returns fair risk values range for glucose fasting
    def getGlucoseFastingFairValueFemale(self):
        return self.glucose_fast_fair_female

    # Function returns moderate risk values range for glucose fasting
    def getGlucoseFastingModerateValueFemale(self):
        return self.glucose_fast_moderate_female

    # Function returns high risk values range for glucose fasting
    def getGlucoseFastingHighValueFemale(self):
        return self.glucose_fast_high_female

    # Function returns function name to parse glucose fasting value from medical reports
    def getGlucoseFastingFunction(self):
        return self.glucose_fast_func 

    # Function to get glucose fasting actual value
    def getGlucosePostprandialValue(self):
        return self.glucose_pp

    # Function returns list of medical annotations for glucose post prandial
    def getGlucosePostprandialMedicalAnnotations(self):
        return self.glucose_pp_medical_annot

    # Function returns unit of glucose post prandial
    def getGlucosePostprandialUnit(self):
        return self.glucose_pp_unit

    # Function returns range of values for glucose postprandial for male
    def getGlucosePostprandialRangeMale(self):
        return self.glucose_pp_range_male

    # Function returns range of values for glucose postprandial for female
    def getGlucosePostprandialRangeFemale(self):
        return self.glucose_pp_range_female

    # Function returns low risk values range for glucose postprandial
    def getGlucosePostprandialLowValueMale(self):
        return self.glucose_pp_low_male

    # Function returns fair risk values range for glucose postprandial
    def getGlucosePostprandialFairValueMale(self):
        return self.glucose_pp_fair_male
    
    # Function retuns moderate risk value ranges for glucose postprandial
    def getGlucosePostprandialModerateValueMale(self):
        return self.glucose_pp_moderate_male

    # Function returns high risk value ranges for glucose postprandial
    def getGlucosePostprandialHighValueMale(self):
        return self.glucose_pp_high_male

    # Function returns low risk values range for glucose postprandial
    def getGlucosePostprandialLowValueFemale(self):
        return self.glucose_pp_low_female

    # Function returns fair risk values range for glucose postprandial
    def getGlucosePostprandialFairValueFemale(self):
        return self.glucose_pp_fair_female

    # Function retuns moderate risk value ranges for glucose postprandial
    def getGlucosePostprandialModerateValueFemale(self):
        return self.glucose_pp_moderate_female

    # Function returns high risk value ranges for glucose postprandial
    def getGlucosePostprandialHighValueFemale(self):
        return self.glucose_pp_high_female

    # Function returns function name to parse HbA1c value from medical report
    def getGlucosePostprandialFunction(self):
        return self.glucose_pp_func
    
    # Function returns list of medical annotations for HbA1c
    def getHemoglobinA1cMedicalAnnotations(self):
        return self.hba1c_medical_annot

    # Function returns actual value of HbA1c
    def getHemoglobinA1cValue(self):
        return self.hbA1c

    # Function returns unit of HbA1c
    def getHemoglobinA1cUnit(self):
        return self.hba1c_unit

    # Function returns range of values for HbA1c for male
    def getHemoglobinA1cRangeMale(self):
        return self.hba1c_range_male

    # Function returns range of values for HbA1c for female
    def getHemoglobinA1cRangeFemale(self):
        return self.hba1c_range_female
    
    # Function returns low risk values range for HbA1c
    def getHemoglobinA1cLowValueMale(self):
        return self.hba1c_low_male 

    # Function returns fair risk values range for HbA1c
    def getHemoglobinA1cFairValueMale(self):
        return self.hba1c_fair_male
   
    # Function returns moderate risk values range for HbA1c
    def getHemoglobinA1cModerateValueMale(self):
        return self.hba1c_moderate_male

    # Function returns high risk values range for HbA1c
    def getHemoglobinA1cHighValueMale(self):
        return self.hba1c_high_male 
   
    # Function returns low risk values range for HbA1c
    def getHemoglobinA1cLowValueFemale(self):
        return self.hba1c_low_female

    # Function returns fair risk values range for HbA1c
    def getHemoglobinA1cFairValueFemale(self):
        return self.hba1c_fair_female

    # Function returns moderate risk values range for HbA1c
    def getHemoglobinA1cModerateValueFemale(self):
        return self.hba1c_moderate_female

    # Function returns high risk values range for HbA1c
    def getHemoglobinA1cHighValueFemale(self):
        return self.hba1c_high_female
 
    # Function returns function name for parsing HbA1c value from medical reports
    def getHemoglobinA1cFunction(self):
        return self.hba1c_func 

    # Function returns actual value for mpg from medical report
    def getMpgValue(self):
        return self.mpg 

    # Function returns list of medical annotations for mpg
    def getMpgMedicalAnnotations(self):
        return self.mpg_medical_annot

    # Function returns unit of mpg
    def getMpgUnit(self):
        return self.mpg_unit 

    # Function returns range of values for Mpg(mean plasma glucose) for male
    def getMpgRangeMale(self):
        return self.mpg_range_male

    # Function returns range of values for Mpg for female
    def getMpgRangeFemale(self):
        return self.mpg_range_female
    
    # Function returns low risk values range for Mpg
    def getMpgLowValueMale(self):
        return self.mpg_low_male 

    # Function returns fair risk values range for Mpg
    def getMpgFairValueMale(self):
        return self.mpg_fair_male
   
    # Function returns moderate risk values range for Mpg
    def getMpgModerateValueMale(self):
        return self.mpg_moderate_male 

    # Function returns high risk values range for Mpg
    def getMpgHighValueMale(self):
        return self.mpg_high_male
   
   # Function returns low risk values range for Mpg
    def getMpgLowValueFemale(self):
        return self.mpg_low_female

    # Function returns fair risk values range for Mpg
    def getMpgFairValueFemale(self):
        return self.mpg_fair_female

    # Function returns moderate risk values range for Mpg
    def getMpgModerateValueFemale(self):
        return self.mpg_moderate_female

    # Function returns high risk values range for Mpg
    def getMpgHighValueFemale(self):
        return self.mpg_high_female
 
    # Function returns function name for parsing Mpg value from medical reports
    def getMpgFunction(self):
        return self.mpg_func

    # Function returns actual value for mpg from medical report
    def getFastingInsulinValue(self):
        return self.fasting_insulin
	
    # Function returns list of medical annotations for mpg
    def getFastingInsulinMedicalAnnotations(self):
        return self.fasting_insulin_medical_annot

    # Function returns unit of mpg
    def getFastingInsulinUnit(self):
        return self.fasting_insulin_unit

    # Function returns range of values for Mpg(mean plasma glucose) for male
    def getFastingInsulinRangeMale(self):
        return self.fasting_insulin_range_male

    # Function returns range of values for Mpg for female
    def getFastingInsulinRangeFemale(self):
        return self.fasting_insulin_range_female

    # Function returns low risk values range for Mpg
    def getFastingInsulinLowValueMale(self):
        return self.fasting_insulin_low_male

    # Function returns fair risk values range for Mpg
    def getFastingInsulinFairValueMale(self):
        return self.fasting_insulin_fair_male

    # Function returns moderate risk values range for Mpg
    def getFastingInsulinModerateValueMale(self):
        return self.fasting_insulin_moderate_male

    # Function returns high risk values range for Mpg
    def getFastingInsulinHighValueMale(self):
        return self.fasting_insulin_high_male

   # Function returns low risk values range for Mpg
    def getFastingInsulinLowValueFemale(self):
        return self.fasting_insulin_low_female

    # Function returns fair risk values range for Mpg
    def getFastingInsulinFairValueFemale(self):
        return self.fasting_insulin_fair_female

    # Function returns moderate risk values range for Mpg
    def getFastingInsulinModerateValueFemale(self):
        return self.fasting_insulin_moderate_female

    # Function returns high risk values range for Mpg
    def getFastingInsulinHighValueFemale(self):
        return self.fasting_insulin_high_female

    # Function returns function name for parsing Mpg value from medical reports
    def getFastingInsulinFunction(self):
        return self.fasting_insulin_func

#Instantiate diabetes profile class
#diabetes_profile = DiabetesProfile()

#call loadMetaData Function 
#diabetes_profile.loadMetaData()

#call getParsedData function to get parsed output values
#diabetes_parsed_value = diabetes_profile.getParsedData("/home/isana/sample-report-1.pdf", "ASHW")
#print json.dumps({"diabetes_parsed_values" : diabetes_parsed_value}, indent = 4)
