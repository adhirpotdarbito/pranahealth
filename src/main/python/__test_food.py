# -*- coding: utf-8 -*- 
from __db_config import *

# create food group lists
food_early_morning = []
food_break_fast = []
food_mid_morning = []
food_lunch = []
food_evening = []
food_dinner = []
rec_party_food = []

tricks_eating_out = ['Opt for a Salad Appetizer','Stick with Chicken or Seafood','Avoid the Fried Food','Choose Meats Cooked Tandoori Style','Skip the Soup','Order Roti Bread Instead of Naan','Order from the Lunch Menu','Don’t be Afraid to Custom Order','Keep It Cool','Watch The Rice','Skip Dessert']

# create exception lists 
exception_diabetes = []
exception_hypertension = []
exception_cardiac = []
exception_obesity = []
exception_renal = []


# define functions
def early_morning(db):
    """
	Function returns list of food item name, calorie and min. quantity for early morning.
    """
    cursor = db.cursor()
    query = "select f2.food_name, f2.food_calories, f2.min_quantity from food_group_food_item as f1 inner join food_item as f2 on f1.fdit_id = f2.fdit_id where f1.fgrp_id=(select fgrp_id from food_group where group_name='Early Morning');"
    cursor.execute(query)
    em = cursor.fetchone()
    while em is not None:
        food_early_morning.append(em[2]+" "+em[0]+":"+str(em[1]))
	em = cursor.fetchone()
    return food_early_morning

def break_fast_food(db):
    """
	Function returns list of all food item name, calorie and min. quantity for break fast. 
    """
    cursor = db.cursor()
    query = "select f2.food_name, f2.food_calories, f2.min_quantity from food_group_food_item as f1 inner join food_item as f2 on f1.fdit_id = f2.fdit_id where f1.fgrp_id=(select fgrp_id from food_group where group_name='Break Fast');"
    cursor.execute(query)
    em = cursor.fetchone()
    while em is not None:
        food_break_fast.append(em[2]+" "+em[0]+":"+str(em[1]))
	em = cursor.fetchone()
    return food_break_fast

def mid_morning_food(db):
    """
	Function returns list of all food item name, calorie and min, quantity for mid morning.
    """
    cursor = db.cursor()
    query = "select f2.food_name, f2.food_calories, f2.min_quantity from food_item as f2 inner join food_group_food_item as f1 on f1.fdit_id = f2.fdit_id where fgrp_id = (select fgrp_id from food_group where group_name='Mid Morning')"
    cursor.execute(query)
    em = cursor.fetchone()
    while em is not None:
        food_mid_morning.append(em[2]+ " "+ em[0]+":"+str(em[1]))
	em = cursor.fetchone()
    return food_mid_morning

def lunch_food(db):
    """
	Function returns list of food item name, calorie and min. quantity for lunch.
    """
    cursor = db.cursor()
    query = "select f2.food_name, f2.food_calories, f2.min_quantity from food_item as f2 inner join food_group_food_item as f1 on f1.fdit_id = f2.fdit_id where fgrp_id = (select fgrp_id from food_group where group_name='Lunch')"
    cursor.execute(query)
    em = cursor.fetchone()
    while em is not None:
        food_lunch.append(em[2] + " " + em[0]+":"+str(em[1]))
	em = cursor.fetchone()
    return food_lunch

def evening_food(db):
    """	
	Function returns list of food item name, calorie and min. quantity for evening.
    """
    cursor = db.cursor()
    query = "select f2.food_name, f2.food_calories, f2.min_quantity from food_item as f2 inner join food_group_food_item as f1 on f1.fdit_id = f2.fdit_id where fgrp_id = (select fgrp_id from food_group where group_name= 'Evening')"
    cursor.execute(query)
    em = cursor.fetchone()
    while em is not None:
        food_evening.append(em[2] + " " + em[0]+":"+str(em[1]))
	em = cursor.fetchone()
    return food_evening

def dinner_food(db):
    """
	Function returns list of food item name, calorie and min. quantity for dinner food.
    """
    cursor = db.cursor()
    query = "select f2.food_name, f2.food_calories, f2.min_quantity from food_item as f2 inner join food_group_food_item as f1 on f1.fdit_id = f2.fdit_id where fgrp_id = (select fgrp_id from food_group where group_name='Dinner')"
    cursor.execute(query)
    em = cursor.fetchone()
    while em is not None:
        food_dinner.append(em[2] + " " + em[0]+":"+str(em[1]))
	em = cursor.fetchone()
    return food_dinner


def food_exception_diab(db):
    """
	Function return list of food items restricted for diabetes.
    """
    cursor = db.cursor()
    query = "select f2.food_name from food_item as f2 inner join food_exception_food_item as f1 on f1.fdit_id = f2.fdit_id where fexp_id = (select fexp_id from food_exception where exception_name='Diabetes')"
    cursor.execute(query)
    exp_dia = cursor.fetchone()
    while exp_dia is not None:
	exception_diabetes.append(exp_dia[0])
	exp_dia = cursor.fetchone()
    return exception_diabetes

def food_exception_htn(db):
    """
	Function return list of food items restricted for hypertension.
    """
    cursor = db.cursor()
    query = "select f2.food_name from food_item as f2 inner join food_exception_food_item as f1 on f1.fdit_id = f2.fdit_id where fexp_id = (select fexp_id from food_exception where exception_name='Hypertension')"
    cursor.execute(query)
    exp_htn = cursor.fetchone()
    while exp_htn is not None:
	exception_hypertension.append(exp_htn[0])
	exp_htn = cursor.fetchone()
    return exception_hypertension

def food_exception_cardiac(db):
    """
	Function return list of food items restricted for cardiac.
    """
    cursor = db.cursor()
    query = "select f2.food_name from food_item as f2 inner join food_exception_food_item as f1 on f1.fdit_id = f2.fdit_id where fexp_id = (select fexp_id from food_exception where exception_name='Cardiac')"
    cursor.execute(query)
    exp_crd = cursor.fetchone()
    while exp_crd is not None:
	exception_cardiac.append(exp_crd[0])
	exp_crd = cursor.fetchone()
    return exception_cardiac

def food_exception_obese(db):
    """
	Function return list of food items restricted for obesity.
    """
    cursor = db.cursor()
    query = "select f2.food_name from food_item as f2 inner join food_exception_food_item as f1 on f1.fdit_id = f2.fdit_id where fexp_id = (select fexp_id from food_exception where exception_name='Obesity')"
    cursor.execute(query)
    exp_obs = cursor.fetchone()
    while exp_obs is not None:
	exception_obesity.append(exp_obs[0])
	exp_obs = cursor.fetchone()
    return exception_obesity

def food_exception_renal(db):
    """
	Function return list of food items restricted for renal.
    """
    cursor = db.cursor()
    query = "select f2.food_name from food_item as f2 inner join food_exception_food_item as f1 on f1.fdit_id = f2.fdit_id where fexp_id = (select fexp_id from food_exception where exception_name='Renal')"
    cursor.execute(query)
    exp_ren = cursor.fetchone()
    while exp_ren is not None:
	exception_renal.append(exp_ren[0])
	exp_ren = cursor.fetchone()
    return exception_renal

def party_food(db):
    """
	Function returns list of restaurant foods.
    """
    cursor = db.cursor()
    query = "select f2.food_name from food_item as f2 inner join restaurant_food_item as f1 on f1.food_item_id = f2.fdit_id;"
    cursor.execute(query)
    em = cursor.fetchone()
    while em is not None:
	rec_party_food.append(em[0])
	em = cursor.fetchone()
    return rec_party_food


#initialize database
init_db()

#get database
db = get_db()

food_em = early_morning(db)
food_mm =  mid_morning_food(db)
food_bf = break_fast_food(db)
food_eve =  evening_food(db)
food_ln =  lunch_food(db)
food_din =  dinner_food(db)
food_exp_dia = food_exception_diab(db)
food_exp_htn = food_exception_htn(db)
food_exp_car = food_exception_cardiac(db)
food_exp_obs = food_exception_obese(db)
food_exp_ren = food_exception_renal(db)
recommended_party_food = party_food(db)
