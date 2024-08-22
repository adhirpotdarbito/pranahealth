'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

# import all the libraries required
import sys
import json
import csv
import os
from __users import *
from __choose_health_insurance import *
from __db_config import *
import statistics
import statsmodels.api as sm
import matplotlib.pyplot as plt
import time
import datetime
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import math


# empty lists for adding diabetes params and date
glucose_fasting = []
glucose_pp = []
HbA1C = []
time_list = []
timestamp_list = []
time_list_future = []
timestamp_list_future = []


expected_crash = 0

MAX_CONSIDER = 1
MIN_CONSIDER = 0

def help_msg():
    print "python __prediction_diabetes.py <user_id>"

# function to plot predicted value
def plot_save(x,y,title,lbl,user_id,param,direction):
    """
        plots the prediction of diabetes params
    """
    global expected_crash
    if (direction == MAX_CONSIDER):
        max_val = get_max_value(param)
    else:
        min_val = get_min_value(param)

    fig = plt.figure()
    ax = plt.subplot(111)
    idx = 0
    label_normal = 0
    label_abnormal = 0
    while (idx < len(y)):
        if (direction == MAX_CONSIDER):
            if y[idx] != None:
                if(float(y[idx]) < float(max_val-0.001)):
                    if (label_normal == 0):
                        ax.plot(datetime.datetime.strptime(x[idx], '%Y-%m-%d'),y[idx],'bo',label="Normal Values")
                    else:
                        ax.plot(datetime.datetime.strptime(x[idx], '%Y-%m-%d'),y[idx],'bo')
                    label_normal = label_normal + 1
                else:
                    if (label_abnormal == 0):
                        expected_crash = idx
                        ax.plot(datetime.datetime.strptime(x[idx], '%Y-%m-%d'),y[idx],'ro',label="Out of Range Values")
                    else:
                        ax.plot(datetime.datetime.strptime(x[idx], '%Y-%m-%d'),y[idx],'ro')
                    label_abnormal = label_abnormal + 1
        else:
            if y[idx] != None:
                if(float(y[idx]) > float(min_val)):
                    ax.plot(datetime.datetime.strptime(x[idx], '%Y-%m-%d'),y[idx],'bo')
                else:
                    ax.plot(datetime.datetime.strptime(x[idx], '%Y-%m-%d'),y[idx],'ro')

        idx = idx + 1

    plt.title(title)
    plt.grid(True)
    ax.legend()
    file_name = lbl + "_%d" %user_id
    fig.savefig(file_name)
    
    return file_name


# function for getting ols coefficient
def get_ols_coefficient(y):
    x = []
    x.append(range(len(y)))
    x.append([1 for ele in xrange(len(y))])
    y = np.matrix(y).T
    x = np.matrix(x).T
    betas = ((x.T*x).I*x.T*y)
    return betas

# function to get maximum value from __config_diabetes file
def get_max_value(param):
    with open('../experiment/__config_diabetes_ref', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if (row['name'] == param):
                max_val = float(row['max'])
                return max_val
            else:
                continue
    return 0

# function to get minimum value from __config_diabetes file
def get_min_value(param):
    with open('../experiment/__config_diabetes_ref', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if (row['name'] == param):
                min_val = float(row['min'])
                return min_val
            else:
                continue
    return 0

# function to calculate risk of diabetes parameters
def calculate_risk_dia_param (param,last_val,direction,predicted):
    """
        Calculates risk of diabetes
    """
    if (direction == MAX_CONSIDER):
        max_val = get_max_value(param)

        if (last_val >= max_val):
            # user already reached max value
            return 3
        # go over the predicted value in coming days
        idx = 0
        while (idx < len(predicted)):
            if (float(predicted[idx]) >= max_val):
                # if the prediction is within 5 yrs
                if (idx < 60):
                    return 2
                else:
                    return 1
            # increment idx
            idx = idx + 1

        return 0
    else:
        min_val = get_min_value(param)
        if (last_val < min_val):
            # user is already reached min value
            return 3
        idx= 0
        while (idx < len(predicted)):
            if (float(predicted[idx]) <= min_val):
                # if the prediction is within 5 yrs
                if (idx < 5):
                    return 2
                else:
                    return 1
            # increment the idx
            idx = idx + 1

        return 0

# linear regression function 
def get_linear_regression(X,Y,X1):
    """
        linear regression (ols) to predict diabetes values
    """
    
    # create a dataframe using pandas for some preprocessing of data
    df = pd.DataFrame()
    # add values to dataframe
    df["date"] = X
    df["value"] = Y
    # drop the row if null value 
    df_new = df.dropna()
    # create ols model and pass the dataframe
    X_1=sm.add_constant(df_new["date"])
    model = sm.OLS(df_new["value"],X_1)
    results = model.fit()
    Y_predicted=results.predict(X_1)
    # add more values to predict
    X1_1 = sm.add_constant(X1)
    Y1_predicted = results.predict(X1_1)
    return Y1_predicted.tolist()
    

# function to fetch users diabetes data and date
def get_user_diabetes_data(db,user_id):
    """
        Fetch diabetes data and date from database
    """
    cursor = db.cursor()
    # exception handling
    try:
        query_str = "select UNIX_TIMESTAMP(report_date) as DATE, glucose_fasting,glucose_pp,HbA1C from prediction_diabetes_params where user_id=%d order by DATE ASC" %user_id
        cursor.execute(query_str)
        prediction_diaall = cursor.fetchall()
        idx = 0
        while (idx < len(prediction_diaall)):
            prediction_dia = prediction_diaall[idx]
            idx = idx + 1
            timestamp_list.append(float(prediction_dia[0]))
            # append date to time list
            time_list.append(datetime.datetime.fromtimestamp(prediction_dia[0]).strftime('%Y-%m-%d'))
            
            # check if diabetes data is not NULL
            if prediction_dia[1] is not None:
                glucose_fasting.append(float(prediction_dia[1]))
            else:
                glucose_fasting.append(None)

            if prediction_dia[2] is not None:
                glucose_pp.append(float(prediction_dia[2]))
            else:
                glucose_pp.append(None)

            if prediction_dia[3] is not None:
                HbA1C.append(float(prediction_dia[3]))
            else:
                HbA1C.append(None)
    except Exception as err:
        print Exception,err
        print "Fatal: get_diabetes_prediction_params"
        cursor.close()
        return -1
    cursor.close()
    return 0

# preparing timeset for prediction

def prepare_next_set_time():
    # sanity check to make sure we have values to predict
    if (len(time_list) == 0):
        return 
    last_report_date = time_list[len(time_list) -1]
    current_date = datetime.datetime.today().strftime('%Y-%m-%d')
    a_date = datetime.datetime.strptime(last_report_date, '%Y-%m-%d')
    b_date = datetime.datetime.strptime(current_date, '%Y-%m-%d')
    time_diff = b_date - a_date
    # total days from last report to next 5 yrs
    total_days = time_diff.days + 1825
    total_months = total_days/30

    # we will be plotting y for every month till next 5 yrs
    idx = 0
    global time_list_future
    global timestamp_list_future

    while idx <= total_months:
        tmp = (a_date+(datetime.timedelta(idx*30))).strftime('%Y-%m-%d')
        time_list_future.append(tmp)
        timestamp_list_future.append(time.mktime(datetime.datetime.strptime(tmp, "%Y-%m-%d").timetuple()))
        idx = idx + 1
    return timestamp_list_future

"""
# function for calculating diabetes prediction
def calculate_dia_prediction():

    global time_list_future
    global time_list

    # sanity check to make sure we have values to predict
    if (len(time_list) == 0):
        return

    # atleast we need 2 or more records to proceed
    # call our OLS model for prediction

    if (len(HbA1C) > 1):
        hba1c_predicted = get_linear_regression(timestamp_list,HbA1C,timestamp_list_future)
    if (len(glucose_fasting) > 1):
        glucose_fasting_predicted = get_linear_regression(timestamp_list,glucose_fasting,timestamp_list_future)
    if (len(glucose_pp) > 1):
        glucose_pp_predicted = get_linear_regression(timestamp_list,glucose_pp,timestamp_list_future)
        
    # try to see if risk involved over time
    risk_glucose_fasting = calculate_risk_dia_param('GLUCOSE FASTING',glucose_fasting[len(glucose_fasting)-1],MAX_CONSIDER,glucose_fasting_predicted)
    risk_glucose_pp = calculate_risk_dia_param('GLUCOSE POST PRANDIAL',glucose_pp[len(glucose_pp)-1],MAX_CONSIDER,glucose_pp_predicted)
    risk_HbA1C = calculate_risk_dia_param('HbA1c',HbA1C[len(HbA1C)-1],MAX_CONSIDER,hba1c_predicted)
    
    # create file name
    file_name_gf = ""
    file_name_gp = ""
    file_name_hba1c = ""
    
    # check for risk HbA1C and  plot prediction graph
    if (risk_HbA1C):
       file_name_hba1c = plot_save (time_list+time_list_future,HbA1C+hba1c_predicted,"HbA1c Values Prediction","HbA1c",user_id,'HbA1c',MAX_CONSIDER)
    
    # check for risk glucose fasting and plot prediction graph
    if (risk_glucose_fasting):
        file_name_gf = plot_save (time_list+time_list_future,glucose_fasting+glucose_fasting_predicted,"Glucose Fasting Values Prediction","Glucose_Fasting",user_id,'GLUCOSE FASTING',MAX_CONSIDER)
   
    # check for risk glucose pp and plot prediction graph
    if (risk_glucose_pp):
        file_name_gp = plot_save (time_list+time_list_future,glucose_pp+glucose_pp_predicted,"Glucose PP Values Prediction","Glucose_PP",user_id,'GLUCOSE POST PRANDIAL',MAX_CONSIDER)

    # create empty dictionaries to add data to json
    json_data = {}
    dia_predict = {}
    dia_predict_gf = {}
    dia_predict_gp = {}
    dia_predict_hba1c = {}
                                                                      
    # add glucose fasting data
    dia_predict_gf['NAME'] = 'Glucose Fasting'
    dia_predict_gf['RISK'] = risk_glucose_fasting
    dia_predict_gf['PLOT'] = file_name_gf
    
    # add glucose pp data
    dia_predict_gp['NAME'] = 'Glucose PP'
    dia_predict_gp['RISK'] = risk_glucose_pp
    dia_predict_gp['PLOT'] = file_name_gp
                                               
    # add hba1c data
    dia_predict_hba1c['NAME'] = 'HbA1c'
    dia_predict_hba1c['RISK'] = risk_HbA1C
    dia_predict_hba1c['PLOT'] = file_name_hba1c
    
    # add diabetes data to dia_predict
    dia_predict['Glucose Fasting'] = dia_predict_gf
    dia_predict['Glucose PP'] = dia_predict_gp
    dia_predict['HbA1c'] = dia_predict_hba1c
    dia_predict['Risk'] = (risk_HbA1C or risk_glucose_pp or risk_glucose_fasting)
    result_time_list = time_list + time_list_future
    dia_predict["Expected Crash"] = result_time_list[expected_crash]
    
    # add dia_predict to json_data
    json_data['Diabetes Prediction'] = dia_predict
    print json.dumps(json_data)
    return 0


if __name__ == '__main__':
    
    argc = len(sys.argv) -1
    # check for arguments
    if (argc < 1):
        help_msg()
        exit(0)
    try:
        user_id = int (sys.argv[1])
    except Exception as err:
        print Exception, err
        help_msg()
        exit(0)
    
    # open database pranacare
    init_db()
    db = get_db()
    
    #get user info
    user_info = init_user_info(int(user_id))

    #prepare user body parameters
    prepare_user_body_params(db, user_info)

    #get user age
    age = get_user_age()

    #prepare user lifestyle habit
    prepare_user_lifestyle_habit(db,user_info)

    #check if user is smoker
    smoker = is_user_smoker()

    #check if user is alcoholic
    alcoholic = is_user_alcoholic()

    #call user risk data
    get_user_risk_data_diabetic(user_id,db)
    
    # get user diabetes data
    ret = get_user_diabetes_data(db,user_id)
    if (ret):
        close_db()
        exit(-1)
        
    # call functions
    prepare_next_set_time()
    calculate_dia_prediction()
    # close db 
    close_db()
    exit(0)
"""
