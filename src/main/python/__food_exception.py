from __db_config import *

class FoodException():
    """
        A class for Food Exception
    """
    init_db()
    def __init__(self):
        self.db = get_db()
        self.exception_diabetes = []
        self.exception_hypertension = []
        self.exception_cardiac = []
        self.exception_obesity = []
        self.exception_renal = []
        self.rec_party_food = []
	self.eating_out_trick = []

    def food_exception_diab(self):
        """
            Function return list of food items restricted for diabetes.
        """
        cursor = self.db.cursor()
        query = "select f2.food_name from food_item as f2 inner join food_exception_food_item as f1 on f1.fdit_id = f2.fdit_id where fexp_id = (select fexp_id from food_exception where exception_name='Diabetes')"
        cursor.execute(query)
        exp_dia = cursor.fetchone()
        while exp_dia is not None:
            self.exception_diabetes.append(exp_dia[0])
            exp_dia = cursor.fetchone()
        return self.exception_diabetes

    def food_exception_htn(self):
        """
          Function return list of food items restricted for hypertension.
        """
        cursor = self.db.cursor()
        query = "select f2.food_name from food_item as f2 inner join food_exception_food_item as f1 on f1.fdit_id = f2.fdit_id where fexp_id = (select fexp_id from food_exception where exception_name='Hypertension')"
        cursor.execute(query)
        exp_htn = cursor.fetchone()
        while exp_htn is not None:
            self.exception_hypertension.append(exp_htn[0])
            exp_htn = cursor.fetchone()
        return self.exception_hypertension

    def food_exception_cardiac(self):
        """
            Function return list of food items restricted for cardiac.
        """
        cursor = self.db.cursor()
        query = "select f2.food_name from food_item as f2 inner join food_exception_food_item as f1 on f1.fdit_id = f2.fdit_id where fexp_id = (select fexp_id from food_exception where exception_name='Cardiac')"
        cursor.execute(query)
        exp_crd = cursor.fetchone()
        while exp_crd is not None:
            self.exception_cardiac.append(exp_crd[0])
            exp_crd = cursor.fetchone()
        return self.exception_cardiac

    def food_exception_obese(self):
        """
            Function return list of food items restricted for obesity.
        """
        cursor = self.db.cursor()
        query = "select f2.food_name from food_item as f2 inner join food_exception_food_item as f1 on f1.fdit_id = f2.fdit_id where fexp_id = (select fexp_id from food_exception where exception_name='Obesity')"
        cursor.execute(query)
        exp_obs = cursor.fetchone()
        while exp_obs is not None:
            self.exception_obesity.append(exp_obs[0])
            exp_obs = cursor.fetchone()
        return self.exception_obesity

    def food_exception_renal(self):
        """
            Function return list of food items restricted for renal.
        """
        cursor = self.db.cursor()
        query = "select f2.food_name from food_item as f2 inner join food_exception_food_item as f1 on f1.fdit_id = f2.fdit_id where fexp_id = (select fexp_id from food_exception where exception_name='Renal')"
        cursor.execute(query)
        exp_ren = cursor.fetchone()
        while exp_ren is not None:
            self.exception_renal.append(exp_ren[0])
            exp_ren = cursor.fetchone()
        return self.exception_renal

    def party_food(self):
        """
            Function returns list of restaurant foods.
        """
        cursor = self.db.cursor()
        query = "select f2.food_name from food_item as f2 inner join restaurant_food_item as f1 on f1.food_item_id = f2.fdit_id;"
        cursor.execute(query)
        em = cursor.fetchone()
        while em is not None:
            self.rec_party_food.append(em[0])
            em = cursor.fetchone()
        return self.rec_party_food

    def food_eating_out(self):
        """
	    Function returns list of tricks eating out
        """
	cursor = self.db.cursor()
	query = "select id, tricks_eating from foods_eating_out_trick"
	cursor.execute(query)
	eat_out = cursor.fetchone()
	while eat_out is not None:
	    self.eating_out_trick.append(eat_out[1])
	    eat_out = cursor.fetchone()
	return self.eating_out_trick


food_exception = FoodException()
food_exp_dia = food_exception.food_exception_diab()
food_exp_htn = food_exception.food_exception_htn()
food_exp_car = food_exception.food_exception_cardiac()
food_exp_obs = food_exception.food_exception_obese()
food_exp_ren = food_exception.food_exception_renal()
recommended_party_food = food_exception.party_food()
tricks_eating_out = food_exception.food_eating_out()
