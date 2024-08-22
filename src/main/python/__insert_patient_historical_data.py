import json
import sys
import csv
from __db_config import *
from collections import OrderedDict
from datetime import datetime

def insertPatientHistoricalData(admin_email, patient_email, section_name, subsection_name, parameter_name, csv_file):
    with open("/opt/atman/config/misc_data.json", "r") as f:
        json_empty_misc_file = json.load(f)

    #get patient id
    cursor = db.cursor()
    query = "select id from users where email='%s'"%(patient_email) 
    cursor.execute(query)
    patient_id = cursor.fetchone()[0]

    #get admin id
    query = "select id from users where email='%s'"%(admin_email) 
    cursor.execute(query)
    admin_id = cursor.fetchone()[0]

    #read csv file
    date_value = OrderedDict()
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            date_value[row['date']] = row['value']

    #handle each date & value available in csv file
    for date, value in date_value.items():

        #for user_history_data
        query = "SELECT parameter_value from user_history_data where user_id=%d and provider_id=%d and parameter_name='user misc data' and time_key='%s'"%(int(patient_id), int(admin_id), date)
        get_data = cursor.execute(query)
        if get_data == 0:
            #initialize empty misc data
            json_misc_file = json_empty_misc_file
 
            json_misc_file[section_name][subsection_name][parameter_name]["measure"] = value 
            timestamp_str = datetime.strptime(date, '%Y%m%d').strftime('%Y-%m-%d') + " 00:00:00"
            query = "INSERT INTO user_history_data(time_key, user_id, provider_id, parameter_type, parameter_name, parameter_value, timestamp) VALUES(%s, %s, %s, 'User Misc Data', 'user misc data', %s, %s)"
            cursor.execute(query, (int(date), int(patient_id), int(admin_id), json.dumps(json_misc_file), timestamp_str))
            db.commit()
            print("History Data added for: "  + date + " for: " + value)
        else:
            misc_data = json.loads(unicode(cursor.fetchone()[0], errors='ignore'))
            misc_data[section_name][subsection_name][parameter_name]["measure"] = value 
            query = "Update user_history_data set parameter_value=%s where user_id=%s and provider_id=%s and parameter_type='User Misc Data' and parameter_name='user misc data' and time_key=%s" 
            cursor.execute(query, (json.dumps(misc_data), int(patient_id), int(admin_id), int(date))) 
            db.commit()
            print("History Data updated for: "  + date + " for: " + value)

        # for user_data_update
        query = "SELECT parameter_value from user_data_update where user_id=%d and provider_id=%d and parameter_name='user misc data'"%(int(patient_id), int(admin_id))  
        get_data = cursor.execute(query)
        if get_data == 0:
            #initialize empty misc data
            json_misc_file = json_empty_misc_file
 
            json_misc_file[section_name][subsection_name][parameter_name]["measure"] = value 
            query = "INSERT INTO user_data_update(time_key, user_id, provider_id, parameter_type, parameter_name, parameter_value) VALUES(%s, %s, %s, 'User Misc Data', 'user misc data', %s)"
            cursor = db.cursor()
            cursor.execute(query, (int(date), int(patient_id), int(admin_id), json.dumps(json_misc_file)))
            db.commit()
            print("Recent Data added for: " + date + " for: " + value)
        else:
            misc_data = json.loads(unicode(cursor.fetchone()[0], errors='ignore'))
            misc_data[section_name][subsection_name][parameter_name]["measure"] = value 
            query = "UPDATE user_data_update set parameter_value=%s, time_key=%s WHERE user_id=%s AND provider_id=%s AND parameter_type='User Misc Data' AND parameter_name='user misc data'"
            cursor.execute(query, (json.dumps(misc_data), int(date), int(patient_id), int(admin_id)))
            db.commit()
            print("Recent Data updated for: " + date + " for: " + value)

        # for user_misc_data
        query = "select misc_data from user_misc_data where id=%d"%(patient_id)
        get_data = cursor.execute(query)
        if get_data == 0:
            #initialize empty misc data
            json_misc_file = json_empty_misc_file
 
            json_misc_file[section_name][subsection_name][parameter_name]["measure"] = value 
            query = "INSERT INTO user_misc_data(id, admin_id, misc_data, recommendations) VALUES(%s, %s, %s, '{}')"
            cursor.execute(query , (int(patient_id), int(admin_id), json.dumps(json_misc_file)))
            db.commit()
            print("Misc Data added for: " + date + " for: " + value)
        else:
            misc_data = json.loads(unicode(cursor.fetchone()[0],errors='ignore'))
            misc_data[section_name][subsection_name][parameter_name]["measure"] = value 
            query = "Update user_misc_data set misc_data=%s where id=%s and admin_id=%s"
            cursor.execute(query , (json.dumps(misc_data), int(patient_id), int(admin_id)))
            db.commit()
            print("Misc Data updated for: " + date + " for: " + value)


if __name__ == "__main__":
    if len(sys.argv) != 7:
        print ("python __insert_patient_historical_data.py <admin_email> <patient_email> <section_name> <subsection_name> <parameter_name> <csv_file>")
        print('python __insert_patient_historical_data.py "admin@gmail.com" "patient@gmail.com" "Anthropometry" "body_measurements" "weight" patient_history_data.csv')
    else:
        admin_email = sys.argv[1]
        patient_email = sys.argv[2]
        section_name = sys.argv[3]
        subsection_name = sys.argv[4]
        parameter_name = sys.argv[5]
        csv_file = sys.argv[6]
        init_db()
        db = get_db()
        insertPatientHistoricalData(admin_email, patient_email, section_name, subsection_name, parameter_name, csv_file)

