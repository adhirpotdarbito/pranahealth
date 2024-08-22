import json
import sys
from collections import OrderedDict
from __insert_biochemical import *
from __diabetes_profile import *
from __lipid_profile import *
from __liver_profile import *
from __kidney_profile import *
from __cbc_profile import *
from __vitamins import *
from __config import *

password = ""
gender = "Male"
user_id = None

def getOverallRisk(parsed_output, config_risk_weightage, profile_name):
    """
        Function to calculate overall risk for respective profiles.
    """
    list_val_low = []
    list_val_fair = []
    list_val_moderate = []
    list_val_high = []
    list_val_na = []
    over_all_risk = {}
    risk_dict = {}
    low = {}
    fair = {}
    moderate = {}
    na = {}
    high = {}
    sum_low = 0
    sum_fair = 0
    sum_moderate = 0
    sum_high = 0
    parameters_profile = {}
    for key, value in parsed_output.items():
        parameters_profile[key] = parsed_output[key].get('risk')

    for key, value in parameters_profile.items():
        if value == Low:
            list_val_low = low.get(config_risk_weightage.get(key), [])
            list_val_low.append(key)
            low[config_risk_weightage.get(key)] = list_val_low
        if value == Fair:
            list_val_fair = fair.get(config_risk_weightage.get(key), [])
            list_val_fair.append(key)
            fair[config_risk_weightage.get(key)] = list_val_fair 
        if value == Moderate:
            list_val_moderate = moderate.get(config_risk_weightage.get(key), [])
            list_val_moderate.append(key) 
            moderate[config_risk_weightage.get(key)] = list_val_moderate 
        if value == High:
            list_val_high = high.get(config_risk_weightage.get(key), [])
            list_val_high.append(key)
            high[config_risk_weightage.get(key)] = list_val_high
        if value == n_a: 
            list_val_na = na.get(config_risk_weightage.get(key), [])
            list_val_na.append(key)
            na[config_risk_weightage.get(key)] = list_val_na

    risk_dict["low_risk"] = low
    risk_dict["fair_risk"] = fair
    risk_dict["moderate_risk"] = moderate
    risk_dict["high_risk"] = high
    risk_dict["na_risk"] = na
    for key, value in risk_dict.get("low_risk").items():
        sum_low += int(key)*len(value)
    for key, value in risk_dict.get("fair_risk").items():
        sum_fair += int(key) * len(value)
    for key, value in risk_dict.get("moderate_risk").items():
        sum_moderate += int(key) * len(value)
    for key, value in risk_dict.get("high_risk").items():
        sum_high += int(key) * len(value)

    #return over_all_risk   
    if sum([sum_low, sum_fair, sum_moderate, sum_high]) == 0:
        over_all_risk["risk"] = n_a
    else:
        if max(sum_low, sum_fair, sum_moderate, sum_high) == sum_low:
            if sum_low == sum_fair: 
                over_all_risk["risk"] = Fair
            if sum_low == sum_moderate:
                over_all_risk["risk"] = Moderate
            if sum_low == sum_high:
                over_all_risk["risk"] = High
            else:
                over_all_risk["risk"] = Low

        elif max(sum_low, sum_fair, sum_moderate, sum_high) == sum_fair:
            if sum_fair == sum_moderate:
                over_all_risk["risk"] = Moderate
            if sum_fair == sum_high:
                over_all_risk["risk"] = High
            else:
                over_all_risk["risk"] = Fair

        elif max(sum_low, sum_fair, sum_moderate, sum_high) == sum_moderate:
            if sum_moderate == sum_high:
                over_all_risk["risk"] = High
            else:
                over_all_risk["risk"] = Moderate

        elif max(sum_low, sum_fair, sum_moderate, sum_high) == sum_high:
            over_all_risk["risk"] = High
   
        else:
            over_all_risk["risk"] = n_a
 
    parsed_output["over_all_risk"] = over_all_risk  
    result = {}
    result[profile_name] = parsed_output  
    return json.dumps(result, indent = 4), over_all_risk

def getDiabetesParsedOutput(file_name, gender, password):
    #Instantiate diabetes profile class
    diabetes_profile = DiabetesProfile()
    #call loadMetaData Function 
    diabetes_profile.loadMetaData()
    #call getParsedData function to get parsed output values
    diabetes_parsed_value = diabetes_profile.getParsedData(file_name, gender, password)
    #print json.dumps({"diabetes_parsed_values" : diabetes_parsed_value}, indent = 4)
    return diabetes_parsed_value 

def getLipidParsedOutput(file_name, gender, password): 
    # create object for lipid profile
    lipid_profile = LipidProfile()
    #call loadMetaData Function
    lipid_profile.loadMetaData()
    #call getParsedData function to get parsed output values
    lipid_parsed_value = lipid_profile.getParsedData(file_name, gender, password)
    #print json.dumps({"lipid_parsed_values" : lipid_parsed_value}, indent = 4)
    return lipid_parsed_value

def getLiverParsedOutput(file_name, gender, password):
    #instantiate class
    liver_profile = LiverProfile()
    #call loadMetaData Function 
    liver_profile.loadMetaData()
    #call getParsedData function to get parsed output values
    liver_parsed_value = liver_profile.getParsedData(file_name, gender, password)
    #print json.dumps({"liver_parsed_values" : liver_parsed_value}, indent = 4)
    return liver_parsed_value
   
def getKidneyParsedOutput(file_name, gender, password):
    #Instantiate the class
    kidney_profile = KidneyProfile()
    #call loadMetaData Function 
    kidney_profile.loadMetaData()
    #call getParsedData function to get parsed output values
    kidney_parsed_value = kidney_profile.getParsedData(file_name, gender, password)
    #print json.dumps({"kidney_parsed_values" : kidney_parsed_value}, indent = 4)
    return kidney_parsed_value

def getCbcParsedOutput(file_name, gender, password):
    # instantiate class
    cbc_profile = CbcProfile()
    #call loadMetaData Function 
    cbc_profile.loadMetaData()
    #call getParsedData function to get parsed output valuE
    cbc_parsed_value = cbc_profile.getParsedData(file_name, gender, password)    
    return cbc_parsed_value
    
def getVitaminParsedOutput(file_name, gender, password):
    # instantiate class
    vitamin_profile = VitaminsProfile()
    # call loadMetaData Function 
    vitamin_profile.loadMetaData()
    #call getParsedData function to get parsed output value
    vitamin_parsed_value = vitamin_profile.getParsedData(file_name, gender, password)
    return vitamin_parsed_value

def getConfigFile():
    with open("/opt/atman/config/weightage_configuration.json","r") as conf:
        read_config = json.load(conf)
    return read_config.get("weightage_config")


weightage_diabetes = getConfigFile()[0].get("diabetes_parameters") 
weightage_lipid = getConfigFile()[1].get("lipid_parameters")
weightage_kidney = getConfigFile()[2].get("kidney_parameters")
weightage_liver = getConfigFile()[3].get("liver_parameters")
weightage_cbc = getConfigFile()[4].get("cbc_parameters")
weightage_vitamin = getConfigFile()[5].get("vitamins")

 
try:
    if len(sys.argv) < 3:
        print "try e.g."
        print "python __overall_risk.py <category name> <file_name> <password> <gender optional> <user_id optional>"
    else:
        init_db()
        db = get_db()
        file_name = sys.argv[2]
        if len(sys.argv) > 3:
            password = sys.argv[3]
        if len(sys.argv) > 4:
            gender = sys.argv[4]
        if len(sys.argv) > 5:
            user_id = int(sys.argv[5])
            provider_id = int(sys.argv[6])
   
    if sys.argv[1] == "Diabetes":
        diabetes_parsed_values = getDiabetesParsedOutput(file_name, gender, password)
        if user_id not in [None, -1]:
            insert_main(user_id, provider_id, "Diabetes", diabetes_parsed_values)
        json_output, dia_risk = getOverallRisk(diabetes_parsed_values, weightage_diabetes, "diabetes")
        print json_output
    
    elif sys.argv[1] == "Lipid Profile" or sys.argv[1] == "Cardiac":
        lipid_parsed_values = getLipidParsedOutput(file_name, gender, password)
        if user_id not in [None, -1]:
            insert_main(user_id, provider_id, "Lipid Profile", lipid_parsed_values) 
        json_output, lipid_risk = getOverallRisk(lipid_parsed_values, weightage_lipid, "lipid")
        print json_output
    
    elif sys.argv[1] == "Kidney Function":
        kidney_parsed_values = getKidneyParsedOutput(file_name, gender, password)
        if user_id not in [None, -1]:
            insert_main(user_id, provider_id, "Kidney Function", kidney_parsed_values) 
        json_output, kidney_risk = getOverallRisk(kidney_parsed_values, weightage_kidney, "kidney")
        print json_output

    elif sys.argv[1] == "Liver Function":
        liver_parsed_values = getLiverParsedOutput(file_name, gender, password)
        if user_id not in [None, -1]:
            insert_main(user_id, provider_id, "Liver Function", liver_parsed_values)
        json_output, liver_risk = getOverallRisk(liver_parsed_values, weightage_liver, "liver")
        print json_output    
        
    elif sys.argv[1] == "Complete Blood Count":
        cbc_parsed_values = getCbcParsedOutput(file_name, gender, password)
        if user_id not in [None, -1]:
            insert_main(user_id, provider_id, "Complete Blood Count", cbc_parsed_values) 
        json_output_cbc, cbc_risk = getOverallRisk(cbc_parsed_values, weightage_cbc, "complete_blood_count")
        print json_output_cbc
        
    elif sys.argv[1] == "Vitamin-D" or sys.argv[1] == "Vitamin-12":
        vitamin_parsed_values = getVitaminParsedOutput(file_name, gender, password)
        if user_id not in [None, -1]:
            insert_main(user_id, provider_id, "Vitamins", vitamin_parsed_values)
        json_output_vitamin, vitamin_risk = getOverallRisk(vitamin_parsed_values, weightage_vitamin, "vitamins")
        print json_output_vitamin
    

    else:
        diabetes_parsed_values = getDiabetesParsedOutput(file_name, gender, password)
        lipid_parsed_values = getLipidParsedOutput(file_name, gender, password)
        kidney_parsed_values = getKidneyParsedOutput(file_name, gender, password)
        liver_parsed_values = getLiverParsedOutput(file_name, gender, password)
        cbc_parsed_values = getCbcParsedOutput(file_name, gender, password)
        vitamin_parsed_values = getVitaminParsedOutput(file_name, gender, password)
        if user_id not in [None, -1]:
            insert_main(user_id, provider_id, "General", [cbc_parsed_values, diabetes_parsed_values, liver_parsed_values, lipid_parsed_values, kidney_parsed_values, vitamin_parsed_values])
        json_output_dia, dia_risk = getOverallRisk(diabetes_parsed_values, weightage_diabetes, "diabetes")
        json_output_lipid, lipid_risk = getOverallRisk(lipid_parsed_values, weightage_lipid, "lipid")
        json_output_kidney, kidney_risk = getOverallRisk(kidney_parsed_values, weightage_kidney, "kidney")
        json_output_liver, liver_risk = getOverallRisk(liver_parsed_values, weightage_liver, "liver")
        json_output_cbc, cbc_risk = getOverallRisk(cbc_parsed_values, weightage_cbc, "complete_blood_count")
        json_output_vitamin, vitamin_risk = getOverallRisk(vitamin_parsed_values, weightage_vitamin, "vitamins")
        result_overall = OrderedDict()
        diabetes_parsed_values["over_all_risk"] = dia_risk
        lipid_parsed_values["over_all_risk"] = lipid_risk
        kidney_parsed_values["over_all_risk"] = kidney_risk
        liver_parsed_values["over_all_risk"] = liver_risk
        cbc_parsed_values["over_all_risk"] = cbc_risk
        vitamin_parsed_values["over_all_risk"] = vitamin_risk
        result_overall["diabetes"] = diabetes_parsed_values
        result_overall["lipid"] = lipid_parsed_values
        result_overall["kidney"] = kidney_parsed_values
        result_overall["liver"] = liver_parsed_values
        result_overall["complete_blood_count"] = cbc_parsed_values
        result_overall["vitamins"] = vitamin_parsed_values
        print json.dumps(result_overall, indent=4)

except Exception as err:
    #print err
    pass
    
