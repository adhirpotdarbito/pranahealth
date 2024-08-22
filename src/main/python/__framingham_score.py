'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

#import libraries required
import sys
import os
import json

def get_point_for_age_women(age):
    """
        Function to calculate fr points for women as per age
    """
    if (age >= 20 and age <= 34):
        return -7
    if (age >= 35 and age <= 39):
        return -3
    if (age >=40 and age <= 44):
        return 0
    if (age >=45 and age <= 49):
        return 3
    if (age >=50 and age <= 54):
        return 6
    if (age >= 55 and age <= 59):
        return 8
    if (age >= 60 and age <= 64):
        return 10
    if (age >=65 and age <= 69):
        return 12
    if (age >=70 and age <= 74):
        return 14
    if (age >= 75 and age <= 79):
        return 16

def get_point_smoker_women(age):
    """
        Function to calculate fr points for women as per age and is smoker
    """
    if (age >= 20 and age <= 39):
        return 9
    if (age >= 40 and age <= 49):
        return 7
    if (age >= 50 and age <= 59):
        return 4
    if (age >= 60 and age <= 69):
        return 2
    if (age >= 70 and age <= 79):
        return 1


def get_point_total_cholestarol_women(age,tc):
    """
	Function to calculate fr points for women as per age and total cholestrol  
    """
    if (age >= 20 and age <= 39):
        if (tc < 160):
            return 0
        if (tc >= 160 and tc <= 199):
            return 4
        if (tc >= 200 and tc <= 239):
            return 8
        if (tc >= 240 and tc <= 279):
            return 11
        if (tc >= 280):
            return 13
    if (age >= 40 and age <= 49):
        if (tc < 160):
            return 0
        if (tc >= 160 and tc <= 199):
            return 3
        if (tc >= 200 and tc <= 239):
            return 6
        if (tc >= 240 and tc <= 279):
            return 8
        if (tc >= 280):
            return 10

    if (age >= 50 and age <= 59):
        if (tc < 160):
            return 0
        if (tc >= 160 and tc <= 199):
            return 2
        if (tc >= 200 and tc <= 239):
            return 4
        if (tc >= 240 and tc <= 279):
            return 5
        if (tc >= 280):
            return 7
    if (age >= 60 and age <= 69):
        if (tc < 160):
            return 0
        if (tc >= 160 and tc <= 199):
            return 1
        if (tc >= 200 and tc <= 239):
            return 2
        if (tc >= 240 and tc <= 279):
            return 3
        if (tc >= 280):
            return 4
    if (age >= 70 and age <= 79):
        if (tc < 160):
            return 0
        if (tc >= 160 and tc <= 199):
            return 1
        if (tc >= 200 and tc <= 239):
            return 1
        if (tc >= 240 and tc <= 279):
            return 2
        if (tc >= 280):
            return 2

def get_point_hdl_cholestarol_women(age,hdlc):
    """
	Function to calculate fr points for women as per age and hdl cholestrol
    """
    if (hdlc >= 60):
        return -1
    if (hdlc >= 50 and hdlc <= 59):
        return 0
    if (hdlc >= 40 and hdlc <= 49):
        return 1
    if (hdlc < 40):
        return 2

def get_point_sbp_women_untreated(age, sbp):
    """
	Function to calculate fr points for women as per sbp(systolic blood pressure) untreated.
    """
    if (sbp <= 120):
        return 0
    if (sbp > 120 and sbp <= 129):
        return 1
    if (sbp >= 130 and sbp <= 139):
        return 2
    if (sbp >= 140 and sbp <= 159):
        return 3
    if (sbp >= 160):
        return 4

def get_point_sbp_women_treated(age, sbp):
    """
        Function to calculate fr points for women as per sbp(systoical blood pressure) treated.
    """
    if (sbp <= 120):
        return 0
    if (sbp > 120 and sbp <= 129):
        return 3
    if (sbp >= 130 and sbp <= 139):
        return 4
    if (sbp >= 140 and sbp <= 159):
        return 5
    if (sbp >= 160):
        return 6


def get_risk_percent_women(tp):
    """
        Function takes tp input and return risk percentage as per given tp for women.
    """
    if (tp < 9):
        return 0
    if (tp >=9 and tp <= 12):
        return 1
    if (tp >= 13 and tp <= 14):
        return 2
    if (tp == 15):
        return 3
    if (tp == 16):
        return 4
    if (tp == 17):
        return 5
    if (tp == 18):
        return 6
    if (tp == 19):
        return 8
    if (tp == 20):
        return 11
    if (tp == 21):
        return 14
    if (tp == 22):
        return 17
    if (tp == 23):
        return 22
    if (tp == 24):
        return 27
    if (tp >= 25):
        return 30


# for men
def get_point_for_age_men(age):
    """
        Function to calculate fr points for men as per age
    """

    if (age >= 20 and age <= 34):
        return -9
    if (age >= 35 and age <= 39):
        return -4
    if (age >=40 and age <= 44):
        return 0
    if (age >=45 and age <= 49):
        return 3
    if (age >=50 and age <= 54):
        return 6
    if (age >= 55 and age <= 59):
        return 8
    if (age >= 60 and age <= 64):
        return 10
    if (age >=65 and age <= 69):
        return 11
    if (age >=70 and age <= 74):
        return 12
    if (age >= 75 and age <= 79):
        return 13

def get_point_smoker_men(age):
    """
        Function to calculate fr points for women as per age and is smoker
    """

    if (age >= 20 and age <= 39):
        return 8
    if (age >= 40 and age <= 49):
        return 5
    if (age >= 50 and age <= 59):
        return 3
    if (age >= 60 and age <= 69):
        return 1
    if (age >= 70 and age <= 79):
        return 1


def get_point_total_cholestarol_men(age,tc):
    """
        Function to calculate fr points for women as per age and total cholestrol
    """

    if (age >= 20 and age <= 39):
        if (tc < 160):
            return 0
        if (tc >= 160 and tc <= 199):
            return 4
        if (tc >= 200 and tc <= 239):
            return 7
        if (tc >= 240 and tc <= 279):
            return 9
        if (tc >= 280):
            return 11
    if (age >= 40 and age <= 49):
        if (tc < 160):
            return 0
        if (tc >= 160 and tc <= 199):
            return 3
        if (tc >= 200 and tc <= 239):
            return 5
        if (tc >= 240 and tc <= 279):
            return 6
        if (tc >= 280):
            return 8

    if (age >= 50 and age <= 59):
        if (tc < 160):
            return 0
        if (tc >= 160 and tc <= 199):
            return 2
        if (tc >= 200 and tc <= 239):
            return 3
        if (tc >= 240 and tc <= 279):
            return 4
        if (tc >= 280):
            return 5
    if (age >= 60 and age <= 69):
        if (tc < 160):
            return 0
        if (tc >= 160 and tc <= 199):
            return 1
        if (tc >= 200 and tc <= 239):
            return 1
        if (tc >= 240 and tc <= 279):
            return 2
        if (tc >= 280):
            return 3
    if (age >= 70 and age <= 79):
        if (tc < 160):
            return 0
        if (tc >= 160 and tc <= 199):
            return 0
        if (tc >= 200 and tc <= 239):
            return 0
        if (tc >= 240 and tc <= 279):
            return 1
        if (tc >= 280):
            return 1

def get_point_hdl_cholestarol_men(age,hdlc):
    """
        Function to calculate fr points for women as per hdl cholestrol 
    """
    if (hdlc >= 60):
        return -1
    if (hdlc >= 50 and hdlc <= 59):
        return 0
    if (hdlc >= 40 and hdlc <= 49):
        return 1
    if (hdlc < 40):
        return 2

def get_point_sbp_men_untreated(age, sbp):
    """
        Function to calculate fr points for women as per sbp (systoical blood pressure) untreated
    """
    if (sbp <= 120):
        return 0
    if (sbp > 120 and sbp <= 129):
        return 0
    if (sbp >= 130 and sbp <= 139):
        return 1
    if (sbp >= 140 and sbp <= 159):
        return 1
    if (sbp >= 160):
        return 2

def get_point_sbp_men_treated(age, sbp):
    """
        Function to calculate fr points for women as per sbp (systoical blood pressure) treated
    """
    if (sbp <= 120):
        return 0
    if (sbp > 120 and sbp <= 129):
        return 1
    if (sbp >= 130 and sbp <= 139):
        return 2
    if (sbp >= 140 and sbp <= 159):
        return 2
    if (sbp >= 160):
        return 3

def get_risk_percent_men(tp):
    """
        Function takes tp input and return risk percentage as per given total point for men.
    """
    if (tp <= 0):
        return 0
    if (tp >=1 and tp <= 4):
        return 1
    if (tp >= 5 and tp <= 6):
        return 2
    if (tp == 7):
        return 3
    if (tp == 8):
        return 4
    if (tp == 9):
        return 5
    if (tp == 10):
        return 6
    if (tp == 11):
        return 8
    if (tp == 12):
        return 10
    if (tp == 13):
        return 12
    if (tp == 14):
        return 16
    if (tp == 15):
        return 20
    if (tp == 16):
        return 25
    if (tp >= 17):
        return 30


# wrapper further branching men vs women

def get_point_for_age(age,sex):
    if sex == 'Female':
        return get_point_for_age_women(age)
    else:
        return get_point_for_age_men(age)

def get_point_for_smoker(age,sex):
    if sex == 'Female':
        return get_point_smoker_women(age)
    else:
        return get_point_smoker_men(age)

def get_point_total_cholesterol(age,sex,tc):
    if sex == 'Female':
        return get_point_total_cholestarol_women(age,tc)
    else:
        return get_point_total_cholestarol_men(age,tc)

def get_point_hdl_cholesterol(age,sex,hdlc):
    if sex == 'Female':
        return get_point_hdl_cholestarol_women(age,hdlc)
    else:
        return get_point_hdl_cholestarol_men(age,hdlc)


def get_point_sbp_untreated(age,sex,sbp):
    if sex == 'Female':
        return get_point_sbp_women_untreated(age,sbp)
    else:
        return get_point_sbp_men_untreated(age,sbp)

def get_point_sbp_treated(age,sex,sbp):
    if sex == 'Female':
        return get_point_sbp_women_treated(age,sbp)
    else:
        return get_point_sbp_men_treated(age,sbp)


def get_risk_percent(sex,tp):
    if sex == 'Female':
        return get_risk_percent_women(tp)
    else:
        return get_risk_percent_men(tp)

def get_score_percent(iage,isex,ismoker,itc,ihdlc,isbp,iutbp):
    """
        Function to calculate risk percent from given arguments age, sex, smoker, tc, hdlc, sbp, utbp(untreated bp)
    """
    UT_BP = 0
    total_point = 0
    age = int(iage)
    sex = isex
    smoker = ismoker
    TC = int(itc)
    HDL = int(ihdlc)
    SBP = int(isbp)
    UT_BP = int(iutbp)
    total_point = total_point + get_point_for_age(age,sex)
    if (smoker):
        total_point = total_point + get_point_for_smoker(age,sex)
    total_point = total_point + get_point_total_cholesterol(age,sex,TC)
    total_point = total_point + get_point_hdl_cholesterol(age,sex,HDL)
    if (UT_BP):
        total_point = total_point + get_point_sbp_treated(age,sex,SBP)
    else:
        total_point = total_point + get_point_sbp_untreated(age,sex,SBP)

    risk = get_risk_percent(sex,total_point)

    return risk

def get_avg_risk_chd_male(age):
    """
        Function to calculate average risk score for chd for men as per age
    """
    if (age < 30):
        return 0
    if (age >=30 and age <= 34):
        return 3
    if (age >=35 and age <= 39):
        return 5
    if (age >=40 and age <= 44):
        return 7
    if (age >=45 and age <= 49):
        return 11
    if (age >=50 and age <= 54):
        return 14
    if (age >= 55 and age <= 59):
        return 16
    if (age >= 60 and age <= 64):
        return 21
    if (age >=65 and age <= 69):
        return 25
    if (age >=70 and age <= 74):
        return 30
    return 30

def get_avg_risk_chd_female(age):
    """
        Function to calculate average risk points for chd for women as per age
    """
    if (age < 30):
        return 0
    if (age >=30 and age <= 34):
        return 1
    if (age >=35 and age <= 39):
        return 1
    if (age >=40 and age <= 44):
        return 2
    if (age >=45 and age <= 49):
        return 5
    if (age >=50 and age <= 54):
        return 8
    if (age >= 55 and age <= 59):
        return 12
    if (age >= 60 and age <= 64):
        return 12
    if (age >=65 and age <= 69):
        return 13
    if (age >=70 and age <= 74):
        return 14
    return 14
