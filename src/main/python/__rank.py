'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

import sys
from __diseases import *
# ultimate score derived after consulting with rank & weight
# Ex. rank_weight['kidney_stone'] = 'High'
rank_weight = {}
evidence_parent_risk = {}
evidence_age_risk = {}
evidence_inactive_risk = {}
evidence_stress_risk = {}
evidence_smoking_risk = {}
evidence_alcoholic_risk = {}
evidence_cholesterol_risk = {}

def get_evidence_parent_risk(disease_name):
    return evidence_parent_risk[disease_name]

def get_evidence_age_risk(disease_name):
    return evidence_age_risk[disease_name]

def get_evidence_inactive_risk(disease_name):
    return evidence_inactive_risk[disease_name]

def get_evidence_stress_risk(disease_name):
    return evidence_stress_risk[disease_name]

def get_evidence_smoking_risk(disease_name):
    return evidence_smoking_risk[disease_name]

def get_evidence_alcohol_risk(disease_name):
    return evidence_alcoholic_risk[disease_name]

def get_evidence_cholesterol_risk(disease_name):
    return evidence_cholesterol_risk[disease_name]

def calculate_rank_weight_per_disease(db,disease_name):
    # this func will check if user has any existing disease that
    # can increase the risk factor
    ret = check_disease_dependency(db,disease_name)
    inc_weight_for_disease_by_val(disease_name,ret)
    # print "Disease Dependency"
    # print ret

    # check user parent risk factor
    ret = check_parent_risk_factor(disease_name)
    inc_weight_for_disease_by_val(disease_name,ret)
    # evidence parent risk
    evidence_parent_risk[disease_name] = ret
    # print "Parent Risk"
    # print ret

    # check disease comonality
    ret = get_disease_age_stats(db,get_user_age(),disease_name)
    # if disease is very common add 1 to weight
    if ret == 'vc':
        inc_weight_for_disease_by_val(disease_name,1)
    # evidence age risk
    if ret == 'vc':
        evidence_age_risk[disease_name] = 1
    else:
        evidence_age_risk[disease_name] = 0
    # print "Disease Stats"
    # print ret

    # check for inactivity
    ret = check_user_inactive_risk_factor(disease_name)
    inc_weight_for_disease_by_val(disease_name,ret)
    # evidence inactive risk
    evidence_inactive_risk[disease_name] = ret
    # print "Inactive risk"
    # print ret

    # check user stress factor
    ret = check_user_stress_factor(disease_name)
    inc_weight_for_disease_by_val(disease_name,ret)
    # evidence stress risk
    evidence_stress_risk[disease_name] = ret

    # check smoker risk facor
    ret = check_user_smoking_risk_factor(disease_name)
    inc_weight_for_disease_by_val(disease_name,ret)
    # evidence smoking risk
    evidence_smoking_risk[disease_name] = ret
    # print "Smoker risk"
    # print ret

    # check drinking risk factor
    ret = check_user_alcohol_risk_factor(disease_name)
    inc_weight_for_disease_by_val(disease_name,ret)
    # evidence alcohol risk
    evidence_alcoholic_risk[disease_name] = ret
    # print "Alcoholic Risk"
    # print ret

    # check user cholesterol risk factor
    ret = check_user_cholesterol_risk_factor(disease_name)
    inc_weight_for_disease_by_val(disease_name,ret)
    # evidence cholesterol risk
    evidence_cholesterol_risk[disease_name] = ret
    # print ret

    # check if user already has this disease that we are suspecting
    # ret = check_user_existing_vs_predict(db,disease_name)
    # print ret
    # if (ret == 1):
    #    inc_weight_for_disease_by_val(disease_name,10)

    weight = get_weight_for_disease(disease_name)
    rank = get_rank_for_disease(disease_name)
    # print "Weight-- %d" %weight
    num_symp_cnt = get_symp_count_for_disease(disease_name)
    # print "Num symp count %d" %num_symp_cnt

    # if weight is > 5 then chance high
    # if weight is between 3 -5 but total symptoms for
    # that disease is 3 or higher and one or more alarming symptom
    # then chance is high, else chance is moderate
    # similarly if weight is less than 3
    # but total symptoms 4 or more and 2 or more alarming symptoms
    # chance is high.
    # if 3 or more and 1 and more alarming symptom chance is fair
    # else chance is low

    if (weight > 5):
        rank_weight[disease_name] = "High"
    elif (weight >=3 and weight <=5):
        if (num_symp_cnt > 2 and rank >= 1):
            rank_weight[disease_name] = "High"
        else:
            rank_weight[disease_name] = "Moderate"
    else:
        if (num_symp_cnt > 3 and rank >= 2):
            rank_weight[disease_name] = "High"
        elif (num_symp_cnt > 2 and rank >= 1):
            rank_weight[disease_name] = "Fair"
        else:
            rank_weight[disease_name] = "Low"

    return 0

def get_rank_weight_per_disease(disease_name):
    return rank_weight[disease_name]
