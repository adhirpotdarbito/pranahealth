import requests
import time
from __composer_config import *
from __composer_insert_data import *
from __db_config import *


def getId(db, patient_id):
    """
        Function to get patient email and wellness email id
    """
    cursor = db.cursor()
    query_1 = "SELECT email from users where id=%d"%(int(patient_id))
    cursor.execute(query_1)
    patient_email = cursor.fetchone()[0] 
    query_2 = "select email from users where id=(select admin_id from admin_patient_mapping where patient_id=%d) and role='DIETITION_ACL'"%(int(patient_id))
    cursor.execute(query_2)
    wellness_email = cursor.fetchone()[0]
    return patient_email, wellness_email

def getMiscData(db, patient_id):
    """
        Function to get list of misc data for patient from user_history_data table
    """
    misc_data_list = [] 
    cursor = db.cursor()
    query = "select timestamp, parameter_value from user_history_data where parameter_type='User Misc Data' and user_id=%d"%(int(patient_id))
    cursor.execute(query)
    get_misc = cursor.fetchone()
    while get_misc is not None:
        misc_data_dict = {}
        misc_data_dict["date"] = str(get_misc[0]).replace("-", "")
        misc_data_dict["misc_data"] = get_misc[1]
        misc_data_list.append(misc_data_dict)
        get_misc = cursor.fetchone()
    return misc_data_list
   
def getFoodPrescriptionData(db, patient_id):
    """
        Function to get list of food prescription for patient from user_history_data table
    """
    food_prescription_list = []
    cursor = db.cursor()
    query = "SELECT at.created_date, ft.instance FROM admin_patient_food_prescription_template at, food_prescription_template_instance ft WHERE at.template_instance_id=ft.instance_id and patient_id=%d"%(int(patient_id))
    cursor.execute(query)
    get_data = cursor.fetchone()
    while get_data is not None:
        food_prescription_dict = {}
        food_prescription_dict["date"] = str(get_data[0]).replace("-", "")
        food_prescription_dict["food_prescription"] = get_data[1]
        food_prescription_list.append(food_prescription_dict)
        get_data = cursor.fetchone()
    return food_prescription_list

def getPathologyPrescriptionData(db, patient_id):
    """
        Function to get list of pathology prescription for patient from user_history_data table
    """
    pathology_prescription_list = []
    cursor = db.cursor()
    query = "select timestamp, patho_prescription from admin_patient_patho_prescription where patient_id=%d"%(int(patient_id))
    cursor.execute(query)
    get_data = cursor.fetchone()
    while get_data is not None:
        pathology_prescription_dict = {}
        pathology_prescription_dict["date"] = str(get_data[0]).replace("-", "")
        pathology_prescription_dict["pathology_prescription"] = get_data[1]
        pathology_prescription_list.append(pathology_prescription_dict)
        get_data = cursor.fetchone()
    return pathology_prescription_list

def getFamilyHistoryData(db, patient_id):
    """
        Function to get list of family history data for patient from user_history_data table
    """
    family_history_list = []
    family_history_data = {}
    family_history_dict = {}
    cursor = db.cursor()
    query = "SELECT user_id, timestamp, parameter_type, parameter_name, parameter_value from user_history_data WHERE parameter_type='User Family History' and user_id=%d order by parameter_name"%(int(patient_id))
    cursor.execute(query)
    get_data = cursor.fetchone()
    if get_data is not None:
        family_history_dict["date"] = str(get_data[1]).replace("-", "")
        family_history_data["id"] = int(get_data[0])
    while get_data is not None:
        family_history_data[get_data[3]] = get_data[4]
        get_data = cursor.fetchone() 
    family_history_dict["family_history"] = family_history_data
    if family_history_dict.get("family_history") != {}:
        family_history_list.append(family_history_dict)
    return family_history_list
       
def getMedicalHistory(db, patient_id):
    """
      Function to get list of medical history data for patient from user_history_data table 
    """
    medical_history_list = []
    cursor = db.cursor()
    query = "SELECT timestamp, parameter_type, parameter_name, parameter_value from user_history_data WHERE parameter_type='User Medical Data' and parameter_name='user_medical_report' and user_id=%d"%(int(patient_id))
    cursor.execute(query)
    get_data = cursor.fetchone()
    while get_data is not None:
        medical_history_dict = {}
        medical_history_dict["date"] = str(get_data[0]).replace("-", "")
        medical_history_dict["medical_history"] = get_data[1]
        medical_history_list.append(medical_history_dict)
        get_data = cursor.fetchone()
    return medical_history_list
      
 
def storeDataToHyperledger(misc_data_lists, food_prescription_lists, path_prescription_lists, patient_id, wellness_id, wellness_type, wellness_info):
    __composer_config = ComposerConfig()
    template_file = __composer_config.getJsonTemplate()
    header = json.loads(__composer_config.getHeader(template_file))
    start_time = time.time()
    print ("Started Storing data for: " + patient_id)
    if getWellnessExpertById(wellness_id, template_file, __composer_config) != 200:
        print("Adding wellness Expert "+wellness_id)
        insertWellnessExpert(wellness_id, wellness_type, wellness_info, template_file, __composer_config, header)
    if getPatientById(patient_id, template_file, __composer_config) != 200:
        print("Adding Patient "+patient_id)
        insertPatient(patient_id, wellness_id, template_file, __composer_config, header)
    if getDataAccessorById(wellness_id, template_file, __composer_config) != 200:
        print("Adding Data Accessor "+wellness_id)
        insertDataAccessor(wellness_id, wellness_type,template_file, __composer_config, header)
    
    for misc_dict in misc_data_lists:
        date = misc_dict.get("date", "") 
        asset_keys = json.loads(unicode(misc_dict.get("misc_data", {}), errors='replace'))
        _asset_keys = asset_keys.keys()
        for asset in _asset_keys:
            if asset == "Personal_History":
                personal_history = str(asset_keys.get(asset, {}))
                if getPatientPersonalHistory(patient_id,template_file, __composer_config) == 200:
                    print (asset + " appended for " + patient_id + ": " + date)
                    updatePatientPersonalHistory(patient_id, date, personal_history, template_file, __composer_config, header)
                else:
                    print (asset + " Inserted for " + patient_id + ": " + date)
                    insertPatientPersonalHistory(patient_id, wellness_id, date, personal_history, wellness_id, template_file, __composer_config, header)
            elif asset == "BioChemical":
                biochemical = str(asset_keys.get(asset, {}))
                if getPatientBiochemicalData(patient_id,template_file, __composer_config) == 200:
                    print (asset + " appended for " + patient_id + ": " + date)
                    updatePatientBiochemicalData(patient_id, date, biochemical, template_file, __composer_config, header)
                else:
                    print (asset + " Inserted for " + patient_id + ": " + date)
                    insertPatientBiochemicalData(patient_id, wellness_id, date, biochemical, wellness_id, template_file, __composer_config, header)
            elif asset == "Food_Frequency":
                food_frequency = str(asset_keys.get(asset, {}))
                if getPatientFoodFrequency(patient_id,template_file, __composer_config) == 200:
                    print (asset + " appended for " + patient_id + ": " + date)
                    updatePatientFoodFrequency(patient_id, date, food_frequency, template_file, __composer_config, header)
                else:
                    print (asset + " Inserted for " + patient_id + ": " + date)
                    insertPatientFoodFrequency(patient_id, wellness_id, date, food_frequency, wellness_id, template_file, __composer_config, header)
            elif asset == "Lifestyle":
                lifestyle_habit = str(asset_keys.get(asset, {}))
                if getPatientLifestyleHabit(patient_id,template_file, __composer_config) == 200:
                    print (asset + " appended for " + patient_id + ": " + date)
                    updatePatientLifestyleHabits(patient_id, date, lifestyle_habit, template_file, __composer_config, header)
                else:
                    print (asset + " Inserted for " + patient_id + ": " + date)
                    insertPatientLifestyleHabits(patient_id, wellness_id, date, lifestyle_habit, wellness_id, template_file, __composer_config, header)
            elif asset == "Anthropometry":
                anthropometry = str(asset_keys.get(asset, {}))
                if getPatientAnthropometryData(patient_id,template_file, __composer_config) == 200:
                    print (asset + " appended for " + patient_id + ": " + date)
                    updatePatientAnthropometryData(patient_id, date, anthropometry, template_file, __composer_config, header)
                else:
                    print (asset + " Inserted for " + patient_id + ": " + date)
                    insertPatientAnthropometryData(patient_id, wellness_id, date, anthropometry, wellness_id, template_file, __composer_config, header)
            elif asset == "Clinical":
                clinical = str(asset_keys.get(asset, {}))
                if getPatientClinicalData(patient_id,template_file, __composer_config) == 200:
                    print (asset + " appended for " + patient_id + ": " + date)
                    updatePatientClinicalData(patient_id, wellness_id, date, clinical, template_file, __composer_config, header)
                else:
                    print (asset + " Inserted for " + patient_id + ": " + date)
                    insertPatientClinicalData(patient_id, wellness_id, date, clinical, wellness_id, template_file, __composer_config, header)
            elif asset == "Dietary_Assessment":
                dietary_assessment = str(asset_keys.get(asset, {}))
                if getPatientDietaryAssessment(patient_id,template_file, __composer_config) == 200:
                    print (asset + " appended for " + patient_id + ": " + date)
                    updatePatientDietaryAssessment(patient_id, date, dietary_assessment, template_file, __composer_config, header)
                else:
                    print (asset + " Inserted for " + patient_id + ": " + date)
                    insertPatientDietaryAssessmentData(patient_id, wellness_id, date, dietary_assessment, wellness_id, template_file, __composer_config, header)
            elif asset == "Food_Recall":
                food_recall = str(asset_keys.get(asset, {}))
                if getPatientFoodRecall(patient_id,template_file, __composer_config) == 200:
                    print (asset + " appended for " + patient_id + ": " + date)
                    updatePatientFoodRecall(patient_id, date, food_recall, template_file, __composer_config, header)
                else:
                    print (asset + " Inserted for " + patient_id + ": " + date)
                    insertPatientFoodRecall(patient_id, wellness_id, date, food_recall, wellness_id, template_file, __composer_config, header)
    
    if food_prescription_lists != []:
        for food_pres_dict in food_prescription_lists:
            date = food_pres_dict.get("date", "")
            food_prescription = str(json.loads(unicode(str(food_pres_dict.get("food_prescription", "{}")), errors='ignore'))).replace('"','\\"')
            if getPatientFoodPrescription(patient_id, template_file, __composer_config) == 200:
                print ("Food_Prescription Appended for " + patient_id + ": " + date)
                updatePatientFoodPrescription(patient_id, date, food_prescription, template_file, __composer_config, header)
            else:
                print ("Food_Prescription Inserted for " + patient_id + ": " + date)
                insertPatientFoodPrescription(patient_id, wellness_id, date, food_prescription, wellness_id, template_file, __composer_config, header)

    if path_prescription_lists != []:
        for path_pres_dict in path_prescription_lists:
            date = path_pres_dict.get("date", "")
            pathology_prescription = str(json.loads(unicode(str(path_pres_dict.get("pathology_prescription", "{}")), errors='ignore'))).replace('"','\\"')
            if getPatientPathologyPrescription(patient_id, template_file, __composer_config) == 200:
                print ("Pathology_Prescription Appended for " + patient_id + ": " + date)
                updatePatientPathologyPrescription(patient_id, date, pathology_prescription, template_file, __composer_config, header)
            else:
                print ("Pathology_Prescription Inserted for " + patient_id + ": " + date)
                insertPatientPathologyPrescription(patient_id, wellness_id, date, pathology_prescription, wellness_id, template_file, __composer_config, header)

    if family_history_lists != []:
        for family_history_dict in family_history_lists:
            date = family_history_dict.get("date", "")
            family_history = str(family_history_dict.get("family_history", "{}"))      
            if getPatientFamilyHistory(patient_id, template_file, __composer_config) == 200:
                print ("Family History Appended for " + patient_id + ": " + date)
                updatePatientFamilyHistory(patient_id, date, family_history, template_file, __composer_config, header)    
            else:
                print ("Family History Inserted for " + patient_id + ": " + date)
                insertPatientFamilyHistory(patient_id, wellness_id, date, family_history, wellness_id, template_file, __composer_config, header)

    if medical_history_lists != []:
        for medical_history_dict in medical_history_lists:
            date = medical_history_dict.get("date", "")
            medical_history = str(medical_history_dict.get("medical_history", "{}"))
            if getPatientMedicalHistory(patient_id, template_file, __composer_config) == 200:
                print ("Medical History Appended for " + patient_id + ": " + date)
                updatePatientMedicalHistory(patient_id, date, medical_history, template_file, __composer_config, header)
            else:
                print ("Medical History Inserted for " + patient_id + ": " + date)
                insertPatientMedicalHistory(patient_id, wellness_id, date, medical_history, wellness_id, template_file, __composer_config, header)



    print ("Assets for "+ patient_id +" stored successfully.")
    print ("--- %s seconds ---" % (time.time() - start_time))
    print ("==========================================================================")

 
def getPatientIdList(db):
    patient_list = []
    cursor = db.cursor()
    query = "SELECT patient_id from admin_patient_mapping WHERE admin_id not in (70,226,252,513,72,212)"
    cursor.execute(query)
    get_data = cursor.fetchone()
    while get_data is not None:
        patient_list.append(get_data[0])
        get_data = cursor.fetchone()
    return patient_list
         
    

if __name__ == "__main__":
    init_db()
    db = get_db()
    patient_lists = getPatientIdList(db)
    for patient_id in patient_lists:
        if patient_id != 268:
            patient_email, wellness_email = getId(db, patient_id)
            misc_data_lists = getMiscData(db, patient_id)
            family_history_lists = getFamilyHistoryData(db, patient_id)
            medical_history_lists = getMedicalHistory(db, patient_id)
            food_prescription_lists = getFoodPrescriptionData(db, patient_id)
            path_prescription_lists = getPathologyPrescriptionData(db, patient_id)
            storeDataToHyperledger(misc_data_lists, food_prescription_lists, path_prescription_lists, patient_email, wellness_email, "Dietitian", {})
    close_db()
  


