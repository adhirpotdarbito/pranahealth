"""
    Prediction of values of liver
"""

# import required libraries
import sys
import json
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

# create empty list of liver params to store values
ast_sgot = []
aly_sgpt = []
alp = []
Bilirubin_total = []
Bilirubin_direct = []
Bilirubin_indirect = []
ag_ratio = []

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
    print "python __prediction_liver.py <user_id>"

# function to calculate risk value
def risk_value_for_prediction(min_val,max_val):
    """
        Function to calculate ideal risk value
    """
    delta = max_val - min_val
    chk  = delta/10
    risk_val = delta + chk*5
    return risk_val

# function to get maximum value from __config_liver file
def get_max_value(param):
    with open('../experiment/__config_liver_ref', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if (row['name'] == param):
                max_val = float(row['max'])
                return max_val
            else:
                continue
    return 0

# function to get minimum value from __config_liver file
def get_min_value(param):
    with open('../experiment/__config_liver_ref', mode='r') as csv_file:
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

# function to calculate risk of cardiac parameters
def calculate_risk_liver_param (param,last_val,direction,predicted):
    """
        Calculates risk of liver param
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
        linear regression (ols) to predict liver params
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

def get_user_cardiac_data(db,user_id):
    """
        Fetch liver data from database
    """
    # create db cursor
    cursor = db.cursor()
    # exception handling
    try:
        query = "SELECT UNIX_TIMESTAMP(report_date) as date,ast_sgot,aly_sgpt,alp,bilirubin_total,bilirubin_direct, bilirubin_indirect,ag_ratio FROM prediction_liver_param WHERE user_id=%d ORDER BY Date ASC"%user_id
        cursor.execute(query)
        prediction_liverall = cursor.fetchall()
        idx = 0
        while (idx < len(prediction_liverall)):
            prediction_liver = prediction_liverall[idx]
            idx = idx + 1
            timestamp_list.append(float(prediction_liver[0]))
            time_list.append(datetime.datetime.fromtimestamp(prediction_liver[0])).strptime('%Y-%m-%d')
            # check whether value is not None and typecast to float
            # append in the list for all the liver parameter
            if prediction_liver[1] is not None:
                ast_sgot.append(float(prediction_liver[1]))
            else:
                ast_sgot.append(None)
            
            if prediction_liver[2] is not None:
                aly_sgpt.append(float(prediction_liver[2]))
            else:
                aly_sgpt.append(None)
                
            if prediction_liver[3] is not None:
                alp.append(float(prediction_liver[3]))
            else:
                alp.append(None)

            if prediction_liver[4] is not None:
                bilirubin_total.append(float(prediction_liver[4]))
            else:
                bilirubin_total.append(None)

            if prediction_liver[5] is not None:
                bilirubin_direct.append(float(prediction_liver[5]))
            else:
                bilirubin_direct.append(None)

            if prediction_liver[6] is not None:
                bilirubin_direct.append(float(prediction_liver[6]))
            else:
                bilirubin_direct.append(None)

            if prediction_liver[7] is not None:
                ag_ratio.append(float(prediction_liver[7]))
            else:
                ag_ratio.append(None)
   
   except Exception as err:
        print Exception, err
        print ("Fatal: get_user_liver-data")
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


# function to check whether prediction is required
def validate_to_predict_liver():
    """
        Function to validate liver parameters and do the prediction and plot the predicted value.
    """
    file_name_ast = ""
    file_name_aly = ""
    file_name_alp = ""
    file_name_bilrbn_tot = ""
    file_name_bilrbn_dir = ""
    file_name_bilrbn_indir = ""
    file_name_ag = ""

    # check whether the length of list of the liver params is greater than or equal to 3 and do the prediction
    if len(ast_sgot) >= 3:
        ast_sgot_predicted = get_linear_regression(timestamp_list,ast_sgot,timestamp_list_future)
        risk_ast_sgot = calculate_risk_liver_param("AST SGOT",ast_sgot[-1],MAX_CONSIDER,ast_sgot_predicted)
        if (risk_ast_sgot):
            file_name_ast = plot_save(time_list+time_list_future,ast_sgot+ast_sgot_predicted,"AST SGOT Values Prediction","AST_SGOT",user_id,"AST SGOT",MAX_CONSIDER)

    if len(aly_sgpt) >= 3:
        aly_sgpt_predicted = get_linear_regression(timestamp_list,aly_sgpt,timestamp_list_future)
        risk_aly_sgpt = calculate_risk_liver_param("ALY SGPT",aly_sgpt[-1],MAX_CONSIDER,aly_sgpt_predicted)
        if (risk_aly_sgpt):
            file_name_aly = plot_save(time_list+time_list_future, aly_sgpt+aly_sgpt_predicted,"ALY SGPT Values Prediction", "ALY SGPT",user_id,"ALY SGPT",MAX_CONSIDER)

    if len(alp) >= 3:
        alp_predicted = get_linear_regression(timestamp_list,alp,timestamp_list_future)
        risk_alp = calculate_risk_liver_param("ALP",alp[-1],MAX_CONSIDER,alp_predicted)
        if (risk_alp):
            file_name_alp = plot_save(time_list+time_list_future, alp+alp_predicted,"ALP Values Prediction","Alp",user_id,"ALP",MAX_CONSIDER)

    if len(bilirubin_total) >= 3:
        bilirubin_total_predicted = get_linear_regression(timestamp_list,bilirubin_total,timestamp_list_future)
        risk_bilrbn_tot = calculate_risk_liver_param("BILIRUBIN TOTAL",bilirubin_total[-1],MAX_CONSIDER,bilirubin_total_predicted)
        if (risk_bilrbn_tot):
            file_name_bilrbn_tot = plot_save(time_list+time_list_future,bilirubin_total+bilirubin_total_predicted,"BILIRUBIN TOTAL Values Prediction","Bilirubin_total",user_id,"BILIRUBIN TOTAL",MAX_CONSIDER)

    if len(bilirubin_direct) >= 3:
        bilirubin_direct_predicted = get_linear_regression(timestamp_list,bilirubin_direct,timestamp_list_future)
        risk_bilrbn_dir = calculate_risk_liver_param("BILIRUBIN DIRECT",bilirubin_direct[-1],MAX_CONSIDER,bilirubin_direct_predicted)
        if (risk_bilrbn_dir):
            file_name_bilrbn_dir = plot_save(time_list+time_list_future,bilirubin_direct+bilirubin_direct_predicted,"BILIRUBIN DIRECT Values Prediction","Bilirubin_direct",user_id,"BILIRUBIN DIRECT",MAX_CONSIDER)

    if len(bilirubin_indirect) >= 3:
        bilirubin_indirect_predicted = get_linear_regression(timestamp_list,bilirubin_indirect,timestamp_list_future)
        risk_bilrbn_indir = calculate_risk_liver_param("BILIRUBIN INDIRECT", bilirubin_indirect[-1],MAX_CONSIDER,bilirubin_indirect_predicted)
        if (risk_bilrbn_indir):
            file_name_bilrbn_indir = plot_save(time_list+timestamp_list_future, bilirubin_indirect+bilirubin_indirect_predicted,"BILIRUBIN INDIRECT VAlues Prediction","Bilirubin_indirect",user_id,"BILIRUBIN INDIRECT",MAX_CONSIDER)

    if len(ag_ratio) >= 3:
        ag_ratio_predicted = get_linear_regression(timestamp_list,ag_ratio,timestamp_list_future)
        risk_ag_ratio = calculate_risk_liver_param("AG RATIO",ag_ratio[-1],MAX_CONSIDER,ag_ratio_predicted)
        if (risk_ag_ratio):
            file_name_ag = plot_save(time_list+time_list_future,ag_ratio+ag_ratio_predicted,"AG RATIO Values Prediction","Ag_Ratio", user_id,"AG RATIO",MAX_CONSIDER)

    # check whether the length of list of liver params is less then 3
    # check whether risk_liver is high or moderate
    # compare the last value of liver param with ideal risk value and then do the predicton





if __name__ === "__main__":
    
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

    min_ast_sgot = get_min_value("AST SGOT")
    max_ast_sgot = get_max_value("AST SGOT")
    min_aly_sgpt = get_min_value("ALP")
    max_aly_sgpt = get_max_value("ALP")
    min_bilrbn_tot = get_min_value("BILIRUBIN TOTAL")
    max_bilrbn_tot = get_max_value("BILIRUBIN TOTAL")
    min_bilrbn_dir = get_min_value("BILIRUBIN DIRECT")
    max_bilrbn_dir = get_max_value("BILIRUBIN INDIRECT")
    min_bilrbn_indir = get_min_value("BILIRUBIN INDIRECT")
    max_bilrbn_indir = get_max_value("BILIRUBIN INDIRECT")
    min_ag_ratio = get_min_value("AG RATIO")
    max_ag_ratio = get_max_value("AG RATIO")

    #get user liver params
    get_user_liver_data(db,user_id)

    #prepare list of dates to predict
    prepare_next_set_time()

    #call the prediction function
    validate_to_predict_cardiac()
    #close db
    close_db()
    exit(0)

