import json
from collections import OrderedDict
from __medical_report_parser import *
from __medical_report_template import *

class LipidProfile(MedicalReportTemplate):
    """
        A class for lipid profile
    """
    def __init__(self):
        try:
            super(LipidProfile, self).__init__()
            self.file_path = json_file_data.get("medical_parser_detail","")[1].get("file_name","")
            self.total_cholesterol = None
            self.hdl_cholesterol = None
            self.ldl_cholesterol = None
            self.triglycerides = None
            self.vldl_cholesterol = None
            self.non_hdl_cholesterol = None
            self.tc_hdl_ratio = None
            self.ldl_hdl_ratio = None
            self.apolipoproteina1 = None
            self.category_id = ""
            self.category_name = ""
            self.version_number = ""
            self.total_chol_unit = ""
            self.total_chol_medical_annot = []
            self.total_chol_range_male = ""
            self.total_chol_range_female = ""
            self.total_chol_low_male = ""
            self.total_chol_fair_male = ""
            self.total_chol_moderate_male = ""
            self.total_chol_high_male = ""
            self.total_chol_low_female = ""
            self.total_chol_fair_female = ""
            self.total_chol_moderate_female = ""
            self.total_chol_high_female = ""
            self.total_chol_func = ""
            self.hdl_chol_unit = ""
            self.hdl_chol_medical_annot = []
            self.hdl_chol_range_male = ""
            self.hdl_chol_range_female = ""
            self.hdl_chol_low_male = ""
            self.hdl_chol_fair_male = ""
            self.hdl_chol_moderate_male = ""
            self.hdl_chol_high_male = ""
            self.hdl_chol_low_female = ""
            self.hdl_chol_fair_female = ""
            self.hdl_chol_moderate_female = ""
            self.hdl_chol_high_female = ""
            self.hdl_chol_func = ""
            self.ldl_chol_unit = ""
            self.ldl_chol_medical_annot = []
            self.ldl_chol_range_male = ""
            self.ldl_chol_range_female = ""
            self.ldl_chol_low_male = ""
            self.ldl_chol_fair_male = ""
            self.ldl_chol_moderate_male = ""
            self.ldl_chol_high_male = ""
            self.ldl_chol_low_female = ""
            self.ldl_chol_fair_female = ""
            self.ldl_chol_moderate_female = ""
            self.ldl_chol_high_female = ""
            self.ldl_chol_func = ""
            self.trigly_unit = ""
            self.trigly_medical_annot = []
            self.trigly_range_male = ""
            self.trigly_range_female = ""
            self.trigly_low_male = ""
            self.trigly_fair_male = ""
            self.trigly_moderate_male = ""
            self.trigly_high_male = ""
            self.trigly_low_female = ""
            self.trigly_fair_female = ""
            self.trigly_moderate_female = ""
            self.trigly_high_female = ""
            self.vldl_func = ""
            self.vldl_unit = ""
            self.vldl_medical_annot = []
            self.vldl_range_male = ""
            self.vldl_range_female = ""
            self.vldl_low_male = ""
            self.vldl_fair_male = ""
            self.vldl_moderate_male = ""
            self.vldl_high_male = ""
            self.vldl_low_female = ""
            self.vldl_fair_female = ""
            self.vldl_moderate_female = ""
            self.vldl_high_female = ""
            self.vldl_func = ""
            self.non_hdl_unit = ""
            self.non_hdl_medical_annot = []
            self.non_hdl_range_male = ""
            self.non_hdl_range_female = ""
            self.non_hdl_low_male = ""
            self.non_hdl_fair_male = ""
            self.non_hdl_moderate_male = ""
            self.non_hdl_high_male = ""
            self.non_hdl_low_female = ""
            self.non_hdl_fair_female = ""
            self.non_hdl_moderate_female = ""
            self.non_hdl_high_female = ""
            self.non_hdl_func = ""
            self.tc_hdl_ratio_unit = ""
            self.tc_hdl_ratio_medical_annot = []
            self.tc_hdl_ratio_range_male = ""
            self.tc_hdl_ratio_range_female = ""
            self.tc_hdl_ratio_low_male = ""
            self.tc_hdl_ratio_fair_male = ""
            self.tc_hdl_ratio_moderate_male = ""
            self.tc_hdl_ratio_high_male = ""
            self.tc_hdl_ratio_low_female = ""
            self.tc_hdl_ratio_fair_female = ""
            self.tc_hdl_ratio_moderate_female = ""
            self.tc_hdl_ratio_high_female = ""
            self.tc_hdl_ratio_func = ""
            self.ldl_hdl_ratio_unit = ""
            self.ldl_hdl_ratio_medical_annot = []
            self.ldl_hdl_ratio_range_male = ""
            self.ldl_hdl_ratio_range_female = ""
            self.ldl_hdl_ratio_low_male = ""
            self.ldl_hdl_ratio_fair_male = ""
            self.ldl_hdl_ratio_moderate_male = ""
            self.ldl_hdl_ratio_high_male = ""
            self.ldl_hdl_ratio_low_female = ""
            self.ldl_hdl_ratio_fair_female = ""
            self.ldl_hdl_ratio_moderate_female = ""
            self.ldl_hdl_ratio_high_female = ""
            self.ldl_hdl_ratio_func = ""
            self.apolipoproteina1_unit = ""
            self.apolipoproteina1_medical_annot = []
            self.apolipoproteina1_range_male = ""
            self.apolipoproteina1_range_female = ""
            self.apolipoproteina1_low_male = ""
            self.apolipoproteina1_fair_male = ""
            self.apolipoproteina1_moderate_male = ""
            self.apolipoproteina1_high_male = ""
            self.apolipoproteina1_low_female = ""
            self.apolipoproteina1_fair_female = ""
            self.apolipoproteina1_moderate_female = ""
            self.apolipoproteina1_high_female = ""
            self.apolipoproteina1_func = ""
            self.tot_chol_output = OrderedDict()
            self.hdl_chol_output = OrderedDict()
            self.ldl_chol_output = OrderedDict()
            self.trigly_output = OrderedDict()
            self.vldl_chol_output = OrderedDict()
            self.non_hdl_chol_output = OrderedDict()
            self.tc_hdl_ratio_output = OrderedDict()
            self.ldl_hdl_ratio_output = OrderedDict()  
            self.apolipoproteina1_output = OrderedDict()
        except Exception as err:
            print err

    def loadMetaData(self):
        super(LipidProfile, self).loadMetaData()
        self.setCategoryid()
        self.setCategoryName()
        self.setVersionNumber()
        self.setTotalCholesterolUnit()
        self.setTotalCholesterolMedicalAnnotations()
        self.setTotalCholesterolRangeMale()
        self.setTotalCholesterolRangeFemale() 
        self.setTotalCholesterolLowValueMale()
        self.setTotalCholesterolFairValueMale()
        self.setTotalCholesterolModerateValueMale()
        self.setTotalCholesterolHighValueMale()
        self.setTotalCholesterolLowValueFemale()
        self.setTotalCholesterolFairValueFemale()
        self.setTotalCholesterolModerateValueFemale()
        self.setTotalCholesterolHighValueFemale()
        self.setTotalCholesterolsFunction()
        self.setHdlCholesterolUnit()
        self.setHdlCholesterolMedicalAnnotations()
        self.setHdlCholesterolRangeMale()
        self.setHdlCholesterolRangeFemale() 
        self.setHdlCholesterolLowValueMale()
        self.setHdlCholesterolFairValueMale()
        self.setHdlCholesterolModerateValueMale()
        self.setHdlCholesterolHighValueMale()
        self.setHdlCholesterolLowValueFemale()
        self.setHdlCholesterolFairValueFemale()
        self.setHdlCholesterolModerateValueFemale()
        self.setHdlCholesterolHighValueFemale()
        self.setHdlCholesterolsFunction()
        self.setLdlCholesterolUnit()
        self.setLdlCholesterolMedicalAnnotations()
        self.setLdlCholesterolRangeMale()
        self.setLdlCholesterolRangeFemale() 
        self.setLdlCholesterolLowValueMale()
        self.setLdlCholesterolFairValueMale()
        self.setLdlCholesterolModerateValueMale()
        self.setLdlCholesterolHighValueMale()
        self.setLdlCholesterolLowValueFemale()
        self.setLdlCholesterolFairValueFemale()
        self.setLdlCholesterolModerateValueFemale()
        self.setLdlCholesterolHighValueFemale()
        self.setLdlCholesterolsFunction()
        self.setTriglyceridesUnit()
        self.setTriglyceridesMedicalAnnotations()
        self.setTriglyceridesRangeMale()
        self.setTriglyceridesRangeFemale() 
        self.setTriglyceridesLowValueMale()
        self.setTriglyceridesFairValueMale()
        self.setTriglyceridesModerateValueMale()
        self.setTriglyceridesHighValueMale()
        self.setTriglyceridesLowValueFemale()
        self.setTriglyceridesFairValueFemale()
        self.setTriglyceridesModerateValueFemale()
        self.setTriglyceridesHighValueFemale()
        self.setTriglyceridesFunction()
        self.setVldlCholesterolUnit()
        self.setVldlCholesterolMedicalAnnotations()
        self.setVldlCholesterolRangeMale()
        self.setVldlCholesterolRangeFemale()
        self.setVldlCholesterolLowValueMale()
        self.setVldlCholesterolFairValueMale()
        self.setVldlCholesterolModerateValueMale()
        self.setVldlCholesterolHighValueMale()
        self.setVldlCholesterolLowValueFemale()
        self.setVldlCholesterolFairValueFemale()
        self.setVldlCholesterolModerateValueFemale()
        self.setVldlCholesterolHighValueFemale()
        self.setVldlCholesterolFunction()
        self.setNonHdlCholesterolUnit()
        self.setNonHdlCholesterolMedicalAnnotations()
        self.setNonHdlCholesterolRangeMale()
        self.setNonHdlCholesterolRangeFemale()
        self.setNonHdlCholesterolLowValueMale()
        self.setNonHdlCholesterolFairValueMale()
        self.setNonHdlCholesterolModerateValueMale()
        self.setNonHdlCholesterolHighValueMale()
        self.setNonHdlCholesterolLowValueFemale()
        self.setNonHdlCholesterolFairValueFemale()
        self.setNonHdlCholesterolModerateValueFemale()
        self.setNonHdlCholesterolHighValueFemale()
        self.setNonHdlCholesterolFunction()
        self.setTcHdlRatioUnit()
        self.setTcHdlRatioMedicalAnnotations()
        self.setTcHdlRatioRangeMale()
        self.setTcHdlRatioRangeFemale()
        self.setTcHdlRatioLowValueMale()
        self.setTcHdlRatioFairValueMale()
        self.setTcHdlRatioModerateValueMale()
        self.setTcHdlRatioHighValueMale()
        self.setTcHdlRatioLowValueFemale()
        self.setTcHdlRatioFairValueFemale()
        self.setTcHdlRatioModerateValueFemale()
        self.setTcHdlRatioHighValueFemale()
        self.setTcHdlRatioFunction()
        self.setLdlHdlRatioUnit()
        self.setLdlHdlRatioMedicalAnnotations()
        self.setLdlHdlRatioRangeMale()
        self.setLdlHdlRatioRangeFemale()
        self.setLdlHdlRatioLowValueMale()
        self.setLdlHdlRatioFairValueMale()
        self.setLdlHdlRatioModerateValueMale()
        self.setLdlHdlRatioHighValueMale()
        self.setLdlHdlRatioLowValueFemale()
        self.setLdlHdlRatioFairValueFemale()
        self.setLdlHdlRatioModerateValueFemale()
        self.setLdlHdlRatioHighValueFemale()
        self.setLdlHdlRatioFunction()
        self.setApolipoA1Unit()
        self.setApolipoA1MedicalAnnotations()
        self.setApolipoA1RangeMale()
        self.setApolipoA1RangeFemale()
        self.setApolipoA1LowValueMale()
        self.setApolipoA1FairValueMale()
        self.setApolipoA1ModerateValueMale()
        self.setApolipoA1HighValueMale()
        self.setApolipoA1LowValueFemale()
        self.setApolipoA1FairValueFemale()
        self.setApolipoA1ModerateValueFemale()
        self.setApolipoA1HighValueFemale()
        self.setApolipoA1Function()


    def getParameters(self):
        return super(LipidProfile, self).getParameters()

    def getAnnotations(self, parameter_name):
        return super(LipidProfile, self).getAnnotations(parameter_name)

    def getParsedData(self, file_name, gender, password=""):
        report_parse = ReportParser(file_name, password)
        report_parse.reportList()
        parameter_name = self.getParameters()
        med_annot_tot_chol = self.getAnnotations(parameter_name[0])
        med_annot_hdl_chol = self.getAnnotations(parameter_name[1])
        med_annot_ldl_chol = self.getAnnotations(parameter_name[2])
        med_annot_trigly = self.getAnnotations(parameter_name[3])
        med_annot_vldl = self.getAnnotations(parameter_name[4])
        med_annot_non_hdl = self.getAnnotations(parameter_name[5])
        med_annot_tc_hdl_ratio = self.getAnnotations(parameter_name[6])
        med_annot_ldl_hdl_ratio = self.getAnnotations(parameter_name[7])
        med_annot_apolipo_a1 = self.getAnnotations(parameter_name[8]) 
        tot_chol = parameter_name[0]
        report_parse.parseMedicalParameter(med_annot_tot_chol, tot_chol)
        hdl_chol = parameter_name[1] 
        report_parse.parseMedicalParameter(med_annot_hdl_chol, hdl_chol)
        ldl_chol = parameter_name[2]
        report_parse.parseMedicalParameter(med_annot_ldl_chol, ldl_chol)
        trigly = parameter_name[3]
        report_parse.parseMedicalParameter(med_annot_trigly, trigly)
        vldl = parameter_name[4]
        report_parse.parseMedicalParameter(med_annot_vldl, vldl)
        non_hdl = parameter_name[5]
        report_parse.parseMedicalParameter(med_annot_non_hdl, non_hdl) 
        tc_hdl_ratio = parameter_name[6]
        report_parse.parseMedicalParameter(med_annot_tc_hdl_ratio, tc_hdl_ratio)
        ldl_hdl_ratio = parameter_name[7]
        report_parse.parseMedicalParameter(med_annot_ldl_hdl_ratio, ldl_hdl_ratio)
        apolipo_a1 = parameter_name[8]
        report_parse.parseMedicalParameter(med_annot_apolipo_a1, apolipo_a1)
        medical_report_dict = report_parse.getMedicalParsedData()
       
        # set actual values from medical report
        tot_chol_value = medical_report_dict.get(tot_chol,None)
        hdl_chol_value = medical_report_dict.get(hdl_chol,None)
        ldl_chol_value = medical_report_dict.get(ldl_chol,None)
        trigly_value = medical_report_dict.get(trigly,None)
        vldl_value = medical_report_dict.get(vldl, None)
        non_hdl_value = medical_report_dict.get(non_hdl, None)
        tc_hdl_ratio_value = medical_report_dict.get(tc_hdl_ratio, None)
        if tc_hdl_ratio_value == None and tot_chol_value != None and hdl_chol_value != None:
            tc_hdl_ratio_value = float(tot_chol_value/hdl_chol_value)
        ldl_hdl_ratio_value = medical_report_dict.get(ldl_hdl_ratio, None)
        if ldl_hdl_ratio_value == None and ldl_chol_value != None and hdl_chol_value != None:
            ldl_hdl_ratio_value = float(ldl_chol_value/hdl_chol_value)
        apolipo_a1_value = medical_report_dict.get(apolipo_a1, None)
        self.setTotalCholesterolValue(tot_chol_value)
        self.setHdlCholesterolValue(hdl_chol_value)
        self.setLdlCholesterolValue(ldl_chol_value)
        self.setTriglyceridesValue(trigly_value)
        self.setVldlCholesterolValue(vldl_value)
        self.setNonHdlCholesterolValue(non_hdl_value)
        self.setTcHdlRatioValue(tc_hdl_ratio_value)
        self.setLdlHdlRatioValue(ldl_hdl_ratio_value)
        self.setApolipoA1Value(apolipo_a1_value)
        self.tot_chol_output["reading_value"] = str(self.getTotalCholesterolValue())
        self.tot_chol_output["reading_unit"] = self.getTotalCholesterolUnit()
        self.tot_chol_output["range_male"] = self.getTotalCholesterolRangeMale()
        self.tot_chol_output["range_female"] = self.getTotalCholesterolRangeFemale()
        self.hdl_chol_output["reading_value"] = str(self.getHdlCholesterolValue())
        self.hdl_chol_output["reading_unit"] = self.getHdlCholesterolUnit()
        self.hdl_chol_output["range_male"] = self.getHdlCholesterolRangeMale()
        self.hdl_chol_output["range_female"] = self.getHdlCholesterolRangeFemale()
        self.ldl_chol_output["reading_value"] = str(self.getLdlCholesterolValue())
        self.ldl_chol_output["reading_unit"] = self.getLdlCholesterolUnit()
        self.ldl_chol_output["range_male"] = self.getLdlCholesterolRangeMale()
        self.ldl_chol_output["range_female"] = self.getLdlCholesterolRangeFemale()
        self.trigly_output["reading_value"] = str(self.getTriglyceridesValue())
        self.trigly_output["reading_unit"] = self.getTriglyceridesUnit()
        self.trigly_output["range_male"] = self.getTriglyceridesRangeMale()
        self.trigly_output["range_female"] = self.getTriglyceridesRangeFemale()
        self.vldl_chol_output["reading_value"] = str(self.getVldlCholesterolValue())
        self.vldl_chol_output["reading_unit"] = self.getVldlCholesterolUnit()
        self.vldl_chol_output["range_male"] = self.getVldlCholesterolRangeMale()
        self.vldl_chol_output["range_female"] = self.getVldlCholesterolRangeFemale()
        self.non_hdl_chol_output["reading_value"] = str(self.getNonHdlCholesterolValue())
        self.non_hdl_chol_output["reading_unit"] = self.getNonHdlCholesterolUnit()
        self.non_hdl_chol_output["range_male"] = self.getNonHdlCholesterolRangeMale()
        self.non_hdl_chol_output["range_female"] = self.getNonHdlCholesterolRangeFemale()
        self.tc_hdl_ratio_output["reading_value"] = str(self.getTcHdlRatioValue())
        self.tc_hdl_ratio_output["reading_unit"] = self.getTcHdlRatioUnit()
        self.tc_hdl_ratio_output["range_male"] = self.getTcHdlRatioRangeMale()
        self.tc_hdl_ratio_output["range_female"] = self.getTcHdlRatioRangeFemale()
        self.ldl_hdl_ratio_output["reading_value"] = str(self.getLdlHdlRatioValue())
        self.ldl_hdl_ratio_output["reading_unit"] = self.getLdlHdlRatioUnit()
        self.ldl_hdl_ratio_output["range_male"] = self.getLdlHdlRatioRangeMale()
        self.ldl_hdl_ratio_output["range_female"] = self.getLdlHdlRatioRangeFemale()
        self.apolipoproteina1_output["reading_value"] = str(self.getApolipoA1Value())
        self.apolipoproteina1_output["reading_unit"] = self.getApolipoA1Unit()
        self.apolipoproteina1_output["range_male"] = self.getApolipoA1RangeMale()
        self.apolipoproteina1_output["range_female"] = self.getApolipoA1RangeFemale()


        if gender == "Female":
            self.tot_chol_output["low_fair_moderate_high"] = [self.getTotalCholesterolLowValueFemale(), self.getTotalCholesterolFairValueFemale(), self.getTotalCholesterolModerateValueFemale(), self.getTotalCholesterolHighValueFemale()]
            if self.getTotalCholesterolValue() <= float(self.getTotalCholesterolLowValueFemale().split("-")[1]):
                self.tot_chol_output["risk"] = Low
            if self.getTotalCholesterolValue() >= float(self.getTotalCholesterolFairValueFemale().split("-")[0]) and self.getTotalCholesterolValue() <= float(self.getTotalCholesterolFairValueFemale().split("-")[1]):
                self.tot_chol_output["risk"] = Fair
            if self.getTotalCholesterolValue() >= float(self.getTotalCholesterolModerateValueFemale().split("-")[0]) and self.getTotalCholesterolValue() <= float(self.getTotalCholesterolModerateValueFemale().split("-")[1]):
                self.tot_chol_output["risk"] = Moderate
            if self.getTotalCholesterolValue() > float(self.getTotalCholesterolHighValueFemale()):
                self.tot_chol_output["risk"] = High
            if self.getTotalCholesterolValue() == None:
                self.tot_chol_output["risk"] = n_a
            self.parsed_output["total_cholesterol"] = self.tot_chol_output
        
            self.hdl_chol_output["low_fair_moderate_high"] = [self.getHdlCholesterolLowValueFemale(), self.getHdlCholesterolFairValueFemale(), self.getHdlCholesterolModerateValueFemale(), self.getHdlCholesterolHighValueFemale()]
            if self.getHdlCholesterolValue() >= float(self.getHdlCholesterolLowValueFemale().split("-")[0]) and self.getHdlCholesterolValue() <= float(self.getHdlCholesterolLowValueFemale().split("-")[1]):
                self.hdl_chol_output["risk"] = Low
            if self.getHdlCholesterolValue() >= float(self.getHdlCholesterolFairValueFemale().split("-")[0]) and self.getHdlCholesterolValue() <= float(self.getHdlCholesterolFairValueFemale().split("-")[1]):
                self.hdl_chol_output["risk"] = Fair
            if self.getHdlCholesterolValue() >= float(self.getHdlCholesterolModerateValueFemale().split("-")[0]) and self.getHdlCholesterolValue() <= float(self.getHdlCholesterolModerateValueFemale().split("-")[1]):
                self.hdl_chol_output["risk"] = Moderate
            if self.getHdlCholesterolValue() < float(self.getHdlCholesterolHighValueFemale()):
                self.hdl_chol_output["risk"] = High
            if self.getHdlCholesterolValue() == None:
                self.hdl_chol_output["risk"] = n_a
            self.parsed_output["hdl_cholesterol"] = self.hdl_chol_output

            self.ldl_chol_output["low_fair_moderate_high"] = [self.getLdlCholesterolLowValueFemale(), self.getLdlCholesterolFairValueFemale(), self.getLdlCholesterolModerateValueFemale(), self.getLdlCholesterolHighValueFemale()]
            if self.getLdlCholesterolValue() <= float(self.getLdlCholesterolLowValueFemale().split("-")[1]):
                self.ldl_chol_output["risk"] = Low
            if self.getLdlCholesterolValue() >= float(self.getLdlCholesterolFairValueFemale().split("-")[0]) and self.getLdlCholesterolValue() <= float(self.getLdlCholesterolFairValueFemale().split("-")[1]):
                self.ldl_chol_output["risk"] = Fair
            if self.getLdlCholesterolValue() >= float(self.getLdlCholesterolModerateValueFemale().split("-")[0]) and self.getLdlCholesterolValue() <= float(self.getLdlCholesterolModerateValueFemale().split("-")[1]):
                self.ldl_chol_output["risk"] = Moderate
            if self.getLdlCholesterolValue() > float(self.getLdlCholesterolHighValueFemale()):
                self.ldl_chol_output["risk"] = High
            if self.getLdlCholesterolValue() == None:
                self.ldl_chol_output["risk"] = n_a
            self.parsed_output["ldl_cholesterol"] = self.ldl_chol_output

            self.trigly_output["low_fair_moderate_high"] = [self.getTriglyceridesLowValueFemale(), self.getTriglyceridesFairValueFemale(), self.getTriglyceridesModerateValueFemale(), self.getTriglyceridesHighValueFemale()]
            if self.getTriglyceridesValue() <= float(self.getTriglyceridesLowValueFemale().split("-")[1]):
                self.trigly_output["risk"] = Low
            if self.getTriglyceridesValue() >= float(self.getTriglyceridesFairValueFemale().split("-")[0]) and self.getTriglyceridesValue() <= float(self.getTriglyceridesFairValueFemale().split("-")[1]):
                self.trigly_output["risk"] = Fair
            if self.getTriglyceridesValue() >= float(self.getTriglyceridesModerateValueFemale().split("-")[0]) and self.getTriglyceridesValue() <= float(self.getTriglyceridesModerateValueFemale().split("-")[1]):
                self.trigly_output["risk"] = Moderate
            if self.getTriglyceridesValue() > float(self.getTriglyceridesHighValueFemale()):
                self.trigly_output["risk"] = High
            if self.getTriglyceridesValue() == None:
                self.trigly_output["risk"] = n_a
            self.parsed_output["triglycerides"] = self.trigly_output

            self.vldl_chol_output["low_fair_moderate_high"] = [self.getVldlCholesterolLowValueFemale(), self.getVldlCholesterolFairValueFemale(), self.getVldlCholesterolModerateValueFemale(), self.getVldlCholesterolHighValueFemale()]
            if self.getVldlCholesterolValue() <= float(self.getVldlCholesterolLowValueFemale().split("-")[1]):
                self.vldl_chol_output["risk"] = Low
            if self.getVldlCholesterolValue() >= float(self.getVldlCholesterolFairValueFemale().split("-")[0]) and self.getVldlCholesterolValue() <= float(self.getVldlCholesterolFairValueFemale().split("-")[1]):
                self.vldl_chol_output["risk"] = Fair
            if self.getVldlCholesterolValue() >= float(self.getVldlCholesterolModerateValueFemale().split("-")[0]) and self.getVldlCholesterolValue() <= float(self.getVldlCholesterolModerateValueFemale().split("-")[1]):
                self.vldl_chol_output["risk"] = Moderate
            if self.getVldlCholesterolValue() > float(self.getVldlCholesterolHighValueFemale()):
                self.vldl_chol_output["risk"] = High
            if self.getVldlCholesterolValue() == None:
                self.vldl_chol_output["risk"] = n_a
            self.parsed_output["vldl_cholesterol"] = self.vldl_chol_output

            self.non_hdl_chol_output["low_fair_moderate_high"] = [self.getNonHdlCholesterolLowValueFemale(), self.getNonHdlCholesterolFairValueFemale(), self.getNonHdlCholesterolModerateValueFemale(), self.getNonHdlCholesterolHighValueFemale()]
            if self.getNonHdlCholesterolValue() <= float(self.getNonHdlCholesterolLowValueFemale().split("-")[1]):
                self.non_hdl_chol_output["risk"] = Low
            if self.getNonHdlCholesterolValue() >= float(self.getNonHdlCholesterolFairValueFemale().split("-")[0]) and self.getNonHdlCholesterolValue() <= float(self.getNonHdlCholesterolFairValueFemale().split("-")[1]):
                self.non_hdl_chol_output["risk"] = Fair
            if self.getNonHdlCholesterolValue() >= float(self.getNonHdlCholesterolModerateValueFemale().split("-")[0]) and self.getNonHdlCholesterolValue() <= float(self.getNonHdlCholesterolModerateValueFemale().split("-")[1]):
                self.non_hdl_chol_output["risk"] = Moderate
            if self.getNonHdlCholesterolValue() > float(self.getNonHdlCholesterolHighValueFemale()):
                self.non_hdl_chol_output["risk"] = High
            if self.getNonHdlCholesterolValue() == None:
                self.non_hdl_chol_output["risk"] = n_a
            self.parsed_output["non_hdl_cholesterol"] = self.non_hdl_chol_output

            self.tc_hdl_ratio_output["low_fair_moderate_high"] = [self.getTcHdlRatioLowValueFemale(), self.getTcHdlRatioFairValueFemale(), self.getTcHdlRatioModerateValueFemale(), self.getTcHdlRatioHighValueFemale()]
            if self.getTcHdlRatioValue() <= float(self.getTcHdlRatioLowValueFemale().split("-")[1]):
                self.tc_hdl_ratio_output["risk"] = Low
            if self.getTcHdlRatioValue() >= float(self.getTcHdlRatioFairValueFemale().split("-")[0]) and self.getTcHdlRatioValue() <= float(self.getTcHdlRatioFairValueFemale().split("-")[1]):
                self.tc_hdl_ratio_output["risk"] = Fair
            if self.getTcHdlRatioValue() >= float(self.getTcHdlRatioModerateValueFemale().split("-")[0]) and self.getTcHdlRatioValue() <= float(self.getTcHdlRatioModerateValueFemale().split("-")[1]):
                self.tc_hdl_ratio_output["risk"] = Moderate
            if self.getTcHdlRatioValue() > float(self.getTcHdlRatioHighValueFemale()):
                self.tc_hdl_ratio_output["risk"] = High
            if self.getTcHdlRatioValue() == None:
                self.tc_hdl_ratio_output["risk"] = n_a
            self.parsed_output["tc_hdl_ratio"] = self.tc_hdl_ratio_output

            self.ldl_hdl_ratio_output["low_fair_moderate_high"] = [self.getLdlHdlRatioLowValueFemale(), self.getLdlHdlRatioFairValueFemale(), self.getLdlHdlRatioModerateValueFemale(), self.getLdlHdlRatioHighValueFemale()]
            if self.getLdlHdlRatioValue() <= float(self.getLdlHdlRatioLowValueFemale().split("-")[1]):
                self.ldl_hdl_ratio_output["risk"] = Low
            if self.getLdlHdlRatioValue() >= float(self.getLdlHdlRatioFairValueFemale().split("-")[0]) and self.getLdlHdlRatioValue() <= float(self.getLdlHdlRatioFairValueFemale().split("-")[1]):
                self.ldl_hdl_ratio_output["risk"] = Fair
            if self.getLdlHdlRatioValue() >= float(self.getLdlHdlRatioModerateValueFemale().split("-")[0]) and self.getLdlHdlRatioValue() <= float(self.getLdlHdlRatioModerateValueFemale().split("-")[1]):
                self.ldl_hdl_ratio_output["risk"] = Moderate
            if self.getLdlHdlRatioValue() > float(self.getLdlHdlRatioHighValueFemale()):
                self.ldl_hdl_ratio_output["risk"] = High
            if self.getLdlHdlRatioValue() == None:
                self.ldl_hdl_ratio_output["risk"] = n_a
            self.parsed_output["ldl_hdl_ratio"] = self.ldl_hdl_ratio_output

            self.apolipoproteina1_output["low_fair_moderate_high"] = [self.getApolipoA1LowValueFemale(), self.getApolipoA1FairValueFemale(), self.getApolipoA1ModerateValueFemale(), self.getApolipoA1HighValueFemale()]
            if self.getLdlHdlRatioValue() <= float(self.getApolipoA1LowValueFemale().split("-")[1]):
                self.apolipoproteina1_output["risk"] = Low
            if self.getApolipoA1Value() >= float(self.getApolipoA1FairValueFemale().split("-")[0]) and self.getApolipoA1Value() <= float(self.getApolipoA1FairValueFemale().split("-")[1]):
                self.apolipoproteina1_output["risk"] = Fair
            if self.getApolipoA1Value() >= float(self.getApolipoA1ModerateValueFemale().split("-")[0]) and self.getApolipoA1Value() <= float(self.getApolipoA1ModerateValueFemale().split("-")[1]):
                self.apolipoproteina1_output["risk"] = Moderate
            if self.getApolipoA1Value() > float(self.getApolipoA1HighValueFemale()):
                self.apolipoproteina1_output["risk"] = High
            if self.getApolipoA1Value() == None:
                self.apolipoproteina1_output["risk"] = n_a
            self.parsed_output["apolipoprotein"] = self.apolipoproteina1_output


        else:
            self.tot_chol_output["low_fair_moderate_high"] = [self.getTotalCholesterolLowValueMale(), self.getTotalCholesterolFairValueMale(), self.getTotalCholesterolModerateValueMale(), self.getTotalCholesterolHighValueMale()]
            if self.getTotalCholesterolValue() <= float(self.getTotalCholesterolLowValueMale().split("-")[1]):
                self.tot_chol_output["risk"] = Low
            if self.getTotalCholesterolValue() >= float(self.getTotalCholesterolFairValueMale().split("-")[0]) and self.getTotalCholesterolValue() <= float(self.getTotalCholesterolFairValueMale().split("-")[1]):
                self.tot_chol_output["risk"] = Fair
            if self.getTotalCholesterolValue() >= float(self.getTotalCholesterolModerateValueMale().split("-")[0]) and self.getTotalCholesterolValue() <= float(self.getTotalCholesterolModerateValueMale().split("-")[1]):
                self.tot_chol_output["risk"] = Moderate
            if self.getTotalCholesterolValue() > float(self.getTotalCholesterolHighValueMale()):
                self.tot_chol_output["risk"] = High
            if self.getTotalCholesterolValue() == None:
                self.tot_chol_output["risk"] = n_a
            self.parsed_output["total_cholesterol"] = self.tot_chol_output
        
            self.hdl_chol_output["low_fair_moderate_high"] = [self.getHdlCholesterolLowValueMale(), self.getHdlCholesterolFairValueMale(), self.getHdlCholesterolModerateValueMale(), self.getHdlCholesterolHighValueMale()]
            if self.getHdlCholesterolValue() >= float(self.getHdlCholesterolLowValueMale().split("-")[0]) and self.getHdlCholesterolValue() <= float(self.getHdlCholesterolLowValueMale().split("-")[1]):
                self.hdl_chol_output["risk"] = Low
            if self.getHdlCholesterolValue() >= float(self.getHdlCholesterolFairValueMale().split("-")[0]) and self.getHdlCholesterolValue() <= float(self.getHdlCholesterolFairValueMale().split("-")[1]):
                self.hdl_chol_output["risk"] = Fair
            if self.getHdlCholesterolValue() >= float(self.getHdlCholesterolModerateValueMale().split("-")[0]) and self.getHdlCholesterolValue() <= float(self.getHdlCholesterolModerateValueMale().split("-")[1]):
                self.hdl_chol_output["risk"] = Moderate
            if self.getHdlCholesterolValue() < float(self.getHdlCholesterolHighValueMale()):
                self.hdl_chol_output["risk"] = High
            if self.getHdlCholesterolValue() == None:
                self.hdl_chol_output["risk"] = n_a
            self.parsed_output["hdl_cholesterol"] = self.hdl_chol_output

            self.ldl_chol_output["low_fair_moderate_high"] = [self.getLdlCholesterolLowValueMale(), self.getLdlCholesterolFairValueMale(), self.getLdlCholesterolModerateValueMale(), self.getLdlCholesterolHighValueMale()]
            if self.getLdlCholesterolValue() <= float(self.getLdlCholesterolLowValueMale().split("-")[1]):
                self.ldl_chol_output["risk"] = Low
            if self.getLdlCholesterolValue() >= float(self.getLdlCholesterolFairValueMale().split("-")[0]) and self.getLdlCholesterolValue() <= float(self.getLdlCholesterolFairValueMale().split("-")[1]):
                self.ldl_chol_output["risk"] = Fair
            if self.getLdlCholesterolValue() >= float(self.getLdlCholesterolModerateValueMale().split("-")[0]) and self.getLdlCholesterolValue() <= float(self.getLdlCholesterolModerateValueMale().split("-")[1]):
                self.ldl_chol_output["risk"] = Moderate
            if self.getLdlCholesterolValue() > float(self.getLdlCholesterolHighValueMale()):
                self.ldl_chol_output["risk"] = High
            if self.getLdlCholesterolValue() == None:
                self.ldl_chol_output["risk"] = n_a
            self.parsed_output["ldl_cholesterol"] = self.ldl_chol_output

            self.trigly_output["low_fair_moderate_high"] = [self.getTriglyceridesLowValueMale(), self.getTriglyceridesFairValueMale(), self.getTriglyceridesModerateValueMale(), self.getTriglyceridesHighValueMale()]
            if self.getTriglyceridesValue() <= float(self.getTriglyceridesLowValueMale().split("-")[1]):
                self.trigly_output["risk"] = Low
            if self.getTriglyceridesValue() >= float(self.getTriglyceridesFairValueMale().split("-")[0]) and self.getTriglyceridesValue() <= float(self.getTriglyceridesFairValueMale().split("-")[1]):
                self.trigly_output["risk"] = Fair
            if self.getTriglyceridesValue() >= float(self.getTriglyceridesModerateValueMale().split("-")[0]) and self.getTriglyceridesValue() <= float(self.getTriglyceridesModerateValueMale().split("-")[1]):
                self.trigly_output["risk"] = Moderate
            if self.getTriglyceridesValue() > float(self.getTriglyceridesHighValueMale()):
                self.trigly_output["risk"] = High
            if self.getTriglyceridesValue() == None:
                self.trigly_output["risk"] = n_a
            self.parsed_output["triglycerides"] = self.trigly_output

            self.vldl_chol_output["low_fair_moderate_high"] = [self.getVldlCholesterolLowValueMale(), self.getVldlCholesterolFairValueMale(), self.getVldlCholesterolModerateValueMale(), self.getVldlCholesterolHighValueMale()]
            if self.getVldlCholesterolValue() <= float(self.getVldlCholesterolLowValueMale().split("-")[1]):
                self.vldl_chol_output["risk"] = Low
            if self.getVldlCholesterolValue() >= float(self.getVldlCholesterolFairValueMale().split("-")[0]) and self.getVldlCholesterolValue() <= float(self.getVldlCholesterolFairValueMale().split("-")[1]):
                self.vldl_chol_output["risk"] = Fair
            if self.getVldlCholesterolValue() >= float(self.getVldlCholesterolModerateValueMale().split("-")[0]) and self.getVldlCholesterolValue() <= float(self.getVldlCholesterolModerateValueMale().split("-")[1]):
                self.vldl_chol_output["risk"] = Moderate
            if self.getVldlCholesterolValue() > float(self.getVldlCholesterolHighValueMale()):
                self.vldl_chol_output["risk"] = High
            if self.getVldlCholesterolValue() == None:
                self.vldl_chol_output["risk"] = n_a
            self.parsed_output["vldl_cholesterol"] = self.vldl_chol_output

            self.non_hdl_chol_output["low_fair_moderate_high"] = [self.getNonHdlCholesterolLowValueMale(), self.getNonHdlCholesterolFairValueMale(), self.getNonHdlCholesterolModerateValueMale(), self.getNonHdlCholesterolHighValueMale()]
            if self.getNonHdlCholesterolValue() <= float(self.getNonHdlCholesterolLowValueMale().split("-")[1]):
                self.non_hdl_chol_output["risk"] = Low
            if self.getNonHdlCholesterolValue() >= float(self.getNonHdlCholesterolFairValueMale().split("-")[0]) and self.getNonHdlCholesterolValue() <= float(self.getNonHdlCholesterolFairValueMale().split("-")[1]):
                self.non_hdl_chol_output["risk"] = Fair
            if self.getNonHdlCholesterolValue() >= float(self.getNonHdlCholesterolModerateValueMale().split("-")[0]) and self.getNonHdlCholesterolValue() <= float(self.getNonHdlCholesterolModerateValueMale().split("-")[1]):
                self.non_hdl_chol_output["risk"] = Moderate
            if self.getNonHdlCholesterolValue() > float(self.getNonHdlCholesterolHighValueMale()):
                self.non_hdl_chol_output["risk"] = High
            if self.getNonHdlCholesterolValue() == None:
                self.non_hdl_chol_output["risk"] = n_a
            self.parsed_output["non_hdl_cholesterol"] = self.non_hdl_chol_output

            self.tc_hdl_ratio_output["low_fair_moderate_high"] = [self.getTcHdlRatioLowValueMale(), self.getTcHdlRatioFairValueMale(), self.getTcHdlRatioModerateValueMale(), self.getTcHdlRatioHighValueMale()]
            if self.getTcHdlRatioValue() <= float(self.getTcHdlRatioLowValueMale().split("-")[1]):
                self.tc_hdl_ratio_output["risk"] = Low
            if self.getTcHdlRatioValue() >= float(self.getTcHdlRatioFairValueMale().split("-")[0]) and self.getTcHdlRatioValue() <= float(self.getTcHdlRatioFairValueMale().split("-")[1]):
                self.tc_hdl_ratio_output["risk"] = Fair
            if self.getTcHdlRatioValue() >= float(self.getTcHdlRatioModerateValueMale().split("-")[0]) and self.getTcHdlRatioValue() <= float(self.getTcHdlRatioModerateValueMale().split("-")[1]):
                self.tc_hdl_ratio_output["risk"] = Moderate
            if self.getTcHdlRatioValue() > float(self.getTcHdlRatioHighValueMale()):
                self.tc_hdl_ratio_output["risk"] = High
            if self.getTcHdlRatioValue() == None:
                self.tc_hdl_ratio_output["risk"] = n_a
            self.parsed_output["tc_hdl_ratio"] = self.tc_hdl_ratio_output

            self.ldl_hdl_ratio_output["low_fair_moderate_high"] = [self.getLdlHdlRatioLowValueMale(), self.getLdlHdlRatioFairValueMale(), self.getLdlHdlRatioModerateValueMale(), self.getLdlHdlRatioHighValueMale()]
            if self.getLdlHdlRatioValue() <= float(self.getLdlHdlRatioLowValueMale().split("-")[1]):
                self.ldl_hdl_ratio_output["risk"] = Low
            if self.getLdlHdlRatioValue() >= float(self.getLdlHdlRatioFairValueMale().split("-")[0]) and self.getLdlHdlRatioValue() <= float(self.getLdlHdlRatioFairValueMale().split("-")[1]):
                self.ldl_hdl_ratio_output["risk"] = Fair
            if self.getLdlHdlRatioValue() >= float(self.getLdlHdlRatioModerateValueMale().split("-")[0]) and self.getLdlHdlRatioValue() <= float(self.getLdlHdlRatioModerateValueMale().split("-")[1]):
                self.ldl_hdl_ratio_output["risk"] = Moderate
            if self.getLdlHdlRatioValue() > float(self.getLdlHdlRatioHighValueMale()):
                self.ldl_hdl_ratio_output["risk"] = High
            if self.getLdlHdlRatioValue() == None:
                self.ldl_hdl_ratio_output["risk"] = n_a
            self.parsed_output["ldl_hdl_ratio"] = self.ldl_hdl_ratio_output

            self.apolipoproteina1_output["low_fair_moderate_high"] = [self.getApolipoA1LowValueMale(), self.getApolipoA1FairValueMale(), self.getApolipoA1ModerateValueMale(), self.getApolipoA1HighValueMale()]
            if self.getApolipoA1Value() <= float(self.getApolipoA1LowValueMale().split("-")[1]):
                self.apolipoproteina1_output["risk"] = Low
            if self.getApolipoA1Value() >= float(self.getApolipoA1FairValueMale().split("-")[0]) and self.getApolipoA1Value() <= float(self.getApolipoA1FairValueMale().split("-")[1]):
                self.apolipoproteina1_output["risk"] = Fair
            if self.getApolipoA1Value() >= float(self.getApolipoA1ModerateValueMale().split("-")[0]) and self.getApolipoA1Value() <= float(self.getApolipoA1ModerateValueMale().split("-")[1]):
                self.apolipoproteina1_output["risk"] = Moderate
            if self.getApolipoA1Value() > float(self.getApolipoA1HighValueMale()):
                self.apolipoproteina1_output["risk"] = High
            if self.getApolipoA1Value() == None:
                self.apolipoproteina1_output["risk"] = n_a
            self.parsed_output["apolipoprotein"] = self.apolipoproteina1_output

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
    
    # Function sets actual cholesterol value
    def setTotalCholesterolValue(self, tc):
        self.total_cholesterol = tc

    # Function sets unit of total cholesterol  
    def setTotalCholesterolUnit(self):
        self.total_chol_unit = self.parameters[0].get('value_meta_data',[])[0].get('unit',"")

    # Function sets list of medical annotations for total cholesterol
    def setTotalCholesterolMedicalAnnotations(self):
        self.total_chol_medical_annot = self.parameters[0].get('medical_annotation',[])

    # Function sets range of values for total cholesterol for male  
    def setTotalCholesterolRangeMale(self):
        self.total_chol_range_male = self.parameters[0].get('value_meta_data',[])[0].get('range',"")

    # Function sets range of values for total cholesterol for female  
    def setTotalCholesterolRangeFemale(self):
        self.total_chol_range_female  = self.parameters[0].get('value_meta_data',[])[1].get('range',"")

    # Function sets low risk values range for total cholesterol
    def setTotalCholesterolLowValueMale(self):
        self.total_chol_low_male  = self.parameters[0].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for total cholesterol
    def setTotalCholesterolFairValueMale(self):
        self.total_chol_fair_male  = self.parameters[0].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function sets moderate risk values range for total cholesterol
    def setTotalCholesterolModerateValueMale(self):
        self.total_chol_moderate_male =  self.parameters[0].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for total cholesterol 
    def setTotalCholesterolHighValueMale(self):
        self.total_chol_high_male = self.parameters[0].get('value_meta_data',[])[0].get('high_value',"")[1:]

    # Function sets low risk values range for total cholesterol
    def setTotalCholesterolLowValueFemale(self):
        self.total_chol_low_female = self.parameters[0].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for total cholesterol
    def setTotalCholesterolFairValueFemale(self):
        self.total_chol_fair_female = self.parameters[0].get('value_meta_data',[])[1].get('fair_value',"")

    # Function sets moderate risk values range for total cholesterol
    def setTotalCholesterolModerateValueFemale(self):
        self.total_chol_moderate_female = self.parameters[0].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for total cholesterol 
    def setTotalCholesterolHighValueFemale(self):
        self.total_chol_high_female = self.parameters[0].get('value_meta_data',[])[1].get('high_value',"")[1:]

    # Function sets function name to parse total cholesterol value from medical reports
    def setTotalCholesterolsFunction(self):
        self.total_chol_func = self.parameters[0].get("value_function",{}).get("function_name","")
    
    # Function sets actual hdl cholesterol value
    def setHdlCholesterolValue(self, hdl):
        self.hdl_cholesterol = hdl

    # Function sets list of medical annotations for hdl cholesterol
    def setHdlCholesterolMedicalAnnotations(self):
        self.hdl_chol_medical_annot = self.parameters[1].get('medical_annotation',[])

    # Function sets unit of hdl cholesterol 
    def setHdlCholesterolUnit(self):
        self.hdl_chol_unit  = self.parameters[1].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for hdl cholesterol for male
    def setHdlCholesterolRangeMale(self):
        self.hdl_chol_range_male = self.parameters[1].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for hdl cholesterol for female
    def setHdlCholesterolRangeFemale(self):
        self.hdl_chol_range_female  = self.parameters[1].get('value_meta_data',[])[1].get('range',"") 

    # Function sets low risk values range for hdl cholesterol
    def setHdlCholesterolLowValueMale(self):
        self.hdl_chol_low_male = self.parameters[1].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for hdl cholesterol
    def setHdlCholesterolFairValueMale(self):
        self.hdl_chol_fair_male = self.parameters[1].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function retuns moderate risk value ranges for hdl cholesterol
    def setHdlCholesterolModerateValueMale(self):
        self.hdl_chol_moderate_male = self.parameters[1].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk value ranges for hdl cholesterol
    def setHdlCholesterolHighValueMale(self):
        self.hdl_chol_high_male = self.parameters[1].get('value_meta_data',[])[0].get('high_value',"")[1:]
  
    # Function sets low risk values range for hdl cholesterol
    def setHdlCholesterolLowValueFemale(self):
        self.hdl_chol_low_female = self.parameters[1].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for hdl cholesterol
    def setHdlCholesterolFairValueFemale(self):
        self.hdl_chol_fair_female = self.parameters[1].get('value_meta_data',[])[1].get('fair_value',"")

    # Function retuns moderate risk value ranges for hdl cholesterol
    def setHdlCholesterolModerateValueFemale(self):
        self.hdl_chol_moderate_female = self.parameters[1].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk value ranges for hdl cholesterol
    def setHdlCholesterolHighValueFemale(self):
        self.hdl_chol_high_female = self.parameters[1].get('value_meta_data',[])[1].get('high_value',"")[1:]
 
    # Function sets function name to parse total cholesterol value from medical reports
    def setHdlCholesterolsFunction(self):
        self.hdl_chol_func = self.parameters[1].get("value_function",{}).get("function_name","")
    
    # Function sets ldl cholesterol actual value
    def setLdlCholesterolValue(self, ldl):
        self.ldl_cholesterol = ldl

    # Function sets list of medical annotations for ldl cholesterol
    def setLdlCholesterolMedicalAnnotations(self):
        self.ldl_chol_medical_annot = self.parameters[2].get('medical_annotation',[])

    # Function sets unit of ldl cholesterol
    def setLdlCholesterolUnit(self):
        self.ldl_chol_unit = self.parameters[2].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for ldl cholesterol for male
    def setLdlCholesterolRangeMale(self):
        self.ldl_chol_range_male = self.parameters[2].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for ldl cholesterol for female
    def setLdlCholesterolRangeFemale(self):
        self.ldl_chol_range_female = self.parameters[2].get('value_meta_data',[])[1].get('range',"") 
    
    # Function sets low risk values range for ldl cholesterol
    def setLdlCholesterolLowValueMale(self):
        self.ldl_chol_low_male = self.parameters[2].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for ldl cholesterol
    def setLdlCholesterolFairValueMale(self):
        self.ldl_chol_fair_male  = self.parameters[2].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function sets moderate risk values range for ldl cholesterol
    def setLdlCholesterolModerateValueMale(self):
        self.ldl_chol_moderate_male = self.parameters[2].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for ldl cholesterol
    def setLdlCholesterolHighValueMale(self):
        self.ldl_chol_high_male = self.parameters[2].get('value_meta_data',[])[0].get('high_value',"")[1:]
   
    # Function sets low risk values range for ldl cholesterol
    def setLdlCholesterolLowValueFemale(self):
        self.ldl_chol_low_female = self.parameters[2].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for ldl cholesterol
    def setLdlCholesterolFairValueFemale(self):
        self.ldl_chol_fair_female  = self.parameters[2].get('value_meta_data',[])[1].get('fair_value',"")

    # Function sets moderate risk values range for ldl cholesterol
    def setLdlCholesterolModerateValueFemale(self):
        self.ldl_chol_moderate_female = self.parameters[2].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for ldl cholesterol
    def setLdlCholesterolHighValueFemale(self):
        self.ldl_chol_high_female = self.parameters[2].get('value_meta_data',[])[1].get('high_value',"")[1:]
 
    # Function sets function name to parse ldl cholesterol value from medical report 
    def setLdlCholesterolsFunction(self):
        self.ldl_chol_func  = self.parameters[2].get("value_function",{}).get("function_name","")
    
    # Function sets triglycerides actual value
    def setTriglyceridesValue(self, triglyc):
        self.triglycerides = triglyc
    
    # Function sets list of medical annotations for triglycerides 
    def setTriglyceridesMedicalAnnotations(self):
        self.trigly_medical_annot = self.parameters[3].get('medical_annotation',[])

    # Function sets unit of triglycerides
    def setTriglyceridesUnit(self):
        self.trigly_unit  = self.parameters[3].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values ranges for triglycerides for male 
    def setTriglyceridesRangeMale(self):
        self.trigly_range_male  = self.parameters[3].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values ranges for triglycerides for female 
    def setTriglyceridesRangeFemale(self):
        self.trigly_range_female = self.parameters[3].get('value_meta_data',[])[1].get('range',"")         

    # Function sets low risk values range for ldl cholesterol
    def setTriglyceridesLowValueMale(self):
        self.trigly_low_male = self.parameters[3].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for ldl cholesterol
    def setTriglyceridesFairValueMale(self):
        self.trigly_fair_male = self.parameters[3].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function sets moderate risk values range for ldl cholesterol
    def setTriglyceridesModerateValueMale(self):
        self.trigly_moderate_male = self.parameters[3].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for ldl cholesterol
    def setTriglyceridesHighValueMale(self):
        self.trigly_high_male = self.parameters[3].get('value_meta_data',[])[0].get('high_value',"")[1:]
    
    # Function sets low risk values range for ldl cholesterol
    def setTriglyceridesLowValueFemale(self):
        self.trigly_low_female = self.parameters[3].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for ldl cholesterol
    def setTriglyceridesFairValueFemale(self):
        self.trigly_fair_female = self.parameters[3].get('value_meta_data',[])[0].get('fair_value',"")

    # Function sets moderate risk values range for ldl cholesterol
    def setTriglyceridesModerateValueFemale(self):
        self.trigly_moderate_female = self.parameters[3].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for ldl cholesterol
    def setTriglyceridesHighValueFemale(self):
        self.trigly_high_female = self.parameters[3].get('value_meta_data',[])[0].get('high_value',"")[1:]

    # Function sets function name for parsing triglycerides value from medical reports
    def setTriglyceridesFunction(self):
        self.trigly_func = self.parameters[3].get("value_function",{}).get("function_name","")

    def setVldlCholesterolValue(self, vldl):
        self.vldl_cholesterol = vldl

    def setVldlCholesterolMedicalAnnotations(self):
        self.vldl_medical_annot = self.parameters[4].get('medical_annotation',[])

    def setVldlCholesterolUnit(self):
        self.vldl_unit  = self.parameters[4].get('value_meta_data',[])[0].get('unit',"")

    def setVldlCholesterolRangeMale(self):
        self.vldl_range_male  = self.parameters[4].get('value_meta_data',[])[0].get('range',"")

    def setVldlCholesterolRangeFemale(self):
        self.vldl_range_female = self.parameters[4].get('value_meta_data',[])[1].get('range',"")

    def setVldlCholesterolLowValueMale(self):
        self.vldl_low_male = self.parameters[4].get('value_meta_data',[])[0].get('low_value',"")

    def setVldlCholesterolFairValueMale(self):
        self.vldl_fair_male = self.parameters[4].get('value_meta_data',[])[0].get('fair_value',"")

    def setVldlCholesterolModerateValueMale(self):
        self.vldl_moderate_male = self.parameters[4].get('value_meta_data',[])[0].get('moderate_value',"")

    def setVldlCholesterolHighValueMale(self):
        self.vldl_high_male = self.parameters[4].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setVldlCholesterolLowValueFemale(self):
        self.vldl_low_female = self.parameters[4].get('value_meta_data',[])[0].get('low_value',"")

    def setVldlCholesterolFairValueFemale(self):
        self.vldl_fair_female = self.parameters[4].get('value_meta_data',[])[0].get('fair_value',"")

    def setVldlCholesterolModerateValueFemale(self):
        self.vldl_moderate_female = self.parameters[4].get('value_meta_data',[])[0].get('moderate_value',"")

    def setVldlCholesterolHighValueFemale(self):
        self.vldl_high_female = self.parameters[4].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setVldlCholesterolFunction(self):
        self.vldl_func = self.parameters[4].get("value_function",{}).get("function_name","")

    def setNonHdlCholesterolValue(self, non_hdl):
        self.non_hdl_cholesterol = non_hdl

    def setNonHdlCholesterolMedicalAnnotations(self):
        self.non_hdl_medical_annot = self.parameters[5].get('medical_annotation',[])

    def setNonHdlCholesterolUnit(self):
        self.non_hdl_unit  = self.parameters[5].get('value_meta_data',[])[0].get('unit',"")

    def setNonHdlCholesterolRangeMale(self):
        self.non_hdl_range_male  = self.parameters[5].get('value_meta_data',[])[0].get('range',"")

    def setNonHdlCholesterolRangeFemale(self):
        self.non_hdl_range_female = self.parameters[5].get('value_meta_data',[])[1].get('range',"")

    def setNonHdlCholesterolLowValueMale(self):
        self.non_hdl_low_male = self.parameters[5].get('value_meta_data',[])[0].get('low_value',"")

    def setNonHdlCholesterolFairValueMale(self):
        self.non_hdl_fair_male = self.parameters[5].get('value_meta_data',[])[0].get('fair_value',"")

    def setNonHdlCholesterolModerateValueMale(self):
        self.non_hdl_moderate_male = self.parameters[5].get('value_meta_data',[])[0].get('moderate_value',"")

    def setNonHdlCholesterolHighValueMale(self):
        self.non_hdl_high_male = self.parameters[5].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setNonHdlCholesterolLowValueFemale(self):
        self.non_hdl_low_female = self.parameters[5].get('value_meta_data',[])[0].get('low_value',"")

    def setNonHdlCholesterolFairValueFemale(self):
        self.non_hdl_fair_female = self.parameters[5].get('value_meta_data',[])[0].get('fair_value',"")

    def setNonHdlCholesterolModerateValueFemale(self):
        self.non_hdl_moderate_female = self.parameters[5].get('value_meta_data',[])[0].get('moderate_value',"")

    def setNonHdlCholesterolHighValueFemale(self):
        self.non_hdl_high_female = self.parameters[5].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setNonHdlCholesterolFunction(self):
        self.non_hdl_func = self.parameters[5].get("value_function",{}).get("function_name","")

    def setTcHdlRatioValue(self, tc_hdl):
        self.tc_hdl_ratio = tc_hdl

    def setTcHdlRatioMedicalAnnotations(self):
        self.tc_hdl_ratio_medical_annot = self.parameters[6].get('medical_annotation',[])

    def setTcHdlRatioUnit(self):
        self.tc_hdl_ratio_unit  = self.parameters[6].get('value_meta_data',[])[0].get('unit',"")

    def setTcHdlRatioRangeMale(self):
        self.tc_hdl_ratio_range_male  = self.parameters[6].get('value_meta_data',[])[0].get('range',"")

    def setTcHdlRatioRangeFemale(self):
        self.tc_hdl_ratio_range_female = self.parameters[6].get('value_meta_data',[])[1].get('range',"")

    def setTcHdlRatioLowValueMale(self):
        self.tc_hdl_ratio_low_male = self.parameters[6].get('value_meta_data',[])[0].get('low_value',"")

    def setTcHdlRatioFairValueMale(self):
        self.tc_hdl_ratio_fair_male = self.parameters[6].get('value_meta_data',[])[0].get('fair_value',"")

    def setTcHdlRatioModerateValueMale(self):
        self.tc_hdl_ratio_moderate_male = self.parameters[6].get('value_meta_data',[])[0].get('moderate_value',"")

    def setTcHdlRatioHighValueMale(self):
        self.tc_hdl_ratio_high_male = self.parameters[6].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setTcHdlRatioLowValueFemale(self):
        self.tc_hdl_ratio_low_female = self.parameters[6].get('value_meta_data',[])[1].get('low_value',"")

    def setTcHdlRatioFairValueFemale(self):
        self.tc_hdl_ratio_fair_female = self.parameters[6].get('value_meta_data',[])[1].get('fair_value',"")

    def setTcHdlRatioModerateValueFemale(self):
        self.tc_hdl_ratio_moderate_female = self.parameters[6].get('value_meta_data',[])[1].get('moderate_value',"")

    def setTcHdlRatioHighValueFemale(self):
        self.tc_hdl_ratio_high_female = self.parameters[6].get('value_meta_data',[])[1].get('high_value',"")[1:]

    def setTcHdlRatioFunction(self):
        self.tc_hdl_ratio_func = self.parameters[6].get("value_function",{}).get("function_name","")

    def setLdlHdlRatioValue(self, ldl_hdl):
        self.ldl_hdl_ratio = ldl_hdl

    def setLdlHdlRatioMedicalAnnotations(self):
        self.ldl_hdl_ratio_medical_annot = self.parameters[7].get('medical_annotation',[])

    def setLdlHdlRatioUnit(self):
        self.ldl_hdl_ratio_unit  = self.parameters[7].get('value_meta_data',[])[0].get('unit',"")

    def setLdlHdlRatioRangeMale(self):
        self.ldl_hdl_ratio_range_male  = self.parameters[7].get('value_meta_data',[])[0].get('range',"")

    def setLdlHdlRatioRangeFemale(self):
        self.ldl_hdl_ratio_range_female = self.parameters[7].get('value_meta_data',[])[1].get('range',"")

    def setLdlHdlRatioLowValueMale(self):
        self.ldl_hdl_ratio_low_male = self.parameters[7].get('value_meta_data',[])[0].get('low_value',"")

    def setLdlHdlRatioFairValueMale(self):
        self.ldl_hdl_ratio_fair_male = self.parameters[7].get('value_meta_data',[])[0].get('fair_value',"")

    def setLdlHdlRatioModerateValueMale(self):
        self.ldl_hdl_ratio_moderate_male = self.parameters[7].get('value_meta_data',[])[0].get('moderate_value',"")

    def setLdlHdlRatioHighValueMale(self):
        self.ldl_hdl_ratio_high_male = self.parameters[7].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setLdlHdlRatioLowValueFemale(self):
        self.ldl_hdl_ratio_low_female = self.parameters[7].get('value_meta_data',[])[1].get('low_value',"")

    def setLdlHdlRatioFairValueFemale(self):
        self.ldl_hdl_ratio_fair_female = self.parameters[7].get('value_meta_data',[])[1].get('fair_value',"")

    def setLdlHdlRatioModerateValueFemale(self):
        self.ldl_hdl_ratio_moderate_female = self.parameters[7].get('value_meta_data',[])[1].get('moderate_value',"")

    def setLdlHdlRatioHighValueFemale(self):
        self.ldl_hdl_ratio_high_female = self.parameters[7].get('value_meta_data',[])[1].get('high_value',"")[1:]

    def setLdlHdlRatioFunction(self):
        self.ldl_hdl_ratio_func = self.parameters[7].get("value_function",{}).get("function_name","")

    def setApolipoA1Value(self, apolipo_a1):
        self.apolipoproteina1 = apolipo_a1

    def setApolipoA1MedicalAnnotations(self):
        self.apolipoproteina1_medical_annot = self.parameters[8].get('medical_annotation',[])

    def setApolipoA1Unit(self):
        self.apolipoproteina1_unit  = self.parameters[8].get('value_meta_data',[])[0].get('unit',"")

    def setApolipoA1RangeMale(self):
        self.apolipoproteina1_range_male  = self.parameters[8].get('value_meta_data',[])[0].get('range',"")

    def setApolipoA1RangeFemale(self):
        self.apolipoproteina1_range_female = self.parameters[8].get('value_meta_data',[])[1].get('range',"")

    def setApolipoA1LowValueMale(self):
        self.apolipoproteina1_low_male = self.parameters[8].get('value_meta_data',[])[0].get('low_value',"")

    def setApolipoA1FairValueMale(self):
        self.apolipoproteina1_fair_male = self.parameters[8].get('value_meta_data',[])[0].get('fair_value',"")

    def setApolipoA1ModerateValueMale(self):
        self.apolipoproteina1_moderate_male = self.parameters[8].get('value_meta_data',[])[0].get('moderate_value',"")

    def setApolipoA1HighValueMale(self):
        self.apolipoproteina1_high_male = self.parameters[8].get('value_meta_data',[])[0].get('high_value',"")[1:]

    def setApolipoA1LowValueFemale(self):
        self.apolipoproteina1_low_female = self.parameters[8].get('value_meta_data',[])[1].get('low_value',"")

    def setApolipoA1FairValueFemale(self):
        self.apolipoproteina1_fair_female = self.parameters[8].get('value_meta_data',[])[1].get('fair_value',"")

    def setApolipoA1ModerateValueFemale(self):
        self.apolipoproteina1_moderate_female = self.parameters[8].get('value_meta_data',[])[1].get('moderate_value',"")

    def setApolipoA1HighValueFemale(self):
        self.apolipoproteina1_high_female = self.parameters[8].get('value_meta_data',[])[1].get('high_value',"")[1:]

    def setApolipoA1Function(self):
        self.apolipoproteina1_func = self.parameters[8].get("value_function",{}).get("function_name","")


 
 
    # Fuction returns category id
    def getCategoryid(self):
        return self.category_id 

    # Function returns category name
    def getCategoryName(self):
        return self.category_name

    # Function returns Version number
    def getVersionNumber(self):
        return self.version_number 
    
    # Function returns actual cholesterol value
    def getTotalCholesterolValue(self):
        return self.total_cholesterol

    # Function returns unit of total cholesterol  
    def getTotalCholesterolUnit(self):
        return self.total_chol_unit 
    
    # Function returns list of medical annotations for total cholesterol
    def getTotalCholesterolMedicalAnnotations(self):
        return self.total_chol_medical_annot 
   
    # Function returns range of values for total cholesterol for male  
    def getTotalCholesterolRangeMale(self):
        return self.total_chol_range_male 

    # Function returns range of values for total cholesterol for female  
    def getTotalCholesterolRangeFemale(self):
        return self.total_chol_range_female

    # Function returns low risk values range for total cholesterol
    def getTotalCholesterolLowValueMale(self):
        return self.total_chol_low_male 

    # Function returns fair risk values range for total cholesterol
    def getTotalCholesterolFairValueMale(self):
        return self.total_chol_fair_male
    
    # Function returns moderate risk values range for total cholesterol
    def getTotalCholesterolModerateValueMale(self):
        return self.total_chol_moderate_male 

    # Function returns high risk values range for total cholesterol 
    def getTotalCholesterolHighValueMale(self):
        return self.total_chol_high_male

    # Function returns low risk values range for total cholesterol
    def getTotalCholesterolLowValueFemale(self):
        return self.total_chol_low_female

    # Function returns fair risk values range for total cholesterol
    def getTotalCholesterolFairValueFemale(self):
        return self.total_chol_fair_female

    # Function returns moderate risk values range for total cholesterol
    def getTotalCholesterolModerateValueFemale(self):
        return self.total_chol_moderate_female

    # Function returns high risk values range for total cholesterol 
    def getTotalCholesterolHighValueFemale(self):
        return self.total_chol_high_female

    # Function returns function name to parse total cholesterol value from medical reports
    def getTotalCholesterolsFunction(self):
        return self.total_chol_func

    # Function returns function name to parse total cholesterol value from medical reports
    def getTotalCholesterolsFunction(self):
        return self.total_chol_func 
    
    # Function returns actual hdl cholesterol value
    def getHdlCholesterolValue(self):
        return self.hdl_cholesterol

    # Function returns list of medical annotations for hdl cholesterol
    def getHdlCholesterolMedicalAnnotations(self):
        return self.hdl_chol_medical_annot

    # Function returns unit of hdl cholesterol 
    def getHdlCholesterolUnit(self):
        return self.hdl_chol_unit

    # Function returns range of values for hdl cholesterol for male
    def getHdlCholesterolRangeMale(self):
        return self.hdl_chol_range_male

    # Function returns range of values for hdl cholesterol for female
    def getHdlCholesterolRangeFemale(self):
        return self.hdl_chol_range_female 

    # Function returns low risk values range for hdl cholesterol
    def getHdlCholesterolLowValueMale(self):
        return self.hdl_chol_low_male

    # Function returns fair risk values range for hdl cholesterol
    def getHdlCholesterolFairValueMale(self):
        return self.hdl_chol_fair_male
    
    # Function retuns moderate risk value ranges for hdl cholesterol
    def getHdlCholesterolModerateValueMale(self):
        return self.hdl_chol_moderate_male 

    # Function returns high risk value ranges for hdl cholesterol
    def getHdlCholesterolHighValueMale(self):
        return self.hdl_chol_high_male
  
    # Function returns low risk values range for hdl cholesterol
    def getHdlCholesterolLowValueFemale(self):
        return self.hdl_chol_low_female

    # Function returns fair risk values range for hdl cholesterol
    def getHdlCholesterolFairValueFemale(self):
        return self.hdl_chol_fair_female

    # Function retuns moderate risk value ranges for hdl cholesterol
    def getHdlCholesterolModerateValueFemale(self):
        return self.hdl_chol_moderate_female

    # Function returns high risk value ranges for hdl cholesterol
    def getHdlCholesterolHighValueFemale(self):
        return self.hdl_chol_high_female
 
    # Function returns function name to parse total cholesterol value from medical reports
    def getHdlCholesterolsFunction(self):
        return self.hdl_chol_func
    
    # Function returns ldl cholesterol actual value
    def getLdlCholesterolValue(self):
        return self.ldl_cholesterol 

    # Function returns list of medical annotations for ldl cholesterol
    def getLdlCholesterolMedicalAnnotations(self):
        return self.ldl_chol_medical_annot

    # Function returns unit of ldl cholesterol
    def getLdlCholesterolUnit(self):
        return self.ldl_chol_unit

    # Function returns range of values for ldl cholesterol for male
    def getLdlCholesterolRangeMale(self):
        return self.ldl_chol_range_male

    # Function returns range of values for ldl cholesterol for female
    def getLdlCholesterolRangeFemale(self):
        return self.ldl_chol_range_female
    
    # Function returns low risk values range for ldl cholesterol
    def getLdlCholesterolLowValueMale(self):
        return self.ldl_chol_low_male

    # Function returns fair risk values range for ldl cholesterol
    def getLdlCholesterolFairValueMale(self):
        return self.ldl_chol_fair_male
    
    # Function returns moderate risk values range for ldl cholesterol
    def getLdlCholesterolModerateValueMale(self):
        return self.ldl_chol_moderate_male

    # Function returns high risk values range for ldl cholesterol
    def getLdlCholesterolHighValueMale(self):
        return self.ldl_chol_high_male
   
    # Function returns low risk values range for ldl cholesterol
    def getLdlCholesterolLowValueFemale(self):
        return self.ldl_chol_low_female

    # Function returns fair risk values range for ldl cholesterol
    def getLdlCholesterolFairValueFemale(self):
        return self.ldl_chol_fair_female

    # Function returns moderate risk values range for ldl cholesterol
    def getLdlCholesterolModerateValueFemale(self):
        return self.ldl_chol_moderate_female

    # Function returns high risk values range for ldl cholesterol
    def getLdlCholesterolHighValueFemale(self):
        return self.ldl_chol_high_female

    # Function returns function name to parse ldl cholesterol value from medical report 
    def getLdlCholesterolsFunction(self):
        return self.ldl_chol_func
    
    # Function returns triglycerides actual value
    def getTriglyceridesValue(self):
        return self.triglycerides
    
    # Function returns list of medical annotations for triglycerides 
    def getTriglyceridesMedicalAnnotations(self):
        return self.trigly_medical_annot 

    # Function returns unit of triglycerides
    def getTriglyceridesUnit(self):
        return self.trigly_unit

    # Function returns range of values ranges for triglycerides for male 
    def getTriglyceridesRangeMale(self):
        return self.trigly_range_male  

    # Function returns range of values ranges for triglycerides for female 
    def getTriglyceridesRangeFemale(self):
        return self.trigly_range_female

    # Function returns low risk values range for ldl cholesterol
    def getTriglyceridesLowValueMale(self):
        return self.trigly_low_male

    # Function returns fair risk values range for ldl cholesterol
    def getTriglyceridesFairValueMale(self):
        return self.trigly_fair_male
    
    # Function returns moderate risk values range for ldl cholesterol
    def getTriglyceridesModerateValueMale(self):
        return self.trigly_moderate_male

    # Function returns high risk values range for ldl cholesterol
    def getTriglyceridesHighValueMale(self):
        return self.trigly_high_male
   
    # Function returns low risk values range for ldl cholesterol
    def getTriglyceridesLowValueFemale(self):
        return self.trigly_low_female

    # Function returns fair risk values range for ldl cholesterol
    def getTriglyceridesFairValueFemale(self):
        return self.trigly_fair_female

    # Function returns moderate risk values range for ldl cholesterol
    def getTriglyceridesModerateValueFemale(self):
        return self.trigly_moderate_female

    # Function returns high risk values range for ldl cholesterol
    def getTriglyceridesHighValueFemale(self):
        return self.trigly_high_female
 
    # Function returns function name for parsing triglycerides value from medical reports
    def getTriglyceridesFunction(self):
        return self.trigly_func

    def getVldlCholesterolValue(self):
        return self.vldl_cholesterol

    def getVldlCholesterolMedicalAnnotations(self):
        return self.vldl_medical_annot

    def getVldlCholesterolUnit(self):
        return self.vldl_unit

    def getVldlCholesterolRangeMale(self):
        return self.vldl_range_male

    def getVldlCholesterolRangeFemale(self):
        return self.vldl_range_female

    def getVldlCholesterolLowValueMale(self):
        return self.vldl_low_male

    def getVldlCholesterolFairValueMale(self):
        return self.vldl_fair_male

    def getVldlCholesterolModerateValueMale(self):
        return self.vldl_moderate_male

    def getVldlCholesterolHighValueMale(self):
        return self.vldl_high_male

    def getVldlCholesterolLowValueFemale(self):
        return self.vldl_low_female

    def getVldlCholesterolFairValueFemale(self):
        return self.vldl_fair_female

    def getVldlCholesterolModerateValueFemale(self):
        return self.vldl_moderate_female

    def getVldlCholesterolHighValueFemale(self):
        return self.vldl_high_female

    def getVldlCholesterolFunction(self):
        return self.vldl_func

    def getNonHdlCholesterolValue(self):
        return self.non_hdl_cholesterol

    def getNonHdlCholesterolMedicalAnnotations(self):
        return self.non_hdl_medical_annot

    def getNonHdlCholesterolUnit(self):
        return self.non_hdl_unit

    def getNonHdlCholesterolRangeMale(self):
        return self.non_hdl_range_male

    def getNonHdlCholesterolRangeFemale(self):
        return self.non_hdl_range_female

    def getNonHdlCholesterolLowValueMale(self):
        return self.non_hdl_low_male

    def getNonHdlCholesterolFairValueMale(self):
        return self.non_hdl_fair_male

    def getNonHdlCholesterolModerateValueMale(self):
        return self.non_hdl_moderate_male

    def getNonHdlCholesterolHighValueMale(self):
        return self.non_hdl_high_male

    def getNonHdlCholesterolLowValueFemale(self):
        return self.non_hdl_low_female

    def getNonHdlCholesterolFairValueFemale(self):
        return self.non_hdl_fair_female

    def getNonHdlCholesterolModerateValueFemale(self):
        return self.non_hdl_moderate_female

    def getNonHdlCholesterolHighValueFemale(self):
        return self.non_hdl_high_female

    def getNonHdlCholesterolFunction(self):
        return self.non_hdl_func

    def getTcHdlRatioValue(self):
        return self.tc_hdl_ratio

    def getTcHdlRatioMedicalAnnotations(self):
        return self.tc_hdl_ratio_medical_annot

    def getTcHdlRatioUnit(self):
        return self.tc_hdl_ratio_unit

    def getTcHdlRatioRangeMale(self):
        return self.tc_hdl_ratio_range_male

    def getTcHdlRatioRangeFemale(self):
        return self.tc_hdl_ratio_range_female

    def getTcHdlRatioLowValueMale(self):
        return self.tc_hdl_ratio_low_male

    def getTcHdlRatioFairValueMale(self):
        return self.tc_hdl_ratio_fair_male

    def getTcHdlRatioModerateValueMale(self):
        return self.tc_hdl_ratio_moderate_male

    def getTcHdlRatioHighValueMale(self):
        return self.tc_hdl_ratio_high_male

    def getTcHdlRatioLowValueFemale(self):
        return self.tc_hdl_ratio_low_female

    def getTcHdlRatioFairValueFemale(self):
        return self.tc_hdl_ratio_fair_female

    def getTcHdlRatioModerateValueFemale(self):
        return self.tc_hdl_ratio_moderate_female

    def getTcHdlRatioHighValueFemale(self):
        return self.tc_hdl_ratio_high_female

    def getTcHdlRatioFunction(self):
        return self.tc_hdl_ratio_func
    
    def getLdlHdlRatioValue(self):
        return self.ldl_hdl_ratio

    def getLdlHdlRatioMedicalAnnotations(self):
        return self.ldl_hdl_ratio_medical_annot

    def getLdlHdlRatioUnit(self):
        return self.ldl_hdl_ratio_unit

    def getLdlHdlRatioRangeMale(self):
        return self.ldl_hdl_ratio_range_male

    def getLdlHdlRatioRangeFemale(self):
        return self.ldl_hdl_ratio_range_female

    def getLdlHdlRatioLowValueMale(self):
        return self.ldl_hdl_ratio_low_male

    def getLdlHdlRatioFairValueMale(self):
        return self.ldl_hdl_ratio_fair_male

    def getLdlHdlRatioModerateValueMale(self):
        return self.ldl_hdl_ratio_moderate_male

    def getLdlHdlRatioHighValueMale(self):
        return self.ldl_hdl_ratio_high_male

    def getLdlHdlRatioLowValueFemale(self):
        return self.ldl_hdl_ratio_low_female

    def getLdlHdlRatioFairValueFemale(self):
        return self.ldl_hdl_ratio_fair_female

    def getLdlHdlRatioModerateValueFemale(self):
        return self.ldl_hdl_ratio_moderate_female

    def getLdlHdlRatioHighValueFemale(self):
        return self.ldl_hdl_ratio_high_female

    def getLdlHdlRatioFunction(self):
        return self.ldl_hdl_ratio_func

    def getApolipoA1Value(self):
        return self.apolipoproteina1

    def getApolipoA1MedicalAnnotations(self):
        return self.apolipoproteina1_medical_annot

    def getApolipoA1Unit(self):
        return self.apolipoproteina1_unit

    def getApolipoA1RangeMale(self):
        return self.apolipoproteina1_range_male

    def getApolipoA1RangeFemale(self):
        return self.apolipoproteina1_range_female

    def getApolipoA1LowValueMale(self):
        return self.apolipoproteina1_low_male

    def getApolipoA1FairValueMale(self):
        return self.apolipoproteina1_fair_male

    def getApolipoA1ModerateValueMale(self):
        return self.apolipoproteina1_moderate_male

    def getApolipoA1HighValueMale(self):
        return self.apolipoproteina1_high_male

    def getApolipoA1LowValueFemale(self):
        return self.apolipoproteina1_low_female

    def getApolipoA1FairValueFemale(self):
        return self.apolipoproteina1_fair_female

    def getApolipoA1ModerateValueFemale(self):
        return self.apolipoproteina1_moderate_female

    def getApolipoA1HighValueFemale(self):
        return self.apolipoproteina1_high_female

    def getApolipoA1Function(self):
        return self.apolipoproteina1_func


# objec for lipid profile
#lipid_profile = LipidProfile()

#call loadMetaData Function
#lipid_profile.loadMetaData()

#call getParsedData function to get parsed output values
#lipid_parsed_value = lipid_profile.getParsedData("/home/isana/160631779_ADHIR_P_POTDAR_WL.pdf")
#print json.dumps({"lipid_parsed_values" : lipid_parsed_value}, indent = 4)
