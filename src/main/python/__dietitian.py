'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

import sys
from __users import *

dietitian_list = []

def build_dietitian_data(dietitian_list):
    dietitians_data = []
    dietitian_data = {}
    dietitian = []

    for dietitian in dietitian_list:
        dietitian_data['id'] = dietitian[0]
        dietitian_data['name'] = dietitian[1]
        dietitian_data['city'] = dietitian[2]
        dietitian_data['address'] = dietitian[3]
        dietitian_data['phone'] = dietitian[4]
        dietitian_data['rating'] = dietitian[5]

        dietitians_data.append(dietitian_data)
        dietitian_data = {}

    return dietitians_data

def prepare_dietitian_details (db):
    cursor = db.cursor()
    try:
        query_str = "select * from dietitian where city='%s'" %get_user_city()
        cursor.execute(query_str)
        dietitian = cursor.fetchone()
        while dietitian is not None:
            dietitian_list.append(dietitian)
            dietitian = cursor.fetchone()
    except Exception as err:
        print (Exception, err)
        print ("Fatal error: prepare_dietitian_details")
        cursor.close()
        return ""

    cursor.close()
    return build_dietitian_data(dietitian_list)
