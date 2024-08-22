"""
    Prediction of values of kidney parameters.
"""

# import libraries required
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


# create empty list of kidney param to store values

urea = []
creatinine = []
uric_acid = []
albumin = []
microalbumin_urine  = []

# create empty list to store datetime and future datetime for prediction
time_list = []
timestamp_list = []
time_list_future = []
timestamp_list_future = []


expected_crash = 0

MAX_CONSIDER = 1
MIN_CONSIDER = 0

# Help message display
def help_msg():
    print "python __prediction_kidney.py <user_id>"


# function to calculate risk value
def risk_value_for_prediction(min_val,max_val):
    """
        Function to calculate ideal risk value
    """
    delta = max_val - min_val
    chk  = delta/10
    risk_val = delta + chk*5
    return risk_val

# function to get maximum value from __config_kidney file
def get_max_value(param):
    with open('../experiment/__config_kidney_ref', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if (row['name'] == param):
                max_val = float(row['max'])
                return max_val
            else:
                continue
    return 0

# function to get minimum value from __config_cardiac file
def get_min_value(param):
    with open('../experiment/__config_kidney_ref', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if (row['name'] == param):
                min_val = float(row['min'])
                return min_val
            else:
                continue
    return 0

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


# function to calculate risk of kidney parameters
def calculate_risk_kidney_param (param,last_val,direction,predicted):
    """
        Calculates risk of kidney param
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
        linear regression (ols) to predict cardiac params
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

#Fetch user kidney data
def get_user_kidney_data(db,user_id):
    """
        Fetch kidney data from database
    """
    #create db cursor
    cursor = db.cursor()
    #exception handling  
    try:
        query = "SELECT UNIX_TIMESTAMP(report_date) as Date,urea,creatinine,uric_acid,albumin,microalbumin_urine FROM prediction_kidney_params WHERE user_id=%d ORDER BY Date ASC"%user_id
        cursor.execute(query)
        prediction_kidneyall = cursor.fetchall()
        idx = 0
        while (idx < len(prediction_kidneyall)):
            prediction_kidney = prediction_kidneyall[idx]
            idx += 1
            timestamp_list.append(float(prediction_kidney[0]))
            time_list.append(datetime.datetime.fromtimestamp(prediction_kidney[0]).strftime('%Y-%m-%d'))
            
            if prediction_kidney[1] is not None:
                urea.append(float(prediction_kidney[1]))
            else:
                urea.append(None)
            
            if prediction_kidney[2] is not None:
                creatinine.append(float(prediction_kidney[2]))
            else:
                creatinine.append(None)

            if prediction_kidney[3] is not None:
                uric_acid.append(float(prediction_kidney[3]))
            else:
                uric_acid.append(None)

            if prediction_kidney[4] is not None:
                albumin.append(float(prediction_kidney[4]))
            else:
                albumin.append(None)

            if prediction_kidney[5] is not None:
                microalbumin_urine.append(float(prediction_kidney[5]))
            else:
                microalbumin_urine.append(None)

    except Exception as err:
        print Exception, err
        print "Fatal: get_kidney_prediction_params"
        cursor.close()
        return -1
    cursor.close()
    return 0                


def validate_to_predict_kidney():
    """
        Function to validate kidney parameters and do the prediction and plot the predicted value.
    """
    file_name_urea = ""
    file_name_creatine = ""
    file_name_uric_acid = ""
    file_name_albumin = ""
    file_name_microalbumin = ""
    
    #check whether the length of list of kidney params is greater than or equal to 3.   
    
    if len(urea) >= 3:
        urea_predicted = get_linear_regression(timestamp_list,urea,timestamp_list_future)
        risk_urea = calculate_risk_kidney_param("UREA", urea[-1], MAX_CONSIDER,urea_predicted)
        if (risk_urea):
            file_name_urea = plot_save(time_list+timestamp_list_future,urea+urea_predicted,"UREA Values Prediction", "Urea", user_id,"UREA",MAX_CONSIDER)

    if len(creatinine) >= 3:
        creatinine_predicted = get_linear_regression(timestamp_list, creatinine,timestamp_list_future)
        risk_creatinine = calculate_risk_kidney_param("CREATININE",creatinine[-1],MAX_CONSIDER,creatinine_predicted)
        if (risk_creatinine):
            file_name_creatine = plot_save(time_list+time_list_future,creatinine+creatinine_predicted,"CREATININE Values prediction", "Creatinine",user_id,"CREATININE",MAX_CONSIDER)
   
    if len(uric_acid) >= 3:
        uric_acid_predicted = get_linear_regression(timestamp_list, uric_acid, timestamp_list_future)
        risk_uric_acid = calculate_risk_kidney_param("URIC ACID", uric_acid[-1],MAX_CONSIDER,uric_acid_predicted)
        if (risk_uric_acid):
            file_name_uric_acid = plot_save(time_list+time_list_future,uric_acid+uric_acid_predicted, "URIC ACID Values Prediction", "Uric Acid",user_id,"URIC ACID",MAX_CONSIDER)

    if len(albumin) >= 3:
        albumin_predicted = get_linear_regression(timestamp_list,albumin,timestamp_list_future)
        risk_albumin = calculate_risk_kidney_param("ALBUMIN", albumin[-1],MAX_CONSIDER,albumin_predicted)
        if (risk_albumin):
            file_name_albumin = plot_save(time_list+time_list_future,albumin+albumin_predicted,"ALBUMIN Values Prediction", "Albumin",user_id,"ALBUMIN",MAX_CONSIDER)

    if len(microalbumin_urine) >= 3:
        microalbumin_urine_predicted = get_linear_regression(timestamp_list,microalbumin_urine,timestamp_list_future)
        risk_microalbumin_urine = calculate_risk_kidney_param("MICROALBUMIN URINE", microalbumin_urine[-1],MAX_CONSIDER,microalbumin_urine_predicted)
        if (risk_microalbumin_urine):
            file_name_microalbumin = plot_save(time_list+time_list_future,microalbumin_urine+microalbumin_urine_predicted,"MICROALBUMIN Values Prediction","Microalbumin",user_id,"MICROALBUMIN URINE",MAX_CONSIDER)

    # check whether the length of list of kidney params is less than 3.
    # check whether risk_diabetes is high or moderate
    # compare the last value of kidney param with ideal risk value and then do the predicton

    if len(urea) < 3:
        if risk_kidney == "High" or risk_kidney == "Moderate":
            if urea[-1] >= risk_value_for_prediction(min_urea,max_urea):
                urea_predicted = get_linear_regression(timestamp_list,urea,timestamp_list_future)
                risk_urea = calculate_risk_kidney_param("UREA", urea[-1],MAX_CONSIDER,urea_predicted)
                if (risk_urea):
                    file_name_urea = plot_save(time_list+timestamp_list_future,urea+urea_predicted,"UREA Values Prediction", "Urea", user_id,"UREA",MAX_CONSIDER)

    if len(creatinine) < 3:
        if risk_kidney == "High" or risk_kidney == "Moderate":
            if creatinine[-1] >= risk_value_for_prediction(min_creatinine,max_creatinine):
                creatinine_predicted = get_linear_regression(timestamp_list, creatinine,timestamp_list_future)
                risk_creatinine = calculate_risk_kidney_param("CREATININE",creatinine[-1],MAX_CONSIDER,creatinine_predicted)
                if (risk_creatinine):
                    file_name_creatine = plot_save(time_list+time_list_future,creatinine+creatinine_predicted,"CREATININE Values prediction", "Creatinine",user_id,"CREATININE",MAX_CONSIDER)
    
    if len(uric_acid) < 3:
         if risk_kidney == "High" or risk_kidney == "Moderate":
             if uric_acid[-1] >= risk_value_for_prediction(min_uric_acid,max_uric_acid):
                uric_acid_predicted = get_linear_regression(timestamp_list, uric_acid, timestamp_list_future)
                risk_uric_acid = calculate_risk_kidney_param("URIC ACID", uric_acid[-1],MAX_CONSIDER,uric_acid_predicted)
                if (risk_uric_acid):
                    file_name_uric_acid = plot_save(time_list+time_list_future,uric_acid+uric_acid_predicted, "URIC ACID Values Prediction", "Uric Acid",user_id,"URIC ACID",MAX_CONSIDER)

    if len(albumin) < 3:
        if risk_kidney == "High" or risk_kidney == "Moderate":
            if albumin[-1] >= risk_value_for_prediction(min_albumin,max_albumin):
                albumin_predicted = get_linear_regression(timestamp_list,albumin,timestamp_list_future)
                risk_albumin = calculate_risk_kidney_param("ALBUMIN", albumin[-1],MAX_CONSIDER,albumin_predicted)
                if (risk_albumin):
                    file_name_albumin = plot_save(time_list+time_list_future,albumin+albumin_predicted,"ALBUMIN Values Prediction", "Albumin",user_id,"ALBUMIN",MAX_CONSIDER)
    
    if len(microalbumin_urine) < 3:
        if risk_kidney == "High" or risk_kidney == "Moderate":
            if microalbumin_urine[-1] >= risk_value_for_prediction(min_microalbumin,max_microalbumin):
                microalbumin_urine_predicted = get_linear_regression(timestamp_list,microalbumin_urine,timestamp_list_future)
                risk_microalbumin_urine = calculate_risk_kidney_param("MICROALBUMIN URINE", microalbumin_urine[-1],MAX_CONSIDER,microalbumin_urine_predicted)
                if (risk_microalbumin_urine):
                    file_name_microalbumin = plot_save(time_list+time_list_future,microalbumin_urine+microalbumin_urine_predicted,"MICROALBUMIN Values Prediction","Microalbumin",user_id,"MICROALBUMIN URINE",MAX_CONSIDER)
                            
    # handle exceptions
    try:
        # add result to json
        json_data = {}
        kidn_predict = {}
        kidn_predict_urea = {}
        kidn_predict_creat = {}
        kidn_predict_uric = {}
        kidn_predict_microalb = {}
        kidn_predict_alb = {}
        
        # add urea data
        kidn_predict_urea['NAME'] = 'Urea'
        kidn_predict_urea['RISK'] = risk_urea
        kidn_predict_urea['PLOT'] = file_name_urea

        # add creatinine data
        kidn_predict_creat['NAME'] = 'Creatinine'
        kidn_predict_creat['RISK'] = risk_creatinine
        kidn_predict_creat['PLOT'] = file_name_creatine

        # add uric acid data
        kidn_predict_uric['NAME'] = "Uric Acid"
        kidn_predict_uric['RISK'] = risk_uric_acid
        kidn_predict_uric['PLOT'] = file_name_uric_acid

        # add microalbunim data
        kidn_predict_microalb['NAME'] = "Microalbumin Urine"
        kidn_predict_microalb['RISK'] = risk_microalbumin_urine
        kidn_predict_microalb['PLOT'] = file_name_microalbumin

        # add albunim data
        kidn_predict_alb['NAME'] = "ALBUMIN"
        kidn_predict_alb['RISK'] = risk_albumin
        kidn_predict_alb['PLOT'] = file_name_albumin
    
        # add kidney data to kidn_predict
        kidn_predict['UREA'] = kidn_predict_urea
        kidn_predict['CREATININE'] = kidn_predict_creat
        kidn_predict['URIC ACID'] = kidn_predict_uric
        kidn_predict['MICROALBUMIN'] = kidn_predict_microalb
        kidn_predict['ALBUMIN'] = kidn_predict_alb
        kidn_predict['RISK'] = (risk_urea or risk_creatinine or risk_uric_acid or risk_microalbumin_urine or risk_albumin)
        result_time_list = time_list + time_list_future 
        kidn_predict['Expected Crash'] = result_time_list[expected_crash]
        # add kidn_predict to json_data
        json_data['Diabetes Prediction'] = dia_predict
        print json.dumps(json_data)
        return 0

    except Exception as err:
        json_data["RISK"] = risk_kidney
        print json.dumps(json_data)
        return 0
 
if __name__ == "__main__":
 
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

    #call user risk kidney
    risk_kidney = get_user_risk_data_kidney(user_id,db)

    #get user  params
    get_user_kidney_data(db,user_id)

    #get min and max values for kidney params
    min_urea = get_min_value("UREA")
    max_urea = get_max_value("UREA")
    min_creatinine = get_min_value("CREATININE")
    max_creatinine = get_max_value("CREATININE")
    min_uric_acid = get_min_value("URIC ACID")
    max_uric_acid = get_max_value("URIC ACID")
    min_microalbumin = get_min_value("MICROALBUMIN URINE")
    max_microalbumin = get_max_value("MICROALBUMIN URINE")
    min_albumin = get_min_value("ALBUMIN")
    max_albumin = get_max_value("ALBUMIN")
    
    #prepare list of dates to predict
    prepare_next_set_time()

    #call the prediction function
    validate_to_predict_kidney()
    #close db
    close_db()
    exit(0)
