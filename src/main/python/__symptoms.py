'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

import sys

# list to store of all symptom id provided by user
symp_id = []
user_symptoms = []
user_symptoms_alarming = {}
user_symptoms_emergency = {}
# common symptoms for disease
# disease_symp_all[disease] --> all common symptoms for disease
disease_symp_all = {}
disease_symp_alarming = {}
disease_symp_emergency = {}

def prepere_user_alarming_emergency_symptoms(disease_name):
    pos = 0
    user_symp_alarm = []
    user_symp_emergen = []
    while (pos < len(user_symptoms)):
        if (user_symptoms[pos] in disease_symp_alarming[disease_name]):
            user_symp_alarm.append(user_symptoms[pos])
        if (user_symptoms[pos] in disease_symp_emergency[disease_name]):
            user_symp_emergen.append(user_symptoms[pos])

        pos = pos + 1
    user_symptoms_alarming[disease_name] = user_symp_alarm
    user_symptoms_emergency[disease_name] = user_symp_emergen
    return 0

def get_user_alarming_symps(disease_name):
    return user_symptoms_alarming[disease_name]

def get_user_emergency_symp(disease_name):
    return user_symptoms_emergency[disease_name]

# this func will retrieve all symptom id
# from symptom table for each symptom user provided
# store all symptom id to symp_id list

def prepare_symp_id(db,count,symptoms):
    # prepare a cursor object
    cursor = db.cursor()
    # symptoms start from pos 2 in command line args
    # pos 1 is for user_id
    pos = 2
    while (count >= pos):
        try:
            user_symptoms.append(symptoms[pos])
            # get s_id for all symptoms that user provided
            #print('Looking for Symptom: ', symptoms[pos])
            query_str = ("select s_id from symptoms where name='%s'" %symptoms[pos])
            cursor.execute(query_str)
            symptom = cursor.fetchone()
            # added s_id to symp_id list
            symp_id.append(symptom[0])
        except Exception as err:
            print (Exception, err)
            print("Unexpected error: prepare_symp_id", sys.exc_info()[0])
            cursor.close()
            return(-1)
        # go to next symptoms
        pos = pos +1
    # close the cursor
    cursor.close()
    return 0

# count total number of symptoms user encountered
def get_num_user_symptoms():
    return len(symp_id)

# get symptom_id by position
def get_sid_by_pos(pos):
    return symp_id[pos]

def get_user_given_symptoms():
    return user_symptoms

def prepare_all_possible_symptom_per_disease(db,disease_name):
    # open the cursor object
    cursor = db.cursor()
    symptoms = []
    try:
        query_str = ("select d_id from disease where name='%s'" %disease_name)
        cursor.execute(query_str)
        d_id = cursor.fetchone()
    except Exception as err:
        print (Exception, err)
        print("Unexpected error: prepare_all_possible_symptom_per_disease", sys.exc_info()[0])
        cursor.close()
        return(-1)
    try:
        query_str = ("select s_id from symptoms_disease where d_id=%s" %d_id)
        cursor.execute(query_str)
        s_id = cursor.fetchone()
        while s_id is not None:
            cursor_in = db.cursor()
            query_str = ("select name from symptoms where s_id=%s" %s_id)
            cursor_in.execute(query_str)
            symp = cursor_in.fetchone()
            symptoms.append(symp[0])
            s_id = cursor.fetchone()
            # close the inner cursor
            cursor_in.close()
    except Exception as err:
        print (Exception, err)
        print("Unexpected error: prepare_all_possible_symptom_per_disease", sys.exc_info()[0])
        cursor.close()
        return(-1)

    # store all possible symptoms for any disease in global dictionary
    disease_symp_all[disease_name] = symptoms
    # close the cursor object
    cursor.close()
    return 0

def prepare_all_alarming_symptom_per_disease(db,disease_name):
    # open the cursor object
    cursor = db.cursor()
    symptoms = []
    try:
        query_str = ("select d_id from disease where name='%s'" %disease_name)
        cursor.execute(query_str)
        d_id = cursor.fetchone()
    except Exception as err:
        print (Exception, err)
        print("Unexpected error: prepare_all_possible_symptom_per_disease", sys.exc_info()[0])
        cursor.close()
        return(-1)
    try:
        query_str = ("select s_id from symptoms_disease where d_id=%s and rank=1" %d_id)
        cursor.execute(query_str)
        s_id = cursor.fetchone()
        while s_id is not None:
            cursor_in = db.cursor()
            query_str = ("select name from symptoms where s_id=%s" %s_id)
            cursor_in.execute(query_str)
            symp = cursor_in.fetchone()
            symptoms.append(symp[0])
            s_id = cursor.fetchone()
            # close the inner cursor
            cursor_in.close()
    except Exception as err:
        print (Exception, err)
        print("Unexpected error: prepare_all_possible_symptom_per_disease", sys.exc_info()[0])
        cursor.close()
        return(-1)

    # store all possible symptoms for any disease in global dictionary
    disease_symp_alarming[disease_name] = symptoms
    # close the cursor object
    cursor.close()
    return 0

def prepare_all_emergency_symptom_per_disease(db,disease_name):
    # open the cursor object
    cursor = db.cursor()
    symptoms = []
    try:
        query_str = ("select d_id from disease where name='%s'" %disease_name)
        cursor.execute(query_str)
        d_id = cursor.fetchone()
    except Exception as err:
        print (Exception, err)
        print("Unexpected error: prepare_all_possible_symptom_per_disease", sys.exc_info()[0])
        cursor.close()
        return(-1)
    try:
        query_str = ("select s_id from symptoms_disease where d_id=%s and weight >=1" %d_id)
        cursor.execute(query_str)
        s_id = cursor.fetchone()
        while s_id is not None:
            cursor_in = db.cursor()
            query_str = ("select name from symptoms where s_id=%s" %s_id)
            cursor_in.execute(query_str)
            symp = cursor_in.fetchone()
            symptoms.append(symp[0])
            s_id = cursor.fetchone()
            # close the inner cursor
            cursor_in.close()
    except Exception as err:
        print (Exception, err)
        print("Unexpected error: prepare_all_possible_symptom_per_disease", sys.exc_info()[0])
        cursor.close()
        return(-1)

    # store all possible symptoms for any disease in global dictionary
    disease_symp_emergency[disease_name] = symptoms
    # close the cursor object
    cursor.close()
    return 0

def get_all_symptoms_per_disease(disease_name):
    return disease_symp_all[disease_name]

def get_all_alarming_symptoms_per_disease(disease_name):
    return disease_symp_alarming[disease_name]

def get_all_emergency_symptoms_per_disease(disease_name):
    return disease_symp_emergency[disease_name]
