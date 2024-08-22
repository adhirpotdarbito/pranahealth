import json
from collections import OrderedDict
from __config import *
from __medical_report_parser import *
from __medical_report_template import *

class LiverProfile(MedicalReportTemplate):
    def __init__(self):
        try:
            super(LiverProfile, self).__init__()
            self.file_path = json_file_data.get("medical_parser_detail","")[3].get("file_name","")
            self.bilirubin_total = None
            self.bilirubin_direct = None
            self.bilirubin_indirect = None
            self.total_protein = None
            self.albumin = None
            self.globulin = None
            self.albumin_globulin_ratio = None
            self.aspartate_aminotrans = None
            self.gamma_glutamyl_trans = None
            self.alkaline_phosphatase = None
            self.alanine_transaminase = None
            self.category_id = "" 
            self.category_name = ""
            self.version_number = ""
            self.bilirubin_total_unit = ""
            self.bilirubin_total_medical_annot = []
            self.bilirubin_total_range_male = ""
            self.bilirubin_total_range_female = ""
            self.bilirubin_total_low_male = ""
            self.bilirubin_total_fair_male = ""
            self.bilirubin_total_moderate_male = ""
            self.bilirubin_total_high_male = ""
            self.bilirubin_total_low_female = ""
            self.bilirubin_total_fair_female = ""
            self.bilirubin_total_moderate_female = ""
            self.bilirubin_total_high_female = ""
            self.bilirubin_total_func = ""
            self.bilirubin_direct_unit = ""
            self.bilirubin_direct_medical_annot = []
            self.bilirubin_direct_range_male = ""
            self.bilirubin_direct_range_female = ""
            self.bilirubin_direct_low_male = ""
            self.bilirubin_direct_fair_male = ""
            self.bilirubin_direct_moderate_male = ""
            self.bilirubin_direct_high_male = ""
            self.bilirubin_direct_low_female = ""
            self.bilirubin_direct_fair_female = ""
            self.bilirubin_direct_moderate_female = ""
            self.bilirubin_direct_high_female = ""
            self.bilirubin_direct_func = ""
            self.bilirubin_indirect_unit = ""
            self.bilirubin_indirect_medical_annot = []
            self.bilirubin_indirect_range_male = ""
            self.bilirubin_indirect_range_female = ""
            self.bilirubin_indirect_low_male = ""
            self.bilirubin_indirect_fair_male = ""
            self.bilirubin_indirect_moderate_male = ""
            self.bilirubin_indirect_high_male = ""
            self.bilirubin_indirect_low_female = ""
            self.bilirubin_indirect_fair_female = ""
            self.bilirubin_indirect_moderate_female = ""
            self.bilirubin_indirect_high_female = ""
            self.bilirubin_indirect_func = ""
            self.total_protein_unit = ""
            self.total_protein_medical_annot = []
            self.total_protein_range_male = ""
            self.total_protein_range_female = ""
            self.total_protein_low_male = ""
            self.total_protein_fair_male = ""
            self.total_protein_moderate_male = ""
            self.total_protein_high_male = ""
            self.total_protein_low_female = ""
            self.total_protein_fair_female = ""
            self.total_protein_moderate_female = ""
            self.total_protein_high_female = ""
            self.total_protein_func = ""
            self.albumin_unit = ""
            self.albumin_medical_annot = []
            self.albumin_range_male = ""
            self.albumin_range_female = ""
            self.albumin_low_male = ""
            self.albumin_fair_male = ""
            self.albumin_moderate_male = ""
            self.albumin_high_male = ""
            self.albumin_low_female = ""
            self.albumin_fair_female = ""
            self.albumin_moderate_female = ""
            self.albumin_high_female = ""
            self.albumin_func = ""
            self.globulin_unit = ""
            self.globulin_medical_annot = []
            self.globulin_range_male = ""
            self.globulin_range_female = ""
            self.globulin_low_male = ""
            self.globulin_fair_male = ""
            self.globulin_moderate_male = ""
            self.globulin_high_male = ""
            self.globulin_low_female = ""
            self.globulin_fair_female = ""
            self.globulin_moderate_female = ""
            self.globulin_high_female = ""
            self.globulin_func = ""
            self.album_glob_ratio_unit = ""
            self.album_glob_ratio_medical_annot = []
            self.album_glob_ratio_range_male = ""
            self.album_glob_ratio__range_female = ""
            self.album_glob_ratio_low_male = ""
            self.album_glob_ratio_fair_male = ""
            self.album_glob_ratio_moderate_male = ""
            self.album_glob_ratio_high_male = ""
            self.album_glob_ratio_low_female = ""
            self.album_glob_ratio_fair_female = ""
            self.album_glob_ratio_moderate_female = ""
            self.album_glob_ratio_high_female = ""
            self.album_glob_ratio_func = ""
            self.aspartate_aminotrans_unit = ""
            self.aspartate_aminotrans_medical_annot = []
            self.aspartate_aminotrans_range_male = ""
            self.aspartate_aminotrans_range_female = ""
            self.aspartate_aminotrans_low_male = ""
            self.aspartate_aminotrans_fair_male = ""
            self.aspartate_aminotrans_moderate_male = ""
            self.aspartate_aminotrans_high_male = ""
            self.aspartate_aminotrans_low_female = ""
            self.aspartate_aminotrans_fair_female = ""
            self.aspartate_aminotrans_moderate_female = ""
            self.aspartate_aminotrans_high_female = ""
            self.aspartate_aminotrans_func = ""
            self.gamma_glutamyl_trans_unit = ""
            self.gamma_glutamyl_trans_medical_annot = []
            self.gamma_glutamyl_trans_range_male = ""
            self.gamma_glutamyl_trans_range_female = ""
            self.gamma_glutamyl_trans_low_male = ""
            self.gamma_glutamyl_trans_fair_male = ""
            self.gamma_glutamyl_trans_moderate_male = ""
            self.gamma_glutamyl_trans_high_male = ""
            self.gamma_glutamyl_trans_low_female = ""
            self.gamma_glutamyl_trans_fair_female = ""
            self.gamma_glutamyl_trans_moderate_female = ""
            self.gamma_glutamyl_trans_high_female = ""
            self.gamma_glutamyl_trans_func = ""
            self.alkaline_phosphatase_unit = ""
            self.alkaline_phosphatase_annot = []
            self.alkaline_phosphatase_male = ""
            self.alkaline_phosphatase_female = ""
            self.alkaline_phosphatase_low_male = ""
            self.alkaline_phosphatase_fair_male = ""
            self.alkaline_phosphatase_moderate_male = ""
            self.alkaline_phosphatase_high_male = ""
            self.alkaline_phosphatase_low_female = ""
            self.alkaline_phosphatase_fair_female = ""
            self.alkaline_phosphatase_moderate_female = ""
            self.alkaline_phosphatase_high_female = ""
            self.alkaline_phosphatase_func = ""
            self.alanine_transaminase_unit = ""
            self.alanine_transaminase_medical_annot = []
            self.alanine_transaminase_range_male = ""
            self.alanine_transaminase_range_female = ""
            self.alanine_transaminase_low_male = ""
            self.alanine_transaminase_fair_male = ""
            self.alanine_transaminase_moderate_male = ""
            self.alanine_transaminase_high_male = ""
            self.alanine_transaminase_low_female = ""
            self.alanine_transaminase_fair_female = ""
            self.alanine_transaminase_moderate_female = ""
            self.alanine_transaminase_high_female = ""
            self.alanine_transaminase_func = ""
            self.bilirubin_total_output = OrderedDict()
            self.bilirubin_direct_output = OrderedDict()
            self.bilirubin_indirect_output = OrderedDict()
            self.total_protein_output = OrderedDict()
            self.albumin_output = OrderedDict()
            self.globulin_output = OrderedDict()
            self.album_glob_ratio_output = OrderedDict()
            self.aspartate_aminotrans_output = OrderedDict()
            self.gamma_glutamyl_trans_output = OrderedDict()
            self.alkaline_phosphatase_output = OrderedDict()
            self.alanine_transaminase_output = OrderedDict()
        except Exception as err:
            print err


    def loadMetaData(self):
        super(LiverProfile, self).loadMetaData()   
        self.setCategoryid()
        self.setCategoryName()
        self.setVersionNumber() 
        self.setBilirubinTotalUnit()
        self.setBilirubinTotalMedicalAnotation()
        self.setBilirubinTotalRangeMale()
        self.setBilirubinTotalRangeFemale()
        self.setBilirubinTotalLowValueMale()
        self.setBilirubinTotalFairValueMale()
        self.setBilirubinTotalModerateValueMale()
        self.setBilirubinTotalHighValueMale()
        self.setBilirubinTotalLowValueFemale()
        self.setBilirubinTotalFairValueFemale()
        self.setBilirubinTotalModerateValueFemale()
        self.setBilirubinTotalHighValueFemale()
        self.setBilirubinTotalFunction()
        self.setBilirubinDirectUnit()
        self.setBilirubinDirectMedicalAnotation()
        self.setBilirubinDirectRangeMale()     
        self.setBilirubinDirectRangeFemale()     
        self.setBilirubinDirectLowValueMale()
        self.setBilirubinDirectFairValueMale()
        self.setBilirubinDirectModerateValueMale()
        self.setBilirubinDirectHighValueMale()
        self.setBilirubinDirectLowValueFemale()
        self.setBilirubinDirectFairValueFemale()
        self.setBilirubinDirectModerateValueFemale()
        self.setBilirubinDirectHighValueFemale()
        self.setBilirubinDirectFunction()
        self.setBilirubinIndirectUnit()
        self.setBilirubinIndirectMedicalAnotation()
        self.setBilirubinIndirectRangeMale()     
        self.setBilirubinIndirectRangeFemale()     
        self.setBilirubinIndirectLowValueMale()
        self.setBilirubinIndirectFairValueMale()
        self.setBilirubinIndirectModerateValueMale()
        self.setBilirubinIndirectHighValueMale()
        self.setBilirubinIndirectLowValueFemale()
        self.setBilirubinIndirectFairValueFemale()
        self.setBilirubinIndirectModerateValueFemale()
        self.setBilirubinIndirectHighValueFemale()
        self.setBilirubinIndirectFunction()
        self.setTotalProteinMedicalAnnotations()
        self.setTotalProteinUnit()
        self.setTotalProteinRangeMale()
        self.setTotalProteinRangeFemale()
        self.setTotalProteinLowValueMale()
        self.setTotalProteinFairValueMale()
        self.setTotalProteinModerateValueMale()
        self.setTotalProteinHighValueMale()
        self.setTotalProteinLowValueFemale()
        self.setTotalProteinFairValueFemale()
        self.setTotalProteinModerateValueFemale()
        self.setTotalProteinHighValueFemale()
        self.setTotalProteinFunction()
        self.setAlbuminUnit()
        self.setAlbuminMedicalAnnotations()
        self.setAlbuminRangeMale()
        self.setAlbuminRangeFemale()
        self.setAlbuminLowValueMale()
        self.setAlbuminFairValueMale()
        self.setAlbuminModerateValueMale()
        self.setAlbuminHighValueMale()
        self.setAlbuminLowValueFemale()
        self.setAlbuminFairValueFemale()
        self.setAlbuminModerateValueFemale()
        self.setAlbuminHighValueFemale()
        self.setAlbuminFunction()
        self.setGlobulinMedicalAnnotations()
        self.setGlobulinUnit()
        self.setGlobulinRangeMale()
        self.setGlobulinRangeFemale()
        self.setGlobulinLowValueMale()
        self.setGlobulinFairValueMale()
        self.setGlobulinModerateValueMale()
        self.setGlobulinHighValueMale()
        self.setGlobulinLowValueFemale()
        self.setGlobulinFairValueFemale()
        self.setGlobulinModerateValueFemale()
        self.setGlobulinHighValueFemale()
        self.setGlobulinFunction()
        self.setAlbumGlobRatioMedicalAnnotations()
        self.setAlbumGlobRatioUnit()
        self.setAlbumGlobRatioRangeMale()       
        self.setAlbumGlobRatioRangeFemale()      
        self.setAlbumGlobRatioLowValueMale() 
        self.setAlbumGlobRatioFairValueMale() 
        self.setAlbumGlobRatioModerateValueMale() 
        self.setAlbumGlobRatioHighValueMale() 
        self.setAlbumGlobRatioLowValueFemale() 
        self.setAlbumGlobRatioFairValueFemale() 
        self.setAlbumGlobRatioModerateValueFemale() 
        self.setAlbumGlobRatioHighValueFemale() 
        self.setAlbumGlobRatiosFunction()
        self.setAspartateAminotransMedicalAnnotations()
        self.setAspartateAminotransUnit()
        self.setAspartateAminotransRangeMale()
        self.setAspartateAminotransRangeFemale()
        self.setAspartateAminotransLowValueMale()
        self.setAspartateAminotransFairValueMale()
        self.setAspartateAminotransModerateValueMale()
        self.setAspartateAminotransHighValueMale()
        self.setAspartateAminotransLowValueFemale()
        self.setAspartateAminotransFairValueFemale()
        self.setAspartateAminotransModerateValueFemale()
        self.setAspartateAminotransHighValueFemale()
        self.setAspartateAminotransFunction()  
        self.setGammaGlutamylTransMedicalAnnotations()
        self.setGammaGlutamylTransUnit()
        self.setGammaGlutamylTransRangeMale()
        self.setGammaGlutamylTransRangeFemale()
        self.setGammaGlutamylTransLowValueMale()
        self.setGammaGlutamylTransFairValueMale()
        self.setGammaGlutamylTransModerateValueMale()
        self.setGammaGlutamylTransHighValueMale()
        self.setGammaGlutamylTransLowValueFemale()
        self.setGammaGlutamylTransFairValueFemale()
        self.setGammaGlutamylTransModerateValueFemale()
        self.setGammaGlutamylTransHighValueFemale()
        self.setGammaGlutamylTransFunction()
        self.setAlkalinePhosphataseMedicalAnnotations()
        self.setAlkalinePhosphataseUnit()
        self.setAlkalinePhosphataseRangeMale()
        self.setAlkalinePhosphataseRangeFemale()
        self.setAlkalinePhosphataseLowValueMale()
        self.setAlkalinePhosphataseFairValueMale()
        self.setAlkalinePhosphataseModerateValueMale()
        self.setAlkalinePhosphataseHighValueMale()
        self.setAlkalinePhosphataseLowValueFemale()
        self.setAlkalinePhosphataseFairValueFemale()
        self.setAlkalinePhosphataseModerateValueFemale()
        self.setAlkalinePhosphataseHighValueFemale()
        self.setAlkalinePhosphataseFunction()
        self.setAlkalinePhosphataseFunction
        self.setAlanineTransaminaseMedicalAnnotations()
        self.setAlanineTransaminaseUnit()
        self.setAlanineTransaminaseRangeMale()
        self.setAlanineTransaminaseRangeFemale()
        self.setAlanineTransaminaseLowValueMale()
        self.setAlanineTransaminaseFairValueMale()
        self.setAlanineTransaminaseModerateValueMale()
        self.setAlanineTransaminaseHighValueMale()
        self.setAlanineTransaminaseLowValueFemale()
        self.setAlanineTransaminaseFairValueFemale()
        self.setAlanineTransaminaseModerateValueFemale()
        self.setAlanineTransaminaseHighValueFemale()
        self.setAlanineTransaminaseFunction()

    def getParameters(self):
        return super(LiverProfile, self).getParameters()

    def getAnnotations(self, parameter_name):
        return super(LiverProfile, self).getAnnotations(parameter_name)       

    def getParsedData(self, file_name, gender, password=""):
        report_parse = ReportParser(file_name, password)
        report_parse.reportList()
        parameter_name = self.getParameters()
        med_annot_bilb_tot = self.getAnnotations(parameter_name[0])        
        med_annot_bilb_dir = self.getAnnotations(parameter_name[1])        
        med_annot_bilb_indir = self.getAnnotations(parameter_name[2])        
        med_annot_tot_protein = self.getAnnotations(parameter_name[3])        
        med_annot_albumin = self.getAnnotations(parameter_name[4])        
        med_annot_globulin = self.getAnnotations(parameter_name[5])        
        med_annot_alb_glob_ratio = self.getAnnotations(parameter_name[6])        
        med_annot_ast = self.getAnnotations(parameter_name[7])        
        med_annot_ggt = self.getAnnotations(parameter_name[8])        
        med_annot_alk_phos = self.getAnnotations(parameter_name[9])        
        med_annot_sgpt = self.getAnnotations(parameter_name[10])        
        report_parse.parseBilirubinTotal(med_annot_bilb_tot) 
        report_parse.parseBilirubinDirect(med_annot_bilb_dir)
        report_parse.parseBilirubinIndirect(med_annot_bilb_indir)
        report_parse.parseTotalProtein(med_annot_tot_protein)
        report_parse.parseAlbumin(med_annot_albumin)
        report_parse.parseGlobulin(med_annot_globulin)
        report_parse.parseAlbumGlobRatio(med_annot_alb_glob_ratio)
        report_parse.parseAspartateAminotransferase(med_annot_ast)
        report_parse.parseGammaGlutamylTrans(med_annot_ggt)
        report_parse.parseAlkalinePhosphatase(med_annot_alk_phos)
        report_parse.parseAlanineTransaminase(med_annot_sgpt)
        medical_report_dict = report_parse.getMedicalParsedData()
        # set actual values from medical report
        bilirubin_total_value = medical_report_dict.get("bilirubin_total",None)
        bilirubin_direct_value = medical_report_dict.get("bilirubin_direct",None)
        bilirubin_indirect_value = medical_report_dict.get("bilirubin_indirect",None)
        total_protein_value = medical_report_dict.get("total_protein",None)
        albumin_value = medical_report_dict.get("albumin",None)
        globulin_value = medical_report_dict.get("globulin",None)
        album_glob_ratio_value = medical_report_dict.get("albumin_globulin_ratio",None)
        aspartate_aminotrans_value = medical_report_dict.get("aspartate_aminotransferase",None) 
        gamma_glutamyl_trans_value = medical_report_dict.get("gamma_glutamyl_transferase",None)
        alkaline_phosphatase_value = medical_report_dict.get("alkaline_phosphatase",None) 
        alanine_transaminase_value = medical_report_dict.get("alanine_transaminase",None)
        self.setBilirubinTotalValue(bilirubin_total_value)
        self.setBilirubinDirectValue(bilirubin_direct_value)
        self.setBilirubinIndirectValue(bilirubin_indirect_value)
        self.setTotalProteinValue(total_protein_value)
        self.setAlbuminValue(albumin_value)
        self.setGlobulinValue(globulin_value)
        self.setAlbumGlobRatioValue(album_glob_ratio_value)
        self.setAspartateAminotransValue(aspartate_aminotrans_value)
        self.setGammaGlutamylTransValue(gamma_glutamyl_trans_value)
        self.setAlkalinePhosphataseValue(alkaline_phosphatase_value) 
        self.setAlanineTransaminaseValue(alanine_transaminase_value)
        self.bilirubin_total_output["reading_value"] = str(self.getBilirubinTotalValue())
        self.bilirubin_total_output["reading_unit"] = self.getBilirubinTotalUnit()
        self.bilirubin_total_output["range_male"] = self.getBilirubinTotalRangeMale()
        self.bilirubin_total_output["range_female"] = self.getBilirubinTotalRangeFemale()
        self.bilirubin_direct_output["reading_value"] = str(self.getBilirubinDirectValue())
        self.bilirubin_direct_output["reading_unit"] = self.getBilirubinDirectUnit()
        self.bilirubin_direct_output["range_male"] = self.getBilirubinDirectRangeMale()
        self.bilirubin_direct_output["range_female"] = self.getBilirubinDirectRangeFemale()
        self.bilirubin_indirect_output["reading_value"] = str(self.getBilirubinIndirectValue())
        self.bilirubin_indirect_output["reading_unit"] = self.getBilirubinIndirectUnit()
        self.bilirubin_indirect_output["range_male"] = self.getBilirubinIndirectRangeMale()
        self.bilirubin_indirect_output["range_female"] = self.getBilirubinIndirectRangeFemale()
        self.total_protein_output["reading_value"] = str(self.getTotalProteinValue())
        self.total_protein_output["reading_unit"] = self.getTotalProteinUnit()
        self.total_protein_output["range_male"] = self.getTotalProteinRangeMale()
        self.total_protein_output["range_female"] = self.getTotalProteinRangeFemale()
        self.albumin_output["reading_value"] = str(self.getAlbuminValue())
        self.albumin_output["reading_unit"] = self.getAlbuminUnit()
        self.albumin_output["range_male"] = self.getAlbuminRangeMale()
        self.albumin_output["range_female"] = self.getAlbuminRangeFemale()
        self.globulin_output["reading_value"] = str(self.getGlobulinValue())
        self.globulin_output["reading_unit"] = self.getGlobulinUnit()
        self.globulin_output["range_male"] = self.getGlobulinRangeMale()
        self.globulin_output["range_female"] = self.getGlobulinRangeFemale()
        self.album_glob_ratio_output["reading_value"] = str(self.getAlbumGlobRatioValue())
        self.album_glob_ratio_output["reading_unit"] = self.getAlbumGlobRatioUnit()
        self.album_glob_ratio_output["range_male"] = self.getAlbumGlobRatioRangeMale()
        self.album_glob_ratio_output["range_female"] = self.getAlbumGlobRatioRangeFemale()
        self.aspartate_aminotrans_output["reading_value"] = str(self.getAspartateAminotransValue())
        self.aspartate_aminotrans_output["reading_unit"] = self.getAspartateAminotransUnit()
        self.aspartate_aminotrans_output["range_male"] = self.getAspartateAminotransRangeMale()
        self.aspartate_aminotrans_output["range_female"] = self.getAspartateAminotransRangeFemale()
        self.gamma_glutamyl_trans_output["reading_value"] = str(self.getGammaGlutamylTransValue())
        self.gamma_glutamyl_trans_output["reading_unit"] = self.getGammaGlutamylTransUnit()
        self.gamma_glutamyl_trans_output["range_male"] = self.getGammaGlutamylTransRangeMale()
        self.gamma_glutamyl_trans_output["range_female"] = self.getGammaGlutamylTransRangeFemale()
        self.alkaline_phosphatase_output["reading_value"] = str(self.getAlkalinePhosphataseValue())
        self.alkaline_phosphatase_output["reading_unit"] = self.getAlkalinePhosphataseUnit()
        self.alkaline_phosphatase_output["range_male"] = self.getAlkalinePhosphataseRangeMale()
        self.alkaline_phosphatase_output["range_female"] = self.getAlkalinePhosphataseRangeFemale()
        self.alanine_transaminase_output["reading_value"] = str(self.getAlanineTransaminaseValue())
        self.alanine_transaminase_output["reading_unit"] = self.getAlanineTransaminaseUnit()
        self.alanine_transaminase_output["range_male"] = self.getAlanineTransaminaseRangeMale()
        self.alanine_transaminase_output["range_female"] = self.getAlanineTransaminaseRangeFemale()
        if gender == "Female":
            self.bilirubin_total_output["low_fair_moderate_high"] = [self.getBilirubinTotalLowValueFemale(), self.getBilirubinTotalFairValueFemale(), self.getBilirubinTotalModerateValueFemale(), self.getBilirubinTotalHighValueFemale()]
            if self.getBilirubinTotalValue() <= float(self.getBilirubinTotalLowValueFemale().split("-")[1]):
                self.bilirubin_total_output["risk"] = Low
            if self.getBilirubinTotalValue() >= float(self.getBilirubinTotalFairValueFemale().split("-")[0]) and self.getBilirubinTotalValue() <= float(self.getBilirubinTotalFairValueFemale().split("-")[1]):
                self.bilirubin_total_output["risk"] = Fair
            if self.getBilirubinTotalValue() >= float(self.getBilirubinTotalModerateValueFemale().split("-")[0]) and self.getBilirubinTotalValue() <= float(self.getBilirubinTotalModerateValueFemale().split("-")[1]):
                self.bilirubin_total_output["risk"] = Moderate
            if self.getBilirubinTotalValue() > float(self.getBilirubinTotalHighValueFemale()):
                self.bilirubin_total_output["risk"] = High
            if self.getBilirubinTotalValue() == None:
                self.bilirubin_total_output["risk"] = n_a
            self.parsed_output["bilirubin_total"] = self.bilirubin_total_output
                
            self.bilirubin_direct_output["low_fair_moderate_high"] = [self.getBilirubinDirectLowValueFemale(), self.getBilirubinDirectFairValueFemale(), self.getBilirubinDirectModerateValueFemale(), self.getBilirubinDirectHighValueFemale()]
            if self.getBilirubinDirectValue() <= float(self.getBilirubinDirectLowValueFemale().split("-")[1]):  
                self.bilirubin_direct_output["risk"] = Low
            if self.getBilirubinDirectValue() >= float(self.getBilirubinDirectFairValueFemale().split("-")[0]) and self.getBilirubinDirectValue() <= float(self.getBilirubinDirectFairValueFemale().split("-")[1]): 
                self.bilirubin_direct_output["risk"] = Fair
            if self.getBilirubinDirectValue() >= float(self.getBilirubinDirectModerateValueFemale().split("-")[0]) and self.getBilirubinDirectValue() <= float(self.getBilirubinDirectModerateValueFemale().split("-")[1]): 
                self.bilirubin_direct_output["risk"] = Moderate
            if self.getBilirubinDirectValue() > float(self.getBilirubinDirectHighValueFemale()): 
                self.bilirubin_direct_output["risk"] = High
            if self.getBilirubinDirectValue() == None:
                self.bilirubin_direct_output["risk"] = n_a
            self.parsed_output["bilirubin_direct"] = self.bilirubin_direct_output

            self.bilirubin_indirect_output["low_fair_moderate_high"] = [self.getBilirubinIndirectLowValueFemale(), self.getBilirubinIndirectFairValueFemale(), self.getBilirubinIndirectModerateValueFemale(), self.getBilirubinIndirectHighValueFemale()]
            if self.getBilirubinIndirectValue() <= float(self.getBilirubinIndirectLowValueFemale().split("-")[1]):  
                self.bilirubin_indirect_output["risk"] = Low
            if self.getBilirubinIndirectValue() >= float(self.getBilirubinIndirectFairValueFemale().split("-")[0]) and self.getBilirubinIndirectValue() <= float(self.getBilirubinIndirectFairValueFemale().split("-")[1]): 
                self.bilirubin_indirect_output["risk"] = Fair
            if self.getBilirubinIndirectValue() >= float(self.getBilirubinIndirectModerateValueFemale().split("-")[0]) and self.getBilirubinIndirectValue() <= float(self.getBilirubinIndirectModerateValueFemale().split("-")[1]): 
                self.bilirubin_indirect_output["risk"] = Moderate
            if self.getBilirubinIndirectValue() > float(self.getBilirubinIndirectHighValueFemale()): 
                self.bilirubin_indirect_output["risk"] = High
            if self.getBilirubinIndirectValue() == None:
                self.bilirubin_indirect_output["risk"] = n_a
            self.parsed_output["bilirubin_indirect"] = self.bilirubin_indirect_output

            self.total_protein_output["low_fair_moderate_high"] = [self.getTotalProteinLowValueFemale(), self.getTotalProteinFairValueFemale(), self.getTotalProteinModerateValueFemale(), self.getTotalProteinHighValueFemale()]
            if self.getTotalProteinValue() <= float(self.getTotalProteinLowValueFemale().split("-")[1]):
                self.total_protein_output["risk"] = Low
            if self.getTotalProteinValue() >= float(self.getTotalProteinFairValueFemale().split("-")[0]) and self.getTotalProteinValue() <= float(self.getTotalProteinFairValueFemale().split("-")[1]):
                self.total_protein_output["risk"] = Fair
            if self.getTotalProteinValue() >= float(self.getTotalProteinModerateValueFemale().split("-")[0]) and self.getTotalProteinValue() <= float(self.getTotalProteinModerateValueFemale().split("-")[1]):
                self.total_protein_output["risk"] = Moderate
            if self.getTotalProteinValue() > float(self.getTotalProteinHighValueFemale()):
                self.total_protein_output["risk"] = High
            if self.getTotalProteinValue() == None:
                self.total_protein_output["risk"] = n_a
            self.parsed_output["total_protein"] = self.total_protein_output

            self.albumin_output["low_fair_moderate_high"] = [self.getAlbuminLowValueFemale(), self.getAlbuminFairValueFemale(), self.getAlbuminModerateValueFemale(), self.getAlbuminHighValueFemale()]
            if self.getAlbuminValue() <= float(self.getAlbuminLowValueFemale().split("-")[1]):
                self.albumin_output["risk"] = Low
            if self.getAlbuminValue() >= float(self.getAlbuminFairValueFemale().split("-")[0]) and self.getAlbuminValue() <= float(self.getAlbuminFairValueFemale().split("-")[1]):
                self.albumin_output["risk"] = Fair
            if self.getAlbuminValue() >= float(self.getAlbuminModerateValueFemale().split("-")[0]) and self.getAlbuminValue() <= float(self.getAlbuminModerateValueFemale().split("-")[1]):
                self.albumin_output["risk"] = Moderate
            if self.getAlbuminValue() > float(self.getAlbuminHighValueFemale()):
                self.albumin_output["risk"] = High
            if self.getAlbuminValue() == None:
                self.albumin_output["risk"] = n_a
            self.parsed_output["albumin"] = self.albumin_output

            self.globulin_output["low_fair_moderate_high"] = [self.getGlobulinLowValueFemale(), self.getGlobulinFairValueFemale(), self.getGlobulinModerateValueFemale(), self.getGlobulinHighValueFemale()]
            if self.getGlobulinValue() <= float(self.getGlobulinLowValueFemale().split("-")[1]):
                self.globulin_output["risk"] = Low
            if self.getGlobulinValue() >= float(self.getGlobulinFairValueFemale().split("-")[0]) and self.getGlobulinValue() <= float(self.getGlobulinFairValueFemale().split("-")[1]):
                self.globulin_output["risk"] = Fair
            if self.getGlobulinValue() >= float(self.getGlobulinModerateValueFemale().split("-")[0]) and self.getGlobulinValue() <= float(self.getGlobulinModerateValueFemale().split("-")[1]):
                self.globulin_output["risk"] = Moderate
            if self.getGlobulinValue() > float(self.getGlobulinHighValueFemale()):
                self.globulin_output["risk"] = High
            if self.getGlobulinValue() == None:
                self.globulin_output["risk"] = n_a
            self.parsed_output["globulin"] = self.globulin_output
    
            self.album_glob_ratio_output["low_fair_moderate_high"] = [self.getAlbumGlobRatioLowValueFemale(), self.getAlbumGlobRatioFairValueFemale(), self.getAlbumGlobRatioModerateValueFemale(), self.getAlbumGlobRatioHighValueFemale()]
            if self.getAlbumGlobRatioValue() <= float(self.getAlbumGlobRatioLowValueFemale().split("-")[1]):  
                self.album_glob_ratio_output["risk"] = Low
            if self.getAlbumGlobRatioValue() >= float(self.getAlbumGlobRatioFairValueFemale().split("-")[0]) and self.getAlbumGlobRatioValue() <= float(self.getAlbumGlobRatioFairValueFemale().split("-")[1]): 
                self.album_glob_ratio_output["risk"] = Fair
            if self.getAlbumGlobRatioValue() >= float(self.getAlbumGlobRatioModerateValueFemale().split("-")[0]) and self.getAlbumGlobRatioValue() <= float(self.getAlbumGlobRatioModerateValueFemale().split("-")[1]): 
                self.album_glob_ratio_output["risk"] = Moderate
            if self.getAlbumGlobRatioValue() > float(self.getAlbumGlobRatioHighValueFemale()): 
                self.album_glob_ratio_output["risk"] = High
            if self.getAlbumGlobRatioValue() == None:
                self.album_glob_ratio_output["risk"] = n_a
            self.parsed_output["albumin_globulin_ratio"] = self.album_glob_ratio_output

            self.aspartate_aminotrans_output["low_fair_moderate_high"] = [self.getAspartateAminotransLowValueFemale(), self.getAspartateAminotransFairValueFemale(), self.getAspartateAminotransModerateValueFemale(), self.getAspartateAminotransHighValueFemale()]
            if self.getAspartateAminotransValue() <= float(self.getAspartateAminotransLowValueFemale().split("-")[1]):
                self.aspartate_aminotrans_output["risk"] = Low
            if self.getAspartateAminotransValue() >= float(self.getAspartateAminotransFairValueFemale().split("-")[0]) and self.getAspartateAminotransValue() <= float(self.getAspartateAminotransFairValueFemale().split("-")[1]):
                self.aspartate_aminotrans_output["risk"] = Fair
            if self.getAspartateAminotransValue() >= float(self.getAspartateAminotransModerateValueFemale().split("-")[0]) and self.getAspartateAminotransValue() <= float(self.getAspartateAminotransModerateValueFemale().split("-")[1]):
                self.aspartate_aminotrans_output["risk"] = Moderate
            if self.getAspartateAminotransValue() > float(self.getAspartateAminotransHighValueFemale()):
                self.aspartate_aminotrans_output["risk"] = High
            if self.getAspartateAminotransValue() == None:
                self.aspartate_aminotrans_output["risk"] = n_a
            self.parsed_output["aspartate_aminotransferase"] = self.aspartate_aminotrans_output

            self.gamma_glutamyl_trans_output["low_fair_moderate_high"] = [self.getGammaGlutamylTransLowValueFemale(), self.getGammaGlutamylTransFairValueFemale(), self.getGammaGlutamylTransModerateValueFemale(), self.getGammaGlutamylTransHighValueFemale()]
            if self.getGammaGlutamylTransValue() <= float(self.getGammaGlutamylTransLowValueFemale().split("-")[1]):
                self.gamma_glutamyl_trans_output["risk"] = Low
            if self.getGammaGlutamylTransValue() >= float(self.getGammaGlutamylTransFairValueFemale().split("-")[0]) and self.getGammaGlutamylTransValue() <= float(self.getGammaGlutamylTransFairValueFemale().split("-")[1]):
                self.gamma_glutamyl_trans_output["risk"] = Fair
            if self.getGammaGlutamylTransValue() >= float(self.getGammaGlutamylTransModerateValueFemale().split("-")[0]) and self.getGammaGlutamylTransValue() <= float(self.getGammaGlutamylTransModerateValueFemale().split("-")[1]):
                self.gamma_glutamyl_trans_output["risk"] = Moderate
            if self.getGammaGlutamylTransValue() > float(self.getGammaGlutamylTransHighValueFemale()): 
                self.gamma_glutamyl_trans_output["risk"] = High
            if self.getGammaGlutamylTransValue() == None:
                self.gamma_glutamyl_trans_output["risk"] = n_a
            self.parsed_output["gamma_glutamyl_transferase"] = self.gamma_glutamyl_trans_output

            self.alkaline_phosphatase_output["low_fair_moderate_high"] = [self.getAlkalinePhosphataseLowValueFemale(), self.getAlkalinePhosphataseFairValueFemale(), self.getAlkalinePhosphataseModerateValueFemale(), self.getAlkalinePhosphataseHighValueFemale()]
            if self.getAlkalinePhosphataseValue() <= float(self.getAlkalinePhosphataseLowValueFemale().split("-")[1]):
                self.alkaline_phosphatase_output["risk"] = Low
            if self.getAlkalinePhosphataseValue() >= float(self.getAlkalinePhosphataseFairValueFemale().split("-")[0]) and self.getAlkalinePhosphataseValue() <= float(self.getAlkalinePhosphataseFairValueFemale().split("-")[1]):
                self.alkaline_phosphatase_output["risk"] = Fair
            if self.getAlkalinePhosphataseValue() >= float(self.getAlkalinePhosphataseModerateValueFemale().split("-")[0]) and self.getAlkalinePhosphataseValue() <= float(self.getAlkalinePhosphataseModerateValueFemale().split("-")[1]):
                self.alkaline_phosphatase_output["risk"] = Moderate
            if self.getAlkalinePhosphataseValue() > float(self.getAlkalinePhosphataseHighValueFemale()):
                self.alkaline_phosphatase_output["risk"] = High
            if self.getAlkalinePhosphataseValue() == None:
                self.alkaline_phosphatase_output["risk"] = n_a
            self.parsed_output["alkaline_phosphatase"] = self.alkaline_phosphatase_output

            self.alanine_transaminase_output["low_fair_moderate_high"] = [self.getAlanineTransaminaseLowValueFemale(), self.getAlanineTransaminaseFairValueFemale(), self.getAlanineTransaminaseModerateValueFemale(), self.getAlanineTransaminaseHighValueFemale()]
            if self.getAlanineTransaminaseValue() <= float(self.getAlanineTransaminaseLowValueFemale().split("-")[1]):
                self.alanine_transaminase_output["risk"] = Low
            if self.getAlanineTransaminaseValue() >= float(self.getAlanineTransaminaseFairValueFemale().split("-")[0]) and self.getAlanineTransaminaseValue() <= float(self.getAlanineTransaminaseFairValueFemale().split("-")[1]):
                self.alanine_transaminase_output["risk"] = Fair
            if self.getAlanineTransaminaseValue() >= float(self.getAlanineTransaminaseModerateValueFemale().split("-")[0]) and self.getAlanineTransaminaseValue() <= float(self.getAlanineTransaminaseModerateValueFemale().split("-")[1]):
                self.alanine_transaminase_output["risk"] = Moderate
            if self.getAlanineTransaminaseValue() > float(self.getAlanineTransaminaseHighValueFemale()):
                self.alanine_transaminase_output["risk"] = High
            if self.getAlanineTransaminaseValue() == None:
                self.alanine_transaminase_output["risk"] = n_a
            self.parsed_output["alanine_transaminase"] = self.alanine_transaminase_output
        else:
            self.bilirubin_total_output["low_fair_moderate_high"] = [self.getBilirubinTotalLowValueMale(), self.getBilirubinTotalFairValueMale(), self.getBilirubinTotalModerateValueMale(), self.getBilirubinTotalHighValueMale()]
            if self.getBilirubinTotalValue() <= float(self.getBilirubinTotalLowValueMale().split("-")[1]):
                self.bilirubin_total_output["risk"] = Low
            if self.getBilirubinTotalValue() >= float(self.getBilirubinTotalFairValueMale().split("-")[0]) and self.getBilirubinTotalValue() <= float(self.getBilirubinTotalFairValueMale().split("-")[1]):
                self.bilirubin_total_output["risk"] = Fair
            if self.getBilirubinTotalValue() >= float(self.getBilirubinTotalModerateValueMale().split("-")[0]) and self.getBilirubinTotalValue() <= float(self.getBilirubinTotalModerateValueMale().split("-")[1]):
                self.bilirubin_total_output["risk"] = Moderate
            if self.getBilirubinTotalValue() > float(self.getBilirubinTotalHighValueMale()):
                self.bilirubin_total_output["risk"] = High
            if self.getBilirubinTotalValue() == None:
                self.bilirubin_total_output["risk"] = n_a
            self.parsed_output["bilirubin_total"] = self.bilirubin_total_output
                
            self.bilirubin_direct_output["low_fair_moderate_high"] = [self.getBilirubinDirectLowValueMale(), self.getBilirubinDirectFairValueMale(), self.getBilirubinDirectModerateValueMale(), self.getBilirubinDirectHighValueMale()]
            if self.getBilirubinDirectValue() <= float(self.getBilirubinDirectLowValueMale().split("-")[1]):  
                self.bilirubin_direct_output["risk"] = Low
            if self.getBilirubinDirectValue() >= float(self.getBilirubinDirectFairValueMale().split("-")[0]) and self.getBilirubinDirectValue() <= float(self.getBilirubinDirectFairValueMale().split("-")[1]): 
                self.bilirubin_direct_output["risk"] = Fair
            if self.getBilirubinDirectValue() >= float(self.getBilirubinDirectModerateValueMale().split("-")[0]) and self.getBilirubinDirectValue() <= float(self.getBilirubinDirectModerateValueMale().split("-")[1]): 
                self.bilirubin_direct_output["risk"] = Moderate
            if self.getBilirubinDirectValue() > float(self.getBilirubinDirectHighValueMale()): 
                self.bilirubin_direct_output["risk"] = High
            if self.getBilirubinDirectValue() == None:
                self.bilirubin_direct_output["risk"] = n_a
            self.parsed_output["bilirubin_direct"] = self.bilirubin_direct_output

            self.bilirubin_indirect_output["low_fair_moderate_high"] = [self.getBilirubinIndirectLowValueMale(), self.getBilirubinIndirectFairValueMale(), self.getBilirubinIndirectModerateValueMale(), self.getBilirubinIndirectHighValueMale()]
            if self.getBilirubinIndirectValue() <= float(self.getBilirubinIndirectLowValueMale().split("-")[1]):  
                self.bilirubin_indirect_output["risk"] = Low
            if self.getBilirubinIndirectValue() >= float(self.getBilirubinIndirectFairValueMale().split("-")[0]) and self.getBilirubinIndirectValue() <= float(self.getBilirubinIndirectFairValueMale().split("-")[1]): 
                self.bilirubin_indirect_output["risk"] = Fair
            if self.getBilirubinIndirectValue() >= float(self.getBilirubinIndirectModerateValueMale().split("-")[0]) and self.getBilirubinIndirectValue() <= float(self.getBilirubinIndirectModerateValueMale().split("-")[1]): 
                self.bilirubin_indirect_output["risk"] = Moderate
            if self.getBilirubinIndirectValue() > float(self.getBilirubinIndirectHighValueMale()): 
                self.bilirubin_indirect_output["risk"] = High
            if self.getBilirubinIndirectValue() == None:
                self.bilirubin_indirect_output["risk"] = n_a
            self.parsed_output["bilirubin_indirect"] = self.bilirubin_indirect_output

            self.total_protein_output["low_fair_moderate_high"] = [self.getTotalProteinLowValueMale(), self.getTotalProteinFairValueMale(), self.getTotalProteinModerateValueMale(), self.getTotalProteinHighValueMale()]
            if self.getTotalProteinValue() <= float(self.getTotalProteinLowValueMale().split("-")[1]):
                self.total_protein_output["risk"] = Low
            if self.getTotalProteinValue() >= float(self.getTotalProteinFairValueMale().split("-")[0]) and self.getTotalProteinValue() <= float(self.getTotalProteinFairValueMale().split("-")[1]):
                self.total_protein_output["risk"] = Fair
            if self.getTotalProteinValue() >= float(self.getTotalProteinModerateValueMale().split("-")[0]) and self.getTotalProteinValue() <= float(self.getTotalProteinModerateValueMale().split("-")[1]):
                self.total_protein_output["risk"] = Moderate
            if self.getTotalProteinValue() > float(self.getTotalProteinHighValueMale()):
                self.total_protein_output["risk"] = High
            if self.getTotalProteinValue() == None:
                self.total_protein_output["risk"] = n_a
            self.parsed_output["total_protein"] = self.total_protein_output

            self.albumin_output["low_fair_moderate_high"] = [self.getAlbuminLowValueMale(), self.getAlbuminFairValueMale(), self.getAlbuminModerateValueMale(), self.getAlbuminHighValueMale()]
            if self.getAlbuminValue() <= float(self.getAlbuminLowValueMale().split("-")[1]):
                self.albumin_output["risk"] = Low
            if self.getAlbuminValue() >= float(self.getAlbuminFairValueMale().split("-")[0]) and self.getAlbuminValue() <= float(self.getAlbuminFairValueMale().split("-")[1]):
                self.albumin_output["risk"] = Fair
            if self.getAlbuminValue() >= float(self.getAlbuminModerateValueMale().split("-")[0]) and self.getAlbuminValue() <= float(self.getAlbuminModerateValueMale().split("-")[1]):
                self.albumin_output["risk"] = Moderate
            if self.getAlbuminValue() > float(self.getAlbuminHighValueMale()):
                self.albumin_output["risk"] = High
            if self.getAlbuminValue() == None:
                self.albumin_output["risk"] = n_a
            self.parsed_output["albumin"] = self.albumin_output

            self.globulin_output["low_fair_moderate_high"] = [self.getGlobulinLowValueMale(), self.getGlobulinFairValueMale(), self.getGlobulinModerateValueMale(), self.getGlobulinHighValueMale()]
            if self.getGlobulinValue() <= float(self.getGlobulinLowValueMale().split("-")[1]):
                self.globulin_output["risk"] = Low
            if self.getGlobulinValue() >= float(self.getGlobulinFairValueMale().split("-")[0]) and self.getGlobulinValue() <= float(self.getGlobulinFairValueMale().split("-")[1]):
                self.globulin_output["risk"] = Fair
            if self.getGlobulinValue() >= float(self.getGlobulinModerateValueMale().split("-")[0]) and self.getGlobulinValue() <= float(self.getGlobulinModerateValueMale().split("-")[1]):
                self.globulin_output["risk"] = Moderate
            if self.getGlobulinValue() > float(self.getGlobulinHighValueMale()):
                self.globulin_output["risk"] = High
            if self.getGlobulinValue() == None:
                self.globulin_output["risk"] = n_a
            self.parsed_output["globulin"] = self.globulin_output
    
            self.album_glob_ratio_output["low_fair_moderate_high"] = [self.getAlbumGlobRatioLowValueMale(), self.getAlbumGlobRatioFairValueMale(), self.getAlbumGlobRatioModerateValueMale(), self.getAlbumGlobRatioHighValueMale()]
            if self.getAlbumGlobRatioValue() <= float(self.getAlbumGlobRatioLowValueMale().split("-")[1]):  
                self.album_glob_ratio_output["risk"] = Low
            if self.getAlbumGlobRatioValue() >= float(self.getAlbumGlobRatioFairValueMale().split("-")[0]) and self.getAlbumGlobRatioValue() <= float(self.getAlbumGlobRatioFairValueMale().split("-")[1]): 
                self.album_glob_ratio_output["risk"] = Fair
            if self.getAlbumGlobRatioValue() >= float(self.getAlbumGlobRatioModerateValueMale().split("-")[0]) and self.getAlbumGlobRatioValue() <= float(self.getAlbumGlobRatioModerateValueMale().split("-")[1]): 
                self.album_glob_ratio_output["risk"] = Moderate
            if self.getAlbumGlobRatioValue() > float(self.getAlbumGlobRatioHighValueMale()): 
                self.album_glob_ratio_output["risk"] = High
            if self.getAlbumGlobRatioValue() == None:
                self.album_glob_ratio_output["risk"] = n_a
            self.parsed_output["albumin_globulin_ratio"] = self.album_glob_ratio_output

            self.aspartate_aminotrans_output["low_fair_moderate_high"] = [self.getAspartateAminotransLowValueMale(), self.getAspartateAminotransFairValueMale(), self.getAspartateAminotransModerateValueMale(), self.getAspartateAminotransHighValueMale()]
            if self.getAspartateAminotransValue() <= float(self.getAspartateAminotransLowValueMale().split("-")[1]):
                self.aspartate_aminotrans_output["risk"] = Low
            if self.getAspartateAminotransValue() >= float(self.getAspartateAminotransFairValueMale().split("-")[0]) and self.getAspartateAminotransValue() <= float(self.getAspartateAminotransFairValueMale().split("-")[1]):
                self.aspartate_aminotrans_output["risk"] = Fair
            if self.getAspartateAminotransValue() >= float(self.getAspartateAminotransModerateValueMale().split("-")[0]) and self.getAspartateAminotransValue() <= float(self.getAspartateAminotransModerateValueMale().split("-")[1]):
                self.aspartate_aminotrans_output["risk"] = Moderate
            if self.getAspartateAminotransValue() > float(self.getAspartateAminotransHighValueMale()):
                self.aspartate_aminotrans_output["risk"] = High
            if self.getAspartateAminotransValue() == None:
                self.aspartate_aminotrans_output["risk"] = n_a
            self.parsed_output["aspartate_aminotransferase"] = self.aspartate_aminotrans_output

            self.gamma_glutamyl_trans_output["low_fair_moderate_high"] = [self.getGammaGlutamylTransLowValueMale(), self.getGammaGlutamylTransFairValueMale(), self.getGammaGlutamylTransModerateValueMale(), self.getGammaGlutamylTransHighValueMale()]
            if self.getGammaGlutamylTransValue() <= float(self.getGammaGlutamylTransLowValueMale().split("-")[1]):
                self.gamma_glutamyl_trans_output["risk"] = Low
            if self.getGammaGlutamylTransValue() >= float(self.getGammaGlutamylTransFairValueMale().split("-")[0]) and self.getGammaGlutamylTransValue() <= float(self.getGammaGlutamylTransFairValueMale().split("-")[1]):
                self.gamma_glutamyl_trans_output["risk"] = Fair
            if self.getGammaGlutamylTransValue() >= float(self.getGammaGlutamylTransModerateValueMale().split("-")[0]) and self.getGammaGlutamylTransValue() <= float(self.getGammaGlutamylTransModerateValueMale().split("-")[1]):
                self.gamma_glutamyl_trans_output["risk"] = Moderate
            if self.getGammaGlutamylTransValue() > float(self.getGammaGlutamylTransHighValueMale()): 
                self.gamma_glutamyl_trans_output["risk"] = High
            if self.getGammaGlutamylTransValue() == None:
                self.gamma_glutamyl_trans_output["risk"] = n_a
            self.parsed_output["gamma_glutamyl_transferase"] = self.gamma_glutamyl_trans_output


            self.alkaline_phosphatase_output["low_fair_moderate_high"] = [self.getAlkalinePhosphataseLowValueMale(), self.getAlkalinePhosphataseFairValueMale(), self.getAlkalinePhosphataseModerateValueMale(), self.getAlkalinePhosphataseHighValueMale()]
            if self.getAlkalinePhosphataseValue() <= float(self.getAlkalinePhosphataseLowValueMale().split("-")[1]):
                self.alkaline_phosphatase_output["risk"] = Low
            if self.getAlkalinePhosphataseValue() >= float(self.getAlkalinePhosphataseFairValueMale().split("-")[0]) and self.getAlkalinePhosphataseValue() <= float(self.getAlkalinePhosphataseFairValueMale().split("-")[1]):
                self.alkaline_phosphatase_output["risk"] = Fair
            if self.getAlkalinePhosphataseValue() >= float(self.getAlkalinePhosphataseModerateValueMale().split("-")[0]) and self.getAlkalinePhosphataseValue() <= float(self.getAlkalinePhosphataseModerateValueMale().split("-")[1]):
                self.alkaline_phosphatase_output["risk"] = Moderate
            if self.getAlkalinePhosphataseValue() > float(self.getAlkalinePhosphataseHighValueMale()):
                self.alkaline_phosphatase_output["risk"] = High
            if self.getAlkalinePhosphataseValue() == None:
                self.alkaline_phosphatase_output["risk"] = n_a
            self.parsed_output["alkaline_phosphatase"] = self.alkaline_phosphatase_output

            self.alanine_transaminase_output["low_fair_moderate_high"] = [self.getAlanineTransaminaseLowValueMale(), self.getAlanineTransaminaseFairValueMale(), self.getAlanineTransaminaseModerateValueMale(), self.getAlanineTransaminaseHighValueMale()]
            if self.getAlanineTransaminaseValue() <= float(self.getAlanineTransaminaseLowValueMale().split("-")[1]):
                self.alanine_transaminase_output["risk"] = Low
            if self.getAlanineTransaminaseValue() >= float(self.getAlanineTransaminaseFairValueMale().split("-")[0]) and self.getAlanineTransaminaseValue() <= float(self.getAlanineTransaminaseFairValueMale().split("-")[1]):
                self.alanine_transaminase_output["risk"] = Fair
            if self.getAlanineTransaminaseValue() >= float(self.getAlanineTransaminaseModerateValueMale().split("-")[0]) and self.getAlanineTransaminaseValue() <= float(self.getAlanineTransaminaseModerateValueMale().split("-")[1]):
                self.alanine_transaminase_output["risk"] = Moderate
            if self.getAlanineTransaminaseValue() > float(self.getAlanineTransaminaseHighValueMale()):
                self.alanine_transaminase_output["risk"] = High
            if self.getAlanineTransaminaseValue() == None:
                self.alanine_transaminase_output["risk"] = n_a
            self.parsed_output["alanine_transaminase"] = self.alanine_transaminase_output
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
	
    # Function sets bilirubin total actual value
    def setBilirubinTotalValue(self, bilirubin_total): 
        self.bilirubin_total = bilirubin_total

    # Function sets unit of Glucose Fasting
    def setBilirubinTotalUnit(self):
        self.bilirubin_total_unit = self.parameters[0].get('value_meta_data',[])[0].get('unit',"")

    # Function sets list of medical annotations for bilirubin total
    def setBilirubinTotalMedicalAnotation(self):
        self.bilirubin_total_medical_annot =  self.parameters[0].get('medical_annotation',[])

    # Function sets range of values for bilirubin total for male  
    def setBilirubinTotalRangeMale(self):
        self.bilirubin_total_range_male =  self.parameters[0].get('value_meta_data',[])[0].get('range',"")
 
    # Function sets range of values for bilirubin total for female  
    def setBilirubinTotalRangeFemale(self):
        self.bilirubin_total_range_female =  self.parameters[0].get('value_meta_data',[])[1].get('range',"")

    # Function sets low risk values range for bilirubin total
    def setBilirubinTotalLowValueMale(self):
        self.bilirubin_total_low_male =  self.parameters[0].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for bilirubin total
    def setBilirubinTotalFairValueMale(self):
        self.bilirubin_total_fair_male = self.parameters[0].get('value_meta_data',[])[0].get('fair_value',"")

    # Function sets moderate risk values range for bilirubin total
    def setBilirubinTotalModerateValueMale(self):
        self.bilirubin_total_moderate_male =  self.parameters[0].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for bilirubin total
    def setBilirubinTotalHighValueMale(self):
        self.bilirubin_total_high_male =  self.parameters[0].get('value_meta_data',[])[0].get('high_value',"")[1:]

    # Function sets low risk values range for bilirubin total
    def setBilirubinTotalLowValueFemale(self):
        self.bilirubin_total_low_female =  self.parameters[0].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for bilirubin total
    def setBilirubinTotalFairValueFemale(self):
        self.bilirubin_total_fair_female = self.parameters[0].get('value_meta_data',[])[1].get('fair_value',"")

    # Function sets moderate risk values range for bilirubin total
    def setBilirubinTotalModerateValueFemale(self):
        self.bilirubin_total_moderate_female = self.parameters[0].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for bilirubin total
    def setBilirubinTotalHighValueFemale(self):
        self.bilirubin_total_high_female =  self.parameters[0].get('value_meta_data',[])[1].get('high_value',"")[1:]

    # Function sets function name to parse bilirubin total value from medical reports
    def setBilirubinTotalFunction(self):
        self.bilirubin_total_function =  self.parameters[0].get("value_function",{}).get("function_name","")
 
    # Function sets bilirubin direct actual value
    def setBilirubinDirectValue(self, bilirubin_direct): 
        self.bilirubin_direct = bilirubin_direct

    # Function sets unit of bilirubin direct
    def setBilirubinDirectUnit(self):
        self.bilirubin_direct_unit = self.parameters[1].get('value_meta_data',[])[0].get('unit',"")

    # Function sets list of medical annotations for bilirubin direct
    def setBilirubinDirectMedicalAnotation(self):
        self.bilirubin_direct_medical_annot =  self.parameters[1].get('medical_annotation',[])

    # Function sets range of values for bilirubin direct for male  
    def setBilirubinDirectRangeMale(self):
        self.bilirubin_direct_range_male =  self.parameters[1].get('value_meta_data',[])[0].get('range',"")
 
    # Function sets range of values for bilirubin direct for female  
    def setBilirubinDirectRangeFemale(self):
        self.bilirubin_direct_range_female =  self.parameters[1].get('value_meta_data',[])[1].get('range',"")

    # Function sets low risk values range for bilirubin direct
    def setBilirubinDirectLowValueMale(self):
        self.bilirubin_direct_low_male =  self.parameters[1].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for bilirubin direct
    def setBilirubinDirectFairValueMale(self):
        self.bilirubin_direct_fair_male = self.parameters[1].get('value_meta_data',[])[0].get('fair_value',"")

    # Function sets moderate risk values range for bilirubin direct
    def setBilirubinDirectModerateValueMale(self):
        self.bilirubin_direct_moderate_male =  self.parameters[1].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for bilirubin direct
    def setBilirubinDirectHighValueMale(self):
        self.bilirubin_direct_high_male =  self.parameters[1].get('value_meta_data',[])[0].get('high_value',"")[1:]

    # Function sets low risk values range for bilirubin direct
    def setBilirubinDirectLowValueFemale(self):
        self.bilirubin_direct_low_female =  self.parameters[1].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for bilirubin direct
    def setBilirubinDirectFairValueFemale(self):
        self.bilirubin_direct_fair_female = self.parameters[1].get('value_meta_data',[])[1].get('fair_value',"")

    # Function sets moderate risk values range for bilirubin direct
    def setBilirubinDirectModerateValueFemale(self):
        self.bilirubin_direct_moderate_female =  self.parameters[1].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for bilirubin direct
    def setBilirubinDirectHighValueFemale(self):
        self.bilirubin_direct_high_female =  self.parameters[1].get('value_meta_data',[])[1].get('high_value',"")[1:]


    # Function sets function name to parse bilirubin direct value from medical reports
    def setBilirubinDirectFunction(self):
        self.bilirubin_direct_function =  self.parameters[1].get("value_function",{}).get("function_name","")

    # Function sets bilirubin direct actual value
    def setBilirubinIndirectValue(self, bilirubin_indirect): 
        self.bilirubin_indirect = bilirubin_indirect

    # Function sets unit of bilirubin indirect
    def setBilirubinIndirectUnit(self):
        self.bilirubin_indirect_unit = self.parameters[2].get('value_meta_data',[])[0].get('unit',"")

    # Function sets list of medical annotations for bilirubin indirect
    def setBilirubinIndirectMedicalAnotation(self):
        self.bilirubin_indirect_medical_annot =  self.parameters[2].get('medical_annotation',[])

    # Function sets range of values for bilirubin indirect for male  
    def setBilirubinIndirectRangeMale(self):
        self.bilirubin_indirect_range_male =  self.parameters[2].get('value_meta_data',[])[0].get('range',"")
 
    # Function sets range of values for bilirubin indirect for female  
    def setBilirubinIndirectRangeFemale(self):
        self.bilirubin_indirect_range_female =  self.parameters[2].get('value_meta_data',[])[1].get('range',"")

    # Function sets low risk values range for bilirubin indirect
    def setBilirubinIndirectLowValueMale(self):
        self.bilirubin_indirect_low_male =  self.parameters[2].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for bilirubin indirect
    def setBilirubinIndirectFairValueMale(self):
        self.bilirubin_indirect_fair_male = self.parameters[2].get('value_meta_data',[])[0].get('fair_value',"")

    # Function sets moderate risk values range for bilirubin indirect
    def setBilirubinIndirectModerateValueMale(self):
        self.bilirubin_indirect_moderate_male = self.parameters[2].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for bilirubin indirect
    def setBilirubinIndirectHighValueMale(self):
        self.bilirubin_indirect_high_male = self.parameters[2].get('value_meta_data',[])[0].get('high_value',"")[1:]

    # Function sets low risk values range for bilirubin indirect
    def setBilirubinIndirectLowValueFemale(self):
        self.bilirubin_indirect_low_female =  self.parameters[2].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for bilirubin indirect
    def setBilirubinIndirectFairValueFemale(self):
        self.bilirubin_indirect_fair_female = self.parameters[2].get('value_meta_data',[])[1].get('fair_value',"")

    # Function sets moderate risk values range for bilirubin indirect
    def setBilirubinIndirectModerateValueFemale(self):
        self.bilirubin_indirect_moderate_female = self.parameters[2].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for bilirubin indirect
    def setBilirubinIndirectHighValueFemale(self):
        self.bilirubin_indirect_high_female = self.parameters[2].get('value_meta_data',[])[1].get('high_value',"")[1:]

    # Function sets function name to parse bilirubin indirect value from medical reports
    def setBilirubinIndirectFunction(self):
        self.bilirubin_indirect_function =  self.parameters[2].get("value_function",{}).get("function_name","")

    # Function sets total protein actual value
    def setTotalProteinValue(self, tot_protein):
        self.total_protein  = tot_protein
    
    # Function sets list of medical annottions for total protein
    def setTotalProteinMedicalAnnotations(self):
        self.total_protein_medical_annot = self.parameters[3].get('medical_annotation',[])

    # Function sets unit of total protein
    def setTotalProteinUnit(self):
        self.total_protein_unit = self.parameters[3].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for total protein for male
    def setTotalProteinRangeMale(self):
        self.total_protein_range_male = self.parameters[3].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for total protein for female
    def setTotalProteinRangeFemale(self):
        self.total_protein_range_female = self.parameters[3].get('value_meta_data',[])[1].get('range',"") 
    
    # Function sets low risk values range for total protein
    def setTotalProteinLowValueMale(self):
        self.total_protein_low_male = self.parameters[3].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for total protein
    def setTotalProteinFairValueMale(self):
        self.total_protein_fair_male = self.parameters[3].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function sets moderate risk values range for total protein
    def setTotalProteinModerateValueMale(self):
        self.total_protein_moderate_male = self.parameters[3].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for total protein
    def setTotalProteinHighValueMale(self):
        self.total_protein_high_male = self.parameters[3].get('value_meta_data',[])[0].get('high_value',"")[1:]
   
    # Function sets low risk values range for total protein
    def setTotalProteinLowValueFemale(self):
        self.total_protein_low_female = self.parameters[3].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for total protein
    def setTotalProteinFairValueFemale(self):
        self.total_protein_fair_female = self.parameters[3].get('value_meta_data',[])[1].get('fair_value',"")

    # Function sets moderate risk values range for total protein
    def setTotalProteinModerateValueFemale(self):
        self.total_protein_moderate_female = self.parameters[3].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for total protein
    def setTotalProteinHighValueFemale(self):
        self.total_protein_high_female = self.parameters[3].get('value_meta_data',[])[1].get('high_value',"")[1:]

 
    # Function sets function name for parsing total protein value from medical reports
    def setTotalProteinFunction(self):
        self.total_protein_func = self.parameters[3].get("value_function",{}).get("function_name","")

    # Function sets albumin actual value
    def setAlbuminValue(self, albumin):
        self.albumin = albumin
    
    # Function sets list of medical annottions for albumin
    def setAlbuminMedicalAnnotations(self):
        self.albumin_medical_annot =  self.parameters[4].get('medical_annotation',[])

    # Function sets unit of albumin
    def setAlbuminUnit(self):
        self.albumin_unit = self.parameters[4].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for albumin for male
    def setAlbuminRangeMale(self):
        self.albumin_range_female = self.parameters[4].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for albumin for female
    def setAlbuminRangeFemale(self):
        self.albumin_range_male = self.parameters[4].get('value_meta_data',[])[1].get('range',"") 
    
    # Function sets low risk values range for albumin
    def setAlbuminLowValueMale(self):
        self.albumin_low_male = self.parameters[4].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for albumin
    def setAlbuminFairValueMale(self):
        self.albumin_fair_male = self.parameters[4].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function sets moderate risk values range for albumin
    def setAlbuminModerateValueMale(self):
        self.albumin_moderate_male = self.parameters[4].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for albumin
    def setAlbuminHighValueMale(self):
        self.albumin_high_male = self.parameters[4].get('value_meta_data',[])[0].get('high_value',"")[1:]
    
    # Function sets low risk values range for albumin
    def setAlbuminLowValueFemale(self):
        self.albumin_low_female = self.parameters[4].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for albumin
    def setAlbuminFairValueFemale(self):
        self.albumin_fair_female = self.parameters[4].get('value_meta_data',[])[1].get('fair_value',"")
    
    # Function sets moderate risk values range for albumin
    def setAlbuminModerateValueFemale(self):
        self.albumin_moderate_female = self.parameters[4].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for albumin
    def setAlbuminHighValueFemale(self):
        self.albumin_high_female = self.parameters[4].get('value_meta_data',[])[1].get('high_value',"")[1:]

    # Function sets function name for parsing albumin value from medical reports
    def setAlbuminFunction(self):
        self.albumin_func = self.parameters[4].get("value_function",{}).get("function_name","")

    # Function sets albumin actual value
    def setGlobulinValue(self, globulin):
        self.globulin = globulin
    
    # Function sets list of medical annottions for albumin
    def setGlobulinMedicalAnnotations(self):
        self.globulin_medical_annot = self.parameters[5].get('medical_annotation',[])

    # Function sets unit of globulin
    def setGlobulinUnit(self):
        self.globulin_unit = self.parameters[5].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for globulin for male
    def setGlobulinRangeMale(self):
        self.globulin_range_male = self.parameters[5].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for globulin for female
    def setGlobulinRangeFemale(self):
        self.globulin_range_female = self.parameters[5].get('value_meta_data',[])[1].get('range',"") 
    
    # Function sets low risk values range for globulin
    def setGlobulinLowValueMale(self):
        self.globulin_low_male = self.parameters[5].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for globulin
    def setGlobulinFairValueMale(self):
        self.globulin_fair_male = self.parameters[5].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function sets moderate risk values range for globulin
    def setGlobulinModerateValueMale(self):
        self.globulin_moderate_male = self.parameters[5].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for globulin
    def setGlobulinHighValueMale(self):
        self.globulin_high_male = self.parameters[5].get('value_meta_data',[])[0].get('high_value',"")[1:]
   
    # Function sets low risk values range for globulin
    def setGlobulinLowValueFemale(self):
        self.globulin_low_female = self.parameters[5].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for globulin
    def setGlobulinFairValueFemale(self):
        self.globulin_fair_female = self.parameters[5].get('value_meta_data',[])[1].get('fair_value',"")

    # Function sets moderate risk values range for globulin
    def setGlobulinModerateValueFemale(self):
        self.globulin_moderate_female = self.parameters[5].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for globulin
    def setGlobulinHighValueFemale(self):
        self.globulin_high_female = self.parameters[5].get('value_meta_data',[])[1].get('high_value',"")[1:]

 
    # Function sets function name for parsing globulin value from medical reports
    def setGlobulinFunction(self):
        self.globulin_func = self.parameters[5].get("value_function",{}).get("function_name","")

    # Function sets album_glob_ratio
    def setAlbumGlobRatioValue(self, album_glob_ratio):
        self.album_glob_ratioinine = album_glob_ratio
 
    # Function sets list of medical annotations for album_glob_ratio
    def setAlbumGlobRatioMedicalAnnotations(self):
        self.album_glob_ratio_medical_annot =  self.parameters[6].get('medical_annotation',[])

    # Function sets unit of album_glob_ratio
    def setAlbumGlobRatioUnit(self):
        self.album_glob_ratio_unit =  self.parameters[6].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for album_glob_ratio for male
    def setAlbumGlobRatioRangeMale(self):
        self.album_glob_ratio_range_male =  self.parameters[6].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for album_glob_ratio for female
    def setAlbumGlobRatioRangeFemale(self):
        self.album_glob_ratio_range_female =  self.parameters[6].get('value_meta_data',[])[1].get('range',"") 

    # Function sets low risk values range for album_glob_ratio
    def setAlbumGlobRatioLowValueMale(self):
        self.album_glob_ratio_low_male = self.parameters[6].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for album_glob_ratio
    def setAlbumGlobRatioFairValueMale(self):
        self.album_glob_ratio_fair_male = self.parameters[6].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function retuns moderate risk value ranges for album_glob_ratio
    def setAlbumGlobRatioModerateValueMale(self):
        self.album_glob_ratio_moderate_male = self.parameters[6].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk value ranges for album_glob_ratio
    def setAlbumGlobRatioHighValueMale(self):
        self.album_glob_ratio_high_male =  self.parameters[6].get('value_meta_data',[])[0].get('high_value',"")[1:]

    # Function sets low risk values range for album_glob_ratio
    def setAlbumGlobRatioLowValueFemale(self):
        self.album_glob_ratio_low_female = self.parameters[6].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for album_glob_ratio
    def setAlbumGlobRatioFairValueFemale(self):
        self.album_glob_ratio_fair_female = self.parameters[6].get('value_meta_data',[])[1].get('fair_value',"")

    # Function retuns moderate risk value ranges for album_glob_ratio
    def setAlbumGlobRatioModerateValueFemale(self):
        self.album_glob_ratio_moderate_female = self.parameters[6].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk value ranges for album_glob_ratio
    def setAlbumGlobRatioHighValueFemale(self):
        self.album_glob_ratio_high_female = self.parameters[6].get('value_meta_data',[])[1].get('high_value',"")[1:]

    # Function sets function name to parse album_glob_ratio value from medical report
    def setAlbumGlobRatiosFunction(self):
        self.album_glob_ratio_func = self.parameters[6].get("value_function",{}).get("function_name","")
   
    # Function sets aspartate aminotransferase actual value
    def setAspartateAminotransValue(self, aspartate_aminotrans):
        self.aspartate_aminotrans = aspartate_aminotrans
           
    # Function sets list of medical annotations for aspartate aminotransferase
    def setAspartateAminotransMedicalAnnotations(self):
        self.aspartate_aminotrans_medical_annot = self.parameters[7].get('medical_annotation',[])

    # Function sets unit of aspartate aminotransferase
    def setAspartateAminotransUnit(self):
        self.aspartate_aminotrans_unit = self.parameters[7].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for aspartate aminotransferase for male
    def setAspartateAminotransRangeMale(self):
        self.aspartate_aminotrans_range_male = self.parameters[7].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for aspartate aminotransferase for female
    def setAspartateAminotransRangeFemale(self):
        self.aspartate_aminotrans_range_female = self.parameters[7].get('value_meta_data',[])[1].get('range',"") 
    
    # Function sets low risk values range for aspartate aminotransferase
    def setAspartateAminotransLowValueMale(self):
        self.aspartate_aminotrans_low_male = self.parameters[7].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for aspartate aminotransferase
    def setAspartateAminotransFairValueMale(self):
        self.aspartate_aminotrans_fair_male = self.parameters[7].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function sets moderate risk values range for aspartate aminotransferase
    def setAspartateAminotransModerateValueMale(self):
        self.aspartate_aminotrans_moderate_male =  self.parameters[7].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for aspartate aminotransferase
    def setAspartateAminotransHighValueMale(self):
        self.aspartate_aminotrans_high_male = self.parameters[7].get('value_meta_data',[])[0].get('high_value',"")[1:]

       # Function sets low risk values range for aspartate aminotransferase
    def setAspartateAminotransLowValueFemale(self):
        self.aspartate_aminotrans_low_female = self.parameters[7].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for aspartate aminotransferase
    def setAspartateAminotransFairValueFemale(self):
        self.aspartate_aminotrans_fair_female = self.parameters[7].get('value_meta_data',[])[1].get('fair_value',"")

    # Function sets moderate risk values range for aspartate aminotransferase
    def setAspartateAminotransModerateValueFemale(self):
        self.aspartate_aminotrans_moderate_female = self.parameters[7].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for aspartate aminotransferase
    def setAspartateAminotransHighValueFemale(self):
        self.aspartate_aminotrans_high_female = self.parameters[7].get('value_meta_data',[])[1].get('high_value',"")[1:]
 
    # Function sets function name for parsing aspartate aminotransferase value from medical reports
    def setAspartateAminotransFunction(self):
        self.aspartate_aminotrans_func =  self.parameters[7].get("value_function",{}).get("function_name","")

    # Function sets gamma glutamyl actual value
    def setGammaGlutamylTransValue(self, gamma_glutamyl_trans):
        self.gamma_glutamyl_trans = gamma_glutamyl_trans
           
    # Function sets list of medical annotations for gamma glutamyl
    def setGammaGlutamylTransMedicalAnnotations(self):
        self.gamma_glutamyl_trans_medical_annot = self.parameters[8].get('medical_annotation',[])

    # Function sets unit of gamma glutamyl
    def setGammaGlutamylTransUnit(self):
        self.gamma_glutamyl_trans_unit = self.parameters[8].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for gamma glutamyl for male
    def setGammaGlutamylTransRangeMale(self):
        self.gamma_glutamyl_trans_range_male = self.parameters[8].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for gamma glutamyl for female
    def setGammaGlutamylTransRangeFemale(self):
        self.gamma_glutamyl_trans_range_female = self.parameters[8].get('value_meta_data',[])[1].get('range',"") 
    
    # Function sets low risk values range for gamma glutamyl
    def setGammaGlutamylTransLowValueMale(self):
        self.gamma_glutamyl_trans_low_male = self.parameters[8].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for gamma glutamyl
    def setGammaGlutamylTransFairValueMale(self):
        self.gamma_glutamyl_trans_fair_male = self.parameters[8].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function sets moderate risk values range for gamma glutamyl
    def setGammaGlutamylTransModerateValueMale(self):
        self.gamma_glutamyl_trans_moderate_male =  self.parameters[8].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for gamma glutamyl
    def setGammaGlutamylTransHighValueMale(self):
        self.gamma_glutamyl_trans_high_male = self.parameters[8].get('value_meta_data',[])[0].get('high_value',"")[1:]

      # Function sets low risk values range for gamma glutamyl
    def setGammaGlutamylTransLowValueFemale(self):
        self.gamma_glutamyl_trans_low_female = self.parameters[8].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for gamma glutamyl
    def setGammaGlutamylTransFairValueFemale(self):
        self.gamma_glutamyl_trans_fair_female = self.parameters[8].get('value_meta_data',[])[1].get('fair_value',"")

    # Function sets moderate risk values range for gamma glutamyl
    def setGammaGlutamylTransModerateValueFemale(self):
        self.gamma_glutamyl_trans_moderate_female =  self.parameters[8].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for gamma glutamyl
    def setGammaGlutamylTransHighValueFemale(self):
        self.gamma_glutamyl_trans_high_female = self.parameters[8].get('value_meta_data',[])[0].get('high_value',"")[1:]
 
    # Function sets function name for parsing gamma glutamyl value from medical reports
    def setGammaGlutamylTransFunction(self):
        self.gamma_glutamyl_trans_func =  self.parameters[8].get("value_function",{}).get("function_name","")

    # Function sets alkaline phosphatase actual value
    def setAlkalinePhosphataseValue(self, alkaline_phosphatase):
        self.alkaline_phosphatase = alkaline_phosphatase
           
    # Function sets list of medical annotations for alkaline phosphatase
    def setAlkalinePhosphataseMedicalAnnotations(self):
        self.alkaline_phosphatase_medical_annot = self.parameters[9].get('medical_annotation',[])

    # Function sets unit of alkaline phosphatase
    def setAlkalinePhosphataseUnit(self):
        self.alkaline_phosphatase_unit = self.parameters[9].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for alkaline phosphatase for male
    def setAlkalinePhosphataseRangeMale(self):
        self.alkaline_phosphatase_range_male = self.parameters[9].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for alkaline phosphatase for female
    def setAlkalinePhosphataseRangeFemale(self):
        self.alkaline_phosphatase_range_female = self.parameters[9].get('value_meta_data',[])[1].get('range',"") 
    
    # Function sets low risk values range for alkaline phosphatase
    def setAlkalinePhosphataseLowValueMale(self):
        self.alkaline_phosphatase_low_male = self.parameters[9].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for alkaline phosphatase
    def setAlkalinePhosphataseFairValueMale(self):
        self.alkaline_phosphatase_fair_male = self.parameters[9].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function sets moderate risk values range for alkaline phosphatase
    def setAlkalinePhosphataseModerateValueMale(self):
        self.alkaline_phosphatase_moderate_male =  self.parameters[9].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for alkaline phosphatase
    def setAlkalinePhosphataseHighValueMale(self):
        self.alkaline_phosphatase_high_male = self.parameters[9].get('value_meta_data',[])[0].get('high_value',"")[1:]
   
    # Function sets low risk values range for alkaline phosphatase
    def setAlkalinePhosphataseLowValueFemale(self):
        self.alkaline_phosphatase_low_female = self.parameters[9].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for alkaline phosphatase
    def setAlkalinePhosphataseFairValueFemale(self):
        self.alkaline_phosphatase_fair_female = self.parameters[9].get('value_meta_data',[])[1].get('fair_value',"")

    # Function sets moderate risk values range for alkaline phosphatase
    def setAlkalinePhosphataseModerateValueFemale(self):
        self.alkaline_phosphatase_moderate_female =  self.parameters[9].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for alkaline phosphatase
    def setAlkalinePhosphataseHighValueFemale(self):
        self.alkaline_phosphatase_high_female = self.parameters[9].get('value_meta_data',[])[1].get('high_value',"")[1:]
 
    # Function sets function name for parsing alkaline phosphatase value from medical reports
    def setAlkalinePhosphataseFunction(self):
        self.alkaline_phosphatase_func =  self.parameters[9].get("value_function",{}).get("function_name","")

    # Function sets alanine transferase actual value
    def setAlanineTransaminaseValue(self, alanine_transaminase):
        self.alanine_transaminase = alanine_transaminase
           
    # Function sets list of medical annotations for alanine transferase
    def setAlanineTransaminaseMedicalAnnotations(self):
        self.alanine_transaminase_medical_annot = self.parameters[10].get('medical_annotation',[])

    # Function sets unit of alanine transferase
    def setAlanineTransaminaseUnit(self):
        self.alanine_transaminase_unit = self.parameters[10].get('value_meta_data',[])[0].get('unit',"") 

    # Function sets range of values for alanine transferase for male
    def setAlanineTransaminaseRangeMale(self):
        self.alanine_transaminase_range_male = self.parameters[10].get('value_meta_data',[])[0].get('range',"") 

    # Function sets range of values for alanine transferase for female
    def setAlanineTransaminaseRangeFemale(self):
        self.alanine_transaminase_range_female = self.parameters[10].get('value_meta_data',[])[1].get('range',"") 
    
    # Function sets low risk values range for alanine transferase
    def setAlanineTransaminaseLowValueMale(self):
        self.alanine_transaminase_low_male = self.parameters[10].get('value_meta_data',[])[0].get('low_value',"")

    # Function sets fair risk values range for alanine transferase
    def setAlanineTransaminaseFairValueMale(self):
        self.alanine_transaminase_fair_male = self.parameters[10].get('value_meta_data',[])[0].get('fair_value',"")
    
    # Function sets moderate risk values range for alanine transferase
    def setAlanineTransaminaseModerateValueMale(self):
        self.alanine_transaminase_moderate_male =  self.parameters[10].get('value_meta_data',[])[0].get('moderate_value',"")

    # Function sets high risk values range for alanine transferase
    def setAlanineTransaminaseHighValueMale(self):
        self.alanine_transaminase_high_male = self.parameters[10].get('value_meta_data',[])[0].get('high_value',"")[1:]
    
    # Function sets low risk values range for alanine transferase
    def setAlanineTransaminaseLowValueFemale(self):
        self.alanine_transaminase_low_female = self.parameters[10].get('value_meta_data',[])[1].get('low_value',"")

    # Function sets fair risk values range for alanine transferase
    def setAlanineTransaminaseFairValueFemale(self):
        self.alanine_transaminase_fair_female = self.parameters[10].get('value_meta_data',[])[1].get('fair_value',"")

    # Function sets moderate risk values range for alanine transferase
    def setAlanineTransaminaseModerateValueFemale(self):
        self.alanine_transaminase_moderate_female =  self.parameters[10].get('value_meta_data',[])[1].get('moderate_value',"")

    # Function sets high risk values range for alanine transferase
    def setAlanineTransaminaseHighValueFemale(self):
        self.alanine_transaminase_high_female = self.parameters[10].get('value_meta_data',[])[1].get('high_value',"")[1:]

    # Function sets function name for parsing alanine transferase value from medical reports
    def setAlanineTransaminaseFunction(self):
        self.alanine_transaminase_func =  self.parameters[10].get("value_function",{}).get("function_name","")



    # Fuction returns category id
    def getCategoryid(self):
        return self.category_id 

    # Function returns category name
    def getCategoryName(self):
        return self.category_name 

    # Function returns Version number
    def getVersionNumber(self):
        return self.version_number 
	
    # Function returns bilirubin total actual value
    def getBilirubinTotalValue(self): 
        return self.bilirubin_total 

    # Function returns unit of bilirubin total
    def getBilirubinTotalUnit(self):
        return self.bilirubin_total_unit 
 
    # Function returns list of medical annotations for bilirubin total
    def getBilirubinTotalMedicalAnotation(self):
        return self.bilirubin_total_medical_annot 

    # Function returns range of values for bilirubin total for male  
    def getBilirubinTotalRangeMale(self):
        return self.bilirubin_total_range_male
 
    # Function returns range of values for bilirubin total for female  
    def getBilirubinTotalRangeFemale(self):
        return self.bilirubin_total_range_female 

    # Function returns low risk values range for bilirubin total
    def getBilirubinTotalLowValueMale(self):
        return self.bilirubin_total_low_male

    # Function returns fair risk values range for bilirubin total
    def getBilirubinTotalFairValueMale(self):
        return self.bilirubin_total_fair_male

    # Function returns moderate risk values range for bilirubin total
    def getBilirubinTotalModerateValueMale(self):
        return self.bilirubin_total_moderate_male

    # Function returns high risk values range for bilirubin total
    def getBilirubinTotalHighValueMale(self):
        return self.bilirubin_total_high_male

   # Function returns low risk values range for bilirubin total
    def getBilirubinTotalLowValueFemale(self):
        return self.bilirubin_total_low_female

    # Function returns fair risk values range for bilirubin total
    def getBilirubinTotalFairValueFemale(self):
        return self.bilirubin_total_fair_female

    # Function returns moderate risk values range for bilirubin total
    def getBilirubinTotalModerateValueFemale(self):
        return self.bilirubin_total_moderate_female

    # Function returns high risk values range for bilirubin total
    def getBilirubinTotalHighValueFemale(self):
        return self.bilirubin_total_high_female

    # Function returns function name to parse bilirubin total value from medical reports
    def getBilirubinTotalFunction(self):
        return self.bilirubin_total_function 

    # Function gets bilirubin direct actual value
    def getBilirubinDirectValue(self): 
        return self.bilirubin_direct

    # Function gets unit of bilirubin direct 
    def getBilirubinDirectUnit(self):
        return self.bilirubin_direct_unit 

    # Function gets list of medical annotations for bilirubin direct
    def getBilirubinDirectMedicalAnotation(self):
        return self.bilirubin_direct_medical_annotation 

    # Function gets range of values for bilirubin direct for male  
    def getBilirubinDirectRangeMale(self):
        return self.bilirubin_direct_range_male 
 
    # Function gets range of values for bilirubin direct for female  
    def getBilirubinDirectRangeFemale(self):
        return self.bilirubin_direct_range_female 

    # Function gets low risk values range for bilirubin direct
    def getBilirubinDirectLowValueMale(self):
        return self.bilirubin_direct_low_male 

    # Function gets fair risk values range for bilirubin direct
    def getBilirubinDirectFairValueMale(self):
        return self.bilirubin_direct_fair_male 

    # Function gets moderate risk values range for bilirubin direct
    def getBilirubinDirectModerateValueMale(self):
        return self.bilirubin_direct_moderate_male 

    # Function gets high risk values range for bilirubin direct
    def getBilirubinDirectHighValueMale(self):
        return self.bilirubin_direct_high_male 

    # Function gets low risk values range for bilirubin direct
    def getBilirubinDirectLowValueFemale(self):
        return self.bilirubin_direct_low_female

    # Function gets fair risk values range for bilirubin direct
    def getBilirubinDirectFairValueFemale(self):
        return self.bilirubin_direct_fair_female

    # Function gets moderate risk values range for bilirubin direct
    def getBilirubinDirectModerateValueFemale(self):
        return self.bilirubin_direct_moderate_female

    # Function gets high risk values range for bilirubin direct
    def getBilirubinDirectHighValueFemale(self):
        return self.bilirubin_direct_high_female

    # Function gets function name to parse bilirubin direct value from medical reports
    def getBilirubinDirectFunction(self):
        return self.bilirubin_direct_function

    # Function gets bilirubin indirect actual value
    def getBilirubinIndirectValue(self): 
        return self.bilirubin_indirect

    # Function gets unit of bilirubin indirect
    def getBilirubinIndirectUnit(self):
        return self.bilirubin_indirect_unit

    # Function gets list of medical annotations for bilirubin indirect
    def getBilirubinIndirectMedicalAnotation(self):
        return self.bilirubin_indirect_medical_annot 

    # Function gets range of values for bilirubin indirect for male  
    def getBilirubinIndirectRangeMale(self):
        return self.bilirubin_indirect_range_male
 
    # Function gets range of values for bilirubin indirect for female  
    def getBilirubinIndirectRangeFemale(self):
        return self.bilirubin_indirect_range_female

    # Function gets low risk values range for bilirubin indirect
    def getBilirubinIndirectLowValueMale(self):
        return self.bilirubin_indirect_low_male

    # Function gets fair risk values range for bilirubin indirect
    def getBilirubinIndirectFairValueMale(self):
        return self.bilirubin_indirect_fair_male

    # Function gets moderate risk values range for bilirubin indirect
    def getBilirubinIndirectModerateValueMale(self):
        return self.bilirubin_indirect_moderate_male

    # Function gets high risk values range for bilirubin indirect
    def getBilirubinIndirectHighValueMale(self):
        return self.bilirubin_indirect_high_male

    # Function gets low risk values range for bilirubin indirect
    def getBilirubinIndirectLowValueFemale(self):
        return self.bilirubin_indirect_low_female

    # Function gets fair risk values range for bilirubin indirect
    def getBilirubinIndirectFairValueFemale(self):
        return self.bilirubin_indirect_fair_female

    # Function gets moderate risk values range for bilirubin indirect
    def getBilirubinIndirectModerateValueFemale(self):
        return self.bilirubin_indirect_moderate_female

    # Function gets high risk values range for bilirubin indirect
    def getBilirubinIndirectHighValueFemale(self):
        return self.bilirubin_indirect_high_female

    # Function gets function name to parse bilirubin indirect value from medical reports
    def getBilirubinIndirectFunction(self):
        return self.bilirubin_indirect_function

    # Function returns album_glob_ratio
    def getAlbumGlobRatioValue(self):
        return self.album_glob_ratioinine
 
    # Function returns list of medical annotations for album_glob_ratio
    def getAlbumGlobRatioMedicalAnnotations(self):
        return self.album_glob_ratio_medical_annot

    # Function returns unit of album_glob_ratioinine
    def getAlbumGlobRatioUnit(self):
        return self.album_glob_ratio_unit

    # Function returns range of values for album_glob_ratio for male
    def getAlbumGlobRatioRangeMale(self):
        return self.album_glob_ratio_range_male

    # Function returns range of values for album_glob_ratio for female
    def getAlbumGlobRatioRangeFemale(self):
        return self.album_glob_ratio_range_female 

    # Function returns low risk values range for album_glob_ratio
    def getAlbumGlobRatioLowValueMale(self):
        return self.album_glob_ratio_low_male 

    # Function returns fair risk values range for album_glob_ratio
    def getAlbumGlobRatioFairValueMale(self):
        return self.album_glob_ratio_fair_male 
    
    # Function retuns moderate risk value ranges for album_glob_ratio
    def getAlbumGlobRatioModerateValueMale(self):
        return self.album_glob_ratio_moderate_male 

    # Function returns high risk value ranges for album_glob_ratio
    def getAlbumGlobRatioHighValueMale(self):
        return self.album_glob_ratio_high_male 

    # Function returns low risk values range for album_glob_ratio
    def getAlbumGlobRatioLowValueFemale(self):
        return self.album_glob_ratio_low_female

    # Function returns fair risk values range for album_glob_ratio
    def getAlbumGlobRatioFairValueFemale(self):
        return self.album_glob_ratio_fair_female

    # Function retuns moderate risk value ranges for album_glob_ratio
    def getAlbumGlobRatioModerateValueFemale(self):
        return self.album_glob_ratio_moderate_female

    # Function returns high risk value ranges for album_glob_ratio
    def getAlbumGlobRatioHighValueFemale(self):
        return self.album_glob_ratio_high_female

    # Function returns function name to parse album_glob_ratio value from medical report
    def getAlbumGlobRatiosFunction(self):
        return self.album_glob_ratio_func
   
    # Function returns aspartate aminotrans actual value
    def getAspartateAminotransValue(self):
        return self.aspartate_aminotrans
           
    # Function returns list of medical annotations for aspartate aminotrans
    def getAspartateAminotransMedicalAnnotations(self):
        return self.aspartate_aminotrans_medical_annot

    # Function returns unit of aspartate aminotrans
    def getAspartateAminotransUnit(self):
        return self.aspartate_aminotrans_unit

    # Function returns range of values for aspartate aminotrans for male
    def getAspartateAminotransRangeMale(self):
        return self.aspartate_aminotrans_range_male 

    # Function returns range of values for aspartate aminotrans for female
    def getAspartateAminotransRangeFemale(self):
        return self.aspartate_aminotrans_range_female
    
    # Function returns low risk values range for aspartate aminotrans
    def getAspartateAminotransLowValueMale(self):
        return self.aspartate_aminotrans_low_male

    # Function returns fair risk values range for aspartate aminotrans
    def getAspartateAminotransFairValueMale(self):
        return self.aspartate_aminotrans_fair_male 
    
    # Function returns moderate risk values range for aspartate aminotrans
    def getAspartateAminotransModerateValueMale(self):
        return self.aspartate_aminotrans_moderate_male 

    # Function returns high risk values range for aspartate aminotrans
    def getAspartateAminotransHighValueMale(self):
        return self.aspartate_aminotrans_high_male 
   
    # Function returns low risk values range for aspartate aminotrans
    def getAspartateAminotransLowValueFemale(self):
        return self.aspartate_aminotrans_low_female

    # Function returns fair risk values range for aspartate aminotrans
    def getAspartateAminotransFairValueFemale(self):
        return self.aspartate_aminotrans_fair_female

    # Function returns moderate risk values range for aspartate aminotrans
    def getAspartateAminotransModerateValueFemale(self):
        return self.aspartate_aminotrans_moderate_female

    # Function returns high risk values range for aspartate aminotrans
    def getAspartateAminotransHighValueFemale(self):
        return self.aspartate_aminotrans_high_female
 
    # Function returns function name for parsing aspartate aminotrans value from medical reports
    def getAspartateAminotransFunction(self):
        return self.aspartate_aminotrans_func

    # Function returns albumin actual value
    def getAlbuminValue(self):
        return self.albumin
    
    # Function returns list of medical annottions for albumin
    def getAlbuminMedicalAnnotations(self):
        return self.albumin_medical_annot

    # Function returns unit of albumin
    def getAlbuminUnit(self):
        return self.albumin_unit 

    # Function returns range of values for albumin for male
    def getAlbuminRangeMale(self):
        return self.albumin_range_female 

    # Function returns range of values for albumin for female
    def getAlbuminRangeFemale(self):
        return self.albumin_range_male
    
    # Function returns low risk values range for albumin
    def getAlbuminLowValueMale(self):
        return self.albumin_low_male

    # Function returns fair risk values range for albumin
    def getAlbuminFairValueMale(self):
        return self.albumin_fair_male 
    
    # Function returns moderate risk values range for albumin
    def getAlbuminModerateValueMale(self):
        return self.albumin_moderate_male

    # Function returns high risk values range for albumin
    def getAlbuminHighValueMale(self):
        return self.albumin_high_male
   
    # Function returns low risk values range for albumin
    def getAlbuminLowValueFemale(self):
        return self.albumin_low_female

    # Function returns fair risk values range for albumin
    def getAlbuminFairValueFemale(self):
        return self.albumin_fair_female

    # Function returns moderate risk values range for albumin
    def getAlbuminModerateValueFemale(self):
        return self.albumin_moderate_female

    # Function returns high risk values range for albumin
    def getAlbuminHighValueFemale(self):
        return self.albumin_high_female
 
    # Function returns function name for parsing albumin value from medical reports
    def getAlbuminFunction(self):
        return self.albumin_func

    # Function returns albumin actual value
    def getGlobulinValue(self):
        return self.globulin
    
    # Function returns list of medical annottions for albumin
    def getGlobulinMedicalAnnotations(self):
        return self.globulin_medical_annot

    # Function returns unit of globulin
    def getGlobulinUnit(self):
        return self.globulin_unit

    # Function returns range of values for globulin for male
    def getGlobulinRangeMale(self):
        return self.globulin_range_male

    # Function returns range of values for globulin for female
    def getGlobulinRangeFemale(self):
        return self.globulin_range_female
    
    # Function returns low risk values range for globulin
    def getGlobulinLowValueFemale(self):
        return self.globulin_low_female

    # Function returns fair risk values range for globulin
    def getGlobulinFairValueFemale(self):
        return self.globulin_fair_female
    
    # Function returns moderate risk values range for globulin
    def getGlobulinModerateValueFemale(self):
        return self.globulin_moderate_female

    # Function returns high risk values range for globulin
    def getGlobulinHighValueFemale(self):
        return self.globulin_high_female
   
    # Function returns low risk values range for globulin
    def getGlobulinLowValueMale(self):
        return self.globulin_low_male

    # Function returns fair risk values range for globulin
    def getGlobulinFairValueMale(self):
        return self.globulin_fair_male

    # Function returns moderate risk values range for globulin
    def getGlobulinModerateValueMale(self):
        return self.globulin_moderate_male

    # Function returns high risk values range for globulin
    def getGlobulinHighValueMale(self):
        return self.globulin_high_male
 
    # Function returns function name for parsing globulin value from medical reports
    def getGlobulinFunction(self):
        return self.globulin_func

    # Function returns total protein actual value
    def getTotalProteinValue(self):
        return self.total_protein 
    
    # Function returns list of medical annottions for total protein
    def getTotalProteinMedicalAnnotations(self):
        return self.total_protein_medical_annot

    # Function returns unit of total protein
    def getTotalProteinUnit(self):
        return self.total_protein_unit

    # Function returns range of values for total protein for male
    def getTotalProteinRangeMale(self):
        return self.total_protein_range_male 

    # Function returns range of values for total protein for female
    def getTotalProteinRangeFemale(self):
        return self.total_protein_range_female
    
    # Function returns low risk values range for total protein
    def getTotalProteinLowValueMale(self):
        return self.total_protein_low_male

    # Function returns fair risk values range for total protein
    def getTotalProteinFairValueMale(self):
        return self.total_protein_fair_male
   
    # Function returns moderate risk values range for total protein
    def getTotalProteinModerateValueMale(self):
        return self.total_protein_moderate_male 

    # Function returns high risk values range for total protein
    def getTotalProteinHighValueMale(self):
        return self.total_protein_high_male 
   
    # Function returns low risk values range for total protein
    def getTotalProteinLowValueFemale(self):
        return self.total_protein_low_female

    # Function returns fair risk values range for total protein
    def getTotalProteinFairValueFemale(self):
        return self.total_protein_fair_female

    # Function returns moderate risk values range for total protein
    def getTotalProteinModerateValueFemale(self):
        return self.total_protein_moderate_female

    # Function returns high risk values range for total protein
    def getTotalProteinHighValueFemale(self):
        return self.total_protein_high_female
 
    # Function returns function name for parsing total protein value from medical reports
    def getTotalProteinFunction(self):
        return self.total_protein_func 

    # Function gets gamma glutaml actual value
    def getGammaGlutamylTransValue(self):
        return self.gamma_glutamyl_trans 
           
    # Function gets list of medical annotations for gamma glutamyl
    def getGammaGlutamylTransMedicalAnnotations(self):
        return self.gamma_glutamyl_trans_medical_annot 

    # Function gets unit of gamma glutamyl
    def getGammaGlutamylTransUnit(self):
        return self.gamma_glutamyl_trans_unit

    # Function gets range of values for gamma glutamyl for male
    def getGammaGlutamylTransRangeMale(self):
        return self.gamma_glutamyl_trans_range_male

    # Function gets range of values for gamma glutamyl for female
    def getGammaGlutamylTransRangeFemale(self):
        return self.gamma_glutamyl_trans_range_female 
    
    # Function gets low risk values range for gamma glutamyl
    def getGammaGlutamylTransLowValueFemale(self):
        return self.gamma_glutamyl_trans_low_female

    # Function gets fair risk values range for gamma glutamyl
    def getGammaGlutamylTransFairValueFemale(self):
        return self.gamma_glutamyl_trans_fair_female
    
    # Function gets moderate risk values range for gamma glutamyl
    def getGammaGlutamylTransModerateValueFemale(self):
        return self.gamma_glutamyl_trans_moderate_female 

    # Function gets high risk values range for gamma glutamyl
    def getGammaGlutamylTransHighValueFemale(self):
        return self.gamma_glutamyl_trans_high_female 
   
    # Function gets low risk values range for gamma glutamyl
    def getGammaGlutamylTransLowValueMale(self):
        return self.gamma_glutamyl_trans_low_male

    # Function gets fair risk values range for gamma glutamyl
    def getGammaGlutamylTransFairValueMale(self):
        return self.gamma_glutamyl_trans_fair_male

    # Function gets moderate risk values range for gamma glutamyl
    def getGammaGlutamylTransModerateValueMale(self):
        return self.gamma_glutamyl_trans_moderate_male

    # Function gets high risk values range for gamma glutamyl
    def getGammaGlutamylTransHighValueMale(self):
        return self.gamma_glutamyl_trans_high_male
 
    # Function gets function name for parsing gamma glutamyl value from medical reports
    def getGammaGlutamylTransFunction(self):
        return self.gamma_glutamyl_trans_func

    # Function gets alkaline phosphatase actual value
    def getAlkalinePhosphataseValue(self):
        return self.alkaline_phosphatase
           
    # Function gets list of medical annotations for alkaline phosphatase
    def getAlkalinePhosphataseMedicalAnnotations(self):
        return self.alkaline_phosphatase_medical_annot

    # Function gets unit of alkaline phosphatase
    def getAlkalinePhosphataseUnit(self):
        return self.alkaline_phosphatase_unit

    # Function gets range of values for alkaline phosphatase for male
    def getAlkalinePhosphataseRangeMale(self):
        return self.alkaline_phosphatase_range_male

    # Function gets range of values for alkaline phosphatase for female
    def getAlkalinePhosphataseRangeFemale(self):
        return self.alkaline_phosphatase_range_female
    
    # Function gets low risk values range for alkaline phosphatase
    def getAlkalinePhosphataseLowValueMale(self):
        return self.alkaline_phosphatase_low_male

    # Function gets fair risk values range for alkaline phosphatase
    def getAlkalinePhosphataseFairValueMale(self):
        return self.alkaline_phosphatase_fair_male
    
    # Function gets moderate risk values range for alkaline phosphatase
    def getAlkalinePhosphataseModerateValueMale(self):
        return self.alkaline_phosphatase_moderate_male

    # Function gets high risk values range for alkaline phosphatase
    def getAlkalinePhosphataseHighValueMale(self):
        return self.alkaline_phosphatase_high_male
   
    # Function gets low risk values range for alkaline phosphatase
    def getAlkalinePhosphataseLowValueFemale(self):
        return self.alkaline_phosphatase_low_female

    # Function gets fair risk values range for alkaline phosphatase
    def getAlkalinePhosphataseFairValueFemale(self):
        return self.alkaline_phosphatase_fair_female

    # Function gets moderate risk values range for alkaline phosphatase
    def getAlkalinePhosphataseModerateValueFemale(self):
        return self.alkaline_phosphatase_moderate_female

    # Function gets high risk values range for alkaline phosphatase
    def getAlkalinePhosphataseHighValueFemale(self):
        return self.alkaline_phosphatase_high_female
 
    # Function gets function name for parsing alkaline phosphatase value from medical reports
    def getAlkalinePhosphataseFunction(self):
        return self.alkaline_phosphatase_func

    # Function gets alanine transaminase actual value
    def getAlanineTransaminaseValue(self):
        return self.alanine_transaminase
           
    # Function gets list of medical annotations for alanine transaminase
    def getAlanineTransaminaseMedicalAnnotations(self):
        return self.alanine_transaminase_medical_annot 

    # Function gets unit of alanine transaminase
    def getAlanineTransaminaseUnit(self):
        return self.alanine_transaminase_unit 

    # Function gets range of values for alanine transaminase for male
    def getAlanineTransaminaseRangeMale(self):
        return self.alanine_transaminase_range_male

    # Function gets range of values for alanine transaminase for female
    def getAlanineTransaminaseRangeFemale(self):
        return self.alanine_transaminase_range_female
    
    # Function gets low risk values range for alanine transaminase
    def getAlanineTransaminaseLowValueMale(self):
        return self.alanine_transaminase_low_male

    # Function gets fair risk values range for alanine transaminase
    def getAlanineTransaminaseFairValueMale(self):
        return self.alanine_transaminase_fair_male
    
    # Function gets moderate risk values range for alanine transaminase
    def getAlanineTransaminaseModerateValueMale(self):
        return self.alanine_transaminase_moderate_male 

    # Function gets high risk values range for alanine transaminase
    def getAlanineTransaminaseHighValueMale(self):
        return self.alanine_transaminase_high_male 

       # Function gets low risk values range for alanine transaminase
    def getAlanineTransaminaseLowValueFemale(self):
        return self.alanine_transaminase_low_female

    # Function gets fair risk values range for alanine transaminase
    def getAlanineTransaminaseFairValueFemale(self):
        return self.alanine_transaminase_fair_female

    # Function gets moderate risk values range for alanine transaminase
    def getAlanineTransaminaseModerateValueFemale(self):
        return self.alanine_transaminase_moderate_female

    # Function gets high risk values range for alanine transaminase
    def getAlanineTransaminaseHighValueFemale(self):
        return self.alanine_transaminase_high_female
 
    # Function gets function name for parsing alanine transaminase value from medical reports
    def getAlanineTransaminaseFunction(self):
        return self.alanine_transaminase_func

#instantiate class
#liver_profile = LiverProfile()

#call loadMetaData Function 
#liver_profile.loadMetaData()

#call getParsedData function to get parsed output values
#liver_parsed_value = liver_profile.getParsedData("/home/isana/sample-report-2.pdf")
#print json.dumps({"liver_parsed_values" : liver_parsed_value}, indent = 4)

