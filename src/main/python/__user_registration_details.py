import json
import os
import sys
from collections import OrderedDict
from __db_config import *


total_num_user = []
user_details_array = []

def numUsers(db):
    cursor = db.cursor()
    query = "select email from users"
    cursor.execute(query)
    num_user = cursor.fetchone()
    while num_user is not None:
        total_num_user.append(num_user[0])
        num_user = cursor.fetchone()
    return total_num_user


def userRegistrationDetails(db):
    user_details = OrderedDict()
    cursor = db.cursor()
    if len(sys.argv) > 1: 
        user_email = sys.argv[1]
        query = "select id, name, contact, email from users where email='%s'"%user_email
        cursor.execute(query)
        user_reg_details = cursor.fetchone()
        #print user_reg_details 
        user_details["user_id"] = user_reg_details[0]
        user_details["name"] = user_reg_details[1]
        user_details["contact_number"] = user_reg_details[2]
        user_details["email_address"] = user_reg_details[3]
        query_1 = "select * from user_body_param where id=%d"%int(user_details["user_id"])
        if cursor.execute(query_1) == 0:
            user_details["user_body_parameter"] = 0
        else:
            user_details["user_body_parameter"] = 1

        query_2 = "select * from user_ls_habit where id=%d"%int(user_details["user_id"])
        if cursor.execute(query_2) == 0:
            user_details["user_lifestyle_habit"] = 0
        else:
            user_details["user_lifestyle_habit"] = 1

        query_3 = "select * from user_family_history where id=%d"%int(user_details["user_id"])
        if cursor.execute(query_3) == 0:
            user_details["user_family_history"] = 0
        else:
            user_details["user_family_history"] = 1

        query_4 = "select * from user_medical_data where id=%d"%int(user_details["user_id"])
        if cursor.execute(query_4) == 0:
            user_details["user_medical_data"] = 0
        else:
            user_details["user_medical_data"] = 1

        query_5 = "select * from user_cr_risk where id=%d"%int(user_details["user_id"])
        if cursor.execute(query) == 0:
            user_details["user_cardiac_data"] = 0
        else:
            user_details["user_cardiac_data"] = 1

        if os.path.isfile('/opt/atman/sql/user_lifestyle_data/lifestyle_activity_'+ str(user_details["user_id"])):
            user_details["user_build_lifestyle_data"] = 1
        else:
            user_details["user_build_lifestyle_data"] = 0

        file_path = '/opt/atman/sql/user_lifestyle_data/daily/'
        file_list = [f for f in os.listdir(file_path) if f.split('_')[0] == str(user_details["user_id"])]
        user_details["daily_food_model"] = [f.split("_")[1][0:8] for f in file_list]

        user_details_array.append(user_details)

    else:
        for user_email in total_num_user:
            query = "select id,name, contact, email from users where email='%s'"%user_email
            cursor.execute(query)
            user_reg_details = cursor.fetchone()
            #print user_reg_details 
            user_details["user_id"] = user_reg_details[0]
            user_details["name"] = user_reg_details[1]
            user_details["contact_number"] = user_reg_details[2]
            user_details["email_address"] = user_reg_details[3]
            query_1 = "select * from user_body_param where id=%d"%int(user_details["user_id"])
            if cursor.execute(query_1) == 0:
                user_details["user_body_parameter"] = 0
            else:
                user_details["user_body_parameter"] = 1

            query_2 = "select * from user_ls_habit where id=%d"%int(user_details["user_id"])
            if cursor.execute(query_2) == 0:
                user_details["user_lifestyle_habit"] = 0
            else:
                user_details["user_lifestyle_habit"] = 1
     
            query_3 = "select * from user_family_history where id=%d"%int(user_details["user_id"])
            if cursor.execute(query_3) == 0:
                user_details["user_family_history"] = 0
            else:
                user_details["user_family_history"] = 1
        
            query_4 = "select * from user_medical_data where id=%d"%int(user_details["user_id"])
            if cursor.execute(query_4) == 0:
                user_details["user_medical_data"] = 0
            else:
                user_details["user_medical_data"] = 1

            query_5 = "select * from user_cr_risk where id=%d"%int(user_details["user_id"])
            if cursor.execute(query) == 0:
                user_details["user_cardiac_data"] = 0
            else:
                user_details["user_cardiac_data"] = 1

            if os.path.isfile('/opt/atman/sql/user_lifestyle_data/lifestyle_activity_'+ str(user_details["user_id"])):
                user_details["user_build_lifestyle_data"] = 1
            else:
                user_details["user_build_lifestyle_data"] = 0
  
            file_path = '/opt/atman/sql/user_lifestyle_data/daily/'
            file_list = [f for f in os.listdir(file_path) if f.split('_')[0] == str(user_details["user_id"])]
            user_details["daily_food_model"] = [f.split("_")[1][0:8] for f in file_list]
       
            user_details_array.append(user_details)
            user_details = OrderedDict()
    return user_details_array


try:
    init_db()
    db = get_db()
    numUsers(db)
    userRegistrationDetails(db)
    print json.dumps({"user_registration_details" : user_details_array}, indent=4)
except Exception as err:
    print "user not found"
