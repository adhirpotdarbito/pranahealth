'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

import sys
import json
import csv
import os
from __db_config import *

def help_msg():
    print "python __parse_report.py <user_id> <dd/mm/yy> <report>"
    return

def update_prediction_diabetes_param(db,user_id,date,val):
    cursor = db.cursor()
    try:
        query_str = "insert into prediction_diabetes_params (user_id,report_date,glucose_fasting,glucose_pp,HbA1C) values(%d,'%s',%s,%s,%s);" %(user_id,date,val[0],str(val[1]),str(val[2]))
        cursor.execute(query_str)
        db.commit()
    except Exception as err:
        print (Exception,err)
        print "Fatal: update_prediction_diabetes_param"
        cursor.close()
        return -1

    cursor.close()
    return 0


def parseReport_dia(db,user_id,date,report):
    val = []
    with open('../experiment/__config_diabetes_ref', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cmd = "../experiment/parseReport %s out '%s'" %(report,row['name'])
            ret = os.system(cmd)
            # open the out file & read the value
            fd = open("out","r")
            rd = fd.read()
            if (rd == ''):
                val.append('NULL')
            else:
                val.append(rd)
            # update the db here
            # update_diabetes_param (fd.read(),row['name'],date)
            fd.close()
            os.system("rm -f out")
    update_prediction_diabetes_param(db,user_id,date,val)

if __name__ == '__main__':

    argc = len(sys.argv) -1
    if (argc < 3):
        help_msg()
        exit(0)
    try:
        user_id = int (sys.argv[1])
    except Exception as err:
        print (Exception, err)
        help_msg()
        exit(0)

    init_db()
    db = get_db()
    parseReport_dia(db,user_id,sys.argv[2],sys.argv[3])
    close_db()
    exit(0)
