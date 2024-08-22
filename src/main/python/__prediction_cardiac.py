"""
    Prediction of values of cardiac parameters.
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


# create empty list of cardiac params to store values
cholestrol_total = []
triglycerides = []
hdl_cholestrol = []
ldl_cholestrol = []
apolipoprotein_a1 = []
apolipoprotein = []
apolipoprotein_b = []
lipoprotein_a = []
s_homocysteine = []
s_fibrinogen =[]

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
    print "python __prediction_cardiac.py <user_id>"


# function to calculate risk value
def risk_value_for_prediction(min_val,max_val):
    """
        Function to calculate ideal risk value
    """
    delta = max_val - min_val
    chk  = delta/10
    risk_val = delta + chk*5
    return risk_val

# function to get maximum value from __config_cardiac file
def get_max_value(param):
    with open('../experiment/__config_cardiac_ref', mode='r') as csv_file:
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
    with open('../experiment/__config_cardiac_ref', mode='r') as csv_file:
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
def calculate_risk_cardiac_param (param,last_val,direction,predicted):
    """
        Calculates risk of cardiac param
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


def get_user_cardiac_data(db,user_id):
    """"
        Fetch cardiac data from database
    """
    # create db cursor
    cursor = db.cursor()
    #exception handling
    try:
        query = "SELECT UNIX_TIMESTAMP(report_date) as Date, cholestrol_total, triglycerides, hdl_cholestrol, ldl_cholestrol, apolipoprotein_A1,apolipoprotein_b, lipoprotein_a, s_homocysteine, s_fibrinogen FROM prediction_cardiac_param WHERE user_id=%d ORDER BY Date ASC"%user_id
        cursor.execute(query)
        prediction_cardiacall = cursor.fetchall()
        idx = 0
        while (idx < len(prediction_cardiacall)):
            prediction_cardiac = prediction_cardiacall[idx]
            idx = idx + 1
            timestamp_list.append(float(prediction_cardiac[0]))
            time_list.append(datetime.datetime.fromtimestamp(prediction_cardiac[0]).strftime('%Y-%m-%d'))
            # check whether value is not None and typecast to float  
            # append in the list for all the cardiac parameter
            if prediction_cardiac[1] is not None:
                cholestrol_total.append(float(prediction_cardiac[1]))
            else:
                cholestrol_total.append(None)

            if prediction_cardiac[2] is not None:
                triglycerides.append(float(prediction_cardiac[2]))
            else:
                triglycerides.append(None)

            if prediction_cardiac[3] is not None:
                hdl_cholestrol.append(float(prediction_cardiac[3]))
            else:
                hdl_cholestrol.append(None)

            if prediction_cardiac[4] is not None:
                ldl_cholestrol.append(float(prediction_cardiac[4]))
            else:
                ldl_cholestrol.append(None)

            if prediction_cardiac[5] is not None:
                apolipoprotein_a1.append(float(prediction_cardiac[5]))
            else:
                apolipoprotein_a1.append(None)

            if prediction_cardiac[6] is not None:
                apolipoprotein_b.append(float(prediction_cardiac[6]))
            else:
                apolipoprotein_b.append(None)

            if prediction_cardiac[7] is not None:
                lipoprotein_a.append(float(prediction_cardiac[7]))
            else:
                lipoprotein_a.append(None)

            if prediction_cardiac[8] is not None:
                s_homocysteine.append(float(prediction_cardiac[8]))
            else:
                s_homocysteine.append(None)

            if prediction_cardiac[9] is not None:
                s_fibrinogen.append(float(prediction_cardiac[9]))
            else:
                s_fibrinogen.append(None)
        
    except Exception as err:
        print Exception, err
        print "Fatal: get_cardiac_prediction_params"
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
def validate_to_predict_cardiac():
    """
        Function to validate cardiac parameters and do the prediction and plot the predicted value.
    """
    file_name_chl = ""
    file_name_trgs = ""
    file_name_hdl_chl = ""
    file_name_ldl_chl = ""
    file_name_ap_pr_a1 = ""
    file_name_ap_pr_b = ""
    file_name_lipr_a = ""
    file_name_hmcst = ""
    file_name_fbrgn = ""

    # check whether the length of list of cardiac params is greater than or equal to 3 and do the prediction
    if len(cholestrol_total) >= 3:
        cholestrol_total_predicted = get_linear_regression(timestamp_list,cholestrol_total, timestamp_list_future)
        risk_cholestrol_total = calculate_risk_cardiac_param("CHOLESTROL TOTAL",cholestrol_total[-1], MAX_CONSIDER, cholestrol_total_predicted)
        if (risk_cholestrol_total):
            file_name_chl = plot_save(time_list+time_list_future, cholestrol_total+cholestrol_total_predicted, "Cholestrol Total Values Prediction", "Cholestrol_Total", user_id, "CHOLESTROL TOTAL",MAX_CONSIDER)
    
    if len(triglycerides) >= 3:
        triglycerides_predicted = get_linear_regression(timestamp_list, triglycerides, timestamp_list_future)
        risk_triglycerides = calculate_risk_cardiac_param("TRIGLYCERIDES", triglycerides[-1],MAX_CONSIDER, triglycerides_predicted)

        if (risk_triglycerides):
            file_name_trgs = plot_save(time_list+time_list_future, triglycerides+triglycerides_predicted,"Triglycerides Values Prediction","Triglycerides", user_id, "TRIGLYCERIDES", MAX_CONSIDER)

    if len(hdl_cholestrol) >= 3:
        hdl_cholestrol_predicted = get_linear_regression(timestamp_list, hdl_cholestrol,timestamp_list_future)
        risk_hdl_cholestrol = calculate_risk_cardiac_param("HDL CHOLESTROL", hdl_cholestrol[-1], MAX_CONSIDER, hdl_cholestrol_predicted)

        if (risk_hdl_cholestrol):
            file_name_hdl_chl = plot_save(time_list+time_list_future, hdl_cholestrol+hdl_cholestrol_predicted,"HDL Cholestrol Values Prediction", "HDL_Cholestrol", user_id, "HDL CHOLESTROL",MAX_CONSIDER)


    if len(ldl_cholestrol) >= 3:
        ldl_cholestrol_predicted = get_linear_regression(timestamp_list, ldl_cholestrol, timestamp_list_future)
        risk_ldl_cholestrol = calculate_risk_cardiac_param("LDL CHOLESTROL", ldl_cholestrol[-1], MAX_CONSIDER, ldl_cholestrol_predicted)

        if (risk_ldl_cholestrol):
            file_name_ldl_chl = plot_save(time_list+time_list_future,ldl_cholestrol+ldl_cholestrol_predicted,"LDL CHOLESTROL Values Prediction","LDL_Cholestrol",user_id, "HDL CHOLESTROL", MAX_CONSIDER)

    if len(apolipoprotein_a1) >= 3:
        apolipoprotein_a1_predicted = get_linear_regression(timestamp_list, apolipoprotein_a1,timestamp_list_future)
        risk_apolipoprotein_a1 = calculate_risk_cardiac_param("APOLIPOPROTEIN A1", apolipoprotein_a1[-1],MAX_CONSIDER,apolipoprotein_a1_predicted)

        if (risk_apolipoprotein_a1):
            file_name_ap_pr_a1 = plot_save(time_list+time_list_future, apolipoprotein_a1_predicted,"APOLIPOPROTEIN A1 Values Prediction", "Apolipoprotein_A1", user_id, "APOLIPOPROTEIN A1", MAX_CONSIDER)

    if len(apolipoprotein_b) >= 3:
        apolipoprotein_b_predicted = get_linear_regression(timestamp_list,apolipoprotein_b,timestamp_list_future)
        risk_apolipoprotein_b = calculate_risk_cardiac_param("APOLIPOPROTEIN B",apolipoprotein_b[-1],MAX_CONSIDER,apolipoprotein_b_predicted)

        if (risk_apolipoprotein_b):
            file_name_ap_pr_b = plot_save(time_list+time_list_future,apolipoprotein_b_predicted,"APOLIPOPROTEIN B Values Prediction","Apolipoprotein_B", user_id, "APOLIPOPROTEIN B",MAX_CONSIDER)

    if len(lipoprotein_a) >= 3:
        lipoprotein_a_predicted = get_linear_regression(timestamp_list,lipoprotein_a,timestamp_list_future)
        risk_lipoprotein_a = calculate_risk_cardiac_param("LIPOPROTEIN A",lipoprotein_a[-1],MAX_CONSIDER,lipoprotein_a_predicted)

        if (lipoprotein_a):
            file_name_lipr_a = plot_save(time_list+time_list_future, lipoprotein_a_predicted,"LIPOPROTEIN A Values Prediction","Lipoprotein_A",user_id,"LIPOPROTEIN A", MAX_CONSIDER) 

    if len(s_homocysteine) >= 3:
        s_homocysteine_predicted = get_linear_regression(timestamp_list,s_homocysteine,timestamp_list_future)
        risk_s_homocysteine = calculate_risk_cardiac_param("HOMOCYSTEINE", s_homocysteine[-1],MAX_CONSIDER,s_homocysteine_predicted)

        if (risk_s_homocysteine):
            file_name_hmcst = plot_save(time_list+time_list_future, s_homocysteine+s_homocysteine_predicted,"HOMOCYSTEINE Values Prediction","S_Homocysteine",user_id,"HOMOCYSTEINE",MAX_CONSIDER)


    if len(s_fibrinogen) >= 3:
        s_fibrinogen_predicted = get_linear_regression(timestamp_list,s_fibrinogen,timestamp_list_future)
        risk_s_fibrinogen = calculate_risk_cardiac_param("FIBRINOGEN", s_fibrinogen[-1],MAX_CONSIDER,s_fibrinogen_predicted)

        if (risk_s_fibrinogen):
            file_name_fbrgn = plot_save(time_list+time_list_future, s_fibrinogen+s_fibrinogen_predicted,"FIBRINOGEN Values Prediction","S_Fibrinogen", user_id, "FIBRINOGEN", MAX_CONSIDER)

    # check whether the length of cardiac params is less than 3
    # check whether risk_cardiac is high or moderate
    # compare the last value of cardiac param with ideal risk value and then do the predicton
    if len(cholestrol_total) < 3:
        if risk_cardiac == "High" or risk_cardiac == "Moderate":
            if cholestrol_total[-1] >= risk_value_for_prediction(min_cholestrol_total,max_cholestrol_total):
                cholestrol_total_predicted = get_linear_regression(timestamp_list,cholestrol_total, timestamp_list_future)
                risk_cholestrol_total = calculate_risk_cardiac_param("CHOLESTROL TOTAL",cholestrol_total[-1], MAX_CONSIDER, cholestrol_total_predicted)
                if (risk_cholestrol_total):
                        file_name_chl = plot_save(time_list+time_list_future, cholestrol_total+cholestrol_total_predicted, "Cholestrol Total Values Prediction", "Cholestrol_Total", user_id, "CHOLESTROL TOTAL",MAX_CONSIDER)
    
    if len(triglycerides) < 3:
        if risk_cardiac == "High" or risk_cardiac == "Moderate":
            if triglycerides[-1] >= risk_value_for_prediction(min_triglycerides, max_triglycerides):
                triglycerides_predicted = get_linear_regression(timestamp_list, triglycerides, timestamp_list_future)
                risk_triglycerides = calculate_risk_cardiac_param("TRIGLYCERIDES", triglycerides[-1],MAX_CONSIDER, triglycerides_predicted)

                if (risk_triglycerides):
                    file_name_trgs = plot_save(time_list+time_list_future, triglycerides+triglycerides_predicted,"Triglycerides Values Prediction","Triglycerides", user_id, "TRIGLYCERIDES", MAX_CONSIDER)

    if len(hdl_cholestrol) < 3:
        if risk_cardiac == "High" or risk_cardiac == "Moderate":
            if hdl_cholestrol[-1] >= risk_value_for_prediction(min_hdl_cholestrol, max_hdl_cholestrol):
                hdl_cholestrol_predicted = get_linear_regression(timestamp_list, hdl_cholestrol,timestamp_list_future)
                risk_hdl_cholestrol = calculate_risk_cardiac_param("HDL CHOLESTROL", hdl_cholestrol[-1], MAX_CONSIDER, hdl_cholestrol_predicted)
                if (risk_hdl_cholestrol):
                    file_name_hdl_chl = plot_save(time_list+time_list_future, hdl_cholestrol+hdl_cholestrol_predicted,"HDL Cholestrol Values Prediction", "HDL_Cholestrol", user_id, "HDL CHOLESTROL",MAX_CONSIDER)
    
    if len(ldl_cholestrol) < 3:
        if risk_cardiac == "High" or risk_cardiac == "Moderate":
            if ldl_cholestrol[-1] >= risk_value_for_prediction(min_ldl_cholestrol,max_ldl_cholestrol):
                ldl_cholestrol_predicted = get_linear_regression(timestamp_list, ldl_cholestrol, timestamp_list_future)
                risk_ldl_cholestrol = calculate_risk_cardiac_param("LDL CHOLESTROL", ldl_cholestrol[-1], MAX_CONSIDER, ldl_cholestrol_predicted) 
                if (risk_ldl_cholestrol):
                    file_name_ldl_chl = plot_save(time_list+time_list_future,ldl_cholestrol+ldl_cholestrol_predicted,"LDL CHOLESTROL Values Prediction","LDL_Cholestrol",user_id, "HDL CHOLESTROL", MAX_CONSIDER)

    if len(apolipoprotein_a1) < 3:
        if risk_cardiac  == "High" or risk_cardiac == "Moderate":
            if apolipoprotein_a1[-1] >= risk_value_for_prediction(min_apolipoprotein_a1, max_apolipoprotein_a1):
                apolipoprotein_a1_predicted = get_linear_regression(timestamp_list, apolipoprotein_a1,timestamp_list_future)
                risk_apolipoprotein_a1 = calculate_risk_cardiac_param("APOLIPOPROTEIN A1", apolipoprotein_a1[-1],MAX_CONSIDER,apolipoprotein_a1_predicted)
                if (risk_apolipoprotein_a1):
                    file_name_ap_pr_a1 = plot_save(time_list+time_list_future, apolipoprotein_a1_predicted,"APOLIPOPROTEIN A1 Values Prediction", "Apolipoprotein_A1", user_id, "APOLIPOPROTEIN A1", MAX_CONSIDER)

    if len(apolipoprotein_b) < 3:
        if risk_cardiac  == "High" or risk_cardiac == "Moderate":
            if apolipoprotein_b[-1] >= risk_value_for_prediction(min_apolipoprotein_b, max_apolipoprotein_b):
                apolipoprotein_b_predicted = get_linear_regression(timestamp_list,apolipoprotein_b,timestamp_list_future)
                risk_apolipoprotein_b = calculate_risk_cardiac_param("APOLIPOPROTEIN B",apolipoprotein_b[-1],MAX_CONSIDER,apolipoprotein_b_predicted)
                if (risk_apolipoprotein_b):
                    file_name_ap_pr_b = plot_save(time_list+time_list_future,apolipoprotein_b_predicted,"APOLIPOPROTEIN B Values Prediction","Apolipoprotein_B", user_id, "APOLIPOPROTEIN B",MAX_CONSIDER)

    if len(lipoprotein_a) < 3:
        if risk_cardiac == "High" or risk_cardiac == "Moderate":
            if lipoprotein_a[-1] >= risk_value_for_prediction(min_lipoprotein_a,max_lipoprotein_a):
                lipoprotein_a_predicted = get_linear_regression(timestamp_list,lipoprotein_a,timestamp_list_future)
                risk_lipoprotein_a = calculate_risk_cardiac_param("LIPOPROTEIN A",lipoprotein_a[-1],MAX_CONSIDER,lipoprotein_a_predicted)

                if (lipoprotein_a):
                    file_name_lipr_a = plot_save(time_list+time_list_future, lipoprotein_a_predicted,"LIPOPROTEIN A Values Prediction","Lipoprotein_A",user_id,"LIPOPROTEIN A", MAX_CONSIDER)

    if len(s_homocysteine) < 3:
        if risk_cardiac == "High" or risk_cardiac == "Moderate":
            if s_homocysteine[-1] >= risk_value_for_prediction(min_s_homocysteine,max_s_homocysteine):
                s_homocysteine_predicted = get_linear_regression(timestamp_list,s_homocysteine,timestamp_list_future)
                risk_s_homocysteine = calculate_risk_cardiac_param("HOMOCYSTEINE", s_homocysteine[-1],MAX_CONSIDER,s_homocysteine_predicted)
    
                if (risk_s_homocysteine):
                    file_name_hmcst = plot_save(time_list+time_list_future, s_homocysteine+s_homocysteine_predicted,"HOMOCYSTEINE Values Prediction","S_Homocysteine",user_id,"HOMOCYSTEINE",MAX_CONSIDER)

    if len(s_fibrinogen) < 3:
        if risk_cardiac == "High" or risk_cardiac == "Moderate":
            if s_fibrinogen[-1] >= risk_value_for_prediction(min_s_fibringen,max_s_fibringen):
                s_fibrinogen_predicted = get_linear_regression(timestamp_list,s_fibrinogen,timestamp_list_future)
                risk_s_fibrinogen = calculate_risk_cardiac_param("FIBRINOGEN", s_fibrinogen[-1],MAX_CONSIDER,s_fibrinogen_predicted)
                if (risk_s_fibrinogen):
                    file_name_fbrgn = plot_save(time_list+time_list_future, s_fibrinogen+s_fibrinogen_predicted,"FIBRINOGEN Values Prediction","S_Fibrinogen", user_id, "FIBRINOGEN", MAX_CONSIDER)
   

    # handle exception like, if data is not there to add in json
    try:  
        # add result to json     
        json_data = {}
        card_predict = {}
        card_predict_chl = {}
        card_predict_trglycs = {}
        card_predict_hdl_chl = {}
        card_predict_ldl_chl = {}
        card_predict_apopr_a1 = {}
        card_predict_apopr_b = {}
        card_predict_lipr = {}
        card_predict_hmcyst = {}
        card_predict_fibrngn = {}

        # add cholestrol_total data
        card_predict_chl['NAME'] = 'Cholestrol Total'
        card_predict_chl['RISK'] = risk_cholestrol_total
        card_predict_chl['PLOT'] = file_name_chl

        # add Triglcerides data
        card_predict_trglycs['NAME'] = 'Triglcerides'
        card_predict_trglycs['RISK'] = risk_triglycerides
        card_predict_trglycs['PLOT'] = file_name_trgs

        # add hdl cholestrol data
        card_predict_hdl_chl['NAME'] = 'HDL Cholestrol'
        card_predict_hdl_chl['RISK'] = risk_hdl_cholestrol
        card_predict_hdl_chl['PLOT'] = file_name_hdl_chl

        # add ldl cholestrol data
        card_predict_ldl_chl['NAME'] = 'HDL Cholestrol'
        card_predict_ldl_chl['RISK'] = risk_ldl_cholestrol
        card_predict_ldl_chl['PLOT'] = file_name_ldl_chl
    
        # add apolipoprotein_a1 data
        card_predict_apopr_a1['NAME'] = "Apolipoprotein A1"
        card_predict_apopr_a1['RISK'] = risk_apolipoprotein_a1
        card_predict_apopr_a1['PLOT'] = file_name_ap_pr_a1

        # add apolipoprotein_a1 data
        card_predict_apopr_b['NAME'] = "Apolipoprotein B"
        card_predict_apopr_b['RISK'] = risk_apolipoprotein_b
        card_predict_apopr_b['PLOT'] = file_name_ap_pr_b

        # add lipoprotein data
        card_predict_lipr['NAME'] = "Lipoprotein A"
        card_predict_lipr['RISK'] = risk_lipoprotein_a
        card_predict_lipr['PLOT'] = file_name_lipr_a

        # add homocysteine data
        card_predict_hmcyst['NAME'] = "Homocysteine"
        card_predict_hmcyst['RISK'] = risk_s_homocysteine
        card_predict_hmcyst['PLOT'] = file_name_hmcst

        # add fibrinoen data
        card_predict_fibrngn['NAME'] = "Homocysteine"
        card_predict_fibrngn['RISK'] = risk_s_fibrinogen
        card_predict_fibrngn['PLOT'] = file_name_hmcst


        # add cardiac data to dia_predict
        card_predict['CHOLESTROL TOTAL'] = card_predict_chl
        card_predict['TRIGLYCERIDES'] = card_predict_trglycs
        card_predict['HDL CHOLESTROL'] = card_predict_hdl_chl
        card_predict['LDL CHOLESTROL'] = card_predict_ldl_chl
        card_predict['APOLIPOPROTEIN A1'] = card_predict_apopr_a1
        card_predict['APOLIPOPROTEIN B'] = card_predict_apopr_b
        card_predict['HOMOCYSTEINE'] = card_predict_hmcyst
        card_predict['FIBRINOGEN'] = card_predict_fibrngn
        card_predict['Risk'] = (risk_cholestrol_total or risk_triglycerides or risk_hdl_cholestrol or risk_ldl_cholestrol or risk_apolipoprotein_a1 or risk_apolipoprotein_b or risk_s_homocysteine or risk_s_fibrinogen)
        result_time_list = time_list + time_list_future
        card_predict["Expected Crash"] = result_time_list[expected_crash]

        # add cardiac_predict to json_data
        json_data['Cardiac Prediction'] = card_predict
        print json.dumps(json_data)
        return 0
    
    except Exception as err:
        json_data["RISK"] = risk_cardiac 
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

    #call user risk data
    risk_cardiac = get_user_risk_data_cardiac(user_id,db)
    
    #get user cardiac params
    get_user_cardiac_data(db,user_id)
    
    #get min and max values for cardiac params
    min_cholestrol_total = get_min_value("CHOLESTROL TOTAL")
    max_cholestrol_total = get_max_value("CHOLESTROL TOTAL")
    min_triglycerides = get_min_value("TRIGLYCERIDES")
    max_triglycerides = get_max_value("TRIGLYCERIDES")
    min_hdl_cholestrol = get_min_value("HDL CHOLESTROL")
    max_hdl_cholestrol = get_max_value("HDL CHOLESTROL")
    min_ldl_cholestrol = get_min_value("LDL CHOLESTROL")
    max_ldl_cholestrol = get_max_value("LDL CHOLESTROL")
    min_apolipoprotein_a1 = get_min_value("APOLIPOPROTEIN A1")
    max_apolipoprotein_a1 = get_max_value("APOLIPOPROTEIN A1")
    min_apolipoprotein_b = get_min_value("APOLIPOPROTEIN B")
    max_apolipoprotein_b = get_max_value("APOLIPOPROTEIN B")
    min_lipoprotein_a = get_min_value("LIPOPROTEIN A")
    max_lipoprotein_a = get_max_value("LIPOPROTEIN A")
    min_s_homocysteine = get_min_value("HOMOCYSTEINE")
    max_s_homocysteine = get_max_value("HOMOCYSTEINE")
    min_s_fibringen = get_min_value("FIBRINOGEN")
    max_s_fibringen = get_max_value("FIBRINOGEN")

    #prepare list of dates to predict
    prepare_next_set_time()

    #call the prediction function
    validate_to_predict_cardiac()
    #close db
    close_db()
    exit(0)
