import os
import json
import sys
from collections import OrderedDict
from __config import *
from __lifestyle_activity import *
from __users import *
from __db_config import *


insurance_need_cat = []
insurance_list = []

insurance_category_general = 0
insurance_category_diabetic = 1
insurance_category_cardiac = 2
insurance_category_hypertension = 3
insurance_category_kidney = 4
insurance_category_obesity = 5
insurance_category_critical_illness = 6

def prepare_insurance_category(age,smoker):
    num_risk = 0
    num_risk_moderate = 0
    
    # if diabetes risk is High or already Diabetic
    # then insurance should cover diabetes related complication
    if (risk_diabetic == 'High' or risk_diabetic == 'Diabetic'):
        num_risk = num_risk + 1
        insurance_need_cat.append(1)

    if (risk_diabetic == 'Moderate'):
        num_risk_moderate = num_risk_moderate + 1

    # if cardiac risk is high or already cardiac
    # insurance should cover cardiac related complication
    if (risk_cardiac == 'High' or risk_cardiac == 'Cardiac'):
        num_risk = num_risk + 1
        insurance_need_cat.append(2)

    if (risk_cardiac == 'Moderate'):
        num_risk_moderate = num_risk_moderate + 1

    # if hypertension then it should cover hypertension
    # related complication
    if (risk_hypertension == 'High' or risk_hypertension == 'Hypertension'):
        num_risk = num_risk + 1
        insurance_need_cat.append(3)

    if (risk_hypertension == 'Moderate'):
        num_risk_moderate = num_risk_moderate + 1

    # if renal risk is high it should cover renal problems
    if (risk_kidney == 'High' or risk_kidney == 'Renal'):
        num_risk = num_risk + 1
        insurance_need_cat.append(4)

    if (risk_kidney == 'Moderate'):
        num_risk_moderate = num_risk_moderate + 1

    # in case of Obesity insurance should cover related complication
    if (risk_obesity == 'High' or risk_obesity == 'Obese'):
        num_risk = num_risk + 1
        insurance_need_cat.append(5)

    if (risk_obesity == 'Moderate'):
        num_risk_moderate = num_risk_moderate + 1

    # if more than 2 risk factor found then suggest to take 
    # some crilical illness insurance policy
    if (num_risk >= 1 or num_risk_moderate >= 2):
        insurance_need_cat.append(6)
    elif (age >= 50 and smoker and num_risk_moderate >= 1):
        insurance_need_cat.append(6)
    else:
        insurance_need_cat.append(0)

def get_user_risk_data_diabetic(user_id,db):
    cursor = db.cursor()
    global risk_diabetic
    try:
        query = "select dia_risk from user_risk_data where user_id=%d" %int(user_id)
        cursor.execute(query)
	risk_data = cursor.fetchone()
	risk_diabetic = risk_data[0]
    except Exception as err:
        print(Exception, err)
        cursor.close()
        return -1
    cursor.close()
    return risk_diabetic


def get_user_risk_data_hypertension(user_id,db):
    cursor = db.cursor()
    global risk_hypertension
    try:
        query = "select htn_risk from user_risk_data where user_id=%d" %int(user_id)
        cursor.execute(query)    
	risk_data = cursor.fetchone() 
	risk_hypertension = risk_data[0]
    except Exception as err:
        print(Exception, err)
        cursor.close()
        return -1
    cursor.close()
    return risk_hypertension


def get_user_risk_data_cardiac(user_id,db):
    cursor = db.cursor()
    global risk_cardiac
    try:
        query = "select card_risk from user_risk_data where user_id=%d" %int(user_id)
        cursor.execute(query)
        risk_data = cursor.fetchone()
        risk_cardiac = risk_data[0]
    except Exception as err:
        print(Exception, err)
        cursor.close()
        return -1
    cursor.close()
    return risk_cardiac


def get_user_risk_data_kidney(user_id,db):
    cursor = db.cursor()
    global risk_kidney
    try:
        query = "select renal_risk from user_risk_data where user_id=%d" %int(user_id)
        cursor.execute(query)
        risk_data = cursor.fetchone()
        risk_kidney = risk_data[0]
    except Exception as err:
        print(Exception, err)
        cursor.close()
        return -1
    cursor.close()
    return risk_kidney

def get_user_risk_data_obesity(user_id,db):
    cursor = db.cursor()
    global risk_obesity
    try:
        query = "select obs_risk from user_risk_data where user_id=%d" %int(user_id)
        cursor.execute(query)
        risk_data = cursor.fetchone()
        risk_obesity = risk_data[0]
    except Exception as err:
        print(Exception, err)
        cursor.close()
        return -1
    cursor.close()
    return risk_obesity

def get_insurance_list(age,db):
    cursor = db.cursor()
    try:
        idx = 0
        while (idx < len(insurance_need_cat)):
            query = "select policy_name, insurance_company, website_link,age_min,age_max from insurance_plans where category=%d" %(insurance_need_cat[idx])
            cursor.execute(query)
            insurance_details_all = cursor.fetchall()
            idx_in = 0
            while (idx_in < len(insurance_details_all)):
                insurance_details = insurance_details_all[idx_in]
                age_min = insurance_details[3]
                age_max = insurance_details[4]
                if get_insurance_eligibility(age,age_min,age_max):
                    insurance_list.append(insurance_details)
                # increment idx_in
                idx_in = idx_in + 1
            # increment idx
            idx = idx + 1
    except Exception as err:
        print (Exception,err)
        cursor.close()
        return -1

    cursor.close()
    return 0

def get_insurance_eligibility(age, age_min, age_max):
    if age in xrange(age_min,age_max+1):
        return True

def json_data_dump(user_id):
    result_json = {}
    json_data = []

    idx = 0
    while (idx < len(insurance_list)):
        insurance_data = OrderedDict()
        insurance = insurance_list[idx]
        insurance_data["Policy Name"] = insurance[0]
        insurance_data["Policy Provider"] = insurance[1]
        insurance_data["Page Link"] = insurance[2]
        insurance_data["Entry Age"] = insurance[3]
        insurance_data["Max Age"] = insurance[4]
        json_data.append(insurance_data)
        idx = idx + 1

    result_json["Health Insurance"] = json_data

    print json.dumps(json_data)

    user_file_str = "/home/isana/atman/pranacare/src/main/sql/user_insurance_data/insurance_plan_%d" %int(user_id)
    
    #open file location and save json data 
    with open(user_file_str, "w+") as f:
        f.write(json.dumps(json_data,ensure_ascii=False))
    close_db()
    exit(0) 


if __name__ == "__main__":
    argc = len(sys.argv) - 1
    if (argc < 1):
	print "python __choose_insurance.py <user_id>"
	print "EX. python __choose_insurance.py 1"
	exit(0)
    
    #initialize database
    init_db()
    db = get_db()

    #get user id
    user_id = sys.argv[1]
    
    #get user info
    user_info = init_user_info(int(user_id))
    
    #prepare user body parameters 
    prepare_user_body_params(db, user_info)    
   
    #get user age
    age = get_user_age()
    
    #prepare user lifestyle habit
    prepare_user_lifestyle_habit(db,user_info)
    
    #check if user is smoker 
    smoker = is_user_smoker()

    #check if user is alcoholic
    alcoholic = is_user_alcoholic()

    #call user risk data and insurance details method
    get_user_risk_data_diabetic(user_id,db)
    get_user_risk_data_cardiac(user_id,db)
    get_user_risk_data_obesity(user_id,db)
    get_user_risk_data_hypertension(user_id,db)
    get_user_risk_data_kidney(user_id,db)

    prepare_insurance_category(age,smoker)

    get_insurance_list(age,db)
    json_data_dump(user_id)

    #close the db
    close_db()

    exit(0)
