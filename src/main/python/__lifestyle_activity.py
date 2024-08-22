'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

#import required libraries
import os
import json
import sys
from __config import *
from __lifestyle_gen import *
from __users import *
from __db_config import *
from __framingham_score import *
from __cvd_risk_tc_hdl_sbp import *
from __cvd_risk_sbp_bmi import *
from __cvd_risk_bmi import *
from __hypertension_frs import *
from __food_recipes import *
from __exercise_list import *
from __dietitian import *


json_data = {}
heart_age = 0.0
__user_risk_profile = None

class user_risk_profile:
    """
        create a class user_risk_profile, initialize class with attributes user_id, user_htn_risk, user_dia_risk, user_cardiac_risk, user_obese_risk, user_renal_risk.
    """
    def __init__(self,id):
        self.user_id = id
        self.user_htn_risk = self.__user_htn_risk()
        self.user_dia_risk = self.__user_dia_risk()
        self.user_cardiac_risk = self.__user_cardiac_risk()
        self.user_obese_risk = self.__user_obese_risk()
        self.user_renal_risk = self.__user_renal_risk()
    # create class for hypertension risk
    class __user_htn_risk:
        risk = None
	hypertension_risk = {}
	hypertension_risk_reason_json = {}
    # create class for diabetes risk
    class __user_dia_risk:
        risk = None
        diabetes_risk = {}
        diabetes_risk_reason_json = {}
    # create class for cardiac risk
    class __user_cardiac_risk:
        risk = None
        cvd_risk = {}
        chd_risk = {}
        cvd_risk_reason_json = {}
        chd_risk_reason_json = {}
        heart_age = None
    # create class for obese risk
    class __user_obese_risk:
        risk = None
	obesity_risk = {}
	obesity_risk_reason_json = {}
    # create class for renal risk
    class __user_renal_risk:
        risk = None
	renal_risk = {}
	renal_risk_reason_json = {}

# function for initializing user profile
def init_user_risk_profile(id):
    global __user_risk_profile
    __user_risk_profile = user_risk_profile(id)
    return __user_risk_profile

# function which return user risk profile
def get_user_risk_profile():
    global __user_risk_profile
    return __user_risk_profile

# function to calculate water intake daily in litres
def get_water_intake_litre(weight,physical_activity):
    litre  = 0.0
    litre = weight/30.0
    if (physical_activity == moderate):
        litre = litre + 0.35
    if (physical_activity == intense):
        litre = litre + 0.7
    return litre

# source "http://www.cadiresearch.org/topic/diabetes-indians/the-indian-diabetes-risk-score"
def get_risk_factor_diabetes(sex,age,waist,physical_activity,parent_diabetes):
    """
        Function to calculate risk factor for diabetes takes arguments sex, age, waist, physical_activity, parent_diabetes  
    """
    total_point = 0
    if age < 20:
        return Low
    # check if family history is empty
    if parent_diabetes == '':
        return n_a
    
    # check user age and add points to the total_point
    if (age >= 35 and age <= 49):
        total_point = total_point + 20
    if (age >= 50):
        total_point = total_point + 30
    # check user's sex and waist size and add points to the total point
    if sex == 'Female':
        if (waist >= 80 and waist <= 89):
            total_point = total_point + 10
        if (waist >= 90):
            total_point = total_point + 20
    else:
        if (waist >= 90 and waist <= 99):
            total_point = total_point + 10
        if (waist >= 100):
            total_point = total_point + 20

    # check if physical activity is n.a, moderate or mild and add points to the total_point
    if (physical_activity == n_a):
        total_point = total_point + 30
    if (physical_activity == moderate):
        total_point = total_point + 10
    if(physical_activity == mild):
        total_point = total_point + 20
    # check if parent diabetes is one or both and add points to the total_point
    if (parent_diabetes == mother) or (parent_diabetes == father):
        total_point = total_point + 10
    if (parent_diabetes == both):
        total_point = total_point + 20
    # check if user has already diabetes
    dia = is_user_diabetic()
    if (dia):
        # user is already diabetes
        total_point =  199
    # check total_point and return the level of diabetes of user
    if (total_point == 199):
        return 'Diabetic'
    if (total_point < 30):
        return Low
    if (total_point >=30 and total_point <=50):
        return Moderate
    if (total_point > 50):
        return High

def get_risk_factor_obesity(alcoholic,physical_activity,whtr_risk,obesity,fast_food_lover,stress,parent_obese):
    """
        Function to calculate risk factor obesity, takes arguments alcoholic,physical_activity,whtr_risk,obesity,fast_food_lover,stress,parent_obese
    """
    total_point = 0.0

    # check if user is alcoholic and add points to the total point
    if (alcoholic):
        total_point = total_point + 10
    # check physical activity of user whether n.a or mild and add points to the total point 
    if (physical_activity == n_a):
        total_point = total_point + 10
    if (physical_activity == mild):
        total_point = total_point + 5
    # check parent obese both or one and add points to the total point
    if (parent_obese == both):
        total_point = total_point + 20
    if (parent_obese == mother) or (parent_obese == father):
        total_point = total_point + 10
    # check risk of weight/height ratio and add points to the total point
    if (whtr_risk):
        total_point = total_point + 40
    # check whether user fast food lover and add points to the total point
    if (fast_food_lover):
        total_point = total_point + 10
    # check whether user in stress and add points
    if (stress):
        total_point = total_point + 5
    # check if user is already obese
    
    if (obesity):
        total_point = 199
    # check total_point and return the level of obesity of user
    if (total_point == 199):
        return 'Obese'
    if (total_point < 30):
        return Low
    if (total_point >=30 and total_point <40):
        return Moderate
    if (total_point >= 40):
        return High

# source "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4724234/#!po=50.0000"
def get_risk_factor_hypertension(age,sex,smoker,hypertensive,waist):
    """
        Function to calculate the risk factor of hypertension, takes arguments age,sex,smoker,hypertensive,waist
    """
    total_point = 0
    # check user hypertension severity
    if hypertensive == -1 or age < 20:
        return n_a

    # check the age of the user and add points to the total point    
    if (age >= 35):
        total_point = total_point + 2
    # check user's hypertensive value and add the points to the total point
    if (hypertensive == 1):
        total_point = total_point + 1
    if (hypertensive == 2):
        total_point = total_point + 2
    if (hypertensive == 3):
        total_point = total_point + 3
    # check if user is smoker and add the points to the total point
    if (smoker):
        total_point = total_point + 1
    # check user's and waist size and add points to the total point
    if sex == 'Female':
        # TDB need to rework on obesity component
        if (waist >= 80):
            total_point = total_point + 1
    else:
        # TDB need to rework on obesity component, I doubt
	if (waist >= 85):
            total_point = total_point + 1
    # check user has already high blood pressure
    already_hypertension = is_user_hypertension()
    if (already_hypertension):
        # user is already diabetes
        total_point =  199
    # check total point and return levels of hypertension of the user
    if (total_point == 199):
        return 'Hypertension'
    if (total_point < 3):
        return Low
    if (total_point >= 3) and (total_point < 5):
        return Moderate
    if (total_point >= 5):
        return High

def get_4_yrs_risk_hypertension(age,sex,sbp,dbp,smk,parent_hypertension,bmi):
    """
        Function to calculate risk level of hypertension for 4 years
    """
    # check if sbp or dbp is empty
    if sbp <= 0 or dbp <= 0 or age < 20:
        return n_a
    # check user already hypertension
    already_hypertension = is_user_hypertension()
    if (already_hypertension):
        return 'Hypertension'
    parent_htn = 0
    # check users's parent hypertension
    if (parent_hypertension == father) or (parent_hypertension == mother):
        parent_htn = 1
    if (parent_hypertension == both):
        parent_htn = 2
    # calculate risk hypertension of the user
    risk = calc_risk_hypertension(4,age,sex,sbp,dbp,smk,parent_htn,bmi)
    # calucalate optimal risk hypertension of the user
    optimal_risk = calc_risk_hypertension(4,age,sex,110,70,0,0,22)
    # compare both values, calculate delta difference and return the level low, moderate or high
    if (risk > optimal_risk):
        delta = 100*risk - 100*optimal_risk
        if (delta >= 5 and delta <= 10):
            return Moderate
        if (delta > 10):
            return High
        if (delta < 5):
            return Low
    return Low

def get_risk_factor_cvd(age,sex,smk,dia,htn,tc,hdl,sbp,bp_treated):
    """
        Function to calculate risk factor for cardiavascular disease
    """
    # check if user cardiac data is empty
    if tc <= 0.0 or hdl <= 0.0 or sbp <= 0 or age < 20:
        return n_a
    already_cardiac = is_user_cardiac()
    # check if user is already cardiac
    if(already_cardiac):
        return 'Cardiac'
    # check paramaters and calculate cvd risk value  of user with optimal and normal cvd risk value.
    if(tc and hdl and sbp):
        cvd_risk = frs_tc_hdl_sbp(sex,10,age,tc,hdl,sbp,dia,smk,bp_treated)
        cvd_risk_optimal = frs_tc_hdl_sbp(sex,10,age,160,60,110,0,0,0)
        cvd_risk_normal = frs_tc_hdl_sbp(sex,10,age,180,45,125,0,0,0)
    elif(sbp and bmi):
        cvd_risk = frs_sbp_bmi(sex,10,age,bmi,sbp,dia,smk,bp_treated)
        cvd_risk_optimal  = frs_sbp_bmi(sex,10,age,22,110,0,0,0)
        cvd_risk_normal  = frs_sbp_bmi(sex,10,age,22.5,125,0,0,0)
    elif(bmi):
        cvd_risk = frs_bmi(sex,10,age,bmi,htn,dia,smk)
        cvd_risk_optimal = frs_bmi(sex,10,age,22.5,0,0,0)
        cvd_risk_normal = frs_bmi(sex,10,age,22.5,0,0,0)
    # calcuate optimal and normal percent of cvd risk
    optimal_risk_percent = cvd_risk_optimal*100
    normal_risk_percent = cvd_risk_normal*100
    your_risk_percent = cvd_risk*100
    # comapre values and return the levels of cvd
    if(your_risk_percent > normal_risk_percent):
        delta = your_risk_percent - normal_risk_percent
        if (delta < 3.0):
            return Moderate
        else:
            return High

    return Low

# source "https://en.wikipedia.org/wiki/Framingham_Risk_Score"
def get_risk_factor_chd(age,sex,smoker,tc,hdl,sbp,bp_treated):
    """
        Function to calculate risk factor for congeneital heart defect 
    """
    # check if user cardiac data is empty
    if tc <= 0.0 or hdl <= 0.0 or sbp <= 0.0 or age < 20:
        return n_a
    # check user had any heart disease in past
    already_cardiac = is_user_cardiac()
    if (already_cardiac):
       # user already gone through heart disease
       return 'Cardiac'

    # get the cr risk score using Framingham analysis
    cr_risk_percent = get_score_percent(age,sex,smoker,tc,hdl,sbp,bp_treated)
    if (cr_risk_percent < 10):
        return Low

    if (cr_risk_percent >= 10 and cr_risk_percent <20):
        return Moderate

    if (cr_risk_percent >= 20):
        return High

def ckd_risk_assesment(age,dia,family_history,cardiac,htn,obese,smk):
    """
        Function to calculate risk level for chronic kidney disease
    """
    total_point = 0
    # check if family history is not provided
    if family_history == '':
        return n_a
    # check user had any renal disease
    already_renal = is_user_renal()
    if (already_renal):
        return 'Renal'
    # check user age and add points to the total_point
    if (age >= 60):
        total_point = total_point + 1
    # check if user diabetic and add points to the total_point
    if (dia):
        total_point = total_point + 2
    # check user's family history and add points to the total_point
    #if (family_history in [father, mother, both]):
    #    total_point = total_point + 1
    # check if user is cardiacand add points to the total_point
    if (cardiac):
        total_point = total_point + 1
    # check if user in hypertension and add points to the total_point
    if (htn):
        total_point = total_point + 1
    # check if user is obese and add points to the total_point
    if (obese):
        total_point = total_point + 1
    # check if user is smoker and add points to the total_point
    if (smoker):
        total_point = total_point + 1
    # check total_point and return the risk level
    if (total_point >= 3 and total_point < 5):
        return Moderate
    if (total_point >= 5):
        return High
    return Low

# source: https://www.freedieting.com/calorie-needs
def calculate_bmr(age,sex,weight,height):
    """
        Function used to calculate basal metabolic rate
    """
    bmr = 0
    if (sex == 'Male'):
        bmr = 10*weight + 6.25*height -5*age +5
    else:
        bmr = 10*weight + 6.25*height -5*age -161
    return bmr

def calculate_bmr_exercise_factor(bmr,physical_activity):
    """
        Function to calculate bmr exercise factor
    """
    effective_bmr = 0.0
    # check physical activity levels and calculate effective_bmr
    if (physical_activity == n_a) or (physical_activity == ''):
        effective_bmr = bmr*1.2
    if (physical_activity == mild):
        effective_bmr = bmr*1.375
    if (physical_activity == moderate):
        effective_bmr = bmr*1.55
    if(physical_activity == intense):
        effective_bmr = bmr*1.725

    return effective_bmr


# Risk reason for chd
def chd_risk_reason_age(sex, age):
    """
        Function to find risk levels (low, moderate, high) of aging of the user using framingham score for chd. 
    """
    if (sex == "Female"):
        age_point = get_point_for_age_women(age)
        if age_point <= 0 :
            return Low
        if age_point in range(1,9):
            return Moderate
        return High
    else:
        age_point = get_point_for_age_men(age)
        if age_point <= 0:
            return Low
        if age_point in range(1,9):
            return Moderate
        return High


def chd_risk_reason_tc(sex, age, tc, aging):
    """
        Function to calculate risk levels of total cholesterol of the user using framingham score for chd.
    """
    if (sex == "Female"):
        tc_point = get_point_total_cholestarol_women(age, tc)
        if tc_point <= 0:
            return Low
        if (aging == Moderate):
            if tc_point <= 3:
                return Moderate
            else:
                return High
        if (aging == High):
            if tc_point <=1:
                return Moderate
            else:
                return High
        if (aging == Low):
            if tc_point <= 4:
                return Moderate
            else:
                return High
    else:
        tc_point = get_point_total_cholestarol_men(age, tc)
        if tc_point <= 0:
            return Low
        if (aging == Moderate):
            if tc_point <= 3:
                return Moderate
            else:
                return High
        if (aging == High):
            if tc_point >= 1:
                return High
            else:
                return Moderate
        if (aging == Low):
            if tc_point <= 4:
                return Moderate
            else:
                return High

def chd_risk_reason_smoker(sex, age, aging, smoker):
    """
        Function to calculate risk levels of smoking of the user using framingham score for chd.
    """
    if (sex == "Female"):
        if (smoker):
            smk_point = get_point_smoker_women(age)
            if (smk_point) <= 0:
                return Low
            if (aging ==  Low) and smk_point <= 7:
                return Moderate
            else:
                return High
            if (aging == Moderate) and smk_point <= 4:
                return  Moderate
            else:
                return High
            if (aging == High) and smk_point <= 1:
                return Moderate
            else:
                return High
        else:
            return Low
    else:
        if (smoker):
            smk_point = get_point_smoker_men(age)
            if (aging == Low) and smk_point <= 5:
                return Moderate
            else:
                return High
            if (aging == Moderate) and smk_point <= 3:
                return Moderate
            else:
                return High
            if (aging == High) and smk_point <= 1:
                return Moderate
            else:
                return High
        else:
            return Low

def chd_risk_reason_hdl(sex, age, hdl):
    """
        Function to calculate risk levels of hdl cholesterol of the user using framingham score for chd. 
    """
    if (sex == 'Female'):
        hdl_point = get_point_hdl_cholestarol_women(age, hdl)
        if hdl_point < 0:
            return Low
        if hdl_point >= 0 and hdl_point <=1:
            return Moderate
        else:
            return High
    else:
        hdl_point = get_point_hdl_cholestarol_men(age, hdl)
        if hdl_point < 0:
            return Low
        if hdl_point >= 0 and hdl_point <= 1:
            return Moderate
        else:
            return High
  
def chd_risk_reason_sbp(sex, age, sbp, bp_treated):
    """
        Function to calculate risk levels of sbp of the user using framingham score for chd.
    """
    if (sex == "Female"):
        if (bp_treated):
            sbp_point = get_point_sbp_women_treated(age, sbp)
            if sbp_point <= 3:
                return Low
            if sbp_point >= 4 and sbp_point <= 5:
                return Moderate
            else:
                return High
        else:
            sbp_point = get_point_sbp_women_untreated(age, sbp)
            if sbp_point <= 1:
                return Low
            if sbp_point > 1 and sbp_point <= 3:
                return Moderate
            else:
                return High
    else:
        if (bp_treated):
            sbp_point = get_point_sbp_men_treated(age, sbp)
            if sbp_point <= 1:
                return Low
            if sbp_point > 1 and sbp_point <= 2:
                return Moderate
            if sbp_point > 2:
                return High
        else:
            sbp_point = get_point_sbp_men_untreated(age, sbp)
            if sbp_point <= 0:
                return Low
            if sbp_point == 1:
                return Moderate
            else:
                return High

# Risk reason for CVD
def cvd_risk_reason_age(sex, age):
    """
        Function to find risk levels (low, moderate, high) of aging of the user using framingham score for chd. 
    """
    if (sex == "Female"):
        age_point = get_point_for_age_women(age)
        if age_point <= 0 :
            return Low
        if age_point in range(1,9):
            return Moderate
        return High
    else:
        age_point = get_point_for_age_men(age)
        if age_point <= 0:
            return Low
        if age_point in range(1,9):
            return Moderate
        return High


def cvd_risk_reason_tc(sex, age, tc, aging):
    """
        Function to calculate risk levels of total cholesterol of the user using framingham score for cvd.
    """
    if (sex == "Female"):
        tc_point = get_point_total_cholestarol_women(age, tc)
        if tc_point <= 0:
            return Low
        if (aging == Moderate):
            if  (tc_point <= 3):
                return Moderate
            else:
                return High
        if (aging == High):
            if tc_point <=1:
                return Moderate
            else:
                return High
        if (aging == Low):
            if tc_point <= 4:
                return Moderate
            else:
                return High
    else:
        tc_point = get_point_total_cholestarol_men(age, tc)
        if tc_point <= 0:
            return Low
        if (aging == Moderate):
            if tc_point <= 3:
                return Moderate
            else:
                return High
        if (aging == High):
            if tc_point >= 1:
                return High
            else:
                return Moderate
        if (aging == Low):
            if tc_point <= 4:
                return Moderate
            else:
                return High

def cvd_risk_reason_smoker(sex, age, aging, smoker):
    """
        Function to calculate risk levels of smoking of the user using framingham score for cvd.
    """
    if (sex == "Female"):
        if (smoker):
            smk_point = get_point_smoker_women(age)
            if (smk_point) <= 0:
                return Low
            if (aging ==  Low) and smk_point <= 5:
                return Moderate
            else:
                return High
            if (aging == Moderate) and smk_point <= 4:
                return  Moderate
            else:
                return High
            if (aging == High) and smk_point <= 1:
                return Moderate
            else:
                return High
        else:
            return Low
    else:
        if (smoker):
            smk_point = get_point_smoker_men(age)
            if (aging == Low) and smk_point <= 5:
                return Moderate
            else:
                return High
            if (aging == Moderate) and smk_point <= 3:
                return Moderate
            else:
                return High
            if (aging == High) and smk_point <= 1:
                return Moderate
            else:
                return High
        else:
            return Low


def cvd_risk_reason_hdl(sex, age, hdl):
    """
        Function to calculate risk levels of hdl cholesterol of the user using framingham score for cvd. 
    """
    if (sex == 'Female'):
        hdl_point = get_point_hdl_cholestarol_women(age, hdl)
        if hdl_point < 0:
            return Low
        if hdl_point >= 0 and hdl_point <=1:
            return Moderate
        else:
            return High
    else:
        hdl_point = get_point_hdl_cholestarol_men(age, hdl)
        if hdl_point < 0:
            return Low
        if hdl_point >= 0 and hdl_point <= 1:
            return Moderate
        else:
            return High

def cvd_risk_reason_sbp(sex, age, sbp, bp_treated):
    """
        Function to calculate risk levels of sbp of the user using framingham score for cvd.
    """
    if (sex == "Female"):
        if (bp_treated):
            sbp_point = get_point_sbp_women_treated(age, sbp)
            if sbp_point <= 3:
                return Low
            if sbp_point >= 4 and sbp_point <= 5:
                return Moderate
            else:
                return High
        else:
            sbp_point = get_point_sbp_women_untreated(age, sbp)
            if sbp_point <= 1:
                return Low
            if sbp_point > 1 and sbp_point <= 3:
                return Moderate
            else:
                return High
    else:
        if (bp_treated):
            sbp_point = get_point_sbp_men_treated(age, sbp)
            if sbp_point <= 1:
                return Low
            if sbp_point > 1 and sbp_point <= 2:
                return Moderate
            if sbp_point > 2:
                return High
        else:
            sbp_point = get_point_sbp_men_untreated(age, sbp)
            if sbp_point <= 0:
                return Low
            if sbp_point == 1:
                return Moderate
            else:
                return High


def update_user_rdca(db,user_id,rdca):
    """
        Function to update recommended rdca the for user
    """
    cursor  = db.cursor()
    try:
        query_str = "delete from user_recommended_rdca where user_id=%d" %user_id
        cursor.execute(query_str)
        db.commit()
        query_str = "insert into user_recommended_rdca (user_id,rdca) values (%d, %d)" %(user_id,rdca)
        cursor.execute(query_str)
        db.commit()
    except Exception as err:
        print (Exception,err)
        print ("Fatal error update_user_rdca")
        cursor.close()
        return -1
    cursor.close()
    return 0

def get_dia_points(sex,age,waist,physical_activity,parent_diabetes):
    """
        Function to calculate total risk points for diabetes takes arguments sex, age, waist, physical_activity, parent_diabetes  
    """
    total_point = 0
    if parent_diabetes == '':
        return total_point
    # check user age and add points to the total_point
    if (age >= 35 and age <= 49):
        total_point = total_point + 20
    if (age >= 50):
        total_point = total_point + 30
    # check user's sex and waist size and add points to the total point
    if sex == 'Female':
        if (waist >= 80 and waist <= 89):
            total_point = total_point + 10
        if (waist >= 90):
            total_point = total_point + 20
    else:
        if (waist >= 90 and waist <= 99):
            total_point = total_point + 10
        if (waist >= 100):
            total_point = total_point + 20
    # check if physical activity is n.a, moderate or mild and add points to the total_point
    if (physical_activity == n_a):
        total_point = total_point + 30
    if (physical_activity == moderate):
        total_point = total_point + 10
    if(physical_activity == mild):
        total_point = total_point + 20
    # check if parent diabetes is one or both and add points to the total_point
    if (parent_diabetes == mother) or (parent_diabetes == father):
        total_point = total_point + 10
    if (parent_diabetes == both):
        total_point = total_point + 20
    return total_point

def diab_risk_reason_age(age, dia_point, dia_risk):
    """
	Function to calculate aging risk reason for diabetes.
    """
    if dia_point < 30 or dia_risk == Low:
        return Low

    if dia_point >= 30 and dia_point < 50 or dia_risk == Moderate:
        if (age < 40):
            return Low
        if (age >= 40 and age < 50):
            return Moderate
        return High

    if dia_point >= 50 or dia_risk in [High, 'Diabetic']:
        if (age < 40):
            return Moderate
        if age < 50:
            return High
        else:
            return 'Diabetic'


def diab_risk_reason_waist(sex,waist, dia_point, dia_risk):
    if dia_point < 30 or dia_risk == Low:
	return Low

    if dia_point >= 30 and dia_point < 50 or dia_risk == Moderate:
	if sex == 'Female':
	    if waist < 80:
		return Low
	    if waist >= 80 and waist <= 89:
		return Moderate
	    else:
		return High
	else:
	    if waist < 90:
		return Low
	    if waist >= 90 and waist <= 99:
		return Moderate
	    else:
		return High

    if dia_point >= 50 or dia_risk in [High,'Diabetic']:
        if sex == 'Female':
            if waist < 80:
                return Low
            if waist >= 80 and waist <= 89:
                return Moderate
            else:
                return High
        else:
            if waist < 90:
                return Low
            if waist >= 90 and waist <= 99:
                return Moderate
            else:
                return High
	             
def diab_risk_reason_tc(age, tc, dia_point, dia_risk, aging):   
    """
	Function to calculate cholestrol risk reason for diabetes
    """ 
    if tc <= 0.0:
        return Low
    if sex == "Female":
    	tc_point = get_point_total_cholestarol_women(age, tc)
    	if dia_point < 30 or dia_risk == Low:
	    if tc_point <= 0:
                return Low
            if (aging == Moderate):
                if tc_point <= 3:
                    return Moderate
                else:
                    return High
            if (aging == High):
                if tc_point <= 1:
                    return Moderate
                else:
                    return High
            if (aging == Low):
                if tc_point <= 4:
                    return Moderate
                else:
                    return High

    	if dia_point >= 30 and dia_point <= 50 or dia_risk == Moderate:
            if tc_point <= 0:
                return Low
            if (aging == Moderate):
                if tc_point <= 3:
                    return Moderate
                else:
                    return High
            if (aging == High):
                if tc_point <= 1:
                    return Moderate
                else:
                    return High
            if (aging == Low):
                if tc_point <= 4:
                    return Moderate
                else:
                    return High

	if dia_point > 50 or dia_risk in  [High, 'Diabetic']:
            if tc_point <= 0:
                return Low
            if (aging == Moderate):
                if tc_point <= 3:
                    return Moderate
                else:
                    return High
            if (aging == High):
                if tc_point <= 1:
                    return Moderate
                else:
                    return High
            if (aging == Low):
                if tc_point <= 4:
                    return Moderate
                else:
                    return High

    else:
	tc_point = get_point_total_cholestarol_men(age, tc)
	if dia_point < 30 or dia_risk == Low:
	    if tc_point <= 0:
                return Low
            if (aging == Moderate):
            	if tc_point <= 3:
                    return Moderate
                else:
                    return High
            if (aging == High):
                if tc_point >= 1:
                    return High
                else:
                    return Moderate
            if (aging == Low):
                if tc_point <= 4:
                    return Moderate
                else:
                    return High
	if dia_point >= 30 and dia_point <= 50 or dia_risk == Moderate:
	    if tc_point <= 0:
                return Low
            if (aging == Moderate):
                if tc_point <= 3:
                    return Moderate
                else:
                    return High
            if (aging == High):
                if tc_point >= 1:
                    return High
                else:
                    return Moderate
            if (aging == Low):
                if tc_point <= 4:
                    return Moderate
                else:
                    return High
        if dia_point > 50 or dia_risk in [High, 'Diabetic']:
	    if tc_point <= 0:
                return Low
            if (aging == Moderate):
                if tc_point <= 3:
                    return Moderate
                else:
                    return High
            if (aging == High):
                if tc_point >= 1:
                    return High
                else:
                    return Moderate
            if (aging == Low):
                if tc_point <= 4:
                    return Moderate
                else:
                    return High
 

def diab_risk_reason_hdl(age, hdl, dia_point, dia_risk):
    """
	Function to calculate hdl cholesterol risk reason for diabetes.
    """
    if hdl <= 0.0:
        return Low
    hdl_point = get_point_hdl_cholestarol_women(age, hdl)
    if dia_point < 30 or dia_risk == Low:
        if hdl_point < 0:
            return Low
        if hdl_point >= 0 and hdl_point <=1:
            return Moderate
        else:
            return High
    if dia_point >= 30 and dia_point <= 50 or dia_risk == Moderate:
        if hdl_point < 0:
            return Low
        if hdl_point >= 0 and hdl_point <=1:
            return Moderate
        else:
            return High
    if dia_point > 50 or dia_risk in [High, "Diabetic"]:
        if hdl_point < 0:
            return Low
        if hdl_point >= 0 and hdl_point <=1:
            return Moderate
        else:
            return High

def diab_risk_reason_smoker(sex, age, smoker, dia_point, dia_risk):
    """
	Function to calculate smoker risk reason for diabetes
    """
    if dia_point > 30 and dia_risk in [High, Moderate, "Diabetic"]:
    	if (sex == "Female"):
            if (smoker):
            	smk_point = get_point_smoker_women(age)
            	if (smk_point) <= 0:
                    return Low
            	if (aging ==  Low) and smk_point <= 7:
                    return Moderate
            	else:
                    return High
            	if (aging == Moderate) and smk_point <= 4:
                    return  Moderate
            	else:
                    return High
            	if (aging == High) and smk_point <= 1:
                    return Moderate
            	else:
                    return High
            else:
                return Low
    	else:
            if (smoker):
            	smk_point = get_point_smoker_men(age)
            	if (aging == Low) and smk_point <= 5:
                    return Moderate
                else:
                    return High
            	if (aging == Moderate) and smk_point <= 3:
                    return Moderate
            	else:
                    return High
            	if (aging == High) and smk_point <= 1:
                    return Moderate
            	else:
                    return High
            else:
                return Low
    else:
	return Low

def diab_risk_reason_sbp(sex, aging, sbp, bp_treated):
    """
	Function to calculate sbp risk reasaon for diabetes.
    """
    if sbp <= 0:
        return Low
    if dia_point > 30 and dia_risk in [High, Moderate, "Diabetic"]:
        if (sex == "Female"):
            if (bp_treated):
                sbp_point = get_point_sbp_women_treated(age, sbp)
                if sbp_point <= 3:
                    return Low
                if sbp_point >= 4 and sbp_point <= 5:
                    return Moderate
            	else:
                    return High
            else:
                sbp_point = get_point_sbp_women_untreated(age, sbp)
                if sbp_point <= 1:
                    return Low
            	if sbp_point > 1 and sbp_point <= 3:
                    return Moderate
            	else:
                    return High
    	else:
            if (bp_treated):
            	sbp_point = get_point_sbp_men_treated(age, sbp)
            	if sbp_point <= 1:
                    return Low
            	if sbp_point > 1 and sbp_point <= 2:
                    return Moderate
           	if sbp_point > 2:
                    return High
            else:
            	sbp_point = get_point_sbp_men_untreated(age, sbp)
            	if sbp_point <= 0:
                    return Low
            	if sbp_point == 1:
                    return Moderate
            	else:
                    return High
    else:
	return Low


# Risk reason Hypertension
def get_htn_points(age,sex,smoker,hypertensive,waist):
    """
	Function to calculate risk points for hypertension
    """
    # check the age of the user and add points to the total point
    total_point = 0
    # check user's hypertensive severity
    if hypertensive == -1:
        return total_point
    if (age >= 35):
        total_point = total_point + 2
    # check user's hypertensive value and add the points to the total point
    if (hypertensive == 1):
        total_point = total_point + 1
    if (hypertensive == 2):
        total_point = total_point + 2
    if (hypertensive == 3):
        total_point = total_point + 3
    # check if user is smoker and add the points to the total point
    if (smoker):
        total_point = total_point + 1
    # check user's and waist size and add points to the total point
    if sex == 'Female':
        # TDB need to rework on obesity component
        if (waist >= 80):
            total_point = total_point + 1
    else:
        # TDB need to rework on obesity component, I doubt
        if (waist >= 85):
            total_point = total_point + 1
    return total_point

	
def htn_risk_reason_age(age, htn_points):
    """
	Function to calculate aging risk reason for hypertension.
    """
    if htn_points < 3 and age >= 35:
	return Moderate
    elif htn_points >= 3 and age >= 35:
        return High
    else:
        return Low

def htn_risk_reason_smoker(htn_points, smoker):
    """
	Function to calculate smoking risk reason for hypertension
    """
    if (smoker):
        if htn_points < 3:
	    return Moderate
	else:
	    return High
    else:
	return Low

def htn_risk_reason_waist(sex, htn_points, waist):
    """
	Function to calculate waist risk reason for hypertension
    """
    if (sex == "Female"):
	if waist >= 80:
	    if htn_points < 3:
		return Moderate
	    else:
		return High
	else:
	    return Low
    else:
	if waist >= 85:
	    if htn_points < 3:
		return Moderate
	    else: 
		return High
 	else:
	    return Low

def htn_risk_reason_sbp(htn_points, hypertensive):
    """
	Function to calculate sbp risk reason for hypertension
    """
    if htn_points == 0:
        return Low
    if hypertensive < 1:
        return Low
    if hypertensive == 1:
        return Moderate
    if htn_points >= 2:
        return High

def htn_risk_reason_dbp(htn_points, dbp):
    """
	Function to calculate dbp risk reason for hypertension
    """
    if htn_points == 0:
        return Low
    if dbp <= 80:
	return Low
    if dbp > 80 and dbp <= 89:
	return Moderate
    return High
        
def htn_risk_reason_bmi(bmi):
    """
        Function to calculate bmi risk reason for hypertension
    """
    if bmi < 18.5:
	return n_a
    if bmi >= 18.5 and bmi <= 24.9:
	return Low
    if bmi >= 25 and  bmi <= 29.9:
	return Moderate
    else:
	return High
    
# Risk reason Obesity
def get_obs_points(alcoholic,physical_activity,whtr_risk,obesity,fast_food_lover,stress,parent_obese):
    """
        Function to calculate obesity risk points
    """
    total_point = 0.0
    # check if user is alcoholic and add points to the total point
    if (alcoholic):
        total_point = total_point + 10
    # check physical activity of user whether n.a or mild and add points to the total point 
    if (physical_activity == n_a):
        total_point = total_point + 10
    if (physical_activity == mild):
        total_point = total_point + 5
    # check parent obese both or one and add points to the total point
    if (parent_obese == both):
        total_point = total_point + 20
    if (parent_obese == father) or (parent_obese == mother):
        total_point = total_point + 10
    # check risk of weight/height ratio and add points to the total point
    if (whtr_risk):
        total_point = total_point + 40
    # check whether user fast food lover and add points to the total point
    if (fast_food_lover):
        total_point = total_point + 10
    # check whether user in stress and add points
    if (stress):
        total_point = total_point + 5
  
    return total_point

def obs_risk_reason_alcohol(obs_point, alcoholic):
    """
        Function to calculate alcohol risk reason factor for obesity
    """
    if (alcoholic):
	if obs_point < 40:
	    return Moderate
	else:
	    return High
    else:
	return Low

def obs_risk_physical_activity(obs_point, physical_activity):
    """
	Function to calculate physical_activity risk reason factor for obesity
    """
    if physical_activity in [n_a, mild]:
	if obs_point < 40:
	    return Moderate
	else:
	    return High
    else:
	return Low

def obs_risk_fast_food_lover(obs_point, fast_food_lover):
    """
	Function to calculate fast_food_lover risk reason factor for obesity
    """
    if (fast_food_lover):
	if obs_point < 40:
	    return Moderate
    	else:
	    return High
    else:
	return Low

def obs_risk_reason_whtr(obs_point, whtr_risk):
    """
	Function to calculate whtr risk reason factor for obesity
    """
    if (whtr_risk):
	if obs_point < 40:
	    return Moderate
	else:
	    return High
    else:
	return Low

def obs_risk_reason_family(obs_point, parent_obese):
    """
	Function to calculate family risk reason factor for obesity
    """
    if parent_obese in [father, mother, both]:
	if obs_point < 40:
	    return Moderate
	else:
	    return High
    else:
	return Low


# Risk reason Renal
def get_renal_points(age,dia,family_kidney,cardiac,htn,obese,smk):
    """
        Function to calculate risk level for chronic kidney disease
    """
    total_point = 0
    if family_kidney == '' or family_kidney == None:
        return total_point
    # check user had any renal disease
    already_renal = is_user_renal()
    if (already_renal):
        return 99
    # check user age and add points to the total_point
    if (age >= 60):
        total_point = total_point + 1
    # check if user diabetic and add points to the total_point
    if (dia):
        total_point = total_point + 2
    # check user's family history and add points to the total_point
    #if (family_kidney in [mother, father, both]):
    #    total_point = total_point + 1
    # check if user is cardiacand add points to the total_point
    if (cardiac):
        total_point = total_point + 1
    # check if user in hypertension and add points to the total_point
    if (htn):
        total_point = total_point + 1
    # check if user is obese and add points to the total_point
    if (obese):
        total_point = total_point + 1
    # check if user is smoker and add points to the total_point
    if (smoker):
        total_point = total_point + 1
    return total_point

def renal_risk_reason_age(age, ren_points):
    """
	Function to calculate age risk reason factor for renal
    """
    if ren_points == 0:
        return Low
    if age > 60:
        if ren_points < 5:
	    return Moderate
	else:
	    return High
    else:
	return Low

def renal_risk_reason_family(ren_points, family_kidney):
    """
	Function to calculate family risk reason factor for renal
    """
    if ren_points == 0:
        return Low
    if family_kidney in [father, mother, both]:
	if ren_points < 5:
	    return Moderate
	else:
	    return High
    else:
        return Low

def renal_risk_reason_obese(ren_points, obesity):
    """
	Function to calculate obsesity risk reason factor for renal
    """
    if ren_points == 0:
        return Low
    if (obesity):
	if ren_points < 5:
	    return Moderate
    	else:
	    return High
    else:
	return Low

def renal_risk_reason_cardiac(ren_points, cardiac):
    """
        Function to calculate cardiac risk reason factor for renal
    """
    if ren_points == 0:
        return Low
    cardiac = is_user_cardiac()
    if (cardiac):
	if ren_points < 5:
	    return Moderate
	else:
	    return High
    else:
	return Low

def renal_risk_reason_htn(ren_points, hypertension):
    """
        Function to calculate hypertension risk reason factor for renal    
    """
    if ren_points == 0:
        return Low
    hypertension = is_user_hypertension()
    if (hypertension):
	if ren_points < 5:
	    return Moderate
	else:
	    return High
    else:
	return Low

def renal_risk_reason_diab(ren_points, dia):
    """
	Function to calculate diabetes risk reason factor for renal
    """
    if ren_points == 0:
        return Low
    if (dia):
	if ren_points < 5:
	    return Moderate
	else:
	    return High
    else:
	return Low
    	
def renal_risk_reason_smk(ren_points, smoker):
    """
        Function to calculate smoking risk reason factor for renal
    """
    if ren_points == 0:
        return Low
    if (smoker):
	if ren_points < 5:
	    return Moderate
	else:
	    return High
    else:
	return Low

def renal_risk_reason_alcohol(ren_points, alcoholic):
    """        
	Function to calculate alcoholic risk reason factor for renal
    """
    if ren_points == 0:
        return Low
    if (alcoholic):
	if ren_points < 5:
	    return Moderate
	else:
	    return High
    else:
	return Low
     
def update_user_risk_profile(db,user_id,user_risk):
    """
        Function to user risk profile data
    """
    cursor = db.cursor()
    try:
        # delete before inserting for same user
        query_str = "delete from user_risk_data where user_id=%d" %user_id
        cursor.execute(query_str)
        db.commit()
        query_str = "insert into user_risk_data (user_id,dia_risk,htn_risk,obs_risk,card_risk,renal_risk) values (%d,'%s','%s','%s','%s','%s');" %(user_id,user_risk.user_dia_risk.risk,user_risk.user_htn_risk.risk,user_risk.user_obese_risk.risk,user_risk.user_cardiac_risk.risk,user_risk.user_renal_risk.risk)
        cursor.execute(query_str)
        db.commit()
    except Exception as err:
        print (Exception,err)
        print ("Fatal: update_user_risk_profile")
        cursor.close()
        return -1
    cursor.close()
    return 0

if __name__ == '__main__':
    argc = len(sys.argv) - 1
    if (argc < 2):
        print "python __lifestyle_activity.py <user_id> <full/periodically>"
        print "EX. Python __lifestyle_activity.py 1 'Full' "
        print "EX. Python __lifestyle_activity.py 1 'EM' "
        exit(0)

    #print "Building the lifestyle activity."
    # intialize database
    init_db()
    db = get_db()
    
    # get user_id and duration from system arguments
    user_id = sys.argv[1]
    duration = sys.argv[2]
    # init the user info class
    user_info = init_user_info(int(user_id))
    # init user risk profile
    __user_risk_profile = init_user_risk_profile(int(user_id))
    # get user profile
    ret = prepare_user_basic_data(db,user_info)
    if (ret != 0):
        print "Failed to retrieve user basic data"
        close_db()
        exit(-1)
    ret = prepare_user_medical_data(db,user_info)
    if (ret != 0):
        print "Failed to retrieve user medical data"
        close_db()
        exit(-1)
    ret = prepare_user_lifestyle_habit(db,user_info)
    if (ret != 0):
        print "Failed to retrieve user lifestyle habit"
        close_db()
        exit(-1)
    ret = prepare_user_cr_data(db,user_info)
    if (ret != 0):
        print "Failed to retrieve user cr data"
        close_db()
        exit(-1)
    ret = prepare_user_body_params(db,user_info)
    if (ret != 0):
        print "Failed to retrieve user body param"
        close_db()
        exit(-1)
    ret = prepare_user_family_data(db,user_info)
    if (ret != 0):
        print "Failed to retrieve user family data"
        close_db()
        exit(-1)

    #print "Prepared all the user data for lifestyle activity."

    # get user body param
    age = get_user_age()
    sex = get_user_sex()
    height = get_user_height()
    weight = get_user_weight()
    waist = get_user_waist()
    # print (age,sex,height,weight,waist)
    # end user body param

    # start user lifestyle habit
    smoker = is_user_smoker()
    alcoholic = is_user_alcoholic()
    physical_activity = get_user_exercise_level()
    stress = is_user_stressful()
    fast_food_lover = is_user_junk_food_lover()
    # print (smoker,alcoholic,physical_activity,stress,fast_food_lover)
    # end user lifestyle habit
    
    # calculate aging low, moderate or high
    aging = chd_risk_reason_age(sex, age)
    
    # start user cr data
    tc = float(get_user_tc())
    hdl = float(get_user_hdl())
    sbp = int(get_user_sbp())
    dbp = int(get_user_dbp())
    bp_treated = is_user_under_bp_treatment()
    # print (tc,hdl,sbp,bp_treated)
    # end uder cr data

    # start user family data
    parent_diabetes = get_parent_diabetes()
    parent_cardiac = get_parent_cardiac()
    parent_obese = get_parent_obese()
    family_kidney = get_family_history_kidney()
    family_hypertension = get_parent_hypertension()
    # print (parent_cardiac,parent_diabetes)
    # end user family data

    # check if hypertension
    hypertensive = is_user_hypertensive(sbp)
    # print hypertensive

    # get ratio total cholesterol:HDL
    tc_hdl_ratio = float(get_tc_hdl_ratio(tc,hdl))

    bmi = get_user_bmi(height,weight)
    whtr = float(waist/height)
    whtr_risk = get_risk_whtr(age,sex,whtr)
    obesity = is_user_obese(age,sex,whtr)
    dia = is_user_diabetic()
    htn = is_user_hypertension()
    # print (dia,smoker,smoker)

    # diabetes risk points and levels
    dia_point = get_dia_points(sex,age,waist,physical_activity,parent_diabetes)
    dia_risk = get_risk_factor_diabetes(sex,age,waist,physical_activity,parent_diabetes)

    # hypertension risk points
    htn_points = get_htn_points(age, sex, smoker, hypertensive, waist)
    
    # obesity risk points
    obs_point = get_obs_points(alcoholic,physical_activity,whtr_risk,obesity,fast_food_lover,stress,parent_obese)

    # renal risk points
    ren_points = get_renal_points(age,dia,family_kidney,is_user_cardiac(),htn,obesity,smoker)    

    # Heart age calculator
    if(tc and hdl and sbp):
        cvd_risk = frs_tc_hdl_sbp(sex,10,age,tc,hdl,sbp,dia,smoker,bp_treated)
        heart_age = heart_age_by_cvd_tc_hdl_sbp(cvd_risk,age,sex)
    # Heart age calculator
    elif(sbp and bmi):
        cvd_risk = frs_sbp_bmi(sex,10,age,bmi,sbp,dia,smoker,bp_treated)
        heart_age = heart_age_by_cvd_sbp_bmi(cvd_risk,age,sex)
    # Heart age calculator
    elif(bmi):
        cvd_risk = frs_bmi(sex,10,age,bmi,htn,dia,smoker)
        heart_age = heart_age_by_cvd_bmi(cvd_risk,age,sex)

    # calculate user current bmr
    bmr_current = calculate_bmr(age,sex,weight,height)
    #print("Current BMR", bmr_current)
    #print("Physical activity", physical_activity)
    bmr_exercise_factor_current = calculate_bmr_exercise_factor(bmr_current,physical_activity)
    #print("BMR Exercise factor current", bmr_exercise_factor_current)
    # calculate bmr ideal based on user height,age,sex & ideal weight
    ideal_weight = get_user_ideal_weight(sex,height,age)
    #print("Ideal Weight", ideal_weight)
    bmr_ideal = calculate_bmr(age,sex,ideal_weight,height)
    #print("Ideal BMR", bmr_ideal)
    #print("Physical activity", physical_activity)
    bmr_exercise_factor_ideal = calculate_bmr_exercise_factor(bmr_ideal,physical_activity)
    #print("BMR Exercise factor ideal", bmr_exercise_factor_ideal)

    recommended_cal_intake_day = bmr_exercise_factor_ideal
    #print ("RDCA-1", recommended_cal_intake_day)
    total_week_diet = 24
    
    # for 1 pound weight loss /week you need to take 500 less
    # So basically if you want to loose your weight then(obese risk)
    # then you have to maintain cal_weight_loss per day
    if (obesity or whtr_risk):
        # user is overweight
        # let's take a look of ideal weight for user
        weight_to_loose = weight - ideal_weight
        # ideal weight to loose per week is 1 pound, i.e 0.45 kg
        ideal_weight_loose_per_week = 0.45
        total_week_diet = weight_to_loose/ideal_weight_loose_per_week
        # in case of loosing 0.45 kg per week you need to take 500 less cal per day
        recommended_cal_intake_day = bmr_exercise_factor_current - 500.0
        #print ("RDCA-2", recommended_cal_intake_day)
        # if cal intake drop below 1200 then it's a unsafe diet
        # may have -ve health impact
        if (recommended_cal_intake_day < 1200.0):
            recommended_cal_intake_day = 1200
            #print ("RDCA-3", recommended_cal_intake_day)
        # we initially provide diet for 6 months i.e 24 weeks
        if (total_week_diet > 24):
            total_week_diet = 24

    # check if htn_points is zero, assign empty dictionary for risk reason hypertension
    if htn_points == 0:
        __user_risk_profile.user_htn_risk.hypertension_risk_reason_json["Risk Reason Hypertension"] = {}   
    else:
        # Call risk reason function for hypertension
        htn_aging = htn_risk_reason_age(age, htn_points)
        htn_smk = htn_risk_reason_smoker(htn_points, smoker)
        htn_waist = htn_risk_reason_waist(sex, htn_points, waist)
        htn_sbp = htn_risk_reason_sbp(htn_points, hypertensive)
        htn_bmi = htn_risk_reason_bmi(bmi)
        htn_dbp = htn_risk_reason_dbp(htn_points, dbp)   

        # Add risk reasons for hypertension to user htn risk in user risk profile
        __user_risk_profile.user_htn_risk.hypertension_risk["aging"] = htn_aging
        __user_risk_profile.user_htn_risk.hypertension_risk["smoking_factor"] = htn_smk
        __user_risk_profile.user_htn_risk.hypertension_risk["waist_factor"] = htn_waist
        __user_risk_profile.user_htn_risk.hypertension_risk["sbp_factor"] = htn_sbp
        __user_risk_profile.user_htn_risk.hypertension_risk["bmi_factor"] = htn_bmi
        __user_risk_profile.user_htn_risk.hypertension_risk["dbp_factor"] = htn_dbp
        if family_hypertension in [mother, father, both]:
	    __user_risk_profile.user_htn_risk.hypertension_risk["family_factor"] = High
        else:
	    __user_risk_profile.user_htn_risk.hypertension_risk["family_factor"] = Low
        # Add hypertension risk reason dictionary to hypertension_risk_reason_json in user risk profile
        __user_risk_profile.user_htn_risk.hypertension_risk_reason_json["Risk Reason Hypertension"] = __user_risk_profile.user_htn_risk.hypertension_risk

    # call risk reason function for obesity
    obs_alcohol = obs_risk_reason_alcohol(obs_point, alcoholic)
    obs_physical_activity = obs_risk_physical_activity(obs_point, physical_activity)
    obs_fast_food_lover = obs_risk_fast_food_lover(obs_point, fast_food_lover)
    obs_whtr_risk = obs_risk_reason_whtr(obs_point, whtr_risk)
    obs_family = obs_risk_reason_family(obs_point, parent_obese)
   
     # Add risk reasons for obesity to user obese risk in user risk profile
    __user_risk_profile.user_obese_risk.obesity_risk["alcohol_factor"] = obs_alcohol
    __user_risk_profile.user_obese_risk.obesity_risk["physical_activity_factor"] = obs_physical_activity 
    __user_risk_profile.user_obese_risk.obesity_risk["fast_food_lover"] = obs_fast_food_lover
    __user_risk_profile.user_obese_risk.obesity_risk["whtr_risk_factor"] = obs_whtr_risk
    __user_risk_profile.user_obese_risk.obesity_risk["family_factor"] = obs_family

    # Add obesity risk reason dictionary to obesity_risk_reason_json in user risk profile
    __user_risk_profile.user_obese_risk.obesity_risk_reason_json["Risk Reason Obesity"] = __user_risk_profile.user_obese_risk.obesity_risk
    

    # check if renal points is zero, assign empty dictionary to risk reason renal
    if ren_points == 0:
         __user_risk_profile.user_renal_risk.renal_risk_reason_json["Risk Reason Renal"] = {}
    else:
        # call risk reason function for renal
        ren_aging = renal_risk_reason_age(age, ren_points)
        ren_family = renal_risk_reason_family(ren_points, family_kidney)
        ren_obese = renal_risk_reason_obese(ren_points, obesity)
        ren_cardiac = renal_risk_reason_cardiac(ren_points, is_user_cardiac())
        ren_htn = renal_risk_reason_htn(ren_points, is_user_hypertension())
        ren_diab = renal_risk_reason_diab(ren_points, dia)
        ren_smk = renal_risk_reason_smk(ren_points, smoker)
        ren_alcoholic = renal_risk_reason_alcohol(ren_points, alcoholic)

        # Add risk reasons for kidney disease to user renal risk in user risk profile
        __user_risk_profile.user_renal_risk.renal_risk["aging"] = ren_aging
        __user_risk_profile.user_renal_risk.renal_risk["family_factor"] = ren_family
        __user_risk_profile.user_renal_risk.renal_risk["obesity_factor"] = ren_obese
        __user_risk_profile.user_renal_risk.renal_risk["cardiac_factor"] = ren_cardiac
        __user_risk_profile.user_renal_risk.renal_risk["hypertension_factor"] = ren_htn
        __user_risk_profile.user_renal_risk.renal_risk["diabetes_factor"] = ren_diab
        __user_risk_profile.user_renal_risk.renal_risk["smoking_factor"] = ren_smk
        __user_risk_profile.user_renal_risk.renal_risk["alcohol_factor"] = ren_alcoholic
 
        # Add renal risk reason dictionary to renal_risk_reason_json in user_risk_profile
        __user_risk_profile.user_renal_risk.renal_risk_reason_json["Risk Reason Renal"] = __user_risk_profile.user_renal_risk.renal_risk
   
    if tc <= 0.0 or hdl <= 0.0 or sbp <= 0 or dbp <= 0:
        __user_risk_profile.user_cardiac_risk.chd_risk_reason_json["Risk Reason CHD"] = {}
    else:

        # Call risk reason function for chd
        chd_tc = chd_risk_reason_tc(sex, age, tc, aging)
        chd_smoker = chd_risk_reason_smoker(sex, age, aging, smoker)
        chd_hdl = chd_risk_reason_hdl(sex, age, hdl)
        chd_sbp = chd_risk_reason_sbp(sex, age, sbp, bp_treated)    

        # Add risk reasons for chd to user cardiac risk in user risk profile
        __user_risk_profile.user_cardiac_risk.chd_risk["aging"] = aging
        __user_risk_profile.user_cardiac_risk.chd_risk["total_cholesterol_factor"] = chd_tc
        __user_risk_profile.user_cardiac_risk.chd_risk["smoking_factor"] = chd_smoker
        __user_risk_profile.user_cardiac_risk.chd_risk["hdl_cholesterol_factor"] = chd_hdl
        __user_risk_profile.user_cardiac_risk.chd_risk["sbp_factor"] = chd_sbp
        if parent_cardiac in [father, mother, both]:
	    __user_risk_profile.user_cardiac_risk.chd_risk["family_factor"] = High
        else:
	    __user_risk_profile.user_cardiac_risk.chd_risk["family_factor"] = Low
    
        # Add chd risk dictionary to chd_risk_reason_json in user risk profile
        __user_risk_profile.user_cardiac_risk.chd_risk_reason_json["Risk Reason CHD"] = __user_risk_profile.user_cardiac_risk.chd_risk
    

    if tc <= 0.0 or hdl <= 0.0 or sbp <= 0 or dbp <= 0:
         __user_risk_profile.user_cardiac_risk.cvd_risk_reason_json["Risk Reason CVD"] = {}
    else:
        # call risk reason function for cvd
        cvd_tc = cvd_risk_reason_tc(sex, age, tc, aging)
        cvd_smoker = cvd_risk_reason_smoker(sex, age,aging,smoker)
        cvd_hdl = cvd_risk_reason_hdl(sex,age,hdl)
        cvd_sbp = cvd_risk_reason_sbp(sex, age, sbp, bp_treated)
    
        # Add risk reasons for cvd to user cardiac risk in user risk profile
        __user_risk_profile.user_cardiac_risk.cvd_risk["aging"] = aging
        __user_risk_profile.user_cardiac_risk.cvd_risk["total_cholesterol_factor"] = cvd_tc
        __user_risk_profile.user_cardiac_risk.cvd_risk["smoking_factor"] = cvd_smoker
        __user_risk_profile.user_cardiac_risk.cvd_risk["hdl_cholesterol_factor"] = cvd_hdl
        __user_risk_profile.user_cardiac_risk.cvd_risk["sbp_factor"] = cvd_sbp
        if parent_cardiac in [father, mother, both]:
            __user_risk_profile.user_cardiac_risk.cvd_risk["family_factor"] = High
        else:
            __user_risk_profile.user_cardiac_risk.cvd_risk["family_factor"] = Low

    # check for diabetes and hypertension assign values yes/no
        if dia == 1:
            __user_risk_profile.user_cardiac_risk.cvd_risk["Diabetic"] = "Yes"
        else:
            __user_risk_profile.user_cardiac_risk.cvd_risk["Diabetic"] = "No"

        if htn == 1:
            __user_risk_profile.user_cardiac_risk.cvd_risk["Hypertension"] = "Yes"
        else:
            __user_risk_profile.user_cardiac_risk.cvd_risk["Hypertension"] = "No"

        # Add cvd risk dictionary to chd_risk_reason_json in user_risk_profile
        __user_risk_profile.user_cardiac_risk.cvd_risk_reason_json["Risk Reason CVD"] = __user_risk_profile.user_cardiac_risk.cvd_risk

    if dia_point == 0:
        __user_risk_profile.user_dia_risk.diabetes_risk_reason_json["Risk Reason Diabetes"] = {}
    else:
        # Call risk reason function for diabetes
        dia_aging = diab_risk_reason_age(age, dia_point, dia_risk)
        dia_tc = diab_risk_reason_tc(age, tc, dia_point, dia_risk,aging)
        dia_smoker = diab_risk_reason_smoker(sex, age, smoker, dia_point, dia_risk)
        dia_hdl = diab_risk_reason_hdl(age, hdl, dia_point, dia_risk)
        dia_sbp = diab_risk_reason_sbp(sex, age, sbp, bp_treated)
        dia_waist = diab_risk_reason_waist(sex,waist,dia_point,dia_risk)
        # Add risk reasons for diabetes to user cardiac risk in user risk profile
        __user_risk_profile.user_dia_risk.diabetes_risk["aging"] = dia_aging
        __user_risk_profile.user_dia_risk.diabetes_risk["total_cholesterol_factor"] = dia_tc
        __user_risk_profile.user_dia_risk.diabetes_risk["smoking_factor"] = dia_smoker
        __user_risk_profile.user_dia_risk.diabetes_risk["hdl_cholesterol_factor"] = dia_hdl
        __user_risk_profile.user_dia_risk.diabetes_risk["sbp_factor"] = dia_sbp    
        __user_risk_profile.user_dia_risk.diabetes_risk["waist_factor"] = dia_waist
        if parent_diabetes in [father, mother, both]:
	    __user_risk_profile.user_dia_risk.diabetes_risk["family_factor"] = High
        else:
	    __user_risk_profile.user_dia_risk.diabetes_risk["family_factor"] = Low
        # Add cvd risk dictionary to diabetes_risk_reason_json in user_risk_profile
        __user_risk_profile.user_dia_risk.diabetes_risk_reason_json["Risk Reason Diabetes"] = __user_risk_profile.user_dia_risk.diabetes_risk


    # Variables assigned for risk reason of cardiac, diabetes, hypertension, obesity and renal
    risk_reason_chd = __user_risk_profile.user_cardiac_risk.chd_risk_reason_json
    risk_reason_cvd = __user_risk_profile.user_cardiac_risk.cvd_risk_reason_json
    risk_reason_diabetes = __user_risk_profile.user_dia_risk.diabetes_risk_reason_json
    risk_reason_hypertension = __user_risk_profile.user_htn_risk.hypertension_risk_reason_json
    risk_reason_obesity = __user_risk_profile.user_obese_risk.obesity_risk_reason_json
    risk_reason_renal = __user_risk_profile.user_renal_risk.renal_risk_reason_json

    #TBD
    json_obj = None

    # check for type 2 diabetes risk
    # type 2 diabetes
    lifestyle_dash_diabetes = {}
    risk = get_risk_factor_diabetes(sex,age,waist,physical_activity,parent_diabetes)
    lifestyle_dash_diabetes['profile'] = 'Type 2 diabetes'
    lifestyle_dash_diabetes['risk'] = risk
    lifestyle_dash_diabetes['reason_diabetes'] = risk_reason_diabetes["Risk Reason Diabetes"]
    lifestyle_dash_diabetes['packages'] = 'Complete Haemogram & ESR,Urine Routine & Microscopy,Serum Creatinine,Blood Urea,Uric Acid,Blood Sugar Fasting,Blood Sugar PP,Glycosylated Hemoglobin (HbA1C),Lipid Profile- LDH, HDL, VLDL, Cholesterol, Triglycerides'
    json_data['diabetes'] = lifestyle_dash_diabetes
    __user_risk_profile.user_dia_risk.risk = risk
    #print "Built the diabetes risk."

    # obesity
    lifestyle_dash_obesity = {}
    risk = get_risk_factor_obesity(alcoholic,physical_activity,whtr_risk,obesity,fast_food_lover,stress,parent_obese)
    lifestyle_dash_obesity['profile'] = 'Obesity'
    lifestyle_dash_obesity['risk'] = risk
    lifestyle_dash_obesity['packages'] = 'Blood Sugar Fasting,Blood Sugar PP,Glycosylated Hemoglobin (HbA1C),Lipid Profile- LDH, HDL, VLDL, Cholesterol, Triglycerides'
    lifestyle_dash_obesity['reason_obesity'] = risk_reason_obesity["Risk Reason Obesity"]
    json_data['obesity'] = lifestyle_dash_obesity
    __user_risk_profile.user_obese_risk.risk = risk
    #print "Built the obesity risk."

    # Hypertension
    lifestyle_dash_ht = {}
    risk_ind_surv = get_risk_factor_hypertension(age,sex,smoker,hypertensive,waist)
    risk_framingham = get_4_yrs_risk_hypertension(age,sex,sbp,dbp,smoker,family_hypertension,bmi)
    risk = None
    if (risk_ind_surv == n_a or risk_framingham == n_a):
        risk = n_a
    elif (risk_ind_surv == 'Hypertension' or risk_framingham == 'Hypertension'):
        risk = 'Hypertension'
    elif (risk_ind_surv == High or risk_framingham == High):
        risk = High
    elif (risk_ind_surv == Moderate or risk_framingham == Moderate):
        risk = Moderate
    else:
        risk = Low

    lifestyle_dash_ht['profile'] = 'Hypertension'
    lifestyle_dash_ht['risk_ind_surv'] = risk_ind_surv
    lifestyle_dash_ht['risk_framingham'] = risk_framingham
    lifestyle_dash_ht['risk'] = risk
    lifestyle_dash_ht['reason_hypertension'] = risk_reason_hypertension["Risk Reason Hypertension"]
    lifestyle_dash_ht['packages'] = 'Complete Haemogram & ESR,Urine Routine & Microscopy,Serum Creatinine,Blood Urea,Uric Acid,Blood Sugar Fasting,Blood Sugar PP,Glycosylated Hemoglobin (HbA1C),Lipid Profile- LDH, HDL, VLDL, Cholesterol, Triglycerides,ECG,TSH,FT3,FT4'
    json_data['hypertension'] = lifestyle_dash_ht
    __user_risk_profile.user_htn_risk.risk = risk
    #print "Built the hypertension risk."

    # Cardiac
    lifestyle_dash_chd = {}
    risk_chd = get_risk_factor_chd(age,sex,smoker,tc,hdl,sbp,bp_treated)
    risk_cvd = get_risk_factor_cvd(age,sex,smoker,dia,htn,tc,hdl,sbp,bp_treated)
    risk = None
    if (risk_chd == n_a or risk_cvd == n_a):
        risk = n_a
    elif (risk_chd == 'Cardiac' or risk_cvd == 'Cardiac'):
        risk = 'Cardiac'
    elif (risk_chd == High or risk_cvd == High):
        risk = High
    elif (risk_chd == Moderate or risk_cvd == Moderate):
        risk = Moderate
    else:
        risk = Low

    lifestyle_dash_chd['profile'] = 'Cardiac'
    lifestyle_dash_chd['chd_risk'] = risk_chd
    lifestyle_dash_chd['cvd_risk'] = risk_cvd
    lifestyle_dash_chd['risk'] = risk
    lifestyle_dash_chd['reason_chd'] = risk_reason_chd["Risk Reason CHD"]
    lifestyle_dash_chd['reason_cvd'] = risk_reason_cvd["Risk Reason CVD"]
    lifestyle_dash_chd['heart_age'] = heart_age
    lifestyle_dash_chd['packages'] = 'Complete Haemogram & ESR,Urine Routine & Microscopy,Serum Creatinine,Blood Urea,Uric Acid,Blood Sugar Fasting,Blood Sugar PP,Glycosylated Hemoglobin (HbA1C),Lipid Profile- LDH, HDL, VLDL, Cholesterol, Triglycerides,ECG,TSH,FT3,FT4'
    json_data['chd'] = lifestyle_dash_chd
    __user_risk_profile.user_cardiac_risk.risk = risk

    lifestyle_dash_kidney = {}
    risk = ckd_risk_assesment(age,dia,family_kidney,is_user_cardiac(),is_user_hypertension(),obesity,smoker)
    lifestyle_dash_kidney['profile'] = 'Kidney'
    lifestyle_dash_kidney['risk'] = risk
    lifestyle_dash_kidney['reason_renal'] = risk_reason_renal["Risk Reason Renal"]
    lifestyle_dash_kidney['packages'] = 'Kidney Profile(BUN,Uric Acid,Total Calcium,Creat,BUN/Serum Creatinine)'
    json_data['kidney'] = lifestyle_dash_kidney
    __user_risk_profile.user_renal_risk.risk = risk
    result_json = {}
    result_json['status'] = '0'
    result_json['status_message'] = 'Success'
    result_json['error_details'] = ''
    result_json['profile_data'] = json_data
    #print "Building the activity model."
    #print getLifeStyleActivityModelHyperTension()
    #print "Built the activity model."

    #print "Built the lifestyle activity."
    # TBD for other
    food_list = {}
    exercise_list = {}
    #food_list['Monday'] = generate_food_set(__user_risk_profile,recommended_cal_intake_day)
    #food_list['Tuesday'] = generate_food_set(__user_risk_profile,recommended_cal_intake_day)
    #food_list['Wednesday'] = generate_food_set(__user_risk_profile,recommended_cal_intake_day)
    #food_list['Thursday'] = generate_food_set(__user_risk_profile,recommended_cal_intake_day)
    #food_list['Friday'] = generate_food_set(__user_risk_profile,recommended_cal_intake_day)
    #food_list['Saturday'] = generate_food_set(__user_risk_profile,recommended_cal_intake_day)
    #food_list['Remark'] = get_special_remark(__user_risk_profile)
    exercise_list['All Day'], exercise_list['exercise_recommendations'] = get_exercise_list(db,user_id,__user_risk_profile,whtr_risk,age)
    if (duration == 'bound'):
        result_json['food_model'] = food_list
    else:
        result_json['food_model'], result_json['food_recommendations'] = get_food_items(__user_risk_profile, recommended_cal_intake_day, age)
    result_json['exercise_model'] = exercise_list
    result_json['RDCA'] = int(round(recommended_cal_intake_day))
    result_json["water_intake_daily"] = get_water_intake_litre(weight,physical_activity)
    result_json['Dietitians'] = prepare_dietitian_details(db)
    print json.dumps(result_json)
    # update user rdca
    update_user_rdca(db,int(user_id),int(round(recommended_cal_intake_day)))

    # update user risk date to DB
    update_user_risk_profile(db,int(user_id),__user_risk_profile)

    user_file_str = "/opt/atman/sql/user_lifestyle_data/lifestyle_activity_%d" %int(user_id)
    with open(user_file_str, 'w+') as f:
        f.write(json.dumps(result_json))
    close_db()

    exit(0)
