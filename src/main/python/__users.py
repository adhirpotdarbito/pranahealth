'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

import sys
from datetime import *
from dateutil.relativedelta import relativedelta
from __config import *

user_info = None
lifestyle_habit = getLifestyleHabitsMetadata()

class __user_info:
    def __init__(self,id):
        self.user_id = id
        self.user_basic_data = self.__user_basic_data()
        self.user_lifestyle_habit = self.__user_lifestyle_habit()
        self.user_medical_data = self.__user_medical_data()
        self.user_body_param = self.__user_body_param()
        self.user_cardiac_risk_data = self.__user_cardiac_risk_data()
        self.user_family_history = self.__user_family_history()
    class __user_basic_data:
        name = None
        email = None
        contact = None
        country = None
        city = None
        gender = None
    class __user_lifestyle_habit:
        smoker = None
        alcoholic = None
        stress = None
        junk_food_lover = None
        exercise = None
    class __user_medical_data:
        existing_disease = None
        current_medication = None
        past_disease = None
        cholesterol = None
    class __user_body_param:
        bod = 0
        age = 0.0
        height = 0.0
        weight = 0.0
        waist = 0.0
    class __user_cardiac_risk_data:
        tc_mg_dl = 0.0
        hdl_mg_dl = 0.0
        sbp_mm_hg = 0
        dp_mm_hg = 0
        bp_treated = None
    class __user_family_history:
        parent_diabetes = None
        parent_cardiac = None
        parent_obese = None
        parent_hypertension = None
        family_kidney = None
        parent_depression = None

def init_user_info(id):
    global user_info
    user_info = __user_info(id)
    return user_info

def get_user_info():
    global user_info
    return user_info

def print_user_info (user_info):
    print user_info.user_id
    print (user_info.user_basic_data.name,user_info.user_basic_data.email,user_info.user_basic_data.country)

# ideal weight for female according to height
weight_matrix_female = {137: [28.5,34.9],140: [30.8,37.6],142: [32.6,39.9],145: [34.9,42.6], 147: [36.4,44.9], 150: [39,47.6], 152: [40.8,49.9], 155: [43.1,52.6], 157: [44.9,54.9], 160: [47.2,57.6], 163: [49,59.9], 165: [51.2,62.6], 168: [53,64.8], 170: [55.3,67.6], 173: [57.1,69.8], 175: [59.4,72.6], 178: [61.2,74.8], 180: [63.5,77.5], 183: [65.3,79.8], 185: [67.6,82.5], 188: [69.4,84.8], 191: [71.6,87.5], 193: [73.5,89.8], 195: [75.7,92.5], 198: [77.5,94.8], 201: [79.8,97.5], 203: [81.6,99.8], 205: [83.9,102.5], 208: [85.7,104.8], 210: [88,107.5], 213: [89.8,109.7]}

# ideal weight for male according to height
weight_matrix_male = {137: [28.5,34.9],140: [30.8,38.1],142: [33.5,40.8],145: [35.8,43.9], 147: [38.5,46.7], 150: [40.8,49.9], 152: [43.1,53], 155: [45.8,55.8], 157: [48.1,58.9], 160: [50.8,61.6], 163: [53,64.8], 165: [55.3,68], 168: [58,70.7], 170: [60.3,73.9], 173: [63,76.6], 175: [65.3,79.8], 178: [67.6,83], 180: [70.3,85.7], 183: [72.6,88.9], 185: [75.3,91.6], 188: [77.5,94.8], 191: [79.8,98], 193: [82.5,100.6], 195: [84.8,103.8], 198: [87.5,106.5], 201: [89.8,109.7], 203: [92,112.9], 205: [94.8,115.6], 208: [97,118.8], 210: [99.8,121.5], 213: [102,124.7]}

# ideal weight for boy according to age
ideal_weight_boy_kg = {1: "9.6", 2: "12.5", 3: "14.0", 4: "16.3", 5: "18.4", 6: "20.6", 7: "22.9", 8: "25.6", 9: "28.6", 10: "32", 11: "35.6", 12: "39.9", 13: "45.3", 14: "50.8", 15: "56.0", 16: "60.8", 17: "64.4", 18: "66.9", 19: "68.9", 20: "70.3"}

# ideal weight for girl according to age
ideal_weight_girl_kg = {1: "9.2", 2: "12.0", 3: "14.2", 4: "15.4", 5: "17.9", 6: "19.9", 7: "22.4", 8: "25.8", 9: "28.1", 10: "31.9", 11: "36.9", 12: "41.5", 13: "45.8", 14: "47.6", 15: "52.1", 16: "53.5", 17: "54.4", 18: "56.7", 19: "57.1", 20: "58.0"}


def calculate_age(bod_str):
    # check if bod is equal to current date
    if str(bod_str[0:4]) == date.today().strftime("%Y%m%d")[0:4] or (int(bod_str) >= int(((datetime.today()- relativedelta(months=12)).strftime("%Y%m%d")))):
	return 1   
    #Note: bod_str is expected to be in YYYYMMDD format e.g. 19740504
    else:
        today = date.today()
        boddate = datetime(year=int(bod_str[0:4]), month=int(bod_str[4:6]), day=int(bod_str[6:8])).date() 
        return today.year - boddate.year - ((today.month, today.day) < (boddate.month, boddate.day))

def is_user_overweight(gender,height,weight):
    max_weight = 0
    if (gender == 'Male'):
        range = weight_matrix_male[height]
    else:
        range = weight_matrix_female[height]

    max_weight = range[1]

    if weight > max_weight:
        return 1

    return 0

def get_user_ideal_weight(gender, height, age):
    if age >= 1 and age <= 20:
        if (gender == 'Male'):
            return float(ideal_weight_boy_kg[age])
        else:
            return float(ideal_weight_girl_kg[age])     
    else:
        if height >= 152.0:
            if (gender == 'Male'):
                ideal_body_weight = 50.0 + 2.3*((height/2.54) - 60)
            else:
                ideal_body_weight = 45.5 + 2.3*((height/2.54) - 60)
            return ideal_body_weight
        else:
            ideal_body_weight = (height*height)*(1.65)/1000
            return ideal_body_weight   

def is_user_underweight(gender,height,weight):
    min_weight = 0
    if (gender == 'Male'):
        range = weight_matrix_male[height]
    else:
        range = weight_matrix_female[height]

    min_weight = range[0]

    if weight < min_weight:
        return 1

    return 0

def is_user_hypertensive(sbp):
    severity = 0
    if sbp <= 0:
        severity = -1
    if (sbp > 120 and sbp < 140):
        severity = 1
    if (sbp >= 140 and sbp<160):
        severity = 2
    if (sbp >= 160):
        severity = 3

    return severity

def get_user_bmi(height,weight):
    height_meter = height/100.0
    bmi = weight/(height_meter*height_meter)
    return bmi

# age group list
age_group = {0: [0, 2], 1: [3, 5], 2: [6, 13], 3: [14, 18], 4: [19, 40], 5: [41, 60], 6: [61, 200]}
age_enum = ['INFANT','YOUNGER_CHILD','OLDER_CHILD','PRE_ADULT','YOUNG_ADULT','ADULT','SENIOR']

def get_age_group(age):
    pos = 0
    while (pos < len(age_group)):
        entry = age_group[pos]
        if(age >= entry[0] and age <= entry[1]):
            return age_enum[pos]
        pos = pos + 1

def prepare_user_family_data(db,user_info):
    cursor = db.cursor()
    try:
        query_str = "select diabetes,cardiac,hypertension,obesity,asthma,depression from user_family_history where id=%d" %user_info.user_id
        cursor.execute(query_str)
        user_details = cursor.fetchone()
        user_info.user_family_history.parent_diabetes = str(user_details[0])
        user_info.user_family_history.parent_cardiac = str(user_details[1])
        user_info.user_family_history.parent_hypertension = str(user_details[2])
        user_info.user_family_history.parent_obese = str(user_details[3])
        user_info.user_family_history.family_kidney = str(user_details[4])
        user_info.user_family_history.parent_depression = str(user_details[5])
    except Exception as err:
        #print (Exception,err)
        #print "Fatal: prepare_user_family_data"
        cursor.close()
        user_info.user_family_history.parent_diabetes = ''
        user_info.user_family_history.parent_cardiac = ''
        user_info.user_family_history.parent_hypertension = ''
        user_info.user_family_history.parent_obese = ''
        user_info.user_family_history.family_kidney = ''
        user_info.user_family_history.parent_depression = ''
        return 0
    cursor.close()
    return 0

def prepare_user_cr_data(db,user_info):
    cursor = db.cursor()
    try:
        query_str = "select tc_mg_dl,hdl_mg_dl,sbp_mm_hg,bp_treated,dp_mm_hg from user_cr_risk where id=%d" %user_info.user_id
        cursor.execute(query_str)
        user_cr_details = cursor.fetchone()
        user_info.user_cardiac_risk_data.tc_mg_dl = float(user_cr_details[0])
        user_info.user_cardiac_risk_data.hdl_mg_dl = float(user_cr_details[1])
        user_info.user_cardiac_risk_data.sbp_mm_hg = int(user_cr_details[2])
        user_info.user_cardiac_risk_data.bp_treated = str(user_cr_details[3])
        user_info.user_cardiac_risk_data.dp_mm_hg = int(user_cr_details[4])
    except Exception as err:
        #print (Exception, err)
        #print "Fatal: Prepare user cardiac risk data"
        cursor.close()
        user_info.user_cardiac_risk_data.tc_mg_dl = 0.0
        user_info.user_cardiac_risk_data.hdl_mg_dl = 0.0
        user_info.user_cardiac_risk_data.sbp_mm_hg = 0
        user_info.user_cardiac_risk_data.bp_treated = ''
        user_info.user_cardiac_risk_data.dp_mm_hg = 0
        return 0

    cursor.close()
    return 0

def prepare_user_body_params(db,user_info):
    cursor = db.cursor()
    try:
        query_str = "select height,weight,bod,waist from user_body_param where id=%d" %user_info.user_id
        cursor.execute(query_str)
        user_details = cursor.fetchone()
        user_info.user_body_param.height = float(user_details[0])
        user_info.user_body_param.weight = float(user_details[1])
        user_info.user_body_param.bod = user_details[2]
        user_info.user_body_param.waist = float(user_details[3])
        user_info.user_body_param.age = float(calculate_age(str(user_info.user_body_param.bod)))
    except Exception as err:
        print (Exception, err)
        print "Fatal: Prepare user body parameter."
        cursor.close()
        return -1

    cursor.close()
    return 0

def prepare_user_medical_data(db,user_info):
    cursor = db.cursor()
    try:
        query_str = "select existing_disease,current_medication,past_disease,cholesterol from user_medical_data where id=%d" %user_info.user_id
        cursor.execute(query_str)
        user_details = cursor.fetchone()
        user_info.user_medical_data.existing_disease = str(user_details[0])
        user_info.user_medical_data.current_medication = str(user_details[1])
        user_info.user_medical_data.past_disease = str(user_details[2])
        user_info.user_medical_data.cholesterol = str(user_details[3])
    except Exception as err:
        #print (Exception, err)
        #print "Fatal: Prepare user medical data."
        cursor.close()
        user_info.user_medical_data.existing_disease = ''
        user_info.user_medical_data.current_medication = ''
        user_info.user_medical_data.past_disease = ''
        user_info.user_medical_data.cholesterol = ''
        return 0
    cursor.close()
    return 0

def prepare_user_lifestyle_habit(db,user_info):
    cursor = db.cursor()
    try:
        query_str = "select smoker,alcoholic,junk_food_lover,stress,regular_exercise from user_ls_habit where id=%d" %user_info.user_id
        cursor.execute(query_str)
        user_details = cursor.fetchone()
        user_info.user_lifestyle_habit.smoker = str(user_details[0])
        user_info.user_lifestyle_habit.alcoholic = str(user_details[1])
        user_info.user_lifestyle_habit.junk_food_lover = str(user_details[2])
        user_info.user_lifestyle_habit.stress = str(user_details[3])
        user_info.user_lifestyle_habit.exercise = str(user_details[4])
    except Exception as err:
        #print (Exception, err)
        #print "Fatal: Prepare user lifestyle habits."
        cursor.close()
        user_info.user_lifestyle_habit.smoker = ''
        user_info.user_lifestyle_habit.alcoholic = ''
        user_info.user_lifestyle_habit.junk_food_lover = ''
        user_info.user_lifestyle_habit.stress = ''
        user_info.user_lifestyle_habit.exercise = ''
        return 0
    cursor.close()
    return 0

def get_tc_hdl_ratio(tc,hdl):
    try:
        return (tc/hdl)
    except Exception as err:
	return 0

# TBD need to add to score user specific details for more accurate result
# Ex. Like we should check smoking habit for cardiac
# disease ratio between male/female and add weight according to that
# add weight if any pre-existing disease can lead to current disease
# add weight based on user geo location
# any medication that lead to current symptoms etc. etc.

def prepare_user_basic_data(db,user_info):
    # prepare a cursor obj
    cursor = db.cursor()
    try:
        query_str = "select name, email, gender,country,city,contact from users where id=%d" %user_info.user_id
        cursor.execute(query_str)
        user_detail = cursor.fetchone()
        user_info.user_basic_data.name = str(user_detail[0])
        user_info.user_basic_data.email = str(user_detail[1])
        user_info.user_basic_data.gender = str(user_detail[2])
        user_info.user_basic_data.country = str(user_detail[3])
        user_info.user_basic_data.city = str(user_detail[4])
        user_info.user_basic_data.contact = str(user_detail[5])
    except Exception as err:
        print (Exception, err)
        print("Unexpected error: prepare_user_basic_data", sys.exc_info()[0])
        cursor.close()
        return -1
    # close the cursor
    cursor.close()
    return 0

def get_user_sex():
    user_info = get_user_info()
    return user_info.user_basic_data.gender

def get_user_age():
    user_info = get_user_info()
    return user_info.user_body_param.age

def get_user_height():
    user_info = get_user_info()
    return user_info.user_body_param.height

def get_user_weight():
    user_info = get_user_info()
    return user_info.user_body_param.weight

def get_user_city():
    user_info = get_user_info()
    return user_info.user_basic_data.city

def get_user_country():
    user_info = get_user_info()
    return user_info.user_basic_data.country

def get_user_existing_disease():
    user_info = get_user_info()
    return user_info.user_medical_data.existing_disease

def get_user_past_disease():
    user_info = get_user_info()
    return user_info.user_medical_data.past_disease

def get_user_current_medication():
    user_info = get_user_info()
    return user_info.user_medical_data.current_medication

def is_user_smoker():
    user_info = get_user_info()
    if user_info.user_lifestyle_habit.smoker == regular:
        return 1
    return 0

def get_user_tc():
    user_info = get_user_info()
    return user_info.user_cardiac_risk_data.tc_mg_dl

def get_user_hdl():
    user_info = get_user_info()
    return user_info.user_cardiac_risk_data.hdl_mg_dl

def get_user_sbp():
    user_info = get_user_info()
    return user_info.user_cardiac_risk_data.sbp_mm_hg

def get_user_dbp():
    user_info = get_user_info()
    return user_info.user_cardiac_risk_data.dp_mm_hg

def is_user_under_bp_treatment():
    user_info = get_user_info()
    if user_info.user_cardiac_risk_data.bp_treated == 'Yes':
        return 1
    return 0

def get_user_waist():
    user_info = get_user_info()
    return user_info.user_body_param.waist

def get_risk_whtr(age,sex,whtr):
    risk = 0
    if age > 2: 
        if sex == 'Female':
            if (whtr >= 0.4920):
                risk = 1
        else:
            if (whtr >= 0.5360):
                risk = 1
    return risk

def is_user_obese(age,sex,whtr):
    obese = 0
    if age > 2:
        if sex == 'Female':
            if (whtr >= 0.54):
                obese = 1
        else:
            if (whtr >= 0.58):
                obese = 1
    return obese

def is_user_alcoholic():
    user_info = get_user_info()
    if user_info.user_lifestyle_habit.alcoholic == regular:
        return 1
    return 0

def is_user_diabetic():
    try:
        existing_list = get_user_existing_disease().split(',')
        if('Diabetes' in existing_list):
            return 1
        return 0
    except Exception as err:
        return 0

def is_user_hypertension():
    try:
        existing_list = get_user_existing_disease().split(',')
        if('Hypertension' in existing_list):
            return 1
        return 0
    except Exception as err:
        return 0

def is_user_cardiac():
    try:
        existing_list = get_user_existing_disease().split(',')
        past_list = get_user_past_disease().split(',')
        if ('Cardiac' in existing_list or 'Cardiac' in past_list):
            return 1
        return 0
    except Exception as err:
        return 0

def is_user_renal():
    try:
        existing_list = get_user_existing_disease().split(',')
        past_list = get_user_past_disease().split(',')
        if ('Renal' in existing_list or 'Renal' in past_list):
            return 1
        return 0
    except Exception as err:
        return 0

def is_user_inactive():
    user_info = get_user_info()
    if user_info.user_lifestyle_habit.exercise == n_a:
        return 1
    return 0

def is_user_stressful():
    user_info = get_user_info()
    if user_info.user_lifestyle_habit.stress == regular:
        return 1
    return 0

def is_user_junk_food_lover():
    user_info = get_user_info()
    if user_info.user_lifestyle_habit.junk_food_lover == regular:
        return 1
    return 0

def get_user_exercise_level():
    user_info = get_user_info()
    return user_info.user_lifestyle_habit.exercise

def get_parent_diabetes():
    user_info = get_user_info()
    return user_info.user_family_history.parent_diabetes

def get_parent_cardiac():
    user_info = get_user_info()
    return user_info.user_family_history.parent_cardiac

def get_parent_hypertension():
    user_info = get_user_info()
    return user_info.user_family_history.parent_hypertension

def get_parent_obese():
    user_info = get_user_info()
    return user_info.user_family_history.parent_obese

def get_family_history_kidney():
    user_info = get_user_info()
    return user_info.user_family_history.family_kidney

def get_parent_depression():
    user_info = get_user_info()
    return user_info.user_family_history.parent_depression

def get_user_cholesterol():
    user_info = get_user_info()
    return user_info.user_medical_data.cholesterol
