import json
import sys
from __config import *
from __db_config import *


parameter_name_dict = {"total_cholesterol":"mr_tc_mg_dl", "hdl_cholesterol":"mr_hdl_mg_dl", "ldl_cholesterol":"mr_ldl_mg_dl", "triglycerides":"mr_trigly_mg_dl", "glucose_fasting":"mr_gluc_fast", "glucose_postprandial":"mr_gluc_pp", "hemoglobin_a1c":"mr_hba1c", "mean_plasma_glucose":"mr_mpg", "blood_urea_nitrogen":"mr_bun", "creatinine":"mr_creatinine", "uric_Acid": "mr_uric_acid", "albumin":"mr_albumin", "globulin":"mr_globulin", "total_protein":"mr_total_protein", "bun_creat_ratio":"mr_bun_creat_ratio", "bilirubin_total":"mr_bil_tot", "bilirubin_direct":"mr_bil_dir", "bilirubin_indirect":"mr_bil_indir", "album_glob_ratio": "mr_album_glob_ratio", "aspartate_aminotransferase":"mr_sgot_ast", "gamma_glutamyl_transferase":"mr_ggt", "alkaline_phosphate":"mr_alk_phosphate", "alanine_transaminase":"mr_sgpt_alt"}

# Function to fetch latest medical report summary 
def getLatestReport(db, user_id, category_name):
    try:
        latest_report = [] 
        cursor = db.cursor()
        query = "select report_summary from user_medical_reports where user_id = %d and report_type = '%s' order by report_date desc limit 1"%(int(user_id),category_name)
        cursor.execute(query)
        report = cursor.fetchone()
        if report[0] is not None:
            latest_report.append(report[0])
        return json.loads(latest_report[0])
    except Exception as err:
        return {}

# Function to get risk reason of medical report based on category name
def riskReasonReport(report_summary, category_name):
    reason_report = {}
    for key, value in report_summary.get(category_name, {}).items():
        if key != "over_all_risk":
            reason_report[key] = value.get("risk", n_a)
    return reason_report

# Function to fetch over_all_risk from report summary
def overallRisk(report_summary, category_name):
    return report_summary.get(category_name, {}).get("over_all_risk", {}).get("risk", n_a) 

# Function will return over_all_risk and risk reason report based on category_name 
def getMedicalReportRisk(db, user_id, category_name):
    report_summary = getLatestReport(db, user_id, category_name)
    return overallRisk(report_summary, category_name), riskReasonReport(report_summary, category_name)

def getReportDateSummary(db, user_id, category_name):
    try:
        report_date_summary = {}
        cursor = db.cursor()
        query = "select report_date, report_summary from user_medical_reports where user_id = %d and report_type = '%s'"%(int(user_id),category_name)
        cursor.execute(query)
        report = cursor.fetchone()
        while report is not None:
            report_date_summary[report[0]] = json.loads(report[1])
            report = cursor.fetchone()
        return report_date_summary
    except Exception as err:
        return {}

def getParameterDateValue(report_summary, category_name, parameter_name):
    if len(report_summary) > 0:
        parameter_date_value = {}
        for key, value in report_summary.items():
            parameter_date_value[key] = value.get(category_name, {}).get(parameter_name, {}).get("reading_value", n_a)
        return parameter_date_value
    else:
        return {}
       
def insertParameterDetails(user_id, parameter_type, parameter_with_date, parameter_name):
    cursor = db.cursor()
    try:
        if len(parameter_with_date) > 0:
            for date, value in parameter_with_date.items():
                query = "INSERT INTO user_history_data(time_key, user_id, provider_id, parameter_type, parameter_name, parameter_value) VALUES(%d, %d, %d, '%s', '%s', '%s')"%(int(date), int(user_id), int(user_id), parameter_type, parameter_name_dict.get(parameter_name), value)
                if value != "None":
                    cursor.execute(query) 
                    db.commit()
            date = max(parameter_with_date)
            value = parameter_with_date.get(date)
            query_1 = "DELETE FROM user_data_update WHERE (user_id=%d AND parameter_name='%s')"%(int(user_id), parameter_name_dict.get(parameter_name))
            query_2 = "INSERT INTO user_data_update(time_key, user_id, provider_id, parameter_type, parameter_name, parameter_value) VALUES(%d, %d, %d, '%s', '%s', '%s')"%(int(date), int(user_id), int(user_id), parameter_type, parameter_name_dict.get(parameter_name), value) 
            if value != "None":
                cursor.execute(query_1)
                cursor.execute(query_2)
                db.commit()
                cursor.close()
    except Exception as err:
        cursor.close()
        return -1
"""
try:
    init_db()
    db = get_db()
    if len(sys.argv) < 3:
        print "try e.g."
        print "python __lifestyle_activity_medical_report.py <user_id> <category_name>"
    else:
        user_id = sys.argv[1]
        category_name = sys.argv[2]
        #diabetes_summary = getLatestReport(db, user_id, category_name)
        #diabetes_report_risk = overallRisk(diabetes_summary, category_name)
        date_summary = getReportDateSummary(db, user_id, category_name)
        parameter_value_tc = getParameterDateValue(date_summary,"lipid", "total_cholesterol")    
        parameter_value_hdl = getParameterDateValue(date_summary,"lipid", "hdl_cholesterol")    
        parameter_value_ldl = getParameterDateValue(date_summary,"lipid", "ldl_cholesterol")    
        parameter_value_trigly = getParameterDateValue(date_summary,"lipid", "triglycerides")    
        insertParameterDetails("lipid_medical_report", parameter_value_tc, "total_cholesterol")
        insertParameterDetails("lipid_medical_report", parameter_value_hdl, "hdl_cholesterol")
        insertParameterDetails("lipid_medical_report", parameter_value_ldl, "ldl_cholesterol")
        insertParameterDetails("lipid_medical_report", parameter_value_trigly, "triglycerides")

except Exception as err:
    print err
"""
