#!/usr/bin/python

'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

import sys
import json
from __config import *
from __db_config import *

# segment
segment_id = []
segment_desc = {}
segment_cause = {}

# lifestyle
lifestyle_changes = {}

# preventive pkg
pkg_name = {}
fasting = {}
cost = {}

# food model
food_ok = {}
food_not_ok = {}

# exercise
exercise = {}

# dietary change
dietary_change = {}

# blog related
blogs = {}

def help_msg():
    print "python __profile.py <segment name>"
    print "e.g. python __profile.py 'Hypertension' 'Diabetes'"

def prepare_json_obj():
    pos = 0
    json_data = {}
    profile_segments = []
    while (pos < len(segment_id)):
        profile_segment = {}
        preventive_packages = []
        segment_details = []
        id = segment_id[pos]
        profile_name = get_segment_name(id)
        profile_segment['segment_name'] = profile_name
        profile_segment['segment_desc'] = segment_desc[id]

        segment_detail = {}
        segment_detail['detail_name'] = 'segment_cause'
        segment_detail['detail_string'] = segment_cause[id]
        segment_details.append(segment_detail)

        segment_detail = {}
        segment_detail['detail_name'] = 'lifestyle_change'
        segment_detail['detail_string'] = lifestyle_changes[id]
        segment_details.append(segment_detail)

        segment_detail = {}
        segment_detail['detail_name'] = 'food_ok'
        segment_detail['detail_string'] = food_ok[id]
        segment_details.append(segment_detail)

        segment_detail = {}
        segment_detail['detail_name'] = 'food_not_ok'
        segment_detail['detail_string'] = food_not_ok[id]
        segment_details.append(segment_detail)

        segment_detail = {}
        segment_detail['detail_name'] = 'exercise'
        segment_detail['detail_string'] = exercise[id]
        segment_details.append(segment_detail)

        segment_detail = {}
        segment_detail['detail_name'] = 'dietary_change'
        segment_detail['detail_string'] = dietary_change[id]
        segment_details.append(segment_detail)

        profile_segment['segment_details'] = segment_details

        i = 0
        while (i < len(pkg_name[id])):
            preventive_package = {}
            str = "preventive_pkg_%d" %i
            preventive_package['pkg_name'] = pkg_name[id][i]
            preventive_package['pre_test_info'] = fasting[id][i]
            preventive_package['avg_pkg_cost'] = cost[id][i]
            preventive_packages.append(preventive_package)
            i = i + 1

        profile_segment['preventive_packages'] = preventive_packages
        profile_segment['blogs'] = blogs[id]

        profile_segments.append(profile_segment)
        pos = pos + 1

    json_data['status'] = '0'
    json_data['status_message'] = 'Success'
    json_data['error_details'] = ''
    json_data['profile_segments'] = profile_segments
    json_obj = json.dumps(json_data)
    return json_obj


def prepare_profile_seg(count,profiles):
    pos = 1
    db = get_db()
    cursor = db.cursor()
    while count >= pos:
        try:
            query_str = "select segment_id, segment_desc, cause from profile_segments where segment_name='%s'" %profiles[pos]
            cursor.execute(query_str)
            profile_segments = cursor.fetchone()
            if profile_segments == None:
                print "profile %s not supported" %profiles[pos]
            segment_id.append(profile_segments[0])
            segment_desc[profile_segments[0]] =profile_segments[1]
            segment_cause[profile_segments[0]] = profile_segments[2]
        except Exception as err:
            print (Exception,err)
            print "Fatal error: prepare_profile_seg"
            cursor.close()
            return -1
        pos = pos + 1
    cursor.close()
    return 0

def get_segment_name(seg_id):
    db = get_db()
    cursor = db.cursor()
    seg_name = None
    try:
        query_str = "select segment_name from profile_segments where segment_id = %s" %seg_id
        cursor.execute(query_str)
        seg_name = cursor.fetchone()
    except Exception as err:
        print (Exception, err)
        print "Fatal get_segment_name"
        cursor.close()
        return None
    cursor.close()
    return seg_name[0]

def prepare_lifestyle_changes(seg_id):
    db = get_db()
    if seg_id == None:
        print "Invalid segment id"
        return -1
    cursor = db.cursor()
    try:
        query_str = "select lifestyle_changes from lifestyle_change where segment_id=%s" %seg_id
        cursor.execute(query_str)
        lifestyle = cursor.fetchone()
        lifestyle_changes[seg_id] = lifestyle[0]
    except Exception as err:
        print (Exception, err)
        print "Fatal: prepare_lifestyle_modification"
        cursor.close()
        return -1
    cursor.close()
    return 0

def prepare_preventive_tests(seg_id):
    db = get_db()
    test_name = []
    fasting_info = []
    avg_cost = []
    if seg_id == None:
        print "Invalid segment id"
    cursor = db.cursor()
    try:
        query_str = "select preventive_id from preventive_segment_map where segment_id=%s" %seg_id
        cursor.execute(query_str)
    except Exception as err:
        print (Exception, err)
        print "Fatal prepare_preventive_tests"
        cursor.close()
        return -1
    pre_ids = cursor.fetchone()
    while pre_ids is not None:
        pre_id = pre_ids[0]
        cursor_in = db.cursor()
        try:
            query_str = "select pkg_name,fasting,avg_rate from preventive_tests where preventive_id = %d" %pre_id
            cursor_in.execute(query_str)
        except Exception as err:
            print (Exception, err)
            print "Fatal prepare_preventive_tests"
            cursor_in.close()
            cursor.close()
            return -1
        test_info = cursor_in.fetchone()
        test_name.append(test_info[0])
        fasting_info.append(test_info[1])
        avg_cost.append(test_info[2])
        cursor_in.close()
        pre_ids = cursor.fetchone()

    pkg_name[seg_id] = test_name
    fasting[seg_id] = fasting_info
    cost[seg_id] = avg_cost
    cursor.close()
    return 0

def blog_reference_for_segment(seg_id):
    db = get_db()
    cursor = db.cursor()
    try:
        query_str = "select blog from blogs where segment_id = %s" %seg_id
        cursor.execute(query_str)
    except Exception as err:
        print (Exception, err)
        print "Fatal: blog_reference_for_segment"
        cursor.close()
        return -1
    blogs_seg = cursor.fetchone()
    blogs[seg_id] = blogs_seg[0]
    cursor.close()
    return 0

def prepare_food_model(seg_id):
    db = get_db()
    cursor = db.cursor()
    try:
        query_str = "select food_should_take ,food_should_avoid from food_model where segment_id = %s" %seg_id
        cursor.execute(query_str)
    except Exception as err:
        print (Exception, err)
        print "Fatal: prepare_food_model"
        cursor.close()
        return -1
    food_model = cursor.fetchone()
    food_ok[seg_id] = food_model[0]
    food_not_ok[seg_id] = food_model[1]
    cursor.close()
    return 0

def prepare_exercise_model(seg_id):
    db = get_db()
    cursor = db.cursor()
    try:
        query_str = "select detail_exercise from exercise_model where segment_id = %s" %seg_id
        cursor.execute(query_str)
    except Exception as err:
        print (Exception, err)
        print "Fatal: prepare_exercise_model"
        cursor.close()
        return -1
    exercise_model = cursor.fetchone()
    exercise[seg_id] = exercise_model[0]
    cursor.close()
    return 0

def prepare_dietary_change(seg_id):
    db = get_db()
    cursor = db.cursor()
    try:
        query_str = "select dietary_change from dietary_change where segment_id = %s" %seg_id
        cursor.execute(query_str)
    except Exception as err:
        print (Exception, err)
        print "Fatal: prepare_dietary_change"
        cursor.close()
        return -1
    dietary_info = cursor.fetchone()
    dietary_change[seg_id] = dietary_info[0]
    cursor.close()
    return 0

def display_result():
    pos = 0
    while pos < len(segment_id):
        seg_id = segment_id[pos]
        print "Name:"
        print get_segment_name(seg_id)
        print ""
        print "Description:"
        print segment_desc[seg_id]
        print ""
        print "Cause:"
        print segment_cause[seg_id]
        print ""
        print "Food Model:"
        print "Preferred list:"
        print food_ok[seg_id]
        print "Avoidance list:"
        print food_not_ok[seg_id]
        print ""
        print "Exercise Model:"
        print exercise[seg_id]
        print ""
        print "Dietary Changes:"
        print dietary_change[seg_id]
        print ""
        print "Lifestyle Changes:"
        print lifestyle_changes[seg_id]
        print ""
        print "Preventive Tests:"
        i = 0
        while (i < len(pkg_name[seg_id])):
            print pkg_name[seg_id][i]
            print "Pre test info:"
            print fasting[seg_id][i]
            print "Avg cost:"
            print cost[seg_id][i]
            i = i + 1

        print ""
        print "Follow blogs:"
        print blogs[seg_id]
        pos = pos + 1

if __name__ == '__main__':

    arguments = len(sys.argv) -1
    if arguments < 1:
        help_msg()
        exit(0)

    init_db()

    ret = prepare_profile_seg(arguments,sys.argv)
    if ret:
        print "Fatal prepare_profile_seg"
        close_db()
        exit(-1)

    pos = 0
    while pos < len(segment_id):
        prepare_lifestyle_changes(segment_id[pos])
        pos = pos + 1
    pos = 0
    while pos < len(segment_id):
        prepare_preventive_tests(segment_id[pos])
        pos = pos + 1
    pos = 0
    while pos < len(segment_id):
        prepare_food_model(segment_id[pos])
        pos = pos + 1
    pos = 0
    while pos < len(segment_id):
        prepare_exercise_model(segment_id[pos])
        pos = pos + 1
    pos = 0
    while pos < len(segment_id):
        prepare_dietary_change(segment_id[pos])
        pos = pos + 1
    pos = 0
    while pos < len(segment_id):
        blog_reference_for_segment(segment_id[pos])
        pos = pos + 1
 
    # display_result()
    json_obj = prepare_json_obj()
    print json_obj
    # close db before exit
    close_db()
    exit(0)
