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

result_json = {}
result_json_ci = {}
result_json_cb = {}

def get_user_rdca(user_id,db):
    user_rdca = 0.0
    cursor = db.cursor()
    try:
        query_str = "select rdca from user_recommended_rdca where user_id=%d" %user_id
        cursor.execute(query_str)
        user_rdca = cursor.fetchone()
    except Exception as err:
        print (Exception,err)
        print ("Fatal Error: get_user_rdca")
        cursor.close()
        return -1
    cursor.close()
    return int(user_rdca[0])

def get_user_rcb(user_id,db):
    user_rcb = 0.0
    cursor = db.cursor()
    try:
        query_str = "select rcb from user_recommended_cb where user_id=%d" %user_id
        cursor.execute(query_str)
        user_rcb = cursor.fetchone()
    except Exception as err:
        print (Exception,err)
        print ("Fatal Error: get_user_rcb")
        cursor.close()
        return -1
    cursor.close()
    return int(user_rcb[0])

def get_user_ci_data(date,user_id,db):
    cal_em = 0
    cal_bf = 0
    cal_mm = 0
    cal_lunch = 0
    cal_es = 0
    cal_din = 0
    result_json_ci['CI_DATE'] = date
    cursor = db.cursor()
    try:
        query_str = "select cal_em,cal_bf,cal_mm,cal_lunch,cal_es,cal_din from user_tracking_ci where user_id=%d and date='%s'" %(user_id,date)
        cursor.execute(query_str)
        user_ci = cursor.fetchone()
        if user_ci:
            cal_em = user_ci[0]
            cal_bf = user_ci[1]
            cal_mm = user_ci[2]
            cal_lunch = user_ci[3]
            cal_es = user_ci[4]
            cal_din = user_ci[5]
            result_json_ci['CI_EM'] = cal_em
            result_json_ci['CI_BF'] = cal_bf
            result_json_ci['CI_MM'] = cal_mm
            result_json_ci['CI_LUNCH'] = cal_lunch
            result_json_ci['CI_ES'] = cal_es
            result_json_ci['CI_DINNER'] = cal_din

    except Exception as err:
        print (Exception,err)
        print "Fatal Error: get_user_ci_data"
        cursor.close()
        return -1

    result_json_ci['CI_TOTAL'] = (cal_em+cal_bf+cal_mm+cal_lunch+cal_es+cal_din)
    result_json_ci['CI_RECOMMENDED'] = get_user_rdca(user_id,db)
    cursor.close()

    return result_json_ci

def get_user_cb_data(date,user_id,db):
    cb_post_lunch = 0.0
    cb_post_dinner = 0.0
    cb_main = 0.0
    result_json_cb['CB_DATE'] = date
    cursor = db.cursor()
    try:
        query_str = "select cb_post_lunch,cb_post_dinner,cb_main from user_tracking_cb where user_id=%d and date='%s'" %(user_id,date)
        cursor.execute(query_str)
        user_cb = cursor.fetchone()
        if user_cb:
            cb_post_lunch = user_cb[0]
            cb_post_dinner = user_cb[1]
            cb_main = user_cb[2]
            result_json_cb['CB_POST_LUNCH'] = cb_post_lunch
            result_json_cb['CB_POST_DINNER'] = cb_post_dinner
            result_json_cb['CB_MAIN'] = cb_main

    except Exception as err:
        print (Exception,err)
        print "Fatal Err: get_user_cb_data"
        cursor.close()
        return -1

    result_json_cb['CB_TOTAL'] = (cb_post_dinner+cb_post_lunch+cb_main)
    result_json_cb['CB_RECOMMENDED'] = get_user_rcb(user_id,db)
    cursor.close()
    return result_json_cb 

if __name__ == '__main__':
    argc = len(sys.argv) - 1
    if (argc < 2):
        print "python __lifestyle_notification <id> <date>"
        exit(0)

    init_db()
    db = get_db()

    user_id = sys.argv[1]
    date = sys.argv[2]

    result_json["USER_ID"] = user_id
    result_json["CI_DATA"] = get_user_ci_data(int(date),int(user_id),db)
    result_json["CB_DATA"] = get_user_cb_data(int(date),int(user_id),db)
    print json.dumps(result_json)
    close_db()
    exit(0)
