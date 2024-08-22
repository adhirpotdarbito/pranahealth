from __db_config import *

class FoodGroup():
    """
        A class for Food Group
    """
    init_db()
    def __init__ (self):
        self.db = get_db()
        self.food_early_morning = []
        self.food_break_fast = []
        self.food_mid_morning = []
        self.food_lunch = []
        self.food_evening = []
        self.food_dinner = []

    def early_morning_food(self):
        """
            Function returns list of food item name, calorie and min. quantity for early morning.
        """
        cursor = self.db.cursor()
        query = "select f2.food_name, f2.food_calories, f2.min_quantity from food_group_food_item as f1 inner join food_item as f2 on f1.fdit_id = f2.fdit_id where f1.fgrp_id=(select fgrp_id from food_group where group_name='Early Morning');"
        cursor.execute(query)
        em = cursor.fetchone()
        while em is not None:
            self.food_early_morning.append(em[2]+" "+em[0]+":"+str(em[1]))
            em = cursor.fetchone()
        return self.food_early_morning

    
    def break_fast_food(self):
        """
	        Function returns list of all food item name, calorie and min. quantity for break fast. 
        """
        cursor = self.db.cursor()
        query = "select f2.food_name, f2.food_calories, f2.min_quantity from food_group_food_item as f1 inner join food_item as f2 on f1.fdit_id = f2.fdit_id where f1.fgrp_id=(select fgrp_id from food_group where group_name='Breakfast');"
        cursor.execute(query)
        bf = cursor.fetchone()
        while bf is not None:
            self.food_break_fast.append(bf[2]+" "+bf[0]+":"+str(bf[1]))
    	    bf = cursor.fetchone()
        return self.food_break_fast

    def mid_morning_food(self):
        """
	        Function returns list of all food item name, calorie and min, quantity for mid morning.
        """ 
        cursor = self.db.cursor()
        query = "select f2.food_name, f2.food_calories, f2.min_quantity from food_item as f2 inner join food_group_food_item as f1 on f1.fdit_id = f2.fdit_id where fgrp_id = (select fgrp_id from food_group where group_name='Mid Morning')"
        cursor.execute(query)
        mm = cursor.fetchone()
        while mm is not None:
            self.food_mid_morning.append(mm[2]+ " "+ mm[0]+":"+str(mm[1]))
    	    mm = cursor.fetchone()
        return self.food_mid_morning

    def lunch_food(self):
        """
	        Function returns list of food item name, calorie and min. quantity for lunch.
        """
        cursor = self.db.cursor()
        query = "select f2.food_name, f2.food_calories, f2.min_quantity from food_item as f2 inner join food_group_food_item as f1 on f1.fdit_id = f2.fdit_id where fgrp_id = (select fgrp_id from food_group where group_name='Lunch')"
        cursor.execute(query)
        lf = cursor.fetchone()
        while lf is not None:
            self.food_lunch.append(lf[2] + " " + lf[0]+":"+str(lf[1]))
    	    lf = cursor.fetchone()
        return self.food_lunch

    def evening_food(self):
        """	
   	        Function returns list of food item name, calorie and min. quantity for evening.
        """
        cursor = self.db.cursor()
        query = "select f2.food_name, f2.food_calories, f2.min_quantity from food_item as f2 inner join food_group_food_item as f1 on f1.fdit_id = f2.fdit_id where fgrp_id = (select fgrp_id from food_group where group_name= 'Evening')"
        cursor.execute(query)
        ef = cursor.fetchone()
        while ef is not None:
            self.food_evening.append(ef[2] + " " + ef[0]+":"+str(ef[1]))
    	    ef = cursor.fetchone()
        return self.food_evening

    def dinner_food(self):
        """
        	Function returns list of food item name, calorie and min. quantity for dinner food.
        """
        cursor = self.db.cursor()
        query = "select f2.food_name, f2.food_calories, f2.min_quantity from food_item as f2 inner join food_group_food_item as f1 on f1.fdit_id = f2.fdit_id where fgrp_id = (select fgrp_id from food_group where group_name='Dinner')"
        cursor.execute(query)
        df = cursor.fetchone()
        while df is not None:
            self.food_dinner.append(df[2] + " " + df[0]+":"+str(df[1]))
            df = cursor.fetchone()
        return self.food_dinner  

food_group = FoodGroup()
food_em = food_group.early_morning_food()
food_bf = food_group.break_fast_food()
food_mm = food_group.mid_morning_food()
food_ln = food_group.lunch_food()
food_eve = food_group.evening_food()
food_din = food_group.dinner_food()
