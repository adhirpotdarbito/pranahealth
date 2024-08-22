'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

import sys
import gmplot
from __users import *
from __symptoms import *
from __diseases import *
from __doctors import *
from __pathology import *
from __rank import *
from __gmap_plot import *
from __config import *
import json
from __db_config import *

def build_doctors_data(doctors):
    doctors_data = []
    doctor_data = {}
    doctor = []
    lat_long = []

    for doctor in doctors:
        doctor_data['doctor_id'] = doctor[0]
        doctor_data['doctor_name'] = doctor[1]
        doctor_data['doctor_address'] = doctor[2]
        doctor_data['doctor_phone'] = doctor[3]
        doctor_data['doctor_rating'] = doctor[4]
        lat_long = get_doc_location(db, doctor)
        doctor_data['doctor_lattitude'] = lat_long[0]
        doctor_data['doctor_longitude'] = lat_long[1]

        doctors_data.append(doctor_data)
        doctor_data = {}
        lat_long = []

    return doctors_data

def prepare_json_obj():
    pos = 0
    json_data = {}
    doctors = []
    symptom_mappings = []
    while (pos < get_len_disease_list()):
        symptom_mapping = {}
        disease_name = get_disease_name_by_pos(pos)
        symptom_mapping['disease_name'] = disease_name
        symptom_mapping['disease_comonality'] = get_disease_commonality(get_db(),disease_name)
        # disease weight is for internal use, require for sorting in UI/UX
        # if weight is higher means top of list
        symptom_mapping['disease_weight_internal'] = get_weight_for_disease(disease_name)
        symptom_mapping['chance'] = get_rank_weight_per_disease(disease_name)
        symptom_mapping['all_symptoms'] = get_all_symptoms_per_disease(disease_name)
        symptom_mapping['alarming_symptoms'] = get_all_alarming_symptoms_per_disease(disease_name)
        symptom_mapping['emergency_symptoms'] = get_all_emergency_symptoms_per_disease(disease_name)
        symptom_mapping['user_alarming_symptoms'] = get_user_alarming_symps(disease_name)
        symptom_mapping['user_emergency_symptoms'] = get_user_emergency_symp(disease_name)
        doctors = get_doctor_list_for_disease(disease_name)
        symptom_mapping['doctor_details'] = build_doctors_data(doctors)
        symptom_mapping['path_tests'] = get_path_tests_per_disease(disease_name)
        symptom_mapping['evidence_parent_risk'] = get_evidence_parent_risk(disease_name)
        symptom_mapping['evidence_age_risk'] = get_evidence_age_risk(disease_name)
        symptom_mapping['evidence_inactive_risk'] = get_evidence_inactive_risk(disease_name)
        symptom_mapping['evidence_stress_risk'] = get_evidence_stress_risk(disease_name)
        symptom_mapping['evidence_smoking_risk'] = get_evidence_smoking_risk(disease_name)
        symptom_mapping['evidence_alcohol_risk'] = get_evidence_alcohol_risk(disease_name)
        symptom_mapping['evidence_cholesterol_risk'] = get_evidence_cholesterol_risk(disease_name)
        symptom_mapping['evidence_existing_disease_impact'] = get_evidence_existing_disease_risk(disease_name)
        symptom_mappings.append(symptom_mapping)
        pos = pos + 1

    # Well, here is the json data I should give to RESTFul API
    #json_data['lat_list'] = get_lat_list_doctors()
    #json_data['long_list'] = get_long_list_doctors()

    json_data['status'] = '0'
    json_data['status_message'] = 'Success'
    json_data['error_details'] = ''
    json_data['symptom_mappings'] = symptom_mappings
    json_data['user_symptoms'] = get_user_given_symptoms()
    json_obj = json.dumps(json_data)
    return json_obj

# this is just for internal use, it should be disabled
# in release mode
def display_result():
    pos = 0
    while (pos < get_len_disease_list()):
        disease_name = get_disease_name_by_pos(pos)
        chance = get_rank_weight_per_disease(disease_name)
        print "disease: %s" %disease_name
        print ""
        print "chance: %s" %chance
        print ""
        print "common symptoms:"

        # list all possible symptoms for the disease
        disease_symp = get_all_symptoms_per_disease(disease_name)
        idx = 0
        while (idx < len(disease_symp)):
            print "%s" %disease_symp[idx]
            idx = idx +1
        print ""

        doctor_details = get_doctor_list_for_disease(disease_name)
        print "doctors details:"
        idx = 0
        while (idx <len(doctor_details)):
            print "%s" %str(doctor_details[idx][1])
            print "ADDRESS: %s" %str(doctor_details[idx][2])
            print "PHONE: %s" %str(doctor_details[idx][3])
            print "RATING: %s" %str(doctor_details[idx][4])
            idx = idx +1
        print ""

        print "pathology tests:"
        path_test = get_path_tests_per_disease(disease_name)
        print "%s" %path_test[0]
        pos = pos + 1
        print "********************************************************************************"        

def help_msg():
    print "python __main.py <user_id> <symptoms>"
    print "Ex: python __main.py 1 'pain during urination' 'frequent urination' 'vomiting' 'chills'"


if __name__ == '__main__':
    # get the total num arg
    arguments = len(sys.argv) - 1
    if arguments <2:
        help_msg()
        exit(0)
    try:
        user_id = int(sys.argv[1])
    except Exception as err:
        print (Exception, err)
        help_msg()
        exit(0)
    #print('User Id: ', user_id) 
    
    # open db pranacare
    init_db()
    db = get_db()
    # init the user info class
    user_info = init_user_info(user_id)
    # prepare user basic data
    ret = prepare_user_basic_data(db,user_info)
    if ret != 0:
        close_db()
        print('Failed to retrieve user_basic_data.')
        exit(-1)
    # prepare user body params
    ret = prepare_user_body_params(db,user_info)
    if ret != 0:
        close_db()
        print ('Failed to retrieve user_body_param.')
        exit(-1)

    # prepare user medical data
    ret = prepare_user_medical_data(db,user_info)
    if ret != 0:
        close_db()
        print('Failed to retrieve user_medical_data.')
        exit(-1)

    # prepare user family history
    ret = prepare_user_family_data(db,user_info)
    if ret != 0:
        close_db()
        print ('Failed to retrieve user_family_history.')
        exit(-1)

    # prepare user lifestyle habit
    ret = prepare_user_lifestyle_habit(db,user_info)
    if ret != 0:
        close_db()
        print('Failed to retrieve user_lifestyle_habit.')
        exit(-1)
    #print('Retrived User Data.')

    # get all symptoms details
    ret = prepare_symp_id(db,arguments,sys.argv)
    if ret != 0:
        close_db()
        print('Unsupported Symptoms are provided.')
        exit(-1)
    #print('Retrived Symptom Data.')

    # prepare the disease list
    pos = 0
    while (pos < get_num_user_symptoms()):
        sid = get_sid_by_pos(pos)
        ret = prepare_disease_list(db,sid)
        if ret != 0:
            close_db()
            print('Failed to retrieve Disease Data.')
            exit(-1)
        pos = pos + 1
    # get other symptoms for disease
    pos = 0
    while (pos < get_len_disease_list()):
        disease_name = get_disease_name_by_pos(pos)
        ret = prepare_all_possible_symptom_per_disease(db,disease_name)
        if ret != 0:
            close_db()
            print('Failed to retrieve Symptoms and Disease Mapping.')
            exit(-1)
        pos = pos + 1
    #print('Retrived and Prepared Disease Data.')
    # prepare alarming symptoms
    pos = 0
    while (pos < get_len_disease_list()):
        disease_name = get_disease_name_by_pos(pos)
        ret = prepare_all_alarming_symptom_per_disease(db,disease_name)
        if ret != 0:
            close_db()
            print('Failed to retrieve all alarming symptoms per disease.')
            exit(-1)
        pos = pos + 1
    pos = 0
    # prepare emergency symptoms
    while (pos < get_len_disease_list()):
        disease_name = get_disease_name_by_pos(pos)
        ret = prepare_all_emergency_symptom_per_disease(db,disease_name)
        if ret != 0:
            close_db()
            print('Failed to retrieve all emergency symptoms per disease.')
            exit(-1)
        pos = pos + 1
    # prepare user alerming/emergency symptoms
    pos = 0
    while (pos < get_len_disease_list()):
        disease_name = get_disease_name_by_pos(pos)
        ret = prepere_user_alarming_emergency_symptoms(disease_name)
        if ret != 0:
            close_db()
            print('Failed to prepare user alarming/emergency symptoms list.')
            exit(-1)
        pos = pos + 1
    # prepare the doc details
    pos = 0
    while (pos < get_len_disease_list()):
        disease_name = get_disease_name_by_pos(pos)
        ret = prepare_doctor_details_per_disease(db,disease_name)
        if ret != 0:
            close_db()
            print('Failed to retrieve Doctors Data.')
            exit(-1)
        pos = pos + 1
    #print('Retrived and Prepared Doctors Data.')

    # prepare pathology details
    pos = 0
    while (pos < get_len_disease_list()):
        disease_name = get_disease_name_by_pos(pos)
        ret = get_path_tests_for_disease(db,disease_name)
        if ret != 0:
            close_db()
            print('Failed to retrieve Pathology Labs Data.')
            exit(-1)
        pos = pos + 1
    #print('Retrived and Prepared Pathology Labs Data.')

    # AI func to score analysis
    pos = 0
    while (pos < get_len_disease_list()):
        disease_name = get_disease_name_by_pos(pos)
        calculate_rank_weight_per_disease(db,disease_name)
        pos = pos + 1
    # prepare marker list for gmap
    pos = 0
    while (pos < get_len_disease_list()):
        disease_name = get_disease_name_by_pos(pos)
        ret = prepare_doc_location_for_disease(db,disease_name)
        if ret != 0:
            close_db()
            exit(-1)
        pos = pos + 1
    # TBD display raw format
    # display_result()
    # plot in google map
    plot_doctors_loc_gmap()
    # prepare a json object
    json_obj = prepare_json_obj()
    print(json_obj)
    # close the db
    close_db()

    exit(0)
