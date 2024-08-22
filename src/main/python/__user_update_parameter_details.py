import json
import sys
import types
from collections import OrderedDict
from datetime import datetime
from __db_config import *
from __get_json_diff import *

def get_parameter_update(db, email, start_time, end_time):
    cursor = db.cursor()
    query = "select id, name from users where email='%s' and role='DIETITION_ACL'"%(email) 
    cursor.execute(query)
    get_data = cursor.fetchone()
    get_admin_id, get_admin_name = get_data[0], get_data[1]
    query = "select u.id, u.name, u.email from admin_patient_mapping a, users u where a.admin_id=%d and a.patient_id=u.id"%(get_admin_id)
    user_data_dict = {}
    user_data_list = []
    cursor.execute(query)
    get_data = cursor.fetchone()
    while get_data is not None:
        user_data_dict["user_id"] = get_data[0]
        user_data_dict["user_name"] = get_data[1]
        user_data_dict["user_email"] = get_data[2]
        user_data_list.append(user_data_dict) 
        user_data_dict = {}
        get_data = cursor.fetchone()
    user_misc_data_dict = {}
    user_misc_data_list = []
    for data in user_data_list:
        query = "select user_id, provider_id, time_key, parameter_value from user_history_data where user_id=%s and parameter_type='User Misc Data' and parameter_name='user misc data' and time_key >=%s and time_key <=%s order by time_key"
        cursor.execute(query, (int(data.get("user_id")), int(start_time), int(end_time)))
        get_misc = cursor.fetchone()
        get_misc_data_dict = {}
        get_misc_data_list = []
        get_misc_data_dict["user_name"] = data.get("user_name")
        get_misc_data_dict["user_email"] = data.get("user_email")
        get_misc_data_dict["dietitian_name"] = get_admin_name
        while get_misc is not None:
            get_misc_data_dict["user_id"] = get_misc[0] 
            get_misc_data_dict["provider_id"] = get_misc[1] 
            get_misc_data_dict["date"] = get_misc[2]
            get_misc_json = unicode(get_misc[3], errors='ignore')
            get_misc_data_dict["misc_data"] = json.loads(get_misc_json, object_pairs_hook=OrderedDict)
            get_misc_data_list.append(get_misc_data_dict)
            get_misc_data_dict = {}
            get_misc = cursor.fetchone()
        if len(get_misc_data_list) != 0:
            user_misc_data_dict["user_data"] = get_misc_data_list
            user_misc_data_list.append(user_misc_data_dict)
        user_misc_data_dict = {}
    return user_misc_data_list
 

init_db()
db=get_db()

if len(sys.argv) < 4:
    print ("try: \npython __user_parameter_update <user_email> <start_time> <end_time>")
else:
    email = sys.argv[1] 
    start_time = int(sys.argv[2])
    end_time = int(sys.argv[3])
    #get_detail_diet, get_parameter_update = get_parameter_update(db, email, start_time, end_time)
    get_parameter_updates = get_parameter_update(db, email, start_time, end_time)

    data_update_list = []
    if get_parameter_update == []:
        print ('{}')
    for data in get_parameter_updates:
        data_update_dict = OrderedDict() 
        data_update_dict["dietitian_name"] = data.get("user_data")[0].get("dietitian_name")
        data_update_dict["dietitian_email"] = email
        data_update_dict["patient_name"] = data.get("user_data")[0].get("user_name")
        data_update_dict["patient_email"] = data.get("user_data")[0].get("user_email")
        json_updated_parameter = []
        for i in range(0,len(data.get("user_data"))):
            if i == len(data.get("user_data"))-1:
                pass
            else:
                json_1 = dict(data.get("user_data")[i].get("misc_data"))
                json_2 = dict(data.get("user_data")[i+1].get("misc_data"))
                diffs = compare(json_1, json_2)
                if diffs == []:
                    continue
                else:
                    for json_diff in diffs:
                        updated_parameter_dict = OrderedDict()
                        diff_list = json_diff.get("parameter_name").split(".")
                        if len(diff_list) < 3: 
                            parameter_group_name = diff_list[0]
                            parameter_subgroup_name = ""
                            parameter_name = diff_list[1]
                        else:
                            parameter_group_name = diff_list[0] 
                            parameter_subgroup_name = diff_list[1]
                            parameter_name = diff_list[2]
                        updated_parameter_dict["parameter_group_name"] = parameter_group_name
                        updated_parameter_dict["parameter_subgroup_name"] = parameter_subgroup_name
                        updated_parameter_dict["parameter_name"] = parameter_name
                        parameter_value = json_diff.get("parameter_updated_value") 
                        updated_parameter_dict["parameter_value"] = parameter_value
                        updated_parameter_dict["parameter_date"] = data.get("user_data")[i+1].get("date")
                        parameter_previous_value = json_diff.get("parameter_previous_value") 
                        updated_parameter_dict["parameter_previous_value"] = parameter_previous_value
                        updated_parameter_dict["parameter_previous_date"] = data.get("user_data")[i].get("date")
                        updated_parameter_dict["updated_by"] = "dietitian"
                        json_updated_parameter.append(updated_parameter_dict)
                    data_update_dict["data_update"] = json_updated_parameter
        data_update_list.append(data_update_dict) 
    print(json.dumps({"Dietitian_data_update": data_update_list}, indent=4)) 
