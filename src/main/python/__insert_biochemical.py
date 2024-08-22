import json, collections
from __db_config import *
from __config import *
from __insert_message_db import *


def getMiscData(user_id, db):
    query = "select misc_data from user_misc_data where id=%d"%(user_id) 
    cursor = db.cursor()
    cursor.execute(query)
    get_data  = cursor.fetchone() 
    if get_data != None:
        misc_data = get_data[0]
        misc_data = unicode(misc_data, errors='ignore')
        misc_data_dict = json.loads(misc_data, object_pairs_hook=collections.OrderedDict)
        return misc_data_dict
    else:
        return 0

def setParameter(parameter_name):
    if parameter_name == "None":
        parameter_name = 0
        return parameter_name
    else:
        return parameter_name

def insertBiochemicalData(user_misc_data, profile, parsed_values): 
    if profile == "Complete Blood Count":
        # cbc profile
        hemoglobin = parsed_values.get("hemoglobin", {}).get("reading_value", 0)
        hemoglobin = setParameter(hemoglobin)
        rbc_count = parsed_values.get("rbc_count", {}).get("reading_value", 0)
        rbc_count = setParameter(rbc_count)
        platelet_count = parsed_values.get("platelet_count", {}).get("reading_value", 0)
        platelet_count = setParameter(platelet_count)
        wbc_count = parsed_values.get("wbc_count", {}).get("reading_value", 0)
        wbc_count = setParameter(wbc_count)
        neutrophils = parsed_values.get("neutrophils", {}).get("reading_value", 0)
        neutrophils = setParameter(neutrophils)
        neutrophils_absolute = parsed_values.get("neutrophils_absolute", {}).get("reading_value", 0)  
        neutrophils_absolute = setParameter(neutrophils_absolute)
        eosinophils = parsed_values.get("eosinophils", {}).get("reading_value", 0)
        eosinophils = setParameter(eosinophils)
        eosinophils_absolute = parsed_values.get("eosinophils_absolute", {}).get("reading_value", 0)
        eosinophils_absolute = setParameter(eosinophils_absolute)
        basophils = parsed_values.get("basophils", {}).get("reading_value", 0)
        basophils = setParameter(basophils)
        basophils_absolute = parsed_values.get("basophils_absolute", {}).get("reading_value", 0)
        basophils_absolute = setParameter(basophils_absolute)
        lymphocytes = parsed_values.get("lymphocytes", {}).get("reading_value", 0)
        lymphocytes = setParameter(lymphocytes)
        lymphocytes_absolute = parsed_values.get("lymphocytes_absolute", {}).get("reading_value", 0)
        lymphocytes_absolute = setParameter(lymphocytes_absolute)
        monocytes = parsed_values.get("monocytes", {}).get("reading_value", 0)
        monocytes = setParameter(monocytes)
        monocytes_absolute = parsed_values.get("monocytes_absolute", {}).get("reading_value", 0)
        monocytes_absolute = setParameter(monocytes_absolute)
        if hemoglobin != 0:
            user_misc_data["BioChemical"]["CBC"]["hemoglobin"]["measure"] = hemoglobin
        if rbc_count != 0:
            user_misc_data["BioChemical"]["CBC"]["redBloodCell"]["measure"] = str(int(float(rbc_count)*1000000)) 
        if platelet_count != 0:
            user_misc_data["BioChemical"]["CBC"]["plateletCount"]["measure"] = str(int(float(platelet_count)))
        if wbc_count != 0:
            user_misc_data["BioChemical"]["CBC"]["totalLeucocytes"]["measure"] = str(int(float(wbc_count)))
        if neutrophils != 0:
            user_misc_data["BioChemical"]["CBC"]["neutrophils"]["measure"] = str(int(float(neutrophils)))
        if neutrophils_absolute != 0:
            user_misc_data["BioChemical"]["CBC"]["absoluteNeutrophils"]["measure"] = str(int(float(neutrophils_absolute)))
        if eosinophils != 0:
            user_misc_data["BioChemical"]["CBC"]["eosinophils"]["measure"] = str(int(float(eosinophils)))
        if eosinophils_absolute != 0:
            user_misc_data["BioChemical"]["CBC"]["absoluteEosinophils"]["measure"] = str(int(float(eosinophils_absolute)))
        if basophils != 0:
            user_misc_data["BioChemical"]["CBC"]["bashophils"]["measure"] = str(int(float(basophils)))
        if basophils_absolute != 0:
            user_misc_data["BioChemical"]["CBC"]["absoluteBasophils"]["measure"] = str(int(float(basophils_absolute)))
        if lymphocytes != 0:
            user_misc_data["BioChemical"]["CBC"]["lymphocytes"]["measure"] = str(int(float(lymphocytes)))
        if lymphocytes_absolute != 0:
            user_misc_data["BioChemical"]["CBC"]["absoluteLymphocytes"]["measure"] = str(int(float(lymphocytes_absolute)))
        if monocytes != 0:
            user_misc_data["BioChemical"]["CBC"]["monocytes"]["measure"] = str(int(float(monocytes)))
        if monocytes_absolute != 0:
            user_misc_data["BioChemical"]["CBC"]["absoluteMonocytes"]["measure"] = str(int(float(monocytes_absolute)))
        
    elif profile == "Diabetes":
        # diabetes parsing
        glucose_fasting = parsed_values.get("glucose_fasting", {}).get("reading_value", 0)
        glucose_fasting = setParameter(glucose_fasting) 
        glucose_postprandial = parsed_values.get("glucose_postprandial", {}).get("reading_value", 0)
        glucose_postprandial = setParameter(glucose_postprandial)
        hemoglobin_a1c = parsed_values.get("hemoglobin_a1c", {}).get("reading_value", 0) 
        hemoglobin_a1c = setParameter(hemoglobin_a1c)
        mean_plasma_glucose = parsed_values.get("mean_plasma_glucose",{}).get("reading_value", 0)
        mean_plasma_glucose = setParameter(mean_plasma_glucose)
        fasting_insulin = parsed_values.get("fasting_insulin", {}).get("reading_value", 0)
        fasting_insulin = setParameter(fasting_insulin)
        if glucose_fasting != 0:
            user_misc_data["BioChemical"]["Diabetic_Profile"]["bloodSugarFasting"]["measure"] = str(int(float(glucose_fasting)))
        if glucose_postprandial != 0:
            user_misc_data["BioChemical"]["Diabetic_Profile"]["bloodSugarPostLunch"]["measure"] = str(int(float(glucose_postprandial)))
        if hemoglobin_a1c != 0:
            user_misc_data["BioChemical"]["Diabetic_Profile"]["glycosylated"]["measure"] = hemoglobin_a1c
        if mean_plasma_glucose != 0:
            user_misc_data["BioChemical"]["Diabetic_Profile"]["meanPlasmaGlucose"]["measure"] = str(int(float(mean_plasma_glucose)))
        if fasting_insulin != 0:
            user_misc_data["BioChemical"]["Diabetic_Profile"]["insulinFasting"]["measure"] = str(int(float(fasting_insulin)))
    elif profile == "Liver Function":
        # liver parsing
        total_protein = parsed_values.get("total_protein", {}).get("reading_value", 0)
        total_protein = setParameter(total_protein)
        albumin = parsed_values.get("albumin", {}).get("reading_value", 0)
        albumin = setParameter(albumin)
        bilirubin_direct = parsed_values.get("bilirubin_direct", {}).get("reading_value", 0)
        bilirubin_direct = setParameter(bilirubin_direct)
        bilirubin_indirect = parsed_values.get("bilirubin_indirect", {}).get("reading_value", 0)
        bilirubin_indirect = setParameter(bilirubin_indirect)
        aspartate_aminotransferase = parsed_values.get("aspartate_aminotransferase", {}).get("reading_value", 0)
        aspartate_aminotransferase = setParameter(aspartate_aminotransferase)
        alanine_transaminase = parsed_values.get("alanine_transaminase", {}).get("reading_value", 0)
        alanine_transaminase = setParameter(alanine_transaminase)
        alkaline_phosphatase = parsed_values.get("alanine_transaminase", {}).get("reading_value", 0)
        alkaline_phosphatase = setParameter(alkaline_phosphatase)
        globulin = parsed_values.get("globulin", {}).get("reading_value", 0)
        globulin = setParameter(globulin)
        if total_protein != 0:
            user_misc_data["BioChemical"]["Liver_Profile"]["totalProtein"]["measure"] = total_protein
        if albumin != 0: 
            user_misc_data["BioChemical"]["Liver_Profile"]["albuminGlobulin"]["measure"] = albumin
        if bilirubin_direct != 0:
            user_misc_data["BioChemical"]["Liver_Profile"]["billirubinDirect"]["measure"] = bilirubin_direct
        if bilirubin_indirect != 0:
            user_misc_data["BioChemical"]["Liver_Profile"]["billirubinIndirect"]["measure"] = bilirubin_indirect
        if aspartate_aminotransferase != 0:
            user_misc_data["BioChemical"]["Liver_Profile"]["sgot"]["measure"] = aspartate_aminotransferase
        if alanine_transaminase != 0:
            user_misc_data["BioChemical"]["Liver_Profile"]["sgpt"]["measure"] = alanine_transaminase 
        if alkaline_phosphatase != 0:
            user_misc_data["BioChemical"]["Liver_Profile"]["alkalinePhospate"]["measure"] = alkaline_phosphatase
        if globulin != 0:
            user_misc_data["BioChemical"]["Liver_Profile"]["globulin"]["measure"] = globulin
    elif profile == "Lipid Profile" or profile == "Cardiac":
        # cardiac parsing
        total_cholesterol = parsed_values.get("total_cholesterol", {}).get("reading_value", 0)
        total_cholesterol = setParameter(total_cholesterol)
        hdl_cholesterol = parsed_values.get("hdl_cholesterol", {}).get("reading_value", 0)
        hdl_cholesterol = setParameter(hdl_cholesterol)
        ldl_cholesterol = parsed_values.get("ldl_cholesterol", {}).get("reading_value", 0)
        ldl_cholesterol = setParameter(ldl_cholesterol)
        triglycerides = parsed_values.get("triglycerides", {}).get("reading_value", 0)
        triglycerides = setParameter(triglycerides)
        vldl_cholesterol = parsed_values.get("vldl_cholesterol", {}).get("reading_value", 0)
        vldl_cholesterol = setParameter(vldl_cholesterol)
        non_hdl_cholesterol = parsed_values.get("non_hdl_cholesterol", {}).get("reading_value", 0)
        non_hdl_cholesterol = setParameter(non_hdl_cholesterol)
        tc_hdl_ratio = parsed_values.get("tc_hdl_ratio", {}).get("reading_value", 0)
        tc_hdl_ratio = setParameter(tc_hdl_ratio)
        ldl_hdl_ratio = parsed_values.get("ldl_hdl_ratio", {}).get("reading_value", 0)
        ldl_hdl_ratio = setParameter(ldl_hdl_ratio)
        apolipoprotein = parsed_values.get("apolipoprotein", {}).get("reading_value",0)
        apolipoprotein = setParameter(apolipoprotein)
        if total_cholesterol != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["totalCholestrol"]["measure"] = str(int(float(total_cholesterol))) 
        if hdl_cholesterol != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["hdl"]["measure"] = str(int(float(hdl_cholesterol)))
        if ldl_cholesterol != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["ldl"]["measure"] = str(int(float(ldl_cholesterol)))
        if triglycerides != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["triglycerides"]["measure"] = str(int(float(triglycerides)))
        if vldl_cholesterol != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["vldl"]["measure"] = str(int(float(vldl_cholesterol)))
        if non_hdl_cholesterol != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["nonHdlCholestrol"]["measure"] = str(int(float(non_hdl_cholesterol)))
        if tc_hdl_ratio != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["totalCholesterolHdlRatio"]["measure"] = tc_hdl_ratio
        if ldl_hdl_ratio != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["ldlHdlRation"]["measure"] = ldl_hdl_ratio
        if apolipoprotein != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["apolipoprotein"]["measure"] = str(int(float(apolipoprotein)))
    elif profile == "Kidney Function":
        # kidney parsing
        blood_urea_nitrogen = parsed_values.get("blood_urea_nitrogen", {}).get("reading_value", 0)
        blood_urea_nitrogen = setParameter(blood_urea_nitrogen) 
        creatinine = parsed_values.get("creatinine", {}).get("reading_value", 0)
        creatinine = setParameter(creatinine)
        uric_acid = parsed_values.get("uric_acid", {}).get("reading_value", 0)
        uric_acid = setParameter(uric_acid)
        if blood_urea_nitrogen != 0:
            user_misc_data["BioChemical"]["Kidney_Profile"]["bun"]["measure"] = str(int(float(blood_urea_nitrogen)))
        if creatinine != 0:
            user_misc_data["BioChemical"]["Kidney_Profile"]["creatinine"]["measure"] = creatinine
        if uric_acid != 0:
            user_misc_data["BioChemical"]["Kidney_Profile"]["uricAcid"]["measure"] = uric_acid
    elif profile == "Vitamins":
        # vitamins parsing
        vitamin_b12 = parsed_values.get("vitamin_b12", {}).get("reading_value", 0)
        vitamin_b12 = setParameter(vitamin_b12)
        vitamin_d = parsed_values.get("vitamin_d", {}).get("reading_value", 0)
        vitamin_d = setParameter(vitamin_d)
        if vitamin_b12 != 0:
            user_misc_data["BioChemical"]["Vitamins"]["vitaminB12"]["measure"] = vitamin_b12
        if vitamin_d != 0:
            user_misc_data["BioChemical"]["Vitamins"]["HYDROPOXYVitaminD"]["measure"] = vitamin_d

    else:
        hemoglobin = parsed_values[0].get("hemoglobin", {}).get("reading_value", 0)
        hemoglobin = setParameter(hemoglobin)
        rbc_count = parsed_values[0].get("rbc_count", {}).get("reading_value", 0)
        rbc_count = setParameter(rbc_count)
        platelet_count = parsed_values[0].get("platelet_count", {}).get("reading_value", 0)
        platelet_count = setParameter(platelet_count)
        wbc_count = parsed_values[0].get("wbc_count", {}).get("reading_value", 0)
        wbc_count = setParameter(wbc_count)
        neutrophils = parsed_values[0].get("neutrophils", {}).get("reading_value", 0)
        neutrophils = setParameter(neutrophils)
        neutrophils_absolute = parsed_values[0].get("neutrophils_absolute", {}).get("reading_value", 0)
        neutrophils_absolute = setParameter(neutrophils_absolute)
        eosinophils = parsed_values[0].get("eosinophils", {}).get("reading_value", 0)
        eosinophils = setParameter(eosinophils)
        eosinophils_absolute = parsed_values[0].get("eosinophils_absolute", {}).get("reading_value", 0)
        eosinophils_absolute = setParameter(eosinophils_absolute)
        basophils = parsed_values[0].get("basophils", {}).get("reading_value", 0)
        basophils = setParameter(basophils)
        basophils_absolute = parsed_values[0].get("basophils_absolute", {}).get("reading_value", 0)
        basophils_absolute = setParameter(basophils_absolute)
        lymphocytes = parsed_values[0].get("lymphocytes", {}).get("reading_value", 0)
        lymphocytes = setParameter(lymphocytes)
        lymphocytes_absolute = parsed_values[0].get("lymphocytes_absolute", {}).get("reading_value", 0)
        lymphocytes_absolute = setParameter(lymphocytes_absolute)
        monocytes = parsed_values[0].get("monocytes", {}).get("reading_value", 0)
        monocytes = setParameter(monocytes)
        monocytes_absolute = parsed_values[0].get("monocytes_absolute", {}).get("reading_value", 0)
        monocytes_absolute = setParameter(monocytes_absolute)
        glucose_fasting = parsed_values[1].get("glucose_fasting", {}).get("reading_value", 0)
        glucose_fasting = setParameter(glucose_fasting)
        glucose_postprandial = parsed_values[1].get("glucose_postprandial", {}).get("reading_value", 0)
        glucose_postprandial = setParameter(glucose_postprandial)
        hemoglobin_a1c = parsed_values[1].get("hemoglobin_a1c", {}).get("reading_value", 0)
        hemoglobin_a1c = setParameter(hemoglobin_a1c)
        mean_plasma_glucose = parsed_values[1].get("mean_plasma_glucose",{}).get("reading_value", 0)
        mean_plasma_glucose = setParameter(mean_plasma_glucose)
        fasting_insulin = parsed_values[1].get("fasting_insulin", {}).get("reading_value", 0)
        fasting_insulin = setParameter(fasting_insulin)
        total_protein = parsed_values[2].get("total_protein", {}).get("reading_value", 0)
        total_protein = setParameter(total_protein)
        albumin = parsed_values[2].get("albumin", {}).get("reading_value", 0)
        albumin = setParameter(albumin)
        bilirubin_direct = parsed_values[2].get("bilirubin_direct", {}).get("reading_value", 0)
        bilirubin_direct = setParameter(bilirubin_direct)
        bilirubin_indirect = parsed_values[2].get("bilirubin_indirect", {}).get("reading_value", 0)
        bilirubin_indirect = setParameter(bilirubin_indirect)
        aspartate_aminotransferase = parsed_values[2].get("aspartate_aminotransferase", {}).get("reading_value", 0)
        aspartate_aminotransferase = setParameter(aspartate_aminotransferase)
        alanine_transaminase = parsed_values[2].get("alanine_transaminase", {}).get("reading_value", 0)
        alanine_transaminase = setParameter(alanine_transaminase)
        alkaline_phosphatase = parsed_values[2].get("alanine_transaminase", {}).get("reading_value", 0)
        alkaline_phosphatase = setParameter(alkaline_phosphatase)
        globulin = parsed_values[2].get("globulin", {}).get("reading_value", 0)
        globulin = setParameter(globulin)
        total_cholesterol = parsed_values[3].get("total_cholesterol", {}).get("reading_value", 0)
        total_cholesterol = setParameter(total_cholesterol)
        hdl_cholesterol = parsed_values[3].get("hdl_cholesterol", {}).get("reading_value", 0)
        hdl_cholesterol = setParameter(hdl_cholesterol)
        ldl_cholesterol = parsed_values[3].get("ldl_cholesterol", {}).get("reading_value", 0)
        ldl_cholesterol = setParameter(ldl_cholesterol)
        triglycerides = parsed_values[3].get("triglycerides", {}).get("reading_value", 0)
        triglycerides = setParameter(triglycerides)
        vldl_cholesterol = parsed_values[3].get("vldl_cholesterol", {}).get("reading_value", 0)
        vldl_cholesterol = setParameter(vldl_cholesterol)
        non_hdl_cholesterol = parsed_values[3].get("non_hdl_cholesterol", {}).get("reading_value", 0)
        non_hdl_cholesterol = setParameter(non_hdl_cholesterol)
        tc_hdl_ratio = parsed_values[3].get("tc_hdl_ratio", {}).get("reading_value", 0)
        tc_hdl_ratio = setParameter(tc_hdl_ratio)
        ldl_hdl_ratio = parsed_values[3].get("ldl_hdl_ratio", {}).get("reading_value", 0)
        ldl_hdl_ratio = setParameter(ldl_hdl_ratio)
        apolipoprotein = parsed_values[3].get("apolipoprotein", {}).get("reading_value",0)
        apolipoprotein = setParameter(apolipoprotein)
        blood_urea_nitrogen = parsed_values[4].get("blood_urea_nitrogen", {}).get("reading_value", 0)
        blood_urea_nitrogen = setParameter(blood_urea_nitrogen)
        creatinine = parsed_values[4].get("creatinine", {}).get("reading_value", 0)
        creatinine = setParameter(creatinine)
        uric_acid = parsed_values[4].get("uric_acid", {}).get("reading_value", 0)
        uric_acid = setParameter(uric_acid)
        vitamin_b12 = parsed_values[5].get("vitamin_b12", {}).get("reading_value", 0)
        vitamin_b12 = setParameter(vitamin_b12)
        vitamin_d = parsed_values[5].get("vitamin_d", {}).get("reading_value", 0)
        vitamin_d = setParameter(vitamin_d)
        if hemoglobin != 0:
            user_misc_data["BioChemical"]["CBC"]["hemoglobin"]["measure"] = hemoglobin
        if rbc_count != 0:
            user_misc_data["BioChemical"]["CBC"]["redBloodCell"]["measure"] = str(int(float(rbc_count)*1000000))
        if platelet_count != 0:
            user_misc_data["BioChemical"]["CBC"]["plateletCount"]["measure"] = str(int(float(platelet_count)))
        if wbc_count != 0:
            user_misc_data["BioChemical"]["CBC"]["totalLeucocytes"]["measure"] = str(int(float(wbc_count)))
        if neutrophils != 0:
            user_misc_data["BioChemical"]["CBC"]["neutrophils"]["measure"] = str(int(float(neutrophils)))
        if neutrophils_absolute != 0:
            user_misc_data["BioChemical"]["CBC"]["absoluteNeutrophils"]["measure"] = str(int(float(neutrophils_absolute)))
        if eosinophils != 0:
            user_misc_data["BioChemical"]["CBC"]["eosinophils"]["measure"] = str(int(float(eosinophils)))
        if eosinophils_absolute != 0:
            user_misc_data["BioChemical"]["CBC"]["absoluteEosinophils"]["measure"] = str(int(float(eosinophils_absolute)))
        if basophils != 0:
            user_misc_data["BioChemical"]["CBC"]["bashophils"]["measure"] = str(int(float(basophils)))
        if basophils_absolute != 0:
            user_misc_data["BioChemical"]["CBC"]["absoluteBasophils"]["measure"] = str(int(float(basophils_absolute)))
        if lymphocytes != 0:
            user_misc_data["BioChemical"]["CBC"]["lymphocytes"]["measure"] = str(int(float(lymphocytes)))
        if lymphocytes_absolute != 0:
            user_misc_data["BioChemical"]["CBC"]["absoluteLymphocytes"]["measure"] = str(int(float(lymphocytes_absolute)))
        if monocytes != 0:
            user_misc_data["BioChemical"]["CBC"]["monocytes"]["measure"] = str(int(float(monocytes)))
        if monocytes_absolute != 0:
            user_misc_data["BioChemical"]["CBC"]["absoluteMonocytes"]["measure"] = str(int(float(monocytes_absolute)))
        if glucose_fasting != 0:
            user_misc_data["BioChemical"]["Diabetic_Profile"]["bloodSugarFasting"]["measure"] = str(int(float(glucose_fasting)))
        if glucose_postprandial != 0:
            user_misc_data["BioChemical"]["Diabetic_Profile"]["bloodSugarPostLunch"]["measure"] = str(int(float(glucose_postprandial)))
        if hemoglobin_a1c != 0:
            user_misc_data["BioChemical"]["Diabetic_Profile"]["glycosylated"]["measure"] = hemoglobin_a1c
        if mean_plasma_glucose != 0:
            user_misc_data["BioChemical"]["Diabetic_Profile"]["meanPlasmaGlucose"]["measure"] = str(int(float(mean_plasma_glucose)))
        if fasting_insulin != 0:
            user_misc_data["BioChemical"]["Diabetic_Profile"]["insulinFasting"]["measure"] = str(int(float(fasting_insulin)))
        if total_protein != 0:
            user_misc_data["BioChemical"]["Liver_Profile"]["totalProtein"]["measure"] = total_protein
        if albumin != 0:
            user_misc_data["BioChemical"]["Liver_Profile"]["albuminGlobulin"]["measure"] = albumin
        if bilirubin_direct != 0:
            user_misc_data["BioChemical"]["Liver_Profile"]["billirubinDirect"]["measure"] = bilirubin_direct
        if bilirubin_indirect != 0:
            user_misc_data["BioChemical"]["Liver_Profile"]["billirubinIndirect"]["measure"] = bilirubin_indirect
        if aspartate_aminotransferase != 0:
            user_misc_data["BioChemical"]["Liver_Profile"]["sgot"]["measure"] = aspartate_aminotransferase
        if alanine_transaminase != 0:
            user_misc_data["BioChemical"]["Liver_Profile"]["sgpt"]["measure"] = alanine_transaminase
        if alkaline_phosphatase != 0:
            user_misc_data["BioChemical"]["Liver_Profile"]["alkalinePhospate"]["measure"] = alkaline_phosphatase
        if globulin != 0:
            user_misc_data["BioChemical"]["Liver_Profile"]["globulin"]["measure"] = globulin
        if total_cholesterol != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["totalCholestrol"]["measure"] = str(int(float(total_cholesterol)))
        if hdl_cholesterol != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["hdl"]["measure"] = str(int(float(hdl_cholesterol)))
        if ldl_cholesterol != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["ldl"]["measure"] = str(int(float(ldl_cholesterol)))
        if triglycerides != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["triglycerides"]["measure"] = str(int(float(triglycerides)))
        if vldl_cholesterol != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["vldl"]["measure"] = str(int(float(vldl_cholesterol)))
        if non_hdl_cholesterol != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["nonHdlCholestrol"]["measure"] = str(int(float(non_hdl_cholesterol)))
        if tc_hdl_ratio != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["totalCholesterolHdlRatio"]["measure"] = tc_hdl_ratio
        if ldl_hdl_ratio != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["ldlHdlRation"]["measure"] = ldl_hdl_ratio
        if apolipoprotein != 0:
            user_misc_data["BioChemical"]["Lipid_Profile"]["apolipoprotein"]["measure"] = str(int(float(apolipoprotein)))
        if blood_urea_nitrogen != 0:
            user_misc_data["BioChemical"]["Kidney_Profile"]["bun"]["measure"] = str(int(float(blood_urea_nitrogen)))
        if creatinine != 0:
            user_misc_data["BioChemical"]["Kidney_Profile"]["creatinine"]["measure"] = creatinine
        if uric_acid != 0:
            user_misc_data["BioChemical"]["Kidney_Profile"]["uricAcid"]["measure"] = uric_acid
        if vitamin_b12 != 0:
            user_misc_data["BioChemical"]["Vitamins"]["vitaminB12"]["measure"] = str(int(float(vitamin_b12)))
        if vitamin_d != 0:
            user_misc_data["BioChemical"]["Vitamins"]["HYDROPOXYVitaminD"]["measure"] = str(int(float(vitamin_d)))
    return json.dumps(user_misc_data, sort_keys=False)
    
def insertMiscDataDb(user_id, provider_id, misc_data, db):
    try:
        query = "UPDATE user_misc_data set misc_data=%s WHERE id=%s"
        cursor = db.cursor()
        cursor.execute(query,(misc_data, int(user_id)))
        db.commit()
        insert_data = InsertData() 
        # insert and update user misc data
        current_date = int(datetime.datetime.now().strftime("%Y%m%d"))
        insert_data.updateData(current_date, user_id, provider_id, "User Misc Data", "user misc data", misc_data)
        misc_data = json.loads(misc_data, object_pairs_hook=collections.OrderedDict)
        # insert and update glucose data to user_data_update and user_history_data
        glucose_fasting = misc_data.get("BioChemical", {}).get("Diabetic_Profile", {}).get("bloodSugarFasting", {}).get("measure", 0)
        insert_data.updateData(current_date, user_id, provider_id, "User Glucose Data", "glucoseFasting", glucose_fasting)
        glucose_pp = misc_data.get("BioChemical", {}).get("Diabetic_Profile", {}).get("bloodSugarPostLunch", {}).get("measure", 0)
        insert_data.updateData(current_date, user_id, provider_id, "User Glucose Data", "glucosePp", glucose_pp)
        hba1c = misc_data.get("BioChemical", {}).get("Diabetic_Profile", {}).get("glycosylated", {}).get("measure", 0)
        insert_data.updateData(current_date, user_id, provider_id, "User Glucose Data", "hba1c", hba1c)
        mpg = misc_data.get("BioChemical", {}).get("Diabetic_Profile", {}).get("meanPlasmaGlucose", {}).get("measure", 0)
        insert_data.updateData(current_date, user_id, provider_id, "User Glucose Data", "mpg", mpg)
        # insert and update cardiac data to user_data_update and user_history_data
        tc = misc_data.get("BioChemical", {}).get("Lipid_Profile", {}).get("totalCholestrol", {}).get("measure", 0)
        insert_data.updateData(current_date, user_id, provider_id, "User Cardiac Data", "tcMgDl", tc)
        hdl = misc_data.get("BioChemical", {}).get("Lipid_Profile", {}).get("hdl", {}).get("measure", 0)  
        insert_data.updateData(current_date, user_id, provider_id, "User Cardiac Data", "hdlMgDl", hdl)
    except Exception as err:
        #print err
        db.rollback()
    finally:
        db.close()
 
def insert_main(user_id, provider_id, profile, parsed_values):
    try:
        init_db()
        db = get_db()
        user_misc_data = getMiscData(user_id, db) 
        if user_misc_data != 0:
            updated_misc_data = insertBiochemicalData(user_misc_data, profile, parsed_values)
            insertMiscDataDb(user_id, provider_id, updated_misc_data, db)
        return 0
    except Exception as err:
        #print (err)
        pass

