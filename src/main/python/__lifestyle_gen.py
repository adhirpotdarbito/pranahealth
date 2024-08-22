'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

import os
import json
import datetime
#import pynotify
import sys

week_day = ['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday','Sunday']

session = {'EM': '7:00AM', 'TT': '7:15AM', 'BF': '8:00AM', 'MM': '11:00AM', 'LT': '12:30PM', 'ES': '5:30PM', 'DT': '9:30PM'}

food = []
amount = []
exercise = []
exer_time = []
kcal_in = []
gms_in = []

def get_week_day_idx():
    day = datetime.datetime.today().weekday()
    return day

def get_activity_periodically(filename,period):
    json_data_food = {}
    json_data_exercise = {}
    result_json = {}
    idx = get_week_day_idx()
    day = week_day[idx]
    slot = session[period]
    with open(filename) as json_file:
        data = json.load(json_file)
        lenght = len(data[day][slot]['food'])
        pos = 0
        while (pos < lenght):
            food.append(data[day][slot]['food'][pos]['MENU'])
            amount.append(data[day][slot]['food'][pos]['AMOUNT'])
            kcal_in.append(data[day][slot]['food'][pos]['KCAL'])
            gms_in.append(data[day][slot]['food'][pos]['GMS'])

            # add to out json
            jdata = {}
            jdata['MENU'] = data[day][slot]['food'][pos]['MENU']
            jdata['AMOUNT'] = data[day][slot]['food'][pos]['AMOUNT']
            jdata['KCAL'] = data[day][slot]['food'][pos]['KCAL']
            jdata['PROTIEN'] = data[day][slot]['food'][pos]['GMS']

            json_data_food[pos] = jdata

            pos = pos + 1

        pos = 0
        length = len(data[day][slot]['exercise'])
        while (pos < length):
            exercise.append(data[day][slot]['exercise'][pos]['EXERCISE'])
            exer_time.append(data[day][slot]['exercise'][pos]['TIME'])
            jdata = {}
            jdata['EXERCISE'] = data[day][slot]['exercise'][pos]['EXERCISE']
            jdata['TIME'] = data[day][slot]['exercise'][pos]['TIME']
            json_data_exercise[pos] = jdata
            pos = pos + 1
        
        result_json['food'] = json_data_food
        result_json['exercise'] = json_data_exercise
    
    json_obj = json.dumps(result_json)
    return json_obj

def get_full_activity(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

