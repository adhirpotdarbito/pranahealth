'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

import sys
from __users import *
from __config import *

# list to store all matching disease for user symptom
disease = []
# if rank[disease] is non zero means chances is high
rank = {}
# weight/score of all symptoms common to disease weight[disease]
# sum of all symptoms weight towards that disease
weight = {}

# number of symptoms common for disease
num_common_symp = {}

# store all user existing segment risk against prediction
evidence_disease_dependency = {}

# this func will tell for the input age the chances
# of disease is RARE, COMMON, UNCOMMON
# if its rare or uncommon for the user given age
# then we have to mention that
def get_disease_age_stats(db,age,disease):
    age_grp = get_age_group(age)
    cursor = db.cursor()
    try:
        query_str = "select d_id from disease where name='%s'" %disease
        cursor.execute(query_str)
        d_id = cursor.fetchone()
        query_str = "select %s from disease_stats where d_id=%d" %(age_grp,d_id[0])
        cursor.execute(query_str)
        age_stat = cursor.fetchone()
    except Exception as err:
        print (Exception, err)
        print("Unexpected error: get_disease_age_stats", sys.exc_info()[0])
        cursor.close()
        return(-1)
    cursor.close()
    return age_stat[0]

# this func will tell is disease common to city or location user 
# belongs to
def get_disease_commonality(db,disease_name):
    cursor = db.cursor()
    try:
        query_str = "select d_id from disease where name='%s'" %disease_name
        cursor.execute(query_str)
        d_id = cursor.fetchone()
        query_str = "select common from disease_stats where d_id=%d" %d_id[0]
        cursor.execute(query_str)
        common = cursor.fetchone()
    except Exception as err:
        print (Exception, err)
        print("Unexpected error: get_disease_commonality", sys.exc_info()[0])
        cursor.close()
        return -1
    cursor.close()
    return common[0]

# this function will tell if there any such disease dependency
# means if the disease can happen due to some other pre existing disease
# Ex. like diabetes,High blood pressure can increse the risk of kidney disease
# so that if we are suspecting that user may encounter the disease-X
# we use to call this function to check if user has any existing disease
# that can lead to suspecting one
def check_disease_dependency(db,disease_name):
    weight_inc = 0
    cursor = db.cursor()
    # set default, overright if any
    evidence_disease_dependency[disease_name] = "No Existing Disease Dependency"
    try:
        query_str = "select disease_dependency from disease where name='%s'" %disease_name
        cursor.execute(query_str)
        preceder_diseases = cursor.fetchone()
        if preceder_diseases[0] == None:
            cursor.close()
            return 0
        preceder_list = preceder_diseases[0].split(',')
    except Exception as err:
        print (Exception, err)
        print("Unexpected error: check_disease_dependency_match_user", sys.exc_info()[0])
        cursor.close()
        return(-1)
    existing_disease = get_user_existing_disease()
    existing_list = existing_disease.split(',')
    pos = 0
    effective_dd = []
    while (pos < len(existing_list)):
        if(existing_list[pos] in preceder_list):
            weight_inc = weight_inc + 1
            effective_dd.append(existing_list[pos])
        pos = pos + 1
    cursor.close()
    if (len(effective_dd)):
        evidence_disease_dependency[disease_name] = effective_dd
    return weight_inc

def get_evidence_existing_disease_risk(disease_name):
    return evidence_disease_dependency[disease_name]

segment_map = {'Hypertension':1,'Diabetes':4,'CHD':2,'Obesity':3}

# check if symptoms is due to existing disease
def check_user_existing_vs_predict(db,disease_name):
    cursor = db.cursor()
    segment = 0
    try:
        cursor.execute("select segment from disease where name='%s'" %disease_name)
        segment = cursor.fetchone()
    except Exception as err:
        print (Exception, err)
        print ("Unexpected error: check_user_existing_vs_predict",sys.exc_info()[0])
        cursor.close()
        return 0
    cursor.close()

    existing_disease = get_user_existing_disease()
    existing_list = existing_disease.split(',')
    pos = 0
    while (pos < len(existing_list)):
        existing_segment = existing_list[pos]
        if(int(segment_map[existing_segment]) == int(segment[0])):
            return 1
        pos = pos + 1
    return 0

# check for user stress risk factor
def check_user_stress_factor(disease_name):
    stress = is_user_stressful()
    if (stress) and (disease_name in stress_disease):
        return 1
    return 0

# check for user inactivity risk factor
def check_user_inactive_risk_factor(disease_name):
    physical_activity = get_user_exercise_level()
    if (physical_activity == n_a) and (disease_name in exercise_impact_disease):
        return 1
    return 0

# check for user cholestrol risk factor
def check_user_cholesterol_risk_factor(disease_name):
    cholesterol = get_user_cholesterol()
    if (cholesterol == High) and (disease_name in cholesterol_disease):
        return 1
    return 0

# check for user smoking risk factor
def check_user_smoking_risk_factor(disease_name):
    smoker = is_user_smoker()
    if (smoker) and (disease_name in smoking_disease):
        return 1
    return 0

# check for user alcohol risk factor 
def check_user_alcohol_risk_factor(disease_name):
    alcoholic = is_user_alcoholic()
    if (alcoholic) and (disease_name in alcohol_disease):
        return 1
    return 0

# check for user parent risk factor
def check_parent_risk_factor(disease_name):
    func = parents_disease.get(disease_name)
    # eval() is a function which takes input string as expression or function and runs the code and return result
    if func != None:
        parent_risk = eval(func+"()")
        return parents_weight.get(parent_risk,0)
    else:
        return 0
# Now for each symptom id we will see in symptoms_disease mapping table
# trying to figure out what all nearest possible disease & their weightage
# if majority of symptoms pointing to same disease then weightage of that
# disease will be higher, We will not eliminate other diseses that comes
# through the search but rank of those will be in lower side.

def prepare_disease_list(db,sid):
    # prepare a cursor object
    cursor = db.cursor()
    try:
        query_str = ("select d_id,weight,rank from symptoms_disease where s_id=%s" %sid)
        cursor.execute(query_str)
    except Exception as err:
        print (Exception, err)
        print("Unexpected error: prepare_disease_list", sys.exc_info()[0])
        cursor.close()
        return(-1)

    # we got the disease id for symptom id, We may get more disease
    # for one symptom id
    symp_disease = cursor.fetchone()
    while symp_disease is not None:
        # get the disease id
        d_id = symp_disease[0]
        # get the score/weight
        weight_en = symp_disease[1]
        # get the rank
        rank_en = symp_disease[2]
        # open another cursor object
        cursor_in = db.cursor()
        # get the disease name for disease id
        try:
            query_str =  "select name,sex_dependency from disease where d_id=%s" %str(d_id)
            cursor_in.execute(query_str)
        except Exception as err:
            print (Exception, err)
            print("Unexpected error: prepare_disease_list", sys.exc_info()[0])
            cursor_in.close()
            cursor.close()
            return(-1)
        # TBD We should check against gender here
        # if disease is not common for a user gender
        # we should skip the disease
        disease_details = cursor_in.fetchone()
        disease_name = disease_details[0]
        # NULL means no sex dependency or Male/Female
        sex_dependency = disease_details[1]
        sex = get_user_sex()
        # check if there is any sex dependency for encountered disease
        if sex_dependency and (sex != sex_dependency):
            # if the disease is not intend for user gender, skipping it
            symp_disease = cursor.fetchone()
            cursor_in.close()
            continue

        # check if disease is already added to disease list
        if disease_name not in disease:
            disease.append(disease_name)
            # get the rank
            rank[disease_name] = rank_en
            # get the score 
            weight[disease_name] = weight_en

            num_common_symp[disease_name] = 1
        else:
            # disease is already added to disease list
            rank[disease_name] = rank[disease_name] + rank_en
            weight[disease_name] = weight[disease_name] + weight_en
            num_common_symp[disease_name] = num_common_symp[disease_name] + 1

        # go to next item
        symp_disease = cursor.fetchone()
        # close the inner cursor object
        cursor_in.close()

    # close the cursor object
    cursor.close()
    return 0

def get_len_disease_list():
    return len(disease)

def get_disease_name_by_pos(pos):
    return disease[pos]

def get_weight_for_disease(disease_name):
    return weight[disease_name]

def get_rank_for_disease(disease_name):
    return rank[disease_name]

def get_symp_count_for_disease(disease_name):
    return num_common_symp[disease_name]

def set_rank_for_disease(disease_name,val):
    rank[disease_name] = val

def inc_weight_for_disease_by_val(disease_name,value):
    weight[disease_name] = weight[disease_name] + int(value)

def dec_weight_for_disease_by_val(disease_name,value):
    weight[disease_name] = weight[disease_name] - int(value)
