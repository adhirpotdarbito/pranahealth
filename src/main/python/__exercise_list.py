'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

import json
import sys
from __exercise_model import *


def update_user_rcb (db,user_id,rcb):
    """
	This function takes input db, user_id and rcb, connects to the database deletes the previous user_recommended_cb of the user and insert new user_recommended_cb.
    """
    cursor  = db.cursor()
    try:
        query_str = "delete from user_recommended_cb where user_id=%d" %user_id
        cursor.execute(query_str)
        db.commit()
        query_str = "insert into user_recommended_cb (user_id,rcb) values (%d, %s)" %(user_id,rcb)
        cursor.execute(query_str)
        db.commit()
    except Exception as err:
        print (Exception,err)
        print ("Fatal error update_user_rcb")
        cursor.close()
        return -1
    cursor.close()
    return 0

def get_exercise_list(db,user_id,user_risk,whtr_risk,age):
    """
	This function takes db, user_id, user_risk, whtr_risk, age as input, get risk for diabetes, hypertension, cardiac, obesity, renal.
Add exercise list of early morning, post lunch, post dinner, exercise normal in dictionaries, check if user has whtr_risk and add exercise obese list in exercise_main dictionary, check for user age and add recommended calories burn in the exercise_list and then call update_user_rcb() and return exercise_list and exercise recommendations.
    """
    # get user risk data
    diabetes = user_risk.user_dia_risk.risk
    htn = user_risk.user_htn_risk.risk
    cardiac = user_risk.user_cardiac_risk.risk
    obese = user_risk.user_obese_risk.risk
    renal = user_risk.user_renal_risk.risk

    # recommended calorie burn
    rcb = 0

    exercise_list = {}
    exercise_early_morning = {}
    exercise_post_lunch = {}
    exercise_post_dinner = {}
    exercise_main = {}
    exercise_recommendations = {}

    exercise_early_morning['Early Morning List'] = exercise_em_list
    exercise_early_morning['User Expose'] = 1
    exercise_post_lunch['Post Lunch List'] = exercise_post_lunch_list
    exercise_post_lunch['User Expose'] = 1
    exercise_post_dinner['Post Dinner List'] = exercise_post_dinner_list
    exercise_post_dinner['User Expose'] = 1

    exercise_main['User Expose'] = 1
    exercise_main['Main List'] = exercise_opt_normal_list

    if (whtr_risk):
        exercise_main['Main List'] = exercise_obese_list
        exercise_main['User Expose'] = 1

        if (age <= 40):
            rcb = 400
            exercise_list['Recommended Daily Cal Burn'] = rcb
        else:
            rcb = 300
            exercise_list['Recommended Daily Cal Burn'] = rcb
    else:
        if (age < 35):
            rcb = 400
            exercise_list['Recommended Daily Cal Burn'] = rcb
        else:
            rcb = 250
            exercise_list['Recommended Daily Cal Burn'] = rcb

    update_user_rcb(db,int(user_id),rcb)

    exercise_list['Early Morning'] = exercise_early_morning
    exercise_list['Post Lunch'] = exercise_post_lunch
    exercise_list['Post Dinner'] = exercise_post_dinner
    exercise_list['Main'] = exercise_main
 
    exercise_recommendations["Remarks"] = "Given Calories Burned per Exercise is an Average Value.It typically depend on your body weight.If you have more weight you may expect more calories to be burned with same amount of exercise."

    return exercise_list, exercise_recommendations
