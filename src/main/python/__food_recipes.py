# -*- coding: utf-8 -*- 
'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''
# import libraries required
import json
import sys
import random
import re
from __food_group import *
from __food_exception import *

def get_special_remark(user_risk):
    """
	Function to add special notes for users based on the risk.
    """
    special_note = []
    dia = 0
    hyper = 0
    heart = 0
    fat = 0
    kidney = 0

    diabetes = user_risk.user_dia_risk.risk
    if (diabetes == 'Diabetic' or diabetes == 'High'):
        dia = 1
        special_note.append('Please do not add Sugar/Use Sugar Free Gold.')
        special_note.append('Please try Avoiding Potatoes from Curry/Sabji.')
    htn = user_risk.user_htn_risk.risk

    if (htn == 'Hypertension' or htn == 'High'):
        hyper = 1
        special_note.append('Please add very little Table Salt in Recipes.')
        special_note.append('Please Avoid Pickles.')
    cardiac = user_risk.user_cardiac_risk.risk

    if (cardiac == 'Cardiac' or cardiac == 'High'):
        heart = 1
        special_note.append('Please try avoiding Butter/Margarine from repies as much as possible.')
        special_note.append('Please try taking Skim Milk rather Fat Rich Milk.')
        special_note.append('Please use little Oil in Recipes.')
    obese = user_risk.user_obese_risk.risk

    if (obese == 'High' or obese == 'Obese'):
        fat = 1
    renal = user_risk.user_renal_risk.risk

    if (renal == 'High' or renal == 'Renal'):
        kidney = 1

    return special_note

def check_food_exception(food,exp_list):
    """
        Function takes input food from food list and exception list for disease category and returns True or False if that food in the exception list. 
    """ 
    i = 0
    while i < len(exp_list):
        exp_food = exp_list[i]
        if re.search(food, exp_food, re.IGNORECASE) or re.search(exp_food, food, re.IGNORECASE):
            return True
        i = i + 1
    return False


def check_user_existing_profile(cardiac,renal,diabetes,htn):
    """
    	Function takes input diseaes cardiac, renal, diabetes, hypertension and check if the user have any disease and adds weights and return the weight.
    """
    weight = 0
    if (cardiac == 'Cardiac' or cardiac == 'High'):
        weight = weight + 1
    if (renal == 'Renal' or renal == 'High'):
        weight = weight + 1
    if (diabetes == 'Diabetic' or diabetes == 'High'):
        weight = weight + 1
    if (htn == 'Hypertension' or htn == 'High'):
        weight = weight + 1
    return weight


def recommended_frequency_eating_out(user_risk,age):
    """
    	This function takes input user_risk profile and age and returns duration for eating.  
    """
    diabetes = user_risk.user_dia_risk.risk
    htn = user_risk.user_htn_risk.risk
    cardiac = user_risk.user_cardiac_risk.risk
    obese = user_risk.user_obese_risk.risk
    renal = user_risk.user_renal_risk.risk

    weight = check_user_existing_profile(cardiac,renal,diabetes,htn)
    if (age > 54):
        if (weight > 3):
            return "Not Recommended"
        elif (weight > 2):
            return "Yearly (Better to Avoid)"
        elif (weight >1):
            return "Six Monthly"
        elif (weight == 1):
            return "Three Monthly"
        else:
            return "Monthly"
    else:
        if (weight > 3):
            return "Not Recommended"
        elif (weight > 2):
            return "Yearly (Better to Avoid)"
        elif (weight >1):
            return "Six Monthly"
        elif (weight == 1):
            return "Three Monthly"
        else:
            if (age > 40):
                return "Monthly"
            else:
                return "No Such Restriction"



def prepare_food_list(user_risk,rdca,food_list):
    """
    This function takes input user_risk profile, recommended calorie and food list and checks for food exception and returns recommended and restricted food items for the user
    """
    item = []
    restricted = []
    food_dict = {}
    diabetes = user_risk.user_dia_risk.risk
    htn = user_risk.user_htn_risk.risk
    cardiac = user_risk.user_cardiac_risk.risk
    obese = user_risk.user_obese_risk.risk
    renal = user_risk.user_renal_risk.risk
    for i in range(len(food_list)):
        food = food_list[i]
        restricted = food_dict.get(food, [])
	if diabetes == "Diabetic" or diabetes == 'High':
            if (check_food_exception(food, food_exp_dia)):
                restricted.append("Diabetes")
	if htn == "Hypertension" or htn == 'High':
            if check_food_exception(food, food_exp_htn):
            	restricted.append("Hypertension")
        if cardiac == "Cardiac" or cardiac == 'High':
	    if check_food_exception(food, food_exp_car):
            	restricted.append("Cardiac")
        if renal == "Renal" or renal == 'High':
	    if check_food_exception(food, food_exp_ren):
            	restricted.append("Renal")
        if obese == "Obese" or obese == 'High':
	    if check_food_exception(food, food_exp_obs):
                restricted.append("Obesity")

        food_dict[food] = list(set(restricted))
    for food, restriction in food_dict.items():
        if len(food_dict[food]) == 0:
            item.append(food)
        else:
            item.append(food+":Restricted:"+",".join(restriction))
    return item

def prepare_food_list_restro(user_risk,rdca,food_list):
    """
    	This function takes input user_risk profile, recommended calorie and restaurant food list and checks for food exception and returns restaurant food items.  
    """
    idx = 0
    item = []

    diabetes = user_risk.user_dia_risk.risk
    htn = user_risk.user_htn_risk.risk
    cardiac = user_risk.user_cardiac_risk.risk
    obese = user_risk.user_obese_risk.risk
    renal = user_risk.user_renal_risk.risk

    while idx < len(food_list):
        food = food_list[idx]
        idx = idx + 1
        if (diabetes == 'Diabetic'):
            # check if selected food is restricted for diabetes
            if (check_food_exception(food ,food_exp_dia)):
                continue
        if (htn == 'Hypertension'):
            # check if selected food is restricted for hypertension
            if (check_food_exception(food ,food_exp_htn)):
                continue
        if (cardiac == 'Cardiac'):
            # check if selected food is restricted for cardiac
            if (check_food_exception(food ,food_exp_car)):
                continue
        if (renal == 'Renal'):
            # check if selected food is restricted for renal
            if (check_food_exception(food ,food_exp_ren)):
                continue
        if (obese == 'Obese'):
            # check if selected food is restricted for obesity
            if (check_food_exception(food ,food_exp_obs)):
                continue
        item.append(food_list[idx-1])
    return item

def get_food_items(user_risk,rdca,age):
    """
    	This function takes input user_risk, rdca, age and call function prepare_food_list() and recommended calories (calculated using formula) for early morning, breakfast, mid morning, lunch, evening, dinner and add to food_list dictionaries for the above following periods, add recommended restaurant from prepare_food_list_restro(), tricks healthy eating out from tricks_eating_out, recommended frequency eating out from recommended_frequency_eating_out(), recommended junk food, special remarks from get_special_remark() in a food_recommendation dictionary and returns two dictionary i.e food_list and foo_recommendation. 
    """
    food_list = {}
    food_recommendations = {}
    food_list_em = {}
    food_list_bf = {}
    food_list_mm = {}
    food_list_lunch = {}
    food_list_es = {}
    food_list_din = {}

    # RDCA devision
    # 1:4:1:6:1:5
    em_rdca = (rdca/18)*1
    bf_rdca = (rdca/18)*4
    mm_rdca = (rdca/18)*1
    lunch_rdca = (rdca/18)*6
    es_rdca = (rdca/18)*1
    din_rdca = (rdca/18)*5

    food_list_em['Early Morning List'] = prepare_food_list(user_risk,rdca,food_em)
    food_list_em['Recommended Cal'] = int(round(em_rdca))
    food_list_em['User Expose'] = 1

    food_list_bf['Breakfast List'] = prepare_food_list(user_risk,rdca,food_bf)
    food_list_bf['Recommended Cal'] = int(round(bf_rdca))
    food_list_bf['User Expose'] = 1

    food_list_mm['Mid Morning List'] = prepare_food_list(user_risk,rdca,food_mm)
    food_list_mm['Recommended Cal'] = int(round(mm_rdca))
    food_list_mm['User Expose'] = 1

    food_list_lunch['Lunch List'] = prepare_food_list(user_risk,rdca,food_ln)
    food_list_lunch['Recommended Cal'] = int(round(lunch_rdca))
    food_list_lunch['User Expose'] = 1

    food_list_es['Evening List'] = prepare_food_list(user_risk,rdca,food_eve)
    food_list_es['Recommended Cal'] = int(round(es_rdca))
    food_list_es['User Expose'] = 1

    food_list_din['Dinner List'] = prepare_food_list(user_risk,rdca,food_din)
    food_list_din['Recommended Cal'] = int(round(din_rdca))
    food_list_din['User Expose'] = 1

    food_list["Early Morning"] = food_list_em
    food_list["Breakfast"] = food_list_bf
    food_list["Mid Morning"] = food_list_mm
    food_list["Lunch"] = food_list_lunch
    food_list["Evening"] = food_list_es
    food_list["Dinner"] = food_list_din

    food_recommendations["Recommended Restaurant Food"] = prepare_food_list_restro(user_risk,rdca,recommended_party_food)
    food_recommendations["Tricks Healthy Eating Out"] = tricks_eating_out
    food_recommendations["Recommended Frequency Eating Out"] = recommended_frequency_eating_out(user_risk,age)
    food_recommendations['Recommended Junk Food'] = "<Example Food>:<Cal>"

    food_recommendations["Remarks"] = get_special_remark(user_risk)

    return food_list, food_recommendations

