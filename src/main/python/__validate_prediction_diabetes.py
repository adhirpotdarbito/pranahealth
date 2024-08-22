# import libraries required
import os
import sys
import json
from __config import *
from __users import *
from __choose_health_insurance import *
from __db_config import *
from __prediction_diabetes import *

# get minimum and maximum value of diabetes params
min_glucose_fasting = get_min_value("GLUCOSE FASTING")
max_glucose_fasting = get_max_value("GlUCOSE FASTING")
min_glucose_pp = get_min_value("GLUCOSE POST PRANDIAL")
max_glucose_pp = get_max_value("GLUCOSE POST PRANDIAL")
min_hba1c = get_min_value("HbA1C")
max_hba1c = get_max_value("HbA1C")


# function to calculate risk value
def risk_value_for_prediction(min_val,max_val):
    """
        Function to calculate ideal risk value
    """
    delta = max_val - min_val
    chk  = delta/10
    risk_val = delta + chk*5
    return risk_val

# function to check whether prediction is required
def validate_to_predict_diabetes(glucose_fasting, glucose_pp,HbA1C):
    """
        Function to validate diabetes parameters and do the prediction and plot the predicted value.
    """
    file_name_gf = ""
    file_name_gp = ""
    file_name_hba1c = ""
    
    # check whether length is greater than 3
    if len(glucose_fasting) >= 3:
        #call prediction function and calculate prediction for glucose_fasting
        glucose_fasting_predicted = get_linear_regression(timestamp_list,glucose_fasting,timestamp_list_future)
        risk_glucose_fasting = calculate_risk_dia_param('GLUCOSE FASTING',glucose_fasting[len(glucose_fasting)-1],MAX_CONSIDER,glucose_fasting_predicted)
        # check for risk glucose fasting and plot prediction graph
        if (risk_glucose_fasting):
            file_name_gf = plot_save (time_list+time_list_future,glucose_fasting+glucose_fasting_predicted,"Glucose Fasting Values Prediction","Glucose_Fasting",user_id,'GLUCOSE FASTING',MAX_CONSIDER)
        
    if len(glucose_pp) >= 3:
        #call prediction function and calculate prediction for glucose_pp
        glucose_pp_predicted = get_linear_regression(timestamp_list,glucose_pp,timestamp_list_future)
        risk_glucose_pp = calculate_risk_dia_param('GLUCOSE POST PRANDIAL',glucose_pp[len(glucose_pp)-1],MAX_CONSIDER,glucose_pp_predicted)
        # check for risk glucose pp and plot prediction graph
        if (risk_glucose_pp):
            file_name_gp = plot_save (time_list+time_list_future,glucose_pp+glucose_pp_predicted,"Glucose PP Values Prediction","Glucose_PP",user_id,'GLUCOSE POST PRANDIAL',MAX_CONSIDER)
    
    if len(HbA1C) >= 3:
        #call prediction function and calculate prediction for HbA1C
        hba1c_predicted = get_linear_regression(timestamp_list,HbA1C,timestamp_list_future)
        risk_HbA1C = calculate_risk_dia_param('HbA1c',HbA1C[len(HbA1C)-1],MAX_CONSIDER,hba1c_predicted)
        # check for risk Hb1AC and plot prediction graph
        if (risk_HbA1C):
            file_name_hba1c = plot_save (time_list+time_list_future,HbA1C+hba1c_predicted,"HbA1c Values Prediction","HbA1c",user_id,'HbA1c',MAX_CONSIDER)
    
    # check whether length is less than 3
    if len(glucose_fasting) < 3:
        #check whether risk is High or moderate
        if risk_diabetic == "High" or risk_diabetic == "Moderate":
            # compare the last value of glucose_fasting with ideal risk value
            if glucose_fasting[-1] >= risk_value_for_prediction(min_glucose_fasting,max_glucose_fasting):
                #call prediction function and calculate prediction for glucose_fasting
                glucose_fasting_predicted = get_linear_regression(timestamp_list,glucose_fasting,timestamp_list_future)
                risk_glucose_fasting = calculate_risk_dia_param('GLUCOSE FASTING',glucose_fasting[len(glucose_fasting)-1],MAX_CONSIDER,glucose_fasting_predicted) 
                # check for risk glucose fasting and plot prediction graph
                if (risk_glucose_fasting):
            	    file_name_gf = plot_save (time_list+time_list_future,glucose_fasting+glucose_fasting_predicted,"Glucose Fasting Values Prediction","Glucose_Fasting",user_id,'GLUCOSE FASTING',MAX_CONSIDER)
    
    if len(glucose_pp) < 3:       
        #check whether risk is High or moderate
        if risk_diabetic == "High" or risk_diabetic == "Moderate":
            # compare the last value of glucose_pp with ideal risk value
            if glucose_pp[-1] >= risk_value_for_prediction(min_glucose_pp,max_glucose_pp):
                #call prediction function and calculate prediction for glucose_pp
                glucose_pp_predicted = get_linear_regression(timestamp_list,glucose_pp,timestamp_list_future)
                risk_glucose_pp = calculate_risk_dia_param('GLUCOSE POST PRANDIAL',glucose_pp[len(glucose_pp)-1],MAX_CONSIDER,glucose_pp_predicted)
                # check for risk glucose pp and plot prediction graph
                if (risk_glucose_pp):
                    file_name_gp = plot_save (time_list+time_list_future,glucose_pp+glucose_pp_predicted,"Glucose PP Values Prediction","Glucose_PP",user_id,'GLUCOSE POST PRANDIAL',MAX_CONSIDER)
      
    if len(HbA1C) < 3:
        #check whether risk is High or moderate
        if risk_diabetic == "High" or risk_diabetic == "Moderate":
            # compare the last value of glucose_pp with ideal risk value
            if HbA1C[-1] >= risk_value_for_prediction(min_hba1c,max_hba1c):
                #call prediction function and calculate prediction for Hb1AC
                hba1c_predicted = get_linear_regression(timestamp_list,HbA1C,timestamp_list_future)
                risk_HbA1C = calculate_risk_dia_param('HbA1c',HbA1C[len(HbA1C)-1],MAX_CONSIDER,hba1c_predicted)
                # check for risk HbA1C and  plot prediction graph
                if (risk_HbA1C):
            	    file_name_hba1c = plot_save (time_list+time_list_future,HbA1C+hba1c_predicted,"HbA1c Values Prediction","HbA1c",user_id,'HbA1c',MAX_CONSIDER)

    # handle exception
    try:
        # add result to json     
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

    except Exception as err:
        json_data['RISK'] = risk_diabetic
        print json.dumps(json_data)
        return 0

if __name__ == '__main__':
    argc = len(sys.argv) - 1
    if (argc < 1):
        print "python __validate_prediction.py <user_id>"
        print "EX. python __validate_prediction.py 1"
        exit(0)

    # open pranacare database
    init_db()
    db = get_db()

    #get user id
    user_id = int(sys.argv[1])

    #get user info
    user_info = init_user_info(user_id)

    #prepare user body parameters
    prepare_user_body_params(db, user_info)

    #get user age
    age = get_user_age()
    
    # call user risk data for diabetes
    risk_diabetic = get_user_risk_data_diabetic(user_id,db)
    
    # get user diabetes data
    get_user_diabetes_data(db,user_id)

    #prepare next date 
    prepare_next_set_time()

    #call prediction function
    validate_to_predict_diabetes(glucose_fasting, glucose_pp, HbA1C)
    # close db
    close_db()
    exit(0)

