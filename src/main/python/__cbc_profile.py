import json
from collections import OrderedDict
from __config import *
from __medical_report_parser import *
from __medical_report_template import *

class CbcProfile(MedicalReportTemplate):
    """
        A class for Cbc profile:
    """
    def __init__(self):
        try:
            super(CbcProfile, self).__init__()
            self.file_path = json_file_data.get("medical_parser_detail","")[4].get("file_name","")
            self.hemoglobin = None
            self.platelet_count = None
            self.rbc_count = None
            self.wbc_count = None
            self.neutrophils = None
            self.neutrophils_absolute = None
            self.eosinophils = None
            self.eosinophils_absolute = None
            self.basophils = None
            self.basophils_absolute = None
            self.lymphocytes = None
            self.lymphocytes_absolute = None
            self.monocytes = None
            self.monocytes_absolute = None 
            self.category_id = ""
            self.category_name = ""
            self.version_number = ""
            self.hemoglobin_unit = ""
            self.hemoglobin_medical_annot = []
            self.hemoglobin_range_male = ""
            self.hemoglobin_range_female = ""
            self.hemoglobin_low_male = ""
            self.hemoglobin_fair_male = ""
            self.hemoglobin_high_male = ""
            self.hemoglobin_moderate_male = ""
            self.hemoglobin_low_female = ""
            self.hemoglobin_fair_female = ""
            self.hemoglobin_high_female = ""
            self.hemoglobin_moderate_female = ""
            self.hemoglobin_func = ""
            self.platelet_count_unit = ""
            self.platelet_count_medical_annot = []
            self.platelet_count_range_male = ""
            self.platelet_count_range_female = ""
            self.platelet_count_low_male = "" 
            self.platelet_count_fair_male = "" 
            self.platelet_count_moderate_male = "" 
            self.platelet_count_high_male = ""
            self.platelet_count_low_female = "" 
            self.platelet_count_fair_female = "" 
            self.platelet_count_moderate_female = "" 
            self.platelet_count_high_female = ""
            self.platelet_count_func = ""
            self.rbc_count_unit = ""
            self.rbc_count_medical_Annot = []
            self.rbc_count_range_male = ""
            self.rbc_count_range_female = ""
            self.rbc_count_low_male = ""
            self.rbc_count_fair_male = ""
            self.rbc_count_moderate_male = ""
            self.rbc_count_high_male = ""
            self.rbc_count_low_female = ""
            self.rbc_count_fair_female = ""
            self.rbc_count_moderate_female = ""
            self.rbc_count_high_female = ""
            self.rbc_count_func = ""
            self.wbc_count_unit = "" 
            self.wbc_count_medical_Annot = []
            self.wbc_count_range_male = ""
            self.wbc_count_range_female = ""
            self.wbc_count_low_male = ""
            self.wbc_count_fair_male = ""
            self.wbc_count_moderate_male = ""
            self.wbc_count_high_male = ""
            self.wbc_count_low_female = ""
            self.wbc_count_fair_female = ""
            self.wbc_count_moderate_female = ""
            self.wbc_count_high_female = ""
            self.wbc_count_func = ""
            self.neutroph_unit = ""
            self.neutroph_medical_annot = []
            self.neutroph_range_male = ""
            self.neutroph_range_female = ""
            self.neutroph_low_male = ""
            self.neutroph_fair_male = ""
            self.neutroph_moderate_male = ""
            self.neutroph_high_male = ""
            self.neutroph_low_female = ""
            self.neutroph_fair_female = ""
            self.neutroph_moderate_female = ""
            self.neutroph_high_female = ""
            self.neutroph_func = ""
            self.neutroph_abs_unit = ""
            self.neutroph_abs_medical_annot = []
            self.neutroph_abs_range_male = ""
            self.neutroph_abs_range_female = ""
            self.neutroph_abs_low_male = ""
            self.neutroph_abs_fair_male = ""
            self.neutroph_abs_moderate_male = ""
            self.neutroph_abs_high_male = ""
            self.neutroph_abs_low_female = ""
            self.neutroph_abs_fair_female = ""
            self.neutroph_abs_moderate_female = ""
            self.neutroph_abs_high_female = ""
            self.neutroph_abs_func = ""
            self.eosino_unit = ""
            self.eosino_medical_annot = []
            self.eosino_range_male = ""
            self.eosino_range_female = ""
            self.eosino_low_male = ""
            self.eosino_fair_male = ""
            self.eosino_moderate_male = ""
            self.eosino_high_male = ""
            self.eosino_low_female = ""
            self.eosino_fair_female = ""
            self.eosino_moderate_female = ""
            self.eosino_high_female = ""
            self.eosino_func = ""
            self.eosino_abs_unit = ""
            self.eosino_abs_medical_annot = []
            self.eosino_abs_range_male = ""
            self.eosino_abs_range_female = ""
            self.eosino_abs_low_male = ""
            self.eosino_abs_fair_male = ""
            self.eosino_abs_moderate_male = ""
            self.eosino_abs_high_male = ""
            self.eosino_abs_low_female = ""
            self.eosino_abs_fair_female = ""
            self.eosino_abs_moderate_female = ""
            self.eosino_abs_high_female = ""
            self.eosino_abs_func = ""
            self.basoph_unit = ""
            self.basoph_medical_annot = []
            self.basoph_range_male = ""
            self.basoph_range_female = ""
            self.basoph_low_male = ""
            self.basoph_fair_male = ""
            self.basoph_moderate_male = ""
            self.basoph_high_male = ""
            self.basoph_low_female = ""
            self.basoph_fair_female = ""
            self.basoph_moderate_female = ""
            self.basoph_high_female = ""
            self.basoph_func = ""
            self.basoph_abs_unit = ""
            self.basoph_abs_medical_annot = []
            self.basoph_abs_range_male = ""
            self.basoph_abs_range_female = ""
            self.basoph_abs_low_male = ""
            self.basoph_abs_fair_male = ""
            self.basoph_abs_moderate_male = ""
            self.basoph_abs_high_male = ""
            self.basoph_abs_low_female = ""
            self.basoph_abs_fair_female = ""
            self.basoph_abs_moderate_female = ""
            self.basoph_abs_high_female = ""
            self.basoph_abs_func = ""
            self.lymph_unit = ""
            self.lymph_medical_annot = []
            self.lymph_range_male = ""
            self.lymph_range_female = ""
            self.lymph_low_male = ""
            self.lymph_fair_male = ""
            self.lymph_moderate_male = ""
            self.lymph_high_male = ""
            self.lymph_low_female = ""
            self.lymph_fair_female = ""
            self.lymph_moderate_female = ""
            self.lymph_high_female = ""
            self.lymph_func = ""
            self.lymph_abs_unit = ""
            self.lymph_abs_medical_annot = []
            self.lymph_abs_range_male = ""
            self.lymph_abs_range_female = ""
            self.lymph_abs_low_male = ""
            self.lymph_abs_fair_male = ""
            self.lymph_abs_moderate_male = ""
            self.lymph_abs_high_male = ""
            self.lymph_abs_low_female = ""
            self.lymph_abs_fair_female = ""
            self.lymph_abs_moderate_female = ""
            self.lymph_abs_high_female = ""
            self.lymph_abs_func = ""
            self.monocy_unit = ""
            self.monocy_medical_annot = []
            self.monocy_range_male = ""
            self.monocy_range_female = ""
            self.monocy_low_male = ""
            self.monocy_fair_male = ""
            self.monocy_moderate_male = ""
            self.monocy_high_male = ""
            self.monocy_low_female = ""
            self.monocy_fair_female = ""
            self.monocy_moderate_female = ""
            self.monocy_high_female = ""
            self.monocy_func = ""
            self.monocy_abs_unit = ""
            self.monocy_abs_medical_annot = []
            self.monocy_abs_range_male = ""
            self.monocy_abs_range_female = ""
            self.monocy_abs_low_male = ""
            self.monocy_abs_fair_male = ""
            self.monocy_abs_moderate_male = ""
            self.monocy_abs_high_male = ""
            self.monocy_abs_low_female = ""
            self.monocy_abs_fair_female = ""
            self.monocy_abs_moderate_female = ""
            self.monocy_abs_high_female = ""
            self.monocy_abs_func = ""
            self.hemoglobin_output = OrderedDict()
            self.platelet_count_output = OrderedDict()
            self.rbc_count_output = OrderedDict()
            self.wbc_count_output = OrderedDict()
            self.neutrophils_output = OrderedDict()
            self.neutrophils_absolute_output = OrderedDict()
            self.eosinophils_output = OrderedDict()
            self.eosinophils_absolute_output = OrderedDict()
            self.basophils_output = OrderedDict()
            self.basophils_absolute_output = OrderedDict()
            self.lymphocytes_output = OrderedDict()
            self.lymphocytes_absolute_output = OrderedDict()
            self.monocytes_output = OrderedDict()
            self.monocytes_absolute_output = OrderedDict()
        except Exception as err:
            print err

    def loadMetaData(self):
        super(CbcProfile, self).loadMetaData()
        self.setCategoryid()
        self.setCategoryName()
        self.setVersionNumber()
        self.setHemoglobinUnit()
        self.setHemoglobinMedicalAnnotation()
        self.setHemoglobinRangeMale()
        self.setHemoglobinRangeFemale()
        self.setHemoglobinLowValueMale()
        self.setHemoglobinFairValueMale()
        self.setHemoglobinModerateValueMale()
        self.setHemoglobinHighValueMale()
        self.setHemoglobinLowValueFemale()
        self.setHemoglobinFairValueFemale()
        self.setHemoglobinModerateValueFemale()
        self.setHemoglobinHighValueFemale()
        self.setHemoglobinFunction()
        self.setPlateletCountUnit()
        self.setPlateletCountMedicalAnnotation()
        self.setPlateletCountRangeMale()
        self.setPlateletCountRangeFemale()
        self.setPlateletCountLowMale()
        self.setPlateletCountFairMale()
        self.setPlateletCountModerateMale()
        self.setPlateletCountHighMale()
        self.setPlateletCountLowFemale()
        self.setPlateletCountFairFemale()
        self.setPlateletCountModerateFemale()
        self.setPlateletCountHighFemale()
        self.setPlateletCountFunc()
        self.setRbcCountUnit()
        self.setRbcCountMedicalAnnotation()
        self.setRbcCountRangeMale()
        self.setRbcCountRangeFemale()
        self.setRbcCountLowMale()
        self.setRbcCountFairMale()
        self.setRbcCountModerateMale()
        self.setRbcCountHighMale()
        self.setRbcCountLowFemale()
        self.setRbcCountFairFemale()
        self.setRbcCountModerateFemale()
        self.setRbcCountHighFemale()
        self.setRbcCountFunc()
        self.setWbcCountUnit()
        self.setWbcCountMedicalAnnotation()
        self.setWbcCountRangeMale()
        self.setWbcCountRangeFemale()
        self.setWbcCountLowMale()
        self.setWbcCountFairMale()
        self.setWbcCountModerateMale()
        self.setWbcCountHighMale()
        self.setWbcCountLowFemale()
        self.setWbcCountFairFemale()
        self.setWbcCountModerateFemale()
        self.setWbcCountHighFemale()
        self.setWbcCountFunc()
        self.setNeutrophilsUnit()
        self.setNeutrophilsMedicalAnnotation()
        self.setNeutrophilsRangeMale()
        self.setNeutrophilsRangeFemale()
        self.setNeutrophilsLowMale()
        self.setNeutrophilsFairMale()
        self.setNeutrophilsModerateMale()
        self.setNeutrophilsHighMale()
        self.setNeutrophilsLowFemale()
        self.setNeutrophilsFairFemale()
        self.setNeutrophilsModerateFemale()
        self.setNeutrophilsHighFemale()
        self.setNeutrophilsFunc()
        self.setNeutrophilsAbsUnit()
        self.setNeutrophilsAbsMedicalAnnotation()
        self.setNeutrophilsAbsRangeMale()
        self.setNeutrophilsAbsRangeFemale()
        self.setNeutrophilsAbsLowMale()
        self.setNeutrophilsAbsFairMale()
        self.setNeutrophilsAbsModerateMale()
        self.setNeutrophilsAbsHighMale()
        self.setNeutrophilsAbsLowFemale()
        self.setNeutrophilsAbsFairFemale()
        self.setNeutrophilsAbsModerateFemale()
        self.setNeutrophilsAbsHighFemale()
        self.setNeutrophilsAbsFunc()
        self.setEosinophilsUnit()
        self.setEosinophilsMedicalAnnotation()
        self.setEosinophilsRangeMale()
        self.setEosinophilsRangeFemale()
        self.setEosinophilsLowMale()
        self.setEosinophilsFairMale()
        self.setEosinophilsModerateMale()
        self.setEosinophilsHighMale()
        self.setEosinophilsLowFemale()
        self.setEosinophilsFairFemale()
        self.setEosinophilsModerateFemale()
        self.setEosinophilsHighFemale()
        self.setEosinophilsFunc()
        self.setEosinophilsAbsUnit()
        self.setEosinophilsAbsMedicalAnnotation()
        self.setEosinophilsAbsRangeMale()
        self.setEosinophilsAbsRangeFemale()
        self.setEosinophilsAbsLowMale()
        self.setEosinophilsAbsFairMale()
        self.setEosinophilsAbsModerateMale()
        self.setEosinophilsAbsHighMale()
        self.setEosinophilsAbsLowFemale()
        self.setEosinophilsAbsFairFemale()
        self.setEosinophilsAbsModerateFemale()
        self.setEosinophilsAbsHighFemale()
        self.setEosinophilsAbsFunc()
        self.setBasophilsUnit()
        self.setBasophilsMedicalAnnotation()
        self.setBasophilsRangeMale()
        self.setBasophilsRangeFemale()
        self.setBasophilsLowMale()
        self.setBasophilsFairMale()
        self.setBasophilsModerateMale()
        self.setBasophilsHighMale()
        self.setBasophilsLowFemale()
        self.setBasophilsFairFemale()
        self.setBasophilsModerateFemale()
        self.setBasophilsHighFemale()
        self.setBasophilsFunc()
        self.setBasophilsAbsUnit()
        self.setBasophilsAbsMedicalAnnotation()
        self.setBasophilsAbsRangeMale()
        self.setBasophilsAbsRangeFemale()
        self.setBasophilsAbsLowMale()
        self.setBasophilsAbsFairMale()
        self.setBasophilsAbsModerateMale()
        self.setBasophilsAbsHighMale()
        self.setBasophilsAbsLowFemale()
        self.setBasophilsAbsFairFemale()
        self.setBasophilsAbsModerateFemale()
        self.setBasophilsAbsHighFemale()
        self.setBasophilsAbsFunc()
        self.setLymphocytesUnit()
        self.setLymphocytesMedicalAnnotation()
        self.setLymphocytesRangeMale()
        self.setLymphocytesRangeFemale()
        self.setLymphocytesLowMale()
        self.setLymphocytesFairMale()
        self.setLymphocytesModerateMale()
        self.setLymphocytesHighMale()
        self.setLymphocytesLowFemale()
        self.setLymphocytesFairFemale()
        self.setLymphocytesModerateFemale()
        self.setLymphocytesHighFemale()
        self.setLymphocytesFunc()
        self.setLymphocytesAbsUnit()
        self.setLymphocytesAbsMedicalAnnotation()
        self.setLymphocytesAbsRangeMale()
        self.setLymphocytesAbsRangeFemale()
        self.setLymphocytesAbsLowMale()
        self.setLymphocytesAbsFairMale()
        self.setLymphocytesAbsModerateMale()
        self.setLymphocytesAbsHighMale()
        self.setLymphocytesAbsLowFemale()
        self.setLymphocytesAbsFairFemale()
        self.setLymphocytesAbsModerateFemale()
        self.setLymphocytesAbsHighFemale()
        self.setLymphocytesAbsFunc()
        self.setMonocytesUnit()
        self.setMonocytesMedicalAnnotation()
        self.setMonocytesRangeMale()
        self.setMonocytesRangeFemale()
        self.setMonocytesLowMale()
        self.setMonocytesFairMale()
        self.setMonocytesModerateMale()
        self.setMonocytesHighMale()
        self.setMonocytesLowFemale()
        self.setMonocytesFairFemale()
        self.setMonocytesModerateFemale()
        self.setMonocytesHighFemale()
        self.setMonocytesFunc()
        self.setMonocytesAbsUnit()
        self.setMonocytesAbsMedicalAnnotation()
        self.setMonocytesAbsRangeMale()
        self.setMonocytesAbsRangeFemale()
        self.setMonocytesAbsLowMale()
        self.setMonocytesAbsFairMale()
        self.setMonocytesAbsModerateMale()
        self.setMonocytesAbsHighMale()
        self.setMonocytesAbsLowFemale()
        self.setMonocytesAbsFairFemale()
        self.setMonocytesAbsModerateFemale()
        self.setMonocytesAbsHighFemale()
        self.setMonocytesAbsFunc()


    def getParameters(self):
        return super(CbcProfile, self).getParameters()

    def getAnnotations(self, parameter_name):
        return super(CbcProfile, self).getAnnotations(parameter_name) 
        
    def getParsedData(self, file_name, gender, password=""):
        report_parse = ReportParser(file_name, password)
        report_parse.reportList()
        parameter_name = self.getParameters()
        med_annot_hemoglobin = self.getAnnotations(parameter_name[0])
        med_annot_platelet = self.getAnnotations(parameter_name[1])
        med_annot_rbc = self.getAnnotations(parameter_name[2])
        med_annot_wbc = self.getAnnotations(parameter_name[3])
        med_annot_neutro = self.getAnnotations(parameter_name[4])
        med_annot_abs_neutro = self.getAnnotations(parameter_name[5])
        med_annot_eosin = self.getAnnotations(parameter_name[6])
        med_annot_abs_eosin = self.getAnnotations(parameter_name[7])
        med_annot_baso = self.getAnnotations(parameter_name[8])
        med_annot_abs_baso = self.getAnnotations(parameter_name[9])
        med_annot_lymph = self.getAnnotations(parameter_name[10])
        med_annot_abs_lymph = self.getAnnotations(parameter_name[11])
        med_annot_monocy = self.getAnnotations(parameter_name[12])
        med_annot_abs_monocy = self.getAnnotations(parameter_name[13])
        hemoglobin = parameter_name[0]
        report_parse.parseMedicalParameter(med_annot_hemoglobin, hemoglobin)
        platelet_count = parameter_name[1] 
        report_parse.parseMedicalParameter(med_annot_platelet, platelet_count)
        rbc_count = parameter_name[2]
        report_parse.parseMedicalParameter(med_annot_rbc, rbc_count)
        wbc_count = parameter_name[3]
        report_parse.parseMedicalParameter(med_annot_wbc, wbc_count)
        neutrophils = parameter_name[4]
        report_parse.parseMedicalParameter(med_annot_neutro, neutrophils)  
        absolute_neutrophils = parameter_name[5] 
        report_parse.parseMedicalParameter(med_annot_abs_neutro, absolute_neutrophils) 
        eosinophils = parameter_name[6] 
        report_parse.parseMedicalParameter(med_annot_eosin,  eosinophils)
        absolute_eosinophils = parameter_name[7]
        report_parse.parseMedicalParameter(med_annot_abs_eosin,  absolute_eosinophils)
        basophils = parameter_name[8]
        report_parse.parseMedicalParameter(med_annot_baso,  basophils)
        absolute_basophils = parameter_name[9]
        report_parse.parseMedicalParameter(med_annot_abs_baso,  absolute_basophils)
        lymphocytes = parameter_name[10]
        report_parse.parseMedicalParameter(med_annot_lymph,  lymphocytes)
        absolute_lymphocytes = parameter_name[11]
        report_parse.parseMedicalParameter(med_annot_abs_lymph, absolute_lymphocytes)
        monocytes = parameter_name[12]
        report_parse.parseMedicalParameter(med_annot_monocy, monocytes)
        absolute_monocytes = parameter_name[13]
        report_parse.parseMedicalParameter(med_annot_abs_monocy, absolute_monocytes)
        medical_report_dict = report_parse.getMedicalParsedData()
        # set actual value from medical report
        hemoglobin_value = medical_report_dict.get(hemoglobin,None)
        platelet_value = medical_report_dict.get(platelet_count,None) 
        if platelet_value != None:
            if len(str(int(platelet_value))) <= 3: 
                platelet_value = platelet_value*1000
        rbc_value = medical_report_dict.get(rbc_count,None)
        wbc_count = medical_report_dict.get(wbc_count,None)
        if wbc_count != None:
            if len(str(wbc_count)) <= 4:
                wbc_count = wbc_count*1000
        neutrophils_value = medical_report_dict.get(neutrophils, None)
        neutrophils_abs_value = medical_report_dict.get(absolute_neutrophils, None)
        if neutrophils_abs_value != None:
            if len(str(neutrophils_abs_value)) <= 4:
                neutrophils_abs_value = neutrophils_abs_value*1000
        eosinophils_value = medical_report_dict.get(eosinophils, None)
        eosinophils_abs_value = medical_report_dict.get(absolute_eosinophils, None)
        if eosinophils_abs_value != None:
            if len(str(eosinophils_abs_value)) <= 4:
                eosinophils_abs_value = eosinophils_abs_value*1000
        basophils_value = medical_report_dict.get(basophils, None)
        basophils_abs_value = medical_report_dict.get(absolute_basophils, None)
        if basophils_abs_value != None:
            if len(str(basophils_abs_value)) <= 4:
                basophils_abs_value = basophils_abs_value*1000
        lymphocytes_value = medical_report_dict.get(lymphocytes, None)
        lymphocytes_abs_value = medical_report_dict.get(absolute_lymphocytes, None)
        if lymphocytes_abs_value != None:
            if len(str(lymphocytes_abs_value)) <= 4:
                lymphocytes_abs_value = lymphocytes_abs_value*1000
        monocytes_value = medical_report_dict.get(monocytes, None)
        monocytes_abs_value = medical_report_dict.get(absolute_monocytes, None)
        if monocytes_abs_value != None:
            if len(str(monocytes_abs_value)) <= 4:
                monocytes_abs_value = monocytes_abs_value*1000
        self.setHemoglobinValue(hemoglobin_value)
        self.setPlateletCountValue(platelet_value)
        self.setWbcCountValue(wbc_count)
        self.setRbcCountValue(rbc_value)
        self.setNeutrophilsValue(neutrophils_value)
        self.setNeutrophilsAbsValue(neutrophils_abs_value)
        self.setEosinophilsValue(eosinophils_value)
        self.setEosinophilsAbsValue(eosinophils_abs_value)
        self.setBasophilsValue(basophils_value)
        self.setBasophilsAbsValue(basophils_abs_value)
        self.setLymphocytesValue(lymphocytes_value)
        self.setLymphocytesAbsValue(lymphocytes_abs_value)
        self.setMonocytesValue(monocytes_value)
        self.setMonocytesAbsValue(monocytes_abs_value)
        self.hemoglobin_output["reading_value"] = str(self.getHemoglobinValue())
        self.hemoglobin_output["reading_unit"] = self.getHemoglobinUnit()
        self.hemoglobin_output["range_female"] = self.getHemoglobinRangeFemale()
        self.hemoglobin_output["range_male"] = self.getHemoglobinRangeMale()
        self.platelet_count_output["reading_value"] = str(self.getPlateletCountValue())
        self.platelet_count_output["reading_unit"] = self.getPlateletCountUnit()
        self.platelet_count_output["range_male"] = self.getPlateletCountRangeMale()
        self.platelet_count_output["range_female"] = self.getPlateletCountRangeFemale()
        self.rbc_count_output["reading_value"] = str(self.getRbcCountValue())
        self.rbc_count_output["reading_unit"] = self.getRbcCountUnit()
        self.rbc_count_output["range_male"] = self.getRbcCountRangeMale()
        self.rbc_count_output["range_female"] = self.getRbcCountRangeFemale()
        self.wbc_count_output["reading_value"] = str(self.getWbcCountValue())
        self.wbc_count_output["reading_unit"] = self.getWbcCountUnit()
        self.wbc_count_output["range_male"] = self.getWbcCountRangeMale()
        self.wbc_count_output["range_female"] = self.getWbcCountRangeFemale()
        self.neutrophils_output["reading_value"] = str(self.getNeutrophilsValue())
        self.neutrophils_output["reading_unit"] = self.getNeutrophilsUnit()
        self.neutrophils_output["range_male"] = self.getNeutrophilsRangeMale()
        self.neutrophils_output["range_female"] = self.getNeutrophilsRangeFemale()
        self.neutrophils_absolute_output["reading_value"] = str(self.getNeutrophilsAbsValue())
        self.neutrophils_absolute_output["reading_unit"] = self.getNeutrophilsAbsUnit()
        self.neutrophils_absolute_output["range_male"] = self.getNeutrophilsAbsRangeMale()
        self.neutrophils_absolute_output["range_female"] = self.getNeutrophilsAbsRangeFemale()
        self.eosinophils_output["reading_value"] = str(self.getEosinophilsValue())
        self.eosinophils_output["reading_unit"] = self.getEosinophilsUnit()
        self.eosinophils_output["range_male"] = self.getEosinophilsRangeMale()
        self.eosinophils_output["range_female"] = self.getEosinophilsRangeFemale()
        self.eosinophils_absolute_output["reading_value"] = str(self.getEosinophilsAbsValue())
        self.eosinophils_absolute_output["reading_unit"] = self.getEosinophilsAbsUnit()
        self.eosinophils_absolute_output["range_male"] = self.getEosinophilsAbsRangeMale()
        self.eosinophils_absolute_output["range_female"] = self.getEosinophilsAbsRangeFemale()
        self.basophils_output["reading_value"] = str(self.getBasophilsValue())
        self.basophils_output["reading_unit"] = self.getBasophilsUnit()
        self.basophils_output["range_male"] = self.getBasophilsRangeMale()
        self.basophils_output["range_female"] = self.getBasophilsRangeFemale()
        self.basophils_absolute_output["reading_value"] = str(self.getBasophilsAbsValue())
        self.basophils_absolute_output["reading_unit"] = self.getBasophilsAbsUnit()
        self.basophils_absolute_output["range_male"] = self.getBasophilsAbsRangeMale()
        self.basophils_absolute_output["range_female"] = self.getBasophilsAbsRangeFemale()
        self.lymphocytes_output["reading_value"] = str(self.getLymphocytesValue())
        self.lymphocytes_output["reading_unit"] = self.getLymphocytesUnit()
        self.lymphocytes_output["range_male"] = self.getLymphocytesRangeMale()
        self.lymphocytes_output["range_female"] = self.getLymphocytesRangeFemale()
        self.lymphocytes_absolute_output["reading_value"] = str(self.getLymphocytesAbsValue())
        self.lymphocytes_absolute_output["reading_unit"] = self.getLymphocytesAbsUnit()
        self.lymphocytes_absolute_output["range_male"] = self.getLymphocytesAbsRangeMale()
        self.lymphocytes_absolute_output["range_female"] = self.getLymphocytesAbsRangeFemale()
        self.monocytes_output["reading_value"] = str(self.getMonocytesValue())
        self.monocytes_output["reading_unit"] = self.getMonocytesUnit()
        self.monocytes_output["range_male"] = self.getMonocytesRangeMale()
        self.monocytes_output["range_female"] = self.getMonocytesRangeFemale()
        self.monocytes_absolute_output["reading_value"] = str(self.getMonocytesAbsValue())
        self.monocytes_absolute_output["reading_unit"] = self.getMonocytesAbsUnit()
        self.monocytes_absolute_output["range_male"] = self.getMonocytesAbsRangeMale()
        self.monocytes_absolute_output["range_female"] = self.getMonocytesAbsRangeFemale()
        if gender == "Female":
            self.hemoglobin_output["low_fair_moderate_high"] = [self.getHemoglobinLowValueFemale(), self.getHemoglobinFairValueFemale(), self.getHemoglobinModerateValueFemale(), self.getHemoglobinHighValueFemale()]
            if self.getHemoglobinValue() >= float(self.getHemoglobinLowValueFemale().split("-")[0]) and self.getHemoglobinValue() <= float(self.getHemoglobinLowValueFemale().split("-")[1]):
                self.hemoglobin_output["risk"] = Low
            if self.getHemoglobinValue() >= float(self.getHemoglobinFairValueFemale().split("-")[0]) and self.getHemoglobinValue() <= float(self.getHemoglobinFairValueFemale().split("-")[1]):
                self.hemoglobin_output["risk"] = Low
            if self.getHemoglobinValue() >= float(self.getHemoglobinModerateValueFemale().split("-")[0]) and self.getHemoglobinValue() <= float(self.getHemoglobinModerateValueFemale().split("-")[1]):
                self.hemoglobin_output["risk"] = Low
            if self.getHemoglobinValue() < float(self.getHemoglobinHighValueFemale()):
                self.hemoglobin_output["risk"] = High
            if self.getHemoglobinValue() == None:
                self.hemoglobin_output["risk"] = n_a
            self.parsed_output["hemoglobin"] = self.hemoglobin_output

            self.platelet_count_output["low_fair_moderate_high"] = [self.getPlateletCountLowValueFemale(), self.getPlateletCountFairValueFemale(), self.getPlateletCountModerateValueFemale(), self.getPlateletCountHighValueFemale()]
            if self.getPlateletCountValue() >= float(self.getPlateletCountLowValueFemale().split("-")[0]) and self.getPlateletCountValue() <= float(self.getPlateletCountLowValueFemale().split("-")[1]):
                self.platelet_count_output["risk"] = Low
            if self.getPlateletCountValue() >= float(self.getPlateletCountFairValueFemale().split("-")[0]) and self.getPlateletCountValue() <= float(self.getPlateletCountFairValueFemale().split("-")[1]):
                self.platelet_count_output["risk"] = Low
            if self.getPlateletCountValue() >= float(self.getPlateletCountModerateValueFemale().split("-")[0]) and self.getPlateletCountValue() <= float(self.getPlateletCountModerateValueFemale().split("-")[1]):
                self.platelet_count_output["risk"] = Low
            if self.getPlateletCountValue() < float(self.getPlateletCountHighValueFemale()):
                self.platelet_count_output["risk"] = High
            if self.getPlateletCountValue() == None:
                self.platelet_count_output["risk"] = n_a
            self.parsed_output["platelet_count"] = self.platelet_count_output

            self.rbc_count_output["low_fair_moderate_high"] = [self.getRbcCountLowValueFemale(), self.getRbcCountFairValueFemale(), self.getRbcCountModerateValueFemale(), self.getRbcCountHighValueFemale()]
            if self.getRbcCountValue() >= float(self.getRbcCountLowValueFemale().split("-")[0]) and self.getRbcCountValue() <= float(self.getRbcCountLowValueFemale().split("-")[1]):
                self.rbc_count_output["risk"] = Low
            if self.getRbcCountValue() >= float(self.getRbcCountFairValueFemale().split("-")[0]) and self.getRbcCountValue() <= float(self.getRbcCountFairValueFemale().split("-")[1]):
                self.rbc_count_output["risk"] = Low
            if self.getRbcCountValue() >= float(self.getRbcCountModerateValueFemale().split("-")[0]) and self.getRbcCountValue() <= float(self.getRbcCountModerateValueFemale().split("-")[1]):
                self.rbc_count_output["risk"] = Low
            if self.getRbcCountValue() < float(self.getRbcCountHighValueFemale()):
                self.rbc_count_output["risk"] = High
            if self.getRbcCountValue() == None:
                self.rbc_count_output["risk"] = n_a
            self.parsed_output["rbc_count"] = self.rbc_count_output

            self.wbc_count_output["low_fair_moderate_high"] = [self.getWbcCountLowValueFemale(), self.getWbcCountFairValueFemale(), self.getWbcCountModerateValueFemale(), self.getWbcCountHighValueFemale()]
            if self.getWbcCountValue() >= float(self.getWbcCountLowValueFemale().split("-")[0]) and self.getWbcCountValue() <= float(self.getWbcCountLowValueFemale().split("-")[1]):
                self.wbc_count_output["risk"] = Low
            if self.getWbcCountValue() >= float(self.getWbcCountFairValueFemale().split("-")[0]) and self.getWbcCountValue() <= float(self.getWbcCountFairValueFemale().split("-")[1]):
                self.wbc_count_output["risk"] = Low
            if self.getWbcCountValue() >= float(self.getWbcCountModerateValueFemale().split("-")[0]) and self.getWbcCountValue() <= float(self.getWbcCountModerateValueFemale().split("-")[1]):
                self.wbc_count_output["risk"] = Low
            if self.getWbcCountValue() < float(self.getWbcCountHighValueFemale()):
                self.wbc_count_output["risk"] = High
            if self.getWbcCountValue() == None:
                self.wbc_count_output["risk"] = n_a
            self.parsed_output["wbc_count"] = self.wbc_count_output

            self.neutrophils_output["low_fair_moderate_high"] = [self.getNeutrophilsLowValueFemale(), self.getNeutrophilsFairValueFemale(), self.getNeutrophilsModerateValueFemale(), self.getNeutrophilsHighValueFemale()]
            if self.getNeutrophilsValue() >= float(self.getNeutrophilsLowValueFemale().split("-")[0]) and self.getNeutrophilsValue() <= float(self.getNeutrophilsLowValueFemale().split("-")[1]):
                self.neutrophils_output["risk"] = Low
            if self.getNeutrophilsValue() >= float(self.getNeutrophilsFairValueFemale().split("-")[0]) and self.getNeutrophilsValue() <= float(self.getNeutrophilsFairValueFemale().split("-")[1]):
                self.neutrophils_output["risk"] = Low
            if self.getNeutrophilsValue() >= float(self.getNeutrophilsModerateValueFemale().split("-")[0]) and self.getNeutrophilsValue() <= float(self.getNeutrophilsModerateValueFemale().split("-")[1]):
                self.neutrophils_output["risk"] = Low
            if self.getNeutrophilsValue() < float(self.getNeutrophilsHighValueFemale()):
                self.neutrophils_output["risk"] = High
            if self.getNeutrophilsValue() == None:
                self.neutrophils_output["risk"] = n_a
            self.parsed_output["neutrophils"] = self.neutrophils_output

            self.neutrophils_absolute_output["low_fair_moderate_high"] = [self.getNeutrophilsAbsLowValueFemale(), self.getNeutrophilsAbsFairValueFemale(), self.getNeutrophilsAbsModerateValueFemale(), self.getNeutrophilsAbsHighValueFemale()]
            if self.getNeutrophilsAbsValue() >= float(self.getNeutrophilsAbsLowValueFemale().split("-")[0]) and self.getNeutrophilsAbsValue() <= float(self.getNeutrophilsAbsLowValueFemale().split("-")[1]):
                self.neutrophils_absolute_output["risk"] = Low
            if self.getNeutrophilsAbsValue() >= float(self.getNeutrophilsAbsFairValueFemale().split("-")[0]) and self.getNeutrophilsAbsValue() <= float(self.getNeutrophilsAbsFairValueFemale().split("-")[1]):
                self.neutrophils_absolute_output["risk"] = Low
            if self.getNeutrophilsAbsValue() >= float(self.getNeutrophilsAbsModerateValueFemale().split("-")[0]) and self.getNeutrophilsAbsValue() <= float(self.getNeutrophilsAbsModerateValueFemale().split("-")[1]):
                self.neutrophils_absolute_output["risk"] = Low
            if self.getNeutrophilsAbsValue() < float(self.getNeutrophilsAbsHighValueFemale()):
                self.neutrophils_absolute_output["risk"] = High
            if self.getNeutrophilsAbsValue() == None:
                self.neutrophils_absolute_output["risk"] = n_a
            self.parsed_output["neutrophils_absolute"] = self.neutrophils_absolute_output

            self.eosinophils_output["low_fair_moderate_high"] = [self.getEosinophilsLowValueFemale(), self.getEosinophilsFairValueFemale(), self.getEosinophilsModerateValueFemale(), self.getEosinophilsHighValueFemale()]
            if self.getEosinophilsValue() >= float(self.getEosinophilsLowValueFemale().split("-")[0]) and self.getEosinophilsValue() <= float(self.getEosinophilsLowValueFemale().split("-")[1]):
                self.eosinophils_output["risk"] = Low
            if self.getEosinophilsValue() >= float(self.getEosinophilsFairValueFemale().split("-")[0]) and self.getEosinophilsValue() <= float(self.getEosinophilsFairValueFemale().split("-")[1]):
                self.eosinophils_output["risk"] = Low
            if self.getEosinophilsValue() >= float(self.getEosinophilsModerateValueFemale().split("-")[0]) and self.getEosinophilsValue() <= float(self.getEosinophilsModerateValueFemale().split("-")[1]):
                self.eosinophils_output["risk"] = Low
            if self.getEosinophilsValue() < float(self.getEosinophilsHighValueFemale()):
                self.eosinophils_output["risk"] = High
            if self.getEosinophilsValue() == None:
                self.eosinophils_output["risk"] = n_a
            self.parsed_output["eosinophils"] = self.eosinophils_output

            self.eosinophils_absolute_output["low_fair_moderate_high"] = [self.getEosinophilsAbsLowValueFemale(), self.getEosinophilsAbsFairValueFemale(), self.getEosinophilsAbsModerateValueFemale(), self.getEosinophilsAbsHighValueFemale()]
            if self.getEosinophilsAbsValue() >= float(self.getEosinophilsAbsLowValueFemale().split("-")[0]) and self.getEosinophilsAbsValue() <= float(self.getEosinophilsAbsLowValueFemale().split("-")[1]):
                self.eosinophils_absolute_output["risk"] = Low
            if self.getEosinophilsAbsValue() >= float(self.getEosinophilsAbsFairValueFemale().split("-")[0]) and self.getEosinophilsAbsValue() <= float(self.getEosinophilsAbsFairValueFemale().split("-")[1]):
                self.eosinophils_absolute_output["risk"] = Low
            if self.getEosinophilsAbsValue() >= float(self.getEosinophilsAbsModerateValueFemale().split("-")[0]) and self.getEosinophilsAbsValue() <= float(self.getEosinophilsAbsModerateValueFemale().split("-")[1]):
                self.eosinophils_absolute_output["risk"] = Low
            if self.getEosinophilsAbsValue() < float(self.getEosinophilsAbsHighValueFemale()):
                self.eosinophils_absolute_output["risk"] = High
            if self.getEosinophilsAbsValue() == None:
                self.eosinophils_absolute_output["risk"] = n_a
            self.parsed_output["eosinophils_absolute"] = self.eosinophils_absolute_output

            self.basophils_output["low_fair_moderate_high"] = [self.getBasophilsLowValueFemale(), self.getBasophilsFairValueFemale(), self.getBasophilsModerateValueFemale(), self.getBasophilsHighValueFemale()]
            if self.getBasophilsValue() >= float(self.getBasophilsLowValueFemale().split("-")[0]) and self.getBasophilsValue() <= float(self.getBasophilsLowValueFemale().split("-")[1]):
                self.basophils_output["risk"] = Low
            if self.getBasophilsValue() >= float(self.getBasophilsFairValueFemale().split("-")[0]) and self.getBasophilsValue() <= float(self.getBasophilsFairValueFemale().split("-")[1]):
                self.basophils_output["risk"] = Low
            if self.getBasophilsValue() >= float(self.getBasophilsModerateValueFemale().split("-")[0]) and self.getBasophilsValue() <= float(self.getBasophilsModerateValueFemale().split("-")[1]):
                self.basophils_output["risk"] = Low
            if self.getBasophilsValue() < float(self.getBasophilsHighValueFemale()):
                self.basophils_output["risk"] = High
            if self.getBasophilsValue() == None:
                self.basophils_output["risk"] = n_a
            self.parsed_output["basophils"] = self.basophils_output

            self.basophils_absolute_output["low_fair_moderate_high"] = [self.getBasophilsAbsLowValueFemale(), self.getBasophilsAbsFairValueFemale(), self.getBasophilsAbsModerateValueFemale(), self.getBasophilsAbsHighValueFemale()]
            if self.getBasophilsAbsValue() >= float(self.getBasophilsAbsLowValueFemale().split("-")[0]) and self.getBasophilsAbsValue() <= float(self.getBasophilsAbsLowValueFemale().split("-")[1]):
                self.basophils_absolute_output["risk"] = Low
            if self.getBasophilsAbsValue() >= float(self.getBasophilsAbsFairValueFemale().split("-")[0]) and self.getBasophilsAbsValue() <= float(self.getBasophilsAbsFairValueFemale().split("-")[1]):
                self.basophils_absolute_output["risk"] = Low
            if self.getBasophilsAbsValue() >= float(self.getBasophilsAbsModerateValueFemale().split("-")[0]) and self.getBasophilsAbsValue() <= float(self.getBasophilsAbsModerateValueFemale().split("-")[1]):
                self.basophils_absolute_output["risk"] = Low
            if self.getBasophilsAbsValue() < float(self.getBasophilsAbsHighValueFemale()):
                self.basophils_absolute_output["risk"] = High
            if self.getBasophilsAbsValue() == None:
                self.basophils_absolute_output["risk"] = n_a
            self.parsed_output["basophils_absolute"] = self.basophils_absolute_output

            self.lymphocytes_output["low_fair_moderate_high"] = [self.getLymphocytesLowValueFemale(), self.getLymphocytesFairValueFemale(), self.getLymphocytesModerateValueFemale(), self.getLymphocytesHighValueFemale()]
            if self.getLymphocytesValue() >= float(self.getLymphocytesLowValueFemale().split("-")[0]) and self.getLymphocytesValue() <= float(self.getLymphocytesLowValueFemale().split("-")[1]):
                self.lymphocytes_output["risk"] = Low
            if self.getLymphocytesValue() >= float(self.getLymphocytesFairValueFemale().split("-")[0]) and self.getLymphocytesValue() <= float(self.getLymphocytesFairValueFemale().split("-")[1]):
                self.lymphocytes_output["risk"] = Low
            if self.getLymphocytesValue() >= float(self.getLymphocytesModerateValueFemale().split("-")[0]) and self.getLymphocytesValue() <= float(self.getLymphocytesModerateValueFemale().split("-")[1]):
                self.lymphocytes_output["risk"] = Low
            if self.getLymphocytesValue() < float(self.getLymphocytesHighValueFemale()):
                self.lymphocytes_output["risk"] = High
            if self.getLymphocytesValue() == None:
                self.lymphocytes_output["risk"] = n_a
            self.parsed_output["lymphocytes"] = self.lymphocytes_output

            self.lymphocytes_absolute_output["low_fair_moderate_high"] = [self.getLymphocytesAbsLowValueFemale(), self.getLymphocytesAbsFairValueFemale(), self.getLymphocytesAbsModerateValueFemale(), self.getLymphocytesAbsHighValueFemale()]
            if self.getLymphocytesAbsValue() >= float(self.getLymphocytesAbsLowValueFemale().split("-")[0]) and self.getLymphocytesAbsValue() <= float(self.getLymphocytesAbsLowValueFemale().split("-")[1]):
                self.lymphocytes_absolute_output["risk"] = Low
            if self.getLymphocytesAbsValue() >= float(self.getLymphocytesAbsFairValueFemale().split("-")[0]) and self.getLymphocytesAbsValue() <= float(self.getLymphocytesAbsFairValueFemale().split("-")[1]):
                self.lymphocytes_absolute_output["risk"] = Low
            if self.getLymphocytesAbsValue() >= float(self.getLymphocytesAbsModerateValueFemale().split("-")[0]) and self.getLymphocytesAbsValue() <= float(self.getLymphocytesAbsModerateValueFemale().split("-")[1]):
                self.lymphocytes_absolute_output["risk"] = Low
            if self.getLymphocytesAbsValue() < float(self.getLymphocytesAbsHighValueFemale()):
                self.lymphocytes_absolute_output["risk"] = High
            if self.getLymphocytesAbsValue() == None:
                self.lymphocytes_absolute_output["risk"] = n_a
            self.parsed_output["lymphocytes_absolute"] = self.lymphocytes_absolute_output

            self.monocytes_output["low_fair_moderate_high"] = [self.getMonocytesLowValueFemale(), self.getMonocytesFairValueFemale(), self.getMonocytesModerateValueFemale(), self.getMonocytesHighValueFemale()]
            if self.getMonocytesValue() >= float(self.getMonocytesLowValueFemale().split("-")[0]) and self.getMonocytesValue() <= float(self.getMonocytesLowValueFemale().split("-")[1]):
                self.monocytes_output["risk"] = Low
            if self.getMonocytesValue() >= float(self.getMonocytesFairValueFemale().split("-")[0]) and self.getMonocytesValue() <= float(self.getMonocytesFairValueFemale().split("-")[1]):
                self.monocytes_output["risk"] = Low
            if self.getMonocytesValue() >= float(self.getMonocytesModerateValueFemale().split("-")[0]) and self.getMonocytesValue() <= float(self.getMonocytesModerateValueFemale().split("-")[1]):
                self.monocytes_output["risk"] = Low
            if self.getMonocytesValue() < float(self.getMonocytesHighValueFemale()):
                self.monocytes_output["risk"] = High
            if self.getMonocytesValue() == None:
                self.monocytes_output["risk"] = n_a
            self.parsed_output["monocytes"] = self.monocytes_output

            self.monocytes_absolute_output["low_fair_moderate_high"] = [self.getMonocytesAbsLowValueFemale(), self.getMonocytesAbsFairValueFemale(), self.getMonocytesAbsModerateValueFemale(), self.getMonocytesAbsHighValueFemale()]
            if self.getMonocytesValue() >= float(self.getMonocytesAbsLowValueFemale().split("-")[0]) and self.getMonocytesAbsValue() <= float(self.getMonocytesAbsLowValueFemale().split("-")[1]):
                self.monocytes_absolute_output["risk"] = Low
            if self.getMonocytesAbsValue() >= float(self.getMonocytesAbsFairValueFemale().split("-")[0]) and self.getMonocytesAbsValue() <= float(self.getMonocytesAbsFairValueFemale().split("-")[1]):
                self.monocytes_absolute_output["risk"] = Low
            if self.getMonocytesAbsValue() >= float(self.getMonocytesAbsModerateValueFemale().split("-")[0]) and self.getMonocytesAbsValue() <= float(self.getMonocytesAbsModerateValueFemale().split("-")[1]):
                self.monocytes_absolute_output["risk"] = Low
            if self.getMonocytesAbsValue() < float(self.getMonocytesAbsHighValueFemale()):
                self.monocytes_absolute_output["risk"] = High
            if self.getMonocytesAbsValue() == None:
                self.monocytes_absolute_output["risk"] = n_a
            self.parsed_output["monocytes_absolute"] = self.monocytes_absolute_output


        else:
            self.hemoglobin_output["low_fair_moderate_high"] = [self.getHemoglobinLowValueMale(), self.getHemoglobinFairValueMale(), self.getHemoglobinModerateValueMale(), self.getHemoglobinHighValueMale()]
            if self.getHemoglobinValue() >= float(self.getHemoglobinLowValueMale().split("-")[0]) and self.getHemoglobinValue() <= float(self.getHemoglobinLowValueMale().split("-")[1]):
                self.hemoglobin_output["risk"] = Low
            if self.getHemoglobinValue() >= float(self.getHemoglobinFairValueMale().split("-")[0]) and self.getHemoglobinValue() <= float(self.getHemoglobinFairValueMale().split("-")[1]):
                self.hemoglobin_output["risk"] = Low
            if self.getHemoglobinValue() >= float(self.getHemoglobinModerateValueMale().split("-")[0]) and self.getHemoglobinValue() <= float(self.getHemoglobinModerateValueMale().split("-")[1]):
                self.hemoglobin_output["risk"] = Low
            if self.getHemoglobinValue() < float(self.getHemoglobinHighValueMale()):
                self.hemoglobin_output["risk"] = High
            if self.getHemoglobinValue() == None:
                self.hemoglobin_output["risk"] = n_a
            self.parsed_output["hemoglobin"] = self.hemoglobin_output

            self.platelet_count_output["low_fair_moderate_high"] = [self.getPlateletCountLowValueMale(), self.getPlateletCountFairValueMale(), self.getPlateletCountModerateValueMale(), self.getPlateletCountHighValueMale()]
            if self.getPlateletCountValue() >= float(self.getPlateletCountLowValueMale().split("-")[0]) and self.getPlateletCountValue() <= float(self.getPlateletCountLowValueMale().split("-")[1]):
                self.platelet_count_output["risk"] = Low
            if self.getPlateletCountValue() >= float(self.getPlateletCountFairValueMale().split("-")[0]) and self.getPlateletCountValue() <= float(self.getPlateletCountFairValueMale().split("-")[1]):
                self.platelet_count_output["risk"] = Low
            if self.getPlateletCountValue() >= float(self.getPlateletCountModerateValueMale().split("-")[0]) and self.getPlateletCountValue() <= float(self.getPlateletCountModerateValueMale().split("-")[1]):
                self.platelet_count_output["risk"] = Low
            if self.getPlateletCountValue() < float(self.getPlateletCountHighValueMale()):
                self.platelet_count_output["risk"] = High
            if self.getPlateletCountValue() == None:
                self.platelet_count_output["risk"] = n_a
            self.parsed_output["platelet_count"] = self.platelet_count_output

            self.rbc_count_output["low_fair_moderate_high"] = [self.getRbcCountLowValueMale(), self.getRbcCountFairValueMale(), self.getRbcCountModerateValueMale(), self.getRbcCountHighValueMale()]
            if self.getRbcCountValue() >= float(self.getRbcCountLowValueMale().split("-")[0]) and self.getRbcCountValue() <= float(self.getRbcCountLowValueMale().split("-")[1]):
                self.rbc_count_output["risk"] = Low
            if self.getRbcCountValue() >= float(self.getRbcCountFairValueMale().split("-")[0]) and self.getRbcCountValue() <= float(self.getRbcCountFairValueMale().split("-")[1]):
                self.rbc_count_output["risk"] = Low
            if self.getRbcCountValue() >= float(self.getRbcCountModerateValueMale().split("-")[0]) and self.getRbcCountValue() <= float(self.getRbcCountModerateValueMale().split("-")[1]):
                self.rbc_count_output["risk"] = Low
            if self.getRbcCountValue() < float(self.getRbcCountHighValueMale()):
                self.rbc_count_output["risk"] = High
            if  self.getRbcCountValue() == None:
                self.rbc_count_output["risk"] = n_a
            self.parsed_output["rbc_count"] = self.rbc_count_output

            self.wbc_count_output["low_fair_moderate_high"] = [self.getWbcCountLowValueMale(), self.getWbcCountFairValueMale(), self.getWbcCountModerateValueMale(), self.getWbcCountHighValueMale()]
            if self.getWbcCountValue() >= float(self.getWbcCountLowValueMale().split("-")[0]) and self.getWbcCountValue() <= float(self.getWbcCountLowValueMale().split("-")[1]):
                self.wbc_count_output["risk"] = Low
            if self.getWbcCountValue() >= float(self.getWbcCountFairValueMale().split("-")[0]) and self.getWbcCountValue() <= float(self.getWbcCountFairValueMale().split("-")[1]):
                self.wbc_count_output["risk"] = Low
            if self.getWbcCountValue() >= float(self.getWbcCountModerateValueMale().split("-")[0]) and self.getWbcCountValue() <= float(self.getWbcCountModerateValueMale().split("-")[1]):
                self.wbc_count_output["risk"] = Low
            if self.getWbcCountValue() < float(self.getWbcCountHighValueMale()):
                self.wbc_count_output["risk"] = High
            if self.getWbcCountValue() == None:
                self.wbc_count_output["risk"] = n_a
            self.parsed_output["wbc_count"] = self.wbc_count_output

            self.neutrophils_output["low_fair_moderate_high"] = [self.getNeutrophilsLowValueMale(), self.getNeutrophilsFairValueMale(), self.getNeutrophilsModerateValueMale(), self.getNeutrophilsHighValueMale()]
            if self.getNeutrophilsValue() >= float(self.getNeutrophilsLowValueMale().split("-")[0]) and self.getNeutrophilsValue() <= float(self.getNeutrophilsLowValueMale().split("-")[1]):
                self.neutrophils_output["risk"] = Low
            if self.getNeutrophilsValue() >= float(self.getNeutrophilsFairValueMale().split("-")[0]) and self.getNeutrophilsValue() <= float(self.getNeutrophilsFairValueMale().split("-")[1]):
                self.neutrophils_output["risk"] = Low
            if self.getNeutrophilsValue() >= float(self.getNeutrophilsModerateValueMale().split("-")[0]) and self.getNeutrophilsValue() <= float(self.getNeutrophilsModerateValueMale().split("-")[1]):
                self.neutrophils_output["risk"] = Low
            if self.getNeutrophilsValue() < float(self.getNeutrophilsHighValueMale()):
                self.neutrophils_output["risk"] = High
            if self.getNeutrophilsValue() == None:
                self.neutrophils_output["risk"] = n_a
            self.parsed_output["neutrophils"] = self.neutrophils_output

            self.neutrophils_absolute_output["low_fair_moderate_high"] = [self.getNeutrophilsAbsLowValueMale(), self.getNeutrophilsAbsFairValueMale(), self.getNeutrophilsAbsModerateValueMale(), self.getNeutrophilsAbsHighValueMale()]
            if self.getNeutrophilsAbsValue() >= float(self.getNeutrophilsAbsLowValueMale().split("-")[0]) and self.getNeutrophilsAbsValue() <= float(self.getNeutrophilsAbsLowValueMale().split("-")[1]):
                self.neutrophils_absolute_output["risk"] = Low
            if self.getNeutrophilsAbsValue() >= float(self.getNeutrophilsAbsFairValueMale().split("-")[0]) and self.getNeutrophilsAbsValue() <= float(self.getNeutrophilsAbsFairValueMale().split("-")[1]):
                self.neutrophils_absolute_output["risk"] = Low
            if self.getNeutrophilsAbsValue() >= float(self.getNeutrophilsAbsModerateValueMale().split("-")[0]) and self.getNeutrophilsAbsValue() <= float(self.getNeutrophilsAbsModerateValueMale().split("-")[1]):
                self.neutrophils_absolute_output["risk"] = Low
            if self.getNeutrophilsAbsValue() < float(self.getNeutrophilsAbsHighValueMale()):
                self.neutrophils_absolute_output["risk"] = High
            if self.getNeutrophilsAbsValue() == None:
                self.neutrophils_absolute_output["risk"] = n_a
            self.parsed_output["neutrophils_absolute"] = self.neutrophils_absolute_output

            self.eosinophils_output["low_fair_moderate_high"] = [self.getEosinophilsLowValueMale(), self.getEosinophilsFairValueMale(), self.getEosinophilsModerateValueMale(), self.getEosinophilsHighValueMale()]
            if self.getEosinophilsValue() >= float(self.getEosinophilsLowValueMale().split("-")[0]) and self.getEosinophilsValue() <= float(self.getEosinophilsLowValueMale().split("-")[1]):
                self.eosinophils_output["risk"] = Low
            if self.getEosinophilsValue() >= float(self.getEosinophilsFairValueMale().split("-")[0]) and self.getEosinophilsValue() <= float(self.getEosinophilsFairValueMale().split("-")[1]):
                self.eosinophils_output["risk"] = Low
            if self.getEosinophilsValue() >= float(self.getEosinophilsModerateValueMale().split("-")[0]) and self.getEosinophilsValue() <= float(self.getEosinophilsModerateValueMale().split("-")[1]):
                self.eosinophils_output["risk"] = Low
            if self.getEosinophilsValue() < float(self.getEosinophilsHighValueMale()):
                self.eosinophils_output["risk"] = High
            if self.getEosinophilsValue() == None:
                self.eosinophils_output["risk"] = n_a
            self.parsed_output["eosinophils"] = self.eosinophils_output

            self.eosinophils_absolute_output["low_fair_moderate_high"] = [self.getEosinophilsAbsLowValueMale(), self.getEosinophilsAbsFairValueMale(), self.getEosinophilsAbsModerateValueMale(), self.getEosinophilsAbsHighValueMale()]
            if self.getEosinophilsAbsValue() >= float(self.getEosinophilsAbsLowValueMale().split("-")[0]) and self.getEosinophilsAbsValue() <= float(self.getEosinophilsAbsLowValueMale().split("-")[1]):
                self.eosinophils_absolute_output["risk"] = Low
            if self.getEosinophilsAbsValue() >= float(self.getEosinophilsAbsFairValueMale().split("-")[0]) and self.getEosinophilsAbsValue() <= float(self.getEosinophilsAbsFairValueMale().split("-")[1]):
                self.eosinophils_absolute_output["risk"] = Low
            if self.getEosinophilsAbsValue() >= float(self.getEosinophilsAbsModerateValueMale().split("-")[0]) and self.getEosinophilsAbsValue() <= float(self.getEosinophilsAbsModerateValueMale().split("-")[1]):
                self.eosinophils_absolute_output["risk"] = Low
            if self.getEosinophilsAbsValue() < float(self.getEosinophilsAbsHighValueMale()):
                self.eosinophils_absolute_output["risk"] = High
            if self.getEosinophilsAbsValue() == None:
                self.eosinophils_absolute_output["risk"] = n_a
            self.parsed_output["eosinophils_absolute"] = self.eosinophils_absolute_output

            self.basophils_output["low_fair_moderate_high"] = [self.getBasophilsLowValueMale(), self.getBasophilsFairValueMale(), self.getBasophilsModerateValueMale(), self.getBasophilsHighValueMale()]
            if self.getBasophilsValue() >= float(self.getBasophilsLowValueMale().split("-")[0]) and self.getBasophilsValue() <= float(self.getBasophilsLowValueMale().split("-")[1]):
                self.basophils_output["risk"] = Low
            if self.getBasophilsValue() >= float(self.getBasophilsFairValueMale().split("-")[0]) and self.getBasophilsValue() <= float(self.getBasophilsFairValueMale().split("-")[1]):
                self.basophils_output["risk"] = Low
            if self.getBasophilsValue() >= float(self.getBasophilsModerateValueMale().split("-")[0]) and self.getBasophilsValue() <= float(self.getBasophilsModerateValueMale().split("-")[1]):
                self.basophils_output["risk"] = Low
            if self.getBasophilsValue() < float(self.getBasophilsHighValueMale()):
                self.basophils_output["risk"] = High
            if self.getBasophilsValue() == None:
                self.basophils_output["risk"] = n_a
            self.parsed_output["basophils"] = self.basophils_output

            self.basophils_absolute_output["low_fair_moderate_high"] = [self.getBasophilsAbsLowValueMale(), self.getBasophilsAbsFairValueMale(), self.getBasophilsAbsModerateValueMale(), self.getBasophilsAbsHighValueMale()]
            if self.getBasophilsAbsValue() >= float(self.getBasophilsAbsLowValueMale().split("-")[0]) and self.getBasophilsAbsValue() <= float(self.getBasophilsAbsLowValueMale().split("-")[1]):
                self.basophils_absolute_output["risk"] = Low
            if self.getBasophilsAbsValue() >= float(self.getBasophilsAbsFairValueMale().split("-")[0]) and self.getBasophilsAbsValue() <= float(self.getBasophilsAbsFairValueMale().split("-")[1]):
                self.basophils_absolute_output["risk"] = Low
            if self.getBasophilsAbsValue() >= float(self.getBasophilsAbsModerateValueMale().split("-")[0]) and self.getBasophilsAbsValue() <= float(self.getBasophilsAbsModerateValueMale().split("-")[1]):
                self.basophils_absolute_output["risk"] = Low
            if self.getBasophilsAbsValue() < float(self.getBasophilsAbsHighValueMale()):
                self.basophils_absolute_output["risk"] = High
            if self.getBasophilsAbsValue() == None:
                self.basophils_absolute_output["risk"] = n_a
            self.parsed_output["basophils_absolute"] = self.basophils_absolute_output

            self.lymphocytes_output["low_fair_moderate_high"] = [self.getLymphocytesLowValueMale(), self.getLymphocytesFairValueMale(), self.getLymphocytesModerateValueMale(), self.getLymphocytesHighValueMale()]
            if self.getLymphocytesValue() >= float(self.getLymphocytesLowValueMale().split("-")[0]) and self.getLymphocytesValue() <= float(self.getLymphocytesLowValueMale().split("-")[1]):
                self.lymphocytes_output["risk"] = Low
            if self.getLymphocytesValue() >= float(self.getLymphocytesFairValueMale().split("-")[0]) and self.getLymphocytesValue() <= float(self.getLymphocytesFairValueMale().split("-")[1]):
                self.lymphocytes_output["risk"] = Low
            if self.getLymphocytesValue() >= float(self.getLymphocytesModerateValueMale().split("-")[0]) and self.getLymphocytesValue() <= float(self.getLymphocytesModerateValueMale().split("-")[1]):
                self.lymphocytes_output["risk"] = Low
            if self.getLymphocytesValue() < float(self.getLymphocytesHighValueMale()):
                self.lymphocytes_output["risk"] = High
            if self.getLymphocytesValue() == None:
                self.lymphocytes_output["risk"] = n_a
            self.parsed_output["lymphocytes"] = self.lymphocytes_output

            self.lymphocytes_absolute_output["low_fair_moderate_high"] = [self.getLymphocytesAbsLowValueMale(), self.getLymphocytesAbsFairValueMale(), self.getLymphocytesAbsModerateValueMale(), self.getLymphocytesAbsHighValueMale()]
            if self.getLymphocytesAbsValue() >= float(self.getLymphocytesAbsLowValueMale().split("-")[0]) and self.getLymphocytesAbsValue() <= float(self.getLymphocytesAbsLowValueMale().split("-")[1]):
                self.lymphocytes_absolute_output["risk"] = Low
            if self.getLymphocytesAbsValue() >= float(self.getLymphocytesAbsFairValueMale().split("-")[0]) and self.getLymphocytesAbsValue() <= float(self.getLymphocytesAbsFairValueMale().split("-")[1]):
                self.lymphocytes_absolute_output["risk"] = Low
            if self.getLymphocytesAbsValue() >= float(self.getLymphocytesAbsModerateValueMale().split("-")[0]) and self.getLymphocytesAbsValue() <= float(self.getLymphocytesAbsModerateValueMale().split("-")[1]):
                self.lymphocytes_absolute_output["risk"] = Low
            if self.getLymphocytesAbsValue() < float(self.getLymphocytesAbsHighValueMale()):
                self.lymphocytes_absolute_output["risk"] = High
            if self.getLymphocytesAbsValue() == None:
                self.lymphocytes_absolute_output["risk"] = n_a
            self.parsed_output["lymphocytes_absolute"] = self.lymphocytes_absolute_output

            self.monocytes_output["low_fair_moderate_high"] = [self.getMonocytesLowValueMale(), self.getMonocytesFairValueMale(), self.getMonocytesModerateValueMale(), self.getMonocytesHighValueMale()]
            if self.getMonocytesValue() >= float(self.getMonocytesLowValueMale().split("-")[0]) and self.getMonocytesValue() <= float(self.getMonocytesLowValueMale().split("-")[1]):
                self.monocytes_output["risk"] = Low
            if self.getMonocytesValue() >= float(self.getMonocytesFairValueMale().split("-")[0]) and self.getMonocytesValue() <= float(self.getMonocytesFairValueMale().split("-")[1]):
                self.monocytes_output["risk"] = Low
            if self.getMonocytesValue() >= float(self.getMonocytesModerateValueMale().split("-")[0]) and self.getMonocytesValue() <= float(self.getMonocytesModerateValueMale().split("-")[1]):
                self.monocytes_output["risk"] = Low
            if self.getMonocytesValue() < float(self.getMonocytesHighValueMale()):
                self.monocytes_output["risk"] = High
            if self.getMonocytesValue() == None:
                self.monocytes_output["risk"] = n_a
            self.parsed_output["monocytes"] = self.monocytes_output

            self.monocytes_absolute_output["low_fair_moderate_high"] = [self.getMonocytesAbsLowValueMale(), self.getMonocytesAbsFairValueMale(), self.getMonocytesAbsModerateValueMale(), self.getMonocytesAbsHighValueMale()]
            if self.getMonocytesValue() >= float(self.getMonocytesAbsLowValueMale().split("-")[0]) and self.getMonocytesAbsValue() <= float(self.getMonocytesAbsLowValueMale().split("-")[1]):
                self.monocytes_absolute_output["risk"] = Low
            if self.getMonocytesAbsValue() >= float(self.getMonocytesAbsFairValueMale().split("-")[0]) and self.getMonocytesAbsValue() <= float(self.getMonocytesAbsFairValueMale().split("-")[1]):
                self.monocytes_absolute_output["risk"] = Low
            if self.getMonocytesAbsValue() >= float(self.getMonocytesAbsModerateValueMale().split("-")[0]) and self.getMonocytesAbsValue() <= float(self.getMonocytesAbsModerateValueMale().split("-")[1]):
                self.monocytes_absolute_output["risk"] = Low
            if self.getMonocytesAbsValue() < float(self.getMonocytesAbsHighValueMale()):
                self.monocytes_absolute_output["risk"] = High
            if self.getMonocytesAbsValue() == None:
                self.monocytes_absolute_output["risk"] = n_a
            self.parsed_output["monocytes_absolute"] = self.monocytes_absolute_output


        if os.path.exists(report_parse.output):
            os.remove(report_parse.output)
        return self.parsed_output

    # Function sets category id    
    def setCategoryid(self):
        self.category_id = self.profile.get("category_id","")

    # Function sets category name
    def setCategoryName(self):
        self.category_name = self.profile.get("category_name","")

    # Function sets Version number
    def setVersionNumber(self):
        self.version_number = self.profile.get("version_number")    
    
    def setHemoglobinValue(self, hemoglobin):
        self.hemoglobin = hemoglobin

    def setHemoglobinUnit(self):
        self.hemoglobin_unit = self.parameters[0].get('value_meta_data', [])[0].get('unit', "")

    def setHemoglobinMedicalAnnotation(self):
        self.hemoglobin_medical_annot = self.parameters[0].get('medical_annotation', [])

    def setHemoglobinRangeMale(self):
        self.hemoglobin_range_male =  self.parameters[0].get('value_meta_data',[])[0].get('range',"") 

    def setHemoglobinRangeFemale(self):
        self.hemoglobin_range_female = self.parameters[0].get('value_meta_data',[])[1].get('range',"") 

    def setHemoglobinLowValueMale(self):
        self.hemoglobin_low_male = self.parameters[0].get('value_meta_data',[])[0].get('low_value',"")

    def setHemoglobinFairValueMale(self):
        self.hemoglobin_fair_male = self.parameters[0].get('value_meta_data',[])[0].get('fair_value', "")

    def setHemoglobinModerateValueMale(self):
        self.hemoglobin_moderate_male = self.parameters[0].get('value_meta_data',[])[0].get('moderate_value', "")

    def setHemoglobinHighValueMale(self):
        self.hemoglobin_high_male = self.parameters[0].get('value_meta_data',[])[0].get('high_value', "")[1:]

    def setHemoglobinLowValueFemale(self):
        self.hemoglobin_low_female = self.parameters[0].get('value_meta_data',[])[1].get('low_value',"")

    def setHemoglobinFairValueFemale(self):
        self.hemoglobin_fair_female = self.parameters[0].get('value_meta_data',[])[1].get('fair_value', "")

    def setHemoglobinModerateValueFemale(self):
        self.hemoglobin_moderate_female = self.parameters[0].get('value_meta_data',[])[1].get('moderate_value', "")

    def setHemoglobinHighValueFemale(self):
        self.hemoglobin_high_female = self.parameters[0].get('value_meta_data',[])[1].get('high_value', "")[1:]

    def setHemoglobinFunction(self):
        self.hemoglobin_func = self.parameters[0].get("value_function",{}).get("function_name","")

    def setPlateletCountValue(self, platelet_count):
        self.platelet_count = platelet_count

    def setPlateletCountUnit(self):
        self.platelet_count_unit = self.parameters[1].get('value_meta_data', [])[0].get('unit', "")

    def setPlateletCountMedicalAnnotation(self):
        self.platelet_count_medical_annot = self.parameters[1].get('medical_annotation',[])

    def setPlateletCountRangeMale(self):
        self.platelet_count_range_male = self.parameters[1].get('value_meta_data',[])[0].get('range',"")

    def setPlateletCountRangeFemale(self):
        self.platelet_count_range_female = self.parameters[1].get('value_meta_data',[])[1].get('range',"")

    def setPlateletCountLowMale(self):
        self.platelet_count_low_male = self.parameters[1].get('value_meta_data',[])[0].get('low_value',"")

    def setPlateletCountFairMale(self):
        self.platelet_count_fair_male = self.parameters[1].get('value_meta_data',[])[0].get('fair_value',"")
        
    def setPlateletCountModerateMale(self):
        self.platelet_count_moderate_male = self.parameters[1].get('value_meta_data',[])[0].get('moderate_value',"")

    def setPlateletCountHighMale(self):
        self.platelet_count_high_male = self.parameters[1].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setPlateletCountLowFemale(self):
        self.platelet_count_low_female = self.parameters[1].get('value_meta_data',[])[0].get('low_value',"")

    def setPlateletCountFairFemale(self):
        self.platelet_count_fair_female = self.parameters[1].get('value_meta_data',[])[0].get('fair_value',"")

    def setPlateletCountModerateFemale(self):
        self.platelet_count_moderate_female = self.parameters[1].get('value_meta_data',[])[0].get('moderate_value',"")

    def setPlateletCountHighFemale(self):
        self.platelet_count_high_female = self.parameters[1].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setPlateletCountFunc(self):
        self.platelet_count_func = self.parameters[1].get("value_function",{}).get("function_name","")

    def setRbcCountValue(self, rbc_count):
        self.rbc_count = rbc_count

    def setRbcCountUnit(self):	
        self.rbc_count_unit = self.parameters[2].get('value_meta_data', [])[0].get('unit', "")
    
    def setRbcCountMedicalAnnotation(self):
        self.rbc_count_medical_annot = self.parameters[2].get('medical_annotation',[])

    def setRbcCountRangeMale(self):
        self.rbc_count_range_male = self.parameters[2].get('value_meta_data',[])[0].get('range',"")

    def setRbcCountRangeFemale(self):
        self.rbc_count_range_female = self.parameters[2].get('value_meta_data',[])[1].get('range',"")

    def setRbcCountLowMale(self):
        self.rbc_count_low_male = self.parameters[2].get('value_meta_data',[])[0].get('low_value',"")

    def setRbcCountFairMale(self):
        self.rbc_count_fair_male = self.parameters[2].get('value_meta_data',[])[0].get('fair_value',"")
        
    def setRbcCountModerateMale(self):
        self.rbc_count_moderate_male = self.parameters[2].get('value_meta_data',[])[0].get('moderate_value',"")

    def setRbcCountHighMale(self):
        self.rbc_count_high_male = self.parameters[2].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setRbcCountLowFemale(self):
        self.rbc_count_low_female = self.parameters[2].get('value_meta_data',[])[1].get('low_value',"")

    def setRbcCountFairFemale(self):
        self.rbc_count_fair_female = self.parameters[2].get('value_meta_data',[])[1].get('fair_value',"")

    def setRbcCountModerateFemale(self):
        self.rbc_count_moderate_female = self.parameters[2].get('value_meta_data',[])[1].get('moderate_value',"")

    def setRbcCountHighFemale(self):
        self.rbc_count_high_female = self.parameters[2].get('value_meta_data',[])[1].get('high_value',"")[1:]

    def setRbcCountFunc(self):
        self.rbc_count_func = self.parameters[2].get("value_function",{}).get("function_name","")

    def setWbcCountValue(self, wbc_count):
        self.wbc_count = wbc_count

    def setWbcCountUnit(self):
        self.wbc_count_unit = self.parameters[3].get('value_meta_data', [])[0].get('unit', "")
    
    def setWbcCountMedicalAnnotation(self):
        self.wbc_count_medical_annot = self.parameters[3].get('medical_annotation',[])

    def setWbcCountRangeMale(self):
        self.wbc_count_range_male = self.parameters[3].get('value_meta_data',[])[0].get('range',"")

    def setWbcCountRangeFemale(self):
        self.wbc_count_range_female = self.parameters[3].get('value_meta_data',[])[1].get('range',"")

    def setWbcCountLowMale(self):
        self.wbc_count_low_male = self.parameters[3].get('value_meta_data',[])[0].get('low_value',"")

    def setWbcCountFairMale(self):
        self.wbc_count_fair_male = self.parameters[3].get('value_meta_data',[])[0].get('fair_value',"")
        
    def setWbcCountModerateMale(self):
        self.wbc_count_moderate_male = self.parameters[3].get('value_meta_data',[])[0].get('moderate_value',"")

    def setWbcCountHighMale(self):
        self.wbc_count_high_male = self.parameters[3].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setWbcCountLowFemale(self):
        self.wbc_count_low_female = self.parameters[3].get('value_meta_data',[])[0].get('low_value',"")

    def setWbcCountFairFemale(self):
        self.wbc_count_fair_female = self.parameters[3].get('value_meta_data',[])[0].get('fair_value',"")
        
    def setWbcCountModerateFemale(self):
        self.wbc_count_moderate_female = self.parameters[3].get('value_meta_data',[])[0].get('moderate_value',"")

    def setWbcCountHighFemale(self):
        self.wbc_count_high_female = self.parameters[3].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setWbcCountFunc(self):
        self.wbc_count_func = self.parameters[3].get("value_function",{}).get("function_name","")

    # setters neutrophils
    def setNeutrophilsValue(self, neutrophil):
        self.neutrophils = neutrophil

    def setNeutrophilsUnit(self):
        self.neutroph_unit = self.parameters[4].get('value_meta_data', [])[0].get('unit', "")

    def setNeutrophilsMedicalAnnotation(self):
        self.neutroph_medical_annot = self.parameters[4].get('medical_annotation',[])

    def setNeutrophilsRangeMale(self):
        self.neutroph_range_male = self.parameters[4].get('value_meta_data',[])[0].get('range',"")

    def setNeutrophilsRangeFemale(self):
        self.neutroph_range_female = self.parameters[4].get('value_meta_data',[])[1].get('range',"")

    def setNeutrophilsLowMale(self):
        self.neutroph_low_male = self.parameters[4].get('value_meta_data',[])[0].get('low_value',"")

    def setNeutrophilsFairMale(self):
        self.neutroph_fair_male = self.parameters[4].get('value_meta_data',[])[0].get('fair_value',"")

    def setNeutrophilsModerateMale(self):
        self.neutroph_moderate_male = self.parameters[4].get('value_meta_data',[])[0].get('moderate_value',"")

    def setNeutrophilsHighMale(self):
        self.neutroph_high_male = self.parameters[4].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setNeutrophilsLowFemale(self):
        self.neutroph_low_female = self.parameters[4].get('value_meta_data',[])[0].get('low_value',"")

    def setNeutrophilsFairFemale(self):
        self.neutroph_fair_female = self.parameters[4].get('value_meta_data',[])[0].get('fair_value',"")

    def setNeutrophilsModerateFemale(self):
        self.neutroph_moderate_female = self.parameters[4].get('value_meta_data',[])[0].get('moderate_value',"")

    def setNeutrophilsHighFemale(self):
        self.neutroph_high_female = self.parameters[4].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setNeutrophilsFunc(self):
        self.neutroph_func = self.parameters[4].get("value_function",{}).get("function_name","")

    def setNeutrophilsAbsValue(self, neutrophil_abs):
        self.neutrophils_absolute = neutrophil_abs

    def setNeutrophilsAbsUnit(self):
        self.neutroph_abs_unit = self.parameters[5].get('value_meta_data', [])[0].get('unit', "")

    def setNeutrophilsAbsMedicalAnnotation(self):
        self.neutroph_abs_medical_annot = self.parameters[5].get('medical_annotation',[])

    def setNeutrophilsAbsRangeMale(self):
        self.neutroph_abs_range_male = self.parameters[5].get('value_meta_data',[])[0].get('range',"")

    def setNeutrophilsAbsRangeFemale(self):
        self.neutroph_abs_range_female = self.parameters[5].get('value_meta_data',[])[1].get('range',"")

    def setNeutrophilsAbsLowMale(self):
        self.neutroph_abs_low_male = self.parameters[5].get('value_meta_data',[])[0].get('low_value',"")

    def setNeutrophilsAbsFairMale(self):
        self.neutroph_abs_fair_male = self.parameters[5].get('value_meta_data',[])[0].get('fair_value',"")

    def setNeutrophilsAbsModerateMale(self):
        self.neutroph_abs_moderate_male = self.parameters[5].get('value_meta_data',[])[0].get('moderate_value',"")

    def setNeutrophilsAbsHighMale(self):
        self.neutroph_abs_high_male = self.parameters[5].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setNeutrophilsAbsLowFemale(self):
        self.neutroph_abs_low_female = self.parameters[5].get('value_meta_data',[])[0].get('low_value',"")

    def setNeutrophilsAbsFairFemale(self):
        self.neutroph_abs_fair_female = self.parameters[5].get('value_meta_data',[])[0].get('fair_value',"")

    def setNeutrophilsAbsModerateFemale(self):
        self.neutroph_abs_moderate_female = self.parameters[5].get('value_meta_data',[])[0].get('moderate_value',"")

    def setNeutrophilsAbsHighFemale(self):
        self.neutroph_abs_high_female = self.parameters[5].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setNeutrophilsAbsFunc(self):
        self.neutroph_abs_func = self.parameters[5].get("value_function",{}).get("function_name","")

    def setEosinophilsValue(self, eosinophil):
        self.eosinophils = eosinophil

    def setEosinophilsUnit(self):
        self.eosino_unit = self.parameters[6].get('value_meta_data', [])[0].get('unit', "")

    def setEosinophilsMedicalAnnotation(self):
        self.eosino_medical_annot = self.parameters[6].get('medical_annotation',[])

    def setEosinophilsRangeMale(self):
        self.eosino_range_male = self.parameters[6].get('value_meta_data',[])[0].get('range',"")

    def setEosinophilsRangeFemale(self):
        self.eosino_range_female = self.parameters[6].get('value_meta_data',[])[1].get('range',"")

    def setEosinophilsLowMale(self):
        self.eosino_low_male = self.parameters[6].get('value_meta_data',[])[0].get('low_value',"")

    def setEosinophilsFairMale(self):
        self.eosino_fair_male = self.parameters[6].get('value_meta_data',[])[0].get('fair_value',"")

    def setEosinophilsModerateMale(self):
        self.eosino_moderate_male = self.parameters[6].get('value_meta_data',[])[0].get('moderate_value',"")

    def setEosinophilsHighMale(self):
        self.eosino_high_male = self.parameters[6].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setEosinophilsLowFemale(self):
        self.eosino_low_female = self.parameters[6].get('value_meta_data',[])[0].get('low_value',"")

    def setEosinophilsFairFemale(self):
        self.eosino_fair_female = self.parameters[6].get('value_meta_data',[])[0].get('fair_value',"")

    def setEosinophilsModerateFemale(self):
        self.eosino_moderate_female = self.parameters[6].get('value_meta_data',[])[0].get('moderate_value',"")

    def setEosinophilsHighFemale(self):
        self.eosino_high_female = self.parameters[6].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setEosinophilsFunc(self):
        self.eosino_func = self.parameters[6].get("value_function",{}).get("function_name","")
  
    def setEosinophilsAbsValue(self, eosinophil_abs):
        self.eosinophils_absolute = eosinophil_abs

    def setEosinophilsAbsUnit(self):
        self.eosino_abs_unit = self.parameters[6].get('value_meta_data', [])[0].get('unit', "")

    def setEosinophilsAbsMedicalAnnotation(self):
        self.eosino_abs_medical_annot = self.parameters[7].get('medical_annotation',[])

    def setEosinophilsAbsRangeMale(self):
        self.eosino_abs_range_male = self.parameters[7].get('value_meta_data',[])[0].get('range',"")

    def setEosinophilsAbsRangeFemale(self):
        self.eosino_abs_range_female = self.parameters[7].get('value_meta_data',[])[1].get('range',"")

    def setEosinophilsAbsLowMale(self):
        self.eosino_abs_low_male = self.parameters[7].get('value_meta_data',[])[0].get('low_value',"")

    def setEosinophilsAbsFairMale(self):
        self.eosino_abs_fair_male = self.parameters[7].get('value_meta_data',[])[0].get('fair_value',"")

    def setEosinophilsAbsModerateMale(self):
        self.eosino_abs_moderate_male = self.parameters[7].get('value_meta_data',[])[0].get('moderate_value',"")

    def setEosinophilsAbsHighMale(self):
        self.eosino_abs_high_male = self.parameters[7].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setEosinophilsAbsLowFemale(self):
        self.eosino_abs_low_female = self.parameters[7].get('value_meta_data',[])[0].get('low_value',"")

    def setEosinophilsAbsFairFemale(self):
        self.eosino_abs_fair_female = self.parameters[7].get('value_meta_data',[])[0].get('fair_value',"")

    def setEosinophilsAbsModerateFemale(self):
        self.eosino_abs_moderate_female = self.parameters[7].get('value_meta_data',[])[0].get('moderate_value',"")

    def setEosinophilsAbsHighFemale(self):
        self.eosino_abs_high_female = self.parameters[7].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setEosinophilsAbsFunc(self):
        self.eosino_abs_func = self.parameters[7].get("value_function",{}).get("function_name","")

    def setBasophilsValue(self, basophil):
        self.basophils = basophil

    def setBasophilsUnit(self):
        self.basoph_unit = self.parameters[8].get('value_meta_data', [])[0].get('unit', "")

    def setBasophilsMedicalAnnotation(self):
        self.basoph_medical_annot = self.parameters[8].get('medical_annotation',[])

    def setBasophilsRangeMale(self):
        self.basoph_range_male = self.parameters[8].get('value_meta_data',[])[0].get('range',"")

    def setBasophilsRangeFemale(self):
        self.basoph_range_female = self.parameters[8].get('value_meta_data',[])[1].get('range',"")

    def setBasophilsLowMale(self):
        self.basoph_low_male = self.parameters[8].get('value_meta_data',[])[0].get('low_value',"")

    def setBasophilsFairMale(self):
        self.basoph_fair_male = self.parameters[8].get('value_meta_data',[])[0].get('fair_value',"")

    def setBasophilsModerateMale(self):
        self.basoph_moderate_male = self.parameters[8].get('value_meta_data',[])[0].get('moderate_value',"")

    def setBasophilsHighMale(self):
        self.basoph_high_male = self.parameters[8].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setBasophilsLowFemale(self):
        self.basoph_low_female = self.parameters[8].get('value_meta_data',[])[0].get('low_value',"")

    def setBasophilsFairFemale(self):
        self.basoph_fair_female = self.parameters[8].get('value_meta_data',[])[0].get('fair_value',"")

    def setBasophilsModerateFemale(self):
        self.basoph_moderate_female = self.parameters[8].get('value_meta_data',[])[0].get('moderate_value',"")

    def setBasophilsHighFemale(self):
        self.basoph_high_female = self.parameters[8].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setBasophilsFunc(self):
        self.basoph_func = self.parameters[8].get("value_function",{}).get("function_name","")

    def setBasophilsAbsValue(self, basophil_abs):
        self.basophils_absolute = basophil_abs

    def setBasophilsAbsUnit(self):
        self.basoph_abs_unit = self.parameters[9].get('value_meta_data', [])[0].get('unit', "")

    def setBasophilsAbsMedicalAnnotation(self):
        self.basoph_abs_medical_annot = self.parameters[9].get('medical_annotation',[])

    def setBasophilsAbsRangeMale(self):
        self.basoph_abs_range_male = self.parameters[9].get('value_meta_data',[])[0].get('range',"")

    def setBasophilsAbsRangeFemale(self):
        self.basoph_abs_range_female = self.parameters[9].get('value_meta_data',[])[1].get('range',"")

    def setBasophilsAbsLowMale(self):
        self.basoph_abs_low_male = self.parameters[9].get('value_meta_data',[])[0].get('low_value',"")

    def setBasophilsAbsFairMale(self):
        self.basoph_abs_fair_male = self.parameters[9].get('value_meta_data',[])[0].get('fair_value',"")

    def setBasophilsAbsModerateMale(self):
        self.basoph_abs_moderate_male = self.parameters[9].get('value_meta_data',[])[0].get('moderate_value',"")

    def setBasophilsAbsHighMale(self):
        self.basoph_abs_high_male = self.parameters[9].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setBasophilsAbsLowFemale(self):
        self.basoph_abs_low_female = self.parameters[9].get('value_meta_data',[])[0].get('low_value',"")

    def setBasophilsAbsFairFemale(self):
        self.basoph_abs_fair_female = self.parameters[9].get('value_meta_data',[])[0].get('fair_value',"")

    def setBasophilsAbsModerateFemale(self):
        self.basoph_abs_moderate_female = self.parameters[9].get('value_meta_data',[])[0].get('moderate_value',"")

    def setBasophilsAbsHighFemale(self):
        self.basoph_abs_high_female = self.parameters[9].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setBasophilsAbsFunc(self):
        self.basoph_abs_func = self.parameters[9].get("value_function",{}).get("function_name","")

    def setLymphocytesValue(self, lymphocyte):
        self.lymphocytes = lymphocyte

    def setLymphocytesUnit(self):
        self.lymph_unit = self.parameters[10].get('value_meta_data', [])[0].get('unit', "")

    def setLymphocytesMedicalAnnotation(self):
        self.lymph_medical_annot = self.parameters[10].get('medical_annotation',[])

    def setLymphocytesRangeMale(self):
        self.lymph_range_male = self.parameters[10].get('value_meta_data',[])[0].get('range',"")

    def setLymphocytesRangeFemale(self):
        self.lymph_range_female = self.parameters[10].get('value_meta_data',[])[1].get('range',"")

    def setLymphocytesLowMale(self):
        self.lymph_low_male = self.parameters[10].get('value_meta_data',[])[0].get('low_value',"")

    def setLymphocytesFairMale(self):
        self.lymph_fair_male = self.parameters[10].get('value_meta_data',[])[0].get('fair_value',"")

    def setLymphocytesModerateMale(self):
        self.lymph_moderate_male = self.parameters[10].get('value_meta_data',[])[0].get('moderate_value',"")

    def setLymphocytesHighMale(self):
        self.lymph_high_male = self.parameters[10].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setLymphocytesLowFemale(self):
        self.lymph_low_female = self.parameters[10].get('value_meta_data',[])[0].get('low_value',"")

    def setLymphocytesFairFemale(self):
        self.lymph_fair_female = self.parameters[10].get('value_meta_data',[])[0].get('fair_value',"")

    def setLymphocytesModerateFemale(self):
        self.lymph_moderate_female = self.parameters[10].get('value_meta_data',[])[0].get('moderate_value',"")

    def setLymphocytesHighFemale(self):
        self.lymph_high_female = self.parameters[10].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setLymphocytesFunc(self):
        self.lymph_func = self.parameters[10].get("value_function",{}).get("function_name","")

    def setLymphocytesAbsValue(self, lymphocyte_abs):
        self.lymphocytes_absolute = lymphocyte_abs

    def setLymphocytesAbsUnit(self):
        self.lymph_abs_unit = self.parameters[11].get('value_meta_data', [])[0].get('unit', "")

    def setLymphocytesAbsMedicalAnnotation(self):
        self.lymph_abs_medical_annot = self.parameters[11].get('medical_annotation',[])

    def setLymphocytesAbsRangeMale(self):
        self.lymph_abs_range_male = self.parameters[11].get('value_meta_data',[])[0].get('range',"")

    def setLymphocytesAbsRangeFemale(self):
        self.lymph_abs_range_female = self.parameters[11].get('value_meta_data',[])[1].get('range',"")

    def setLymphocytesAbsLowMale(self):
        self.lymph_abs_low_male = self.parameters[11].get('value_meta_data',[])[0].get('low_value',"")

    def setLymphocytesAbsFairMale(self):
        self.lymph_abs_fair_male = self.parameters[11].get('value_meta_data',[])[0].get('fair_value',"")

    def setLymphocytesAbsModerateMale(self):
        self.lymph_abs_moderate_male = self.parameters[11].get('value_meta_data',[])[0].get('moderate_value',"")

    def setLymphocytesAbsHighMale(self):
        self.lymph_abs_high_male = self.parameters[11].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setLymphocytesAbsLowFemale(self):
        self.lymph_abs_low_female = self.parameters[11].get('value_meta_data',[])[0].get('low_value',"")

    def setLymphocytesAbsFairFemale(self):
        self.lymph_abs_fair_female = self.parameters[11].get('value_meta_data',[])[0].get('fair_value',"")

    def setLymphocytesAbsModerateFemale(self):
        self.lymph_abs_moderate_female = self.parameters[11].get('value_meta_data',[])[0].get('moderate_value',"")

    def setLymphocytesAbsHighFemale(self):
        self.lymph_abs_high_female = self.parameters[11].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setLymphocytesAbsFunc(self):
        self.lymph_abs_func = self.parameters[11].get("value_function",{}).get("function_name","")

    def setMonocytesValue(self, monocyte):
        self.monocytes = monocyte

    def setMonocytesUnit(self):
        self.monocy_unit = self.parameters[12].get('value_meta_data', [])[0].get('unit', "")

    def setMonocytesMedicalAnnotation(self):
        self.monocy_medical_annot = self.parameters[12].get('medical_annotation',[])

    def setMonocytesRangeMale(self):
        self.monocy_range_male = self.parameters[12].get('value_meta_data',[])[0].get('range',"")

    def setMonocytesRangeFemale(self):
        self.monocy_range_female = self.parameters[12].get('value_meta_data',[])[1].get('range',"")

    def setMonocytesLowMale(self):
        self.monocy_low_male = self.parameters[12].get('value_meta_data',[])[0].get('low_value',"")

    def setMonocytesFairMale(self):
        self.monocy_fair_male = self.parameters[12].get('value_meta_data',[])[0].get('fair_value',"")

    def setMonocytesModerateMale(self):
        self.monocy_moderate_male = self.parameters[12].get('value_meta_data',[])[0].get('moderate_value',"")

    def setMonocytesHighMale(self):
        self.monocy_high_male = self.parameters[12].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setMonocytesLowFemale(self):
        self.monocy_low_female = self.parameters[12].get('value_meta_data',[])[0].get('low_value',"")

    def setMonocytesFairFemale(self):
        self.monocy_fair_female = self.parameters[12].get('value_meta_data',[])[0].get('fair_value',"")

    def setMonocytesModerateFemale(self):
        self.monocy_moderate_female = self.parameters[12].get('value_meta_data',[])[0].get('moderate_value',"")

    def setMonocytesHighFemale(self):
        self.monocy_high_female = self.parameters[12].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setMonocytesFunc(self):
        self.monocy_func = self.parameters[12].get("value_function",{}).get("function_name","")

    def setMonocytesAbsValue(self, monocyte_abs):
        self.monocytes_absolute = monocyte_abs

    def setMonocytesAbsUnit(self):
        self.monocy_abs_unit = self.parameters[13].get('value_meta_data', [])[0].get('unit', "")

    def setMonocytesAbsMedicalAnnotation(self):
        self.monocy_abs_medical_annot = self.parameters[13].get('medical_annotation',[])

    def setMonocytesAbsRangeMale(self):
        self.monocy_abs_range_male = self.parameters[13].get('value_meta_data',[])[0].get('range',"")

    def setMonocytesAbsRangeFemale(self):
        self.monocy_abs_range_female = self.parameters[13].get('value_meta_data',[])[1].get('range',"")

    def setMonocytesAbsLowMale(self):
        self.monocy_abs_low_male = self.parameters[13].get('value_meta_data',[])[0].get('low_value',"")

    def setMonocytesAbsFairMale(self):
        self.monocy_abs_fair_male = self.parameters[13].get('value_meta_data',[])[0].get('fair_value',"")

    def setMonocytesAbsModerateMale(self):
        self.monocy_abs_moderate_male = self.parameters[13].get('value_meta_data',[])[0].get('moderate_value',"")

    def setMonocytesAbsHighMale(self):
        self.monocy_abs_high_male = self.parameters[13].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setMonocytesAbsLowFemale(self):
        self.monocy_abs_low_female = self.parameters[13].get('value_meta_data',[])[0].get('low_value',"")

    def setMonocytesAbsFairFemale(self):
        self.monocy_abs_fair_female = self.parameters[13].get('value_meta_data',[])[0].get('fair_value',"")

    def setMonocytesAbsModerateFemale(self):
        self.monocy_abs_moderate_female = self.parameters[13].get('value_meta_data',[])[0].get('moderate_value',"")

    def setMonocytesAbsHighFemale(self):
        self.monocy_abs_high_female = self.parameters[13].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setMonocytesAbsFunc(self):
        self.monocy_abs_func = self.parameters[13].get("value_function",{}).get("function_name","")

 
    # getter functions
    # Fuction returns category id
    def getCategoryid(self):
        return self.category_id 

    # Function returns category name
    def getCategoryName(self):
        return self.category_name

    # Function returns Version number
    def getVersionNumber(self):
        return self.version_number

    def getHemoglobinValue(self):
        return self.hemoglobin

    def getHemoglobinUnit(self):
        return self.hemoglobin_unit

    def getHemoglobinMedicalAnnotation(self):
        return self.hemoglobin_medical_annot

    def getHemoglobinRangeMale(self):
        return self.hemoglobin_range_male
    
    def getHemoglobinRangeFemale(self):
        return self.hemoglobin_range_female

    def getHemoglobinLowValueMale(self):
        return self.hemoglobin_low_male

    def getHemoglobinFairValueMale(self):
        return self.hemoglobin_fair_male
    
    def getHemoglobinModerateValueMale(self):
        return self.hemoglobin_moderate_male

    def getHemoglobinHighValueMale(self):
        return self.hemoglobin_high_male

    def getHemoglobinLowValueFemale(self):
        return self.hemoglobin_low_female

    def getHemoglobinFairValueFemale(self):
        return self.hemoglobin_fair_female

    def getHemoglobinModerateValueFemale(self):
        return self.hemoglobin_moderate_female

    def getHemoglobinHighValueFemale(self):
        return self.hemoglobin_high_female

    def getHemoglobinFunc(self):
        return self.hemoglobin_func

    def getPlateletCountValue(self):
        return self.platelet_count

    def getPlateletCountUnit(self):
        return self.platelet_count_unit

    def getPlateletCountMedicalAnnotation(self):
        return self.platelet_count_medical_annot

    def getPlateletCountRangeMale(self):
        return self.platelet_count_range_male

    def getPlateletCountRangeFemale(self):
        return self.platelet_count_range_female

    def getPlateletCountLowValueMale(self):
        return self.platelet_count_low_male

    def getPlateletCountFairValueMale(self):
        return self.platelet_count_fair_male

    def getPlateletCountModerateValueMale(self):
        return self.platelet_count_moderate_male

    def getPlateletCountHighValueMale(self):
        return self.platelet_count_high_male

    def getPlateletCountLowValueFemale(self):
        return self.platelet_count_low_female

    def getPlateletCountFairValueFemale(self):
        return self.platelet_count_fair_female

    def getPlateletCountModerateValueFemale(self):
        return self.platelet_count_moderate_female

    def getPlateletCountHighValueFemale(self):
        return self.platelet_count_high_female

    def getPlateletCountFunc(self):
        return self.platelet_count_func

    def getWbcCountValue(self):
        return self.wbc_count

    def getWbcCountUnit(self):
        return self.wbc_count_unit

    def getWbcCountMedicalAnnotation(self):
        return self.wbc_count_medical_annot

    def getWbcCountRangeMale(self):
        return self.wbc_count_range_male

    def getWbcCountRangeFemale(self):
        return self.wbc_count_range_female

    def getWbcCountLowValueMale(self):
        return self.wbc_count_low_male

    def getWbcCountFairValueMale(self):
        return self.wbc_count_fair_male

    def getWbcCountModerateValueMale(self):
        return self.wbc_count_moderate_male

    def getWbcCountHighValueMale(self):
        return self.wbc_count_high_male

    def getWbcCountLowValueFemale(self):
        return self.wbc_count_low_female

    def getWbcCountFairValueFemale(self):
        return self.wbc_count_fair_female

    def getWbcCountModerateValueFemale(self):
        return self.wbc_count_moderate_female

    def getWbcCountHighValueFemale(self):
        return self.wbc_count_high_female

    def getWbcCountFunc(self):
        return self.wbc_count_func     

    def getRbcCountValue(self):
        return self.rbc_count

    def getRbcCountUnit(self):
        return self.rbc_count_unit

    def getRbcCountMedicalAnnotation(self):
        return self.rbc_count_medical_annot

    def getRbcCountRangeMale(self):
        return self.rbc_count_range_male

    def getRbcCountRangeFemale(self):
        return self.rbc_count_range_female

    def getRbcCountLowValueMale(self):
        return self.rbc_count_low_male

    def getRbcCountFairValueMale(self):
        return self.rbc_count_fair_male

    def getRbcCountModerateValueMale(self):
        return self.rbc_count_moderate_male

    def getRbcCountHighValueMale(self):
        return self.rbc_count_high_male

    def getRbcCountLowValueFemale(self):
        return self.rbc_count_low_female

    def getRbcCountFairValueFemale(self):
        return self.rbc_count_fair_female

    def getRbcCountModerateValueFemale(self):
        return self.rbc_count_moderate_female

    def getRbcCountHighValueFemale(self):
        return self.rbc_count_high_female

    def getRbcCountFunc(self):
        return self.rbc_count_func        

    def getNeutrophilsValue(self):
        return self.neutrophils

    def getNeutrophilsUnit(self):
        return self.neutroph_unit

    def getNeutrophilsMedicalAnnotation(self):
        return self.neutroph_medical_annot

    def getNeutrophilsRangeMale(self):
        return self.neutroph_range_male

    def getNeutrophilsRangeFemale(self):
        return self.neutroph_range_female

    def getNeutrophilsLowValueMale(self):
        return self.neutroph_low_male

    def getNeutrophilsFairValueMale(self):
        return self.neutroph_fair_male

    def getNeutrophilsModerateValueMale(self):
        return self.neutroph_moderate_male

    def getNeutrophilsHighValueMale(self):
        return self.neutroph_high_male

    def getNeutrophilsLowValueFemale(self):
        return self.neutroph_low_female

    def getNeutrophilsFairValueFemale(self):
        return self.neutroph_fair_female

    def getNeutrophilsModerateValueFemale(self):
        return self.neutroph_moderate_female

    def getNeutrophilsHighValueFemale(self):
        return self.neutroph_high_female

    def getNeutrophilsFunc(self):
        return self.neutroph_func

    def getNeutrophilsAbsValue(self):
        return self.neutrophils_absolute

    def getNeutrophilsAbsUnit(self):
        return self.neutroph_abs_unit

    def getNeutrophilsAbsMedicalAnnotation(self):
        return self.neutroph_abs_medical_annot

    def getNeutrophilsAbsRangeMale(self):
        return self.neutroph_abs_range_male

    def getNeutrophilsAbsRangeFemale(self):
        return self.neutroph_abs_range_female

    def getNeutrophilsAbsLowValueMale(self):
        return self.neutroph_abs_low_male

    def getNeutrophilsAbsFairValueMale(self):
        return self.neutroph_abs_fair_male

    def getNeutrophilsAbsModerateValueMale(self):
        return self.neutroph_abs_moderate_male

    def getNeutrophilsAbsHighValueMale(self):
        return self.neutroph_abs_high_male

    def getNeutrophilsAbsLowValueFemale(self):
        return self.neutroph_abs_low_female

    def getNeutrophilsAbsFairValueFemale(self):
        return self.neutroph_abs_fair_female

    def getNeutrophilsAbsModerateValueFemale(self):
        return self.neutroph_abs_moderate_female

    def getNeutrophilsAbsHighValueFemale(self):
        return self.neutroph_abs_high_female

    def getNeutrophilsAbsFunc(self):
        return self.neutroph_abs_func

    def getEosinophilsValue(self):
        return self.eosinophils

    def getEosinophilsUnit(self):
        return self.eosino_unit

    def getEosinophilsMedicalAnnotation(self):
        return self.eosino_medical_annot

    def getEosinophilsRangeMale(self):
        return self.eosino_range_male

    def getEosinophilsRangeFemale(self):
        return self.eosino_range_female

    def getEosinophilsLowValueMale(self):
        return self.eosino_low_male

    def getEosinophilsFairValueMale(self):
        return self.eosino_fair_male

    def getEosinophilsModerateValueMale(self):
        return self.eosino_moderate_male

    def getEosinophilsHighValueMale(self):
        return self.eosino_high_male

    def getEosinophilsLowValueFemale(self):
        return self.eosino_low_female

    def getEosinophilsFairValueFemale(self):
        return self.eosino_fair_female

    def getEosinophilsModerateValueFemale(self):
        return self.eosino_moderate_female

    def getEosinophilsHighValueFemale(self):
        return self.eosino_high_female

    def getEosinophilsFunc(self):
        return self.eosino_func

    def getEosinophilsAbsValue(self):
        return self.eosinophils_absolute

    def getEosinophilsAbsUnit(self):
        return self.eosino_abs_unit

    def getEosinophilsAbsMedicalAnnotation(self):
        return self.eosino_abs_medical_annot

    def getEosinophilsAbsRangeMale(self):
        return self.eosino_abs_range_male

    def getEosinophilsAbsRangeFemale(self):
        return self.eosino_abs_range_female

    def getEosinophilsAbsLowValueMale(self):
        return self.eosino_abs_low_male

    def getEosinophilsAbsFairValueMale(self):
        return self.eosino_abs_fair_male

    def getEosinophilsAbsModerateValueMale(self):
        return self.eosino_abs_moderate_male

    def getEosinophilsAbsHighValueMale(self):
        return self.eosino_abs_high_male

    def getEosinophilsAbsLowValueFemale(self):
        return self.eosino_abs_low_female

    def getEosinophilsAbsFairValueFemale(self):
        return self.eosino_abs_fair_female

    def getEosinophilsAbsModerateValueFemale(self):
        return self.eosino_abs_moderate_female

    def getEosinophilsAbsHighValueFemale(self):
        return self.eosino_abs_high_female

    def getEosinophilsAbsFunc(self):
        return self.eosino_abs_func

    def getBasophilsValue(self):
        return self.basophils

    def getBasophilsUnit(self):
        return self.basoph_unit

    def getBasophilsMedicalAnnotation(self):
        return self.basoph_medical_annot

    def getBasophilsRangeMale(self):
        return self.basoph_range_male

    def getBasophilsRangeFemale(self):
        return self.basoph_range_female

    def getBasophilsLowValueMale(self):
        return self.basoph_low_male

    def getBasophilsFairValueMale(self):
        return self.basoph_fair_male

    def getBasophilsModerateValueMale(self):
        return self.basoph_moderate_male

    def getBasophilsHighValueMale(self):
        return self.basoph_high_male

    def getBasophilsLowValueFemale(self):
        return self.basoph_low_female

    def getBasophilsFairValueFemale(self):
        return self.basoph_fair_female

    def getBasophilsModerateValueFemale(self):
        return self.basoph_moderate_female

    def getBasophilsHighValueFemale(self):
        return self.basoph_high_female

    def getBasophilsFunc(self):
        return self.basoph_func

    def getBasophilsAbsValue(self):
        return self.basophils_absolute

    def getBasophilsAbsUnit(self):
        return self.basoph_abs_unit

    def getBasophilsAbsMedicalAnnotation(self):
        return self.basoph_abs_medical_annot

    def getBasophilsAbsRangeMale(self):
        return self.basoph_abs_range_male

    def getBasophilsAbsRangeFemale(self):
        return self.basoph_abs_range_female

    def getBasophilsAbsLowValueMale(self):
        return self.basoph_abs_low_male

    def getBasophilsAbsFairValueMale(self):
        return self.basoph_abs_fair_male

    def getBasophilsAbsModerateValueMale(self):
        return self.basoph_abs_moderate_male

    def getBasophilsAbsHighValueMale(self):
        return self.basoph_abs_high_male

    def getBasophilsAbsLowValueFemale(self):
        return self.basoph_abs_low_female

    def getBasophilsAbsFairValueFemale(self):
        return self.basoph_abs_fair_female

    def getBasophilsAbsModerateValueFemale(self):
        return self.basoph_abs_moderate_female

    def getBasophilsAbsHighValueFemale(self):
        return self.basoph_abs_high_female

    def getBasophilsAbsFunc(self):
        return self.basoph_abs_func

    def getLymphocytesValue(self):
        return self.lymphocytes

    def getLymphocytesUnit(self):
        return self.lymph_unit

    def getLymphocytesMedicalAnnotation(self):
        return self.lymph_medical_annot

    def getLymphocytesRangeMale(self):
        return self.lymph_range_male

    def getLymphocytesRangeFemale(self):
        return self.lymph_range_female

    def getLymphocytesLowValueMale(self):
        return self.lymph_low_male

    def getLymphocytesFairValueMale(self):
        return self.lymph_fair_male

    def getLymphocytesModerateValueMale(self):
        return self.lymph_moderate_male

    def getLymphocytesHighValueMale(self):
        return self.lymph_high_male

    def getLymphocytesLowValueFemale(self):
        return self.lymph_low_female

    def getLymphocytesFairValueFemale(self):
        return self.lymph_fair_female

    def getLymphocytesModerateValueFemale(self):
        return self.lymph_moderate_female

    def getLymphocytesHighValueFemale(self):
        return self.lymph_high_female

    def getLymphocytesFunc(self):
        return self.lymph_func

    def getLymphocytesAbsValue(self):
        return self.lymphocytes_absolute

    def getLymphocytesAbsUnit(self):
        return self.lymph_abs_unit

    def getLymphocytesAbsMedicalAnnotation(self):
        return self.lymph_abs_medical_annot

    def getLymphocytesAbsRangeMale(self):
        return self.lymph_abs_range_male

    def getLymphocytesAbsRangeFemale(self):
        return self.lymph_abs_range_female

    def getLymphocytesAbsLowValueMale(self):
        return self.lymph_abs_low_male

    def getLymphocytesAbsFairValueMale(self):
        return self.lymph_abs_fair_male

    def getLymphocytesAbsModerateValueMale(self):
        return self.lymph_abs_moderate_male

    def getLymphocytesAbsHighValueMale(self):
        return self.lymph_abs_high_male

    def getLymphocytesAbsLowValueFemale(self):
        return self.lymph_abs_low_female

    def getLymphocytesAbsFairValueFemale(self):
        return self.lymph_abs_fair_female

    def getLymphocytesAbsModerateValueFemale(self):
        return self.lymph_abs_moderate_female

    def getLymphocytesAbsHighValueFemale(self):
        return self.lymph_abs_high_female

    def getLymphocytesAbsFunc(self):
        return self.lymph_abs_func

    def getMonocytesValue(self):
        return self.monocytes

    def getMonocytesUnit(self):
        return self.monocy_unit

    def getMonocytesMedicalAnnotation(self):
        return self.monocy_medical_annot

    def getMonocytesRangeMale(self):
        return self.monocy_range_male

    def getMonocytesRangeFemale(self):
        return self.monocy_range_female

    def getMonocytesLowValueMale(self):
        return self.monocy_low_male

    def getMonocytesFairValueMale(self):
        return self.monocy_fair_male

    def getMonocytesModerateValueMale(self):
        return self.monocy_moderate_male

    def getMonocytesHighValueMale(self):
        return self.monocy_high_male

    def getMonocytesLowValueFemale(self):
        return self.monocy_low_female

    def getMonocytesFairValueFemale(self):
        return self.monocy_fair_female

    def getMonocytesModerateValueFemale(self):
        return self.monocy_moderate_female

    def getMonocytesHighValueFemale(self):
        return self.monocy_high_female

    def getMonocytesFunc(self):
        return self.monocy_func

    def getMonocytesAbsValue(self):
        return self.monocytes_absolute

    def getMonocytesAbsUnit(self):
        return self.monocy_abs_unit

    def getMonocytesAbsMedicalAnnotation(self):
        return self.monocy_abs_medical_annot

    def getMonocytesAbsRangeMale(self):
        return self.monocy_abs_range_male

    def getMonocytesAbsRangeFemale(self):
        return self.monocy_abs_range_female

    def getMonocytesAbsLowValueMale(self):
        return self.monocy_abs_low_male

    def getMonocytesAbsFairValueMale(self):
        return self.monocy_abs_fair_male

    def getMonocytesAbsModerateValueMale(self):
        return self.monocy_abs_moderate_male

    def getMonocytesAbsHighValueMale(self):
        return self.monocy_abs_high_male

    def getMonocytesAbsLowValueFemale(self):
        return self.monocy_abs_low_female

    def getMonocytesAbsFairValueFemale(self):
        return self.monocy_abs_fair_female

    def getMonocytesAbsModerateValueFemale(self):
        return self.monocy_abs_moderate_female

    def getMonocytesAbsHighValueFemale(self):
        return self.monocy_abs_high_female

    def getMonocytesAbsFunc(self):
        return self.monocy_abs_func

