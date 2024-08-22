import sys
import operator
import json
import os
import csv
import datetime
from __composer_config import *
from __composer_insert_data import *
from __db_config import *


def getAllPatientsData(template_file, __composer_config):
    return getAllPatients(template_file, __composer_config)

def getAllWellnessExpertData(template_file, __composer_config):
    return getAllWellnessExpert(template_file, __composer_config)

def getAllDataDateRange(template_file, __composer_config, start_date, end_date, file_name):
    anthropometry_data = json.loads(getAllPatientAnthropometryByDate(template_file, __composer_config, start_date, end_date))
    biochemical_data = json.loads(getAllPatientBiochemicalByDate(template_file, __composer_config, start_date, end_date))
    clinical_data = json.loads(getAllPatientClinicalByDate(template_file, __composer_config, start_date, end_date))
    family_history_data = json.loads(getAllPatientFamilyHistoryByDate(template_file, __composer_config, start_date, end_date))
    lifestyle_habits_data = json.loads(getAllPatientLifestyleHabitsByDate(template_file, __composer_config, start_date, end_date))
    medical_history_data = json.loads(getAllPatientMedicalHistoryByDate(template_file, __composer_config, start_date, end_date))
    dietary_assessment_data = json.loads(getAllPatientDietaryAssessmentByDate(template_file, __composer_config, start_date, end_date))
    personal_history_data = json.loads(getAllPatientPersonalHistoryByDate(template_file, __composer_config, start_date, end_date))
    food_prescription_data = json.loads(getAllPatientFoodPrescriptionByDate(template_file, __composer_config, start_date, end_date))
    pathology_prescription_data = json.loads(getAllPatientPathologyPrescriptionByDate(template_file, __composer_config, start_date, end_date))
    food_frequency_data = json.loads(getAllPatientFoodFrequencyByDate(template_file, __composer_config, start_date, end_date))
    food_recall_data = json.loads(getAllPatientFoodRecallByDate(template_file, __composer_config, start_date, end_date))
    #print (anthropometry_data, biochemical_data, clinical_data, family_history, lifestyle_habits, medical_history, dietary_assessment, personal_history, food_prescription, pathology_prescription)
    if clinical_data != []:
        for i in range(len(clinical_data)):
            patient_id_clinic = clinical_data[i].get("patientId")
            wellness_id_clinic = clinical_data[i].get("wellnessId")
            date_clinic_list = clinical_data[i].get("clinicaldata", [])
            for date_clinic in date_clinic_list:
                if len(date_clinic_list) == 1:
                    mode = "Inserted"
                else:
                    mode = "Updated"
                if date_clinic.get("date") >= datetime.datetime.now().strftime("%Y%m%d") + " 00:00:00" and date_clinic.get("date") <= datetime.datetime.now().strftime("%Y%m%d") + " 23:59:59":
                    _date_clinic = date_clinic.get("date", "")
                    createCsvBlockchainInfo(file_name, wellness_id_clinic, patient_id_clinic,"Clinical", mode, _date_clinic)

    if food_recall_data != []:
        for i in range(len(food_recall_data)):
            patient_id_fr = food_recall_data[i].get("patientId")
            wellness_id_fr = food_recall_data[i].get("wellnessId")
            date_fr_list = food_recall_data[i].get("foodrecall", [])
            for date_fr in date_fr_list:
                if len(date_fr_list) == 1:
                    mode = "Inserted"
                else:
                    mode = "Updated"
                if date_fr.get("date") >= datetime.datetime.now().strftime("%Y%m%d") + " 00:00:00" and date_fr.get("date") <= datetime.datetime.now().strftime("%Y%m%d") + " 23:59:59":
                    _date_fr = date_fr.get("date", "")
                    createCsvBlockchainInfo(file_name, wellness_id_fr, patient_id_fr, "Food_Recall", mode, _date_fr)

    if anthropometry_data != []:
        for i in range(len(anthropometry_data)):
            patient_id_anth = anthropometry_data[i].get("patientId")
            wellness_id_anth = anthropometry_data[i].get("wellnessId")
            date_anth_list = anthropometry_data[i].get("anthropometrydata", [])
            for date_anth in date_anth_list:
                if len(date_anth_list) == 1:
                    mode = "Inserted"
                else:
                    mode = "Updated"
                if str(date_anth.get("date")) >= datetime.datetime.now().strftime("%Y%m%d")+" 00:00:00" and str(date_anth.get("date")) <= datetime.datetime.now().strftime("%Y%m%d") + " 23:59:59":
                    _date_anth = date_anth.get("date", "")
                    createCsvBlockchainInfo(file_name, wellness_id_anth, patient_id_anth, "Anthropometry", mode, _date_anth)
            
    if personal_history_data != []:
        for i in range(len(personal_history_data)):
            patient_id_ph = personal_history_data[i].get("patientId")
            wellness_id_ph = personal_history_data[i].get("wellnessId")
            date_ph_list = personal_history_data[i].get("personalhistory", [])
            for date_ph in date_ph_list:
                if len(date_ph_list) == 1:
                    mode = "Inserted"
                else:
                    mode = "Updated"
                if date_ph.get("date") >= datetime.datetime.now().strftime("%Y%m%d") + " 00:00:00" and date_ph.get("date") <= datetime.datetime.now().strftime("%Y%m%d") + " 23:59:59":
                    _date_ph = date_ph.get("date", "")
                    createCsvBlockchainInfo(file_name, wellness_id_ph, patient_id_ph, "Personal_History", mode, _date_ph)


    if dietary_assessment_data != []:
        for i in range(len(dietary_assessment_data)):
            patient_id_da = dietary_assessment_data[i].get("patientId")
            wellness_id_da = dietary_assessment_data[i].get("wellnessId")
            date_da_list = dietary_assessment_data[i].get("dietaryassessment", [])
            for date_da in date_da_list:
                if len(date_da_list) == 1:
                    mode = "Inserted"
                else:
                    mode = "Updated"
                if date_da.get("date") >= datetime.datetime.now().strftime("%Y%m%d") + " 00:00:00" and date_da.get("date") <= datetime.datetime.now().strftime("%Y%m%d") + " 23:59:59":
                    _date_da = date_da.get("date", "")
                    createCsvBlockchainInfo(file_name, wellness_id_da, patient_id_da, "Dietary_Assessment", mode, _date_da)
        
    if lifestyle_habits_data != []:
        for i in range(len(lifestyle_habits_data)):
            patient_id_ls = lifestyle_habits_data[i].get("patientId")
            wellness_id_ls = lifestyle_habits_data[i].get("wellnessId")
            date_ls_list = lifestyle_habits_data[i].get("lifestylehabits", [])
            for date_ls in date_ls_list:
                if len(date_ls_list) == 1:
                    mode = "Inserted"
                else:
                    mode = "Updated"
                if date_ls.get("date") >= datetime.datetime.now().strftime("%Y%m%d") + " 00:00:00" and date_ls.get("date") <= datetime.datetime.now().strftime("%Y%m%d") + " 23:59:59":
                    _date_ls = date_ls.get("date", "")
                    createCsvBlockchainInfo(file_name, wellness_id_ls, patient_id_ls, "Lifestyle", mode, _date_ls)

    if food_frequency_data != []:
        for i in range(len(food_frequency_data)):
            patient_id_ff = food_frequency_data[i].get("patientId")
            wellness_id_ff = food_frequency_data[i].get("wellnessId")
            date_ff_list = food_frequency_data[i].get("foodfrequency", [])
            for date_ff in date_ff_list:
                if len(date_ff_list) == 1:
                    mode = "Inserted"
                else:
                    mode = "Updated"
                if date_ff.get("date") >= datetime.datetime.now().strftime("%Y%m%d") + " 00:00:00" and date_ff.get("date") <= datetime.datetime.now().strftime("%Y%m%d") + " 23:59:59":
                    _date_ff = date_ff.get("date", "")
                    createCsvBlockchainInfo(file_name, wellness_id_ff, patient_id_ff, "Food_Frequency", mode, _date_ff)

    if biochemical_data != []:
        for i in range(len(biochemical_data)):
            patient_id_bio = biochemical_data[i].get("patientId")
            wellness_id_bio = biochemical_data[i].get("wellnessId")
            date_bio_list = biochemical_data[i].get("biochemical")
            for date_bio in date_bio_list:
                if len(date_bio_list) == 1:
                    mode = "Inserted"
                else:
                    mode = "Updated"
                if date_bio.get("date") >= datetime.datetime.now().strftime("%Y%m%d") + " 00:00:00" and date_bio.get("date") <= datetime.datetime.now().strftime("%Y%m%d") + " 23:59:59":
                    _date_bio = date_bio.get("date", "")
                    createCsvBlockchainInfo(file_name, wellness_id_bio, patient_id_bio,"Biochemical", mode, _date_bio)

    if family_history_data != []:
        for i in range(len(family_history_data)):
            patient_id_fh = family_history_data[i].get("patientId")
            wellness_id_fh = family_history_data[i].get("wellnessId")
            date_fh_list = family_history_data[i].get("familyhistory", [])
            for date_fh in date_fh_list:
                if len(date_fh_list) == 1:
                    mode = "Inserted"
                else:
                    mode = "Updated"
                if date_fh.get("date") >= datetime.datetime.now().strftime("%Y%m%d") + " 00:00:00" and date_fh.get("date") <= datetime.datetime.now().strftime("%Y%m%d") + " 23:59:59":
                    _date_fh = date_fh.get("date", "")
                    createCsvBlockchainInfo(file_name, wellness_id_fh, patient_id_fh, "Family History", mode, _date_fh)


    if medical_history_data != []:
        for i in range(len(medical_history_data)):
            patient_id_mh = medical_history_data[i].get("patientId")
            wellness_id_mh = medical_history_data[i].get("wellnessId")
            date_mh_list = medical_history_data[i].get("medicalhistory", []) 
            for date_mh in date_mh_list:
                if len(date_mh_list) == 1:
                    mode = "Inserted"
                else:
                    mode = "Updated"
                if date_mh.get("date") >= datetime.datetime.now().strftime("%Y%m%d") + " 00:00:00"  and date_mh.get("date") <= datetime.datetime.now().strftime("%Y%m%d") + " 23:59:59":
                    _date_mh = date_mh.get("date", "")
                    createCsvBlockchainInfo(file_name, wellness_id_mh, patient_id_mh,"Medical History", mode, _date_mh)



    if food_prescription_data != []:
        for i in range(len(food_prescription_data)):
            patient_id_fp = food_prescription_data[i].get("patientId")
            wellness_id_fp = food_prescription_data[i].get("wellnessId")
            date_fp_list = food_prescription_data[i].get("foodprescription", [])
            for date_fp in date_fp_list: 
                if len(date_fp_list) == 1:
                    mode = "Inserted"
                else:
                    mode = "Updated"
                if date_fp.get("date") >= datetime.datetime.now().strftime("%Y%m%d") + " 00:00:00" and date_fp.get("date") <= datetime.datetime.now().strftime("%Y%m%d") + " 23:59:59":
                    _date_fp = date_fp.get("date", "")
                    createCsvBlockchainInfo(file_name, wellness_id_fp, patient_id_fp,"Food Prescription", mode, _date_fp)

    if pathology_prescription_data != []:
        for i in range(len(pathology_prescription_data)):
            patient_id_pp = pathology_prescription_data[i].get("patientId")
            wellness_id_pp = pathology_prescription_data[i].get("wellnessId")
            date_pp_list = pathology_prescription_data[i].get("pathologyprescription", [])
            for date_pp in date_pp_list:
                if len(date_pp_list) == 1:
                    mode = "Inserted"
                else:
                    mode = "Updated"
                if date_pp.get("date") >= datetime.datetime.now().strftime("%Y%m%d") + " 00:00:00" and date_pp.get("date") <= datetime.datetime.now().strftime("%Y%m%d") + " 23:59:59":
                    _date_pp = date_pp.get("date", "")
                    createCsvBlockchainInfo(file_name, wellness_id_pp, patient_id_pp, "Pathology Prescription", mode, _date_pp)
           
      
    
def createCsvBlockchainInfo(file_name, wellness_id, patient_id, asset, mode, timestamp):
    try:
        query = "SELECT name from users where email='%s'"%(wellness_id)
        cursor = db.cursor()
        cursor.execute(query)
        wellness_name = cursor.fetchone()[0]
        query = "SELECT id, name from users where email='%s'"%(patient_id)
        cursor.execute(query)
        _patient_id = cursor.fetchone()[0]
        file_exists = os.path.isfile(file_name)
        with open(file_name, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=["Dietition Name", "Patient", "Asset Name","Date Time", "Mode"])
            if not file_exists:
                writer.writeheader()
            fields = {"Dietition Name" : wellness_name, "Patient": "patient_"+ str(_patient_id), "Asset Name":asset, "Date Time": timestamp, "Mode":mode}
            writer.writerow(fields)
            return file_name
    except Exception as err:
        cursor.close()
        print err


if __name__ == "__main__":
    init_db()
    db = get_db()
    __composer_config = ComposerConfig()
    template_file = __composer_config.getJsonTemplate()
    header = json.loads(__composer_config.getHeader(template_file))
    file_name = "/opt/atman/bin/composer_blockchain_data_" + datetime.datetime.now().strftime("%Y%m%d") + ".csv" 
    start_date = sys.argv[1]
    end_date = sys.argv[2]
    getAllDataDateRange(template_file, __composer_config, start_date, end_date, file_name)
    with open(file_name) as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=",")
        sortedlist = sorted(spamreader, key=lambda row:(row['Date Time']), reverse=False)

    with open("/opt/atman/bin/_composer_blockchain_data_" + datetime.datetime.now().strftime("%Y%m%d") + ".csv", 'w') as f:
        fieldnames = ["Dietition Name", "Patient", "Asset Name","Date Time", "Mode"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in sortedlist:
            writer.writerow(row)
    os.system("/bin/rm -r "+file_name)
