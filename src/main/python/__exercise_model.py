from __db_config import *

class Exercise():
    """
	A class of Exercise
    """
    init_db()    
    def __init__(self):
        self.db = get_db()
        self.exercise_early_morning = []
        self.exercise_post_lunch = []
        self.exercise_post_dinner = []
        self.exercise_normal = []
        self.exercise_obese = []

    def exercises_early_morning(self):
        cursor = self.db.cursor()
        query = "select e1.exercise_name, e1.time_in_minutes,e1.calories_burned from exercise_list as e1 inner join exercise_group_exercise_name as e2 on e1.exc_id = e2.exc_id where grp_id=1"
        cursor.execute(query)
        em = cursor.fetchone()
        while em is not None:
            self.exercise_early_morning.append(em[1]+" " + em[0] + ":"  + em[2])
            em = cursor.fetchone()
        return self.exercise_early_morning

    def exercises_post_lunch(self):
        cursor = self.db.cursor()
        query = "select e1.exercise_name, e1.time_in_minutes,e1.calories_burned from exercise_list as e1 inner join exercise_group_exercise_name as e2 on e1.exc_id = e2.exc_id where grp_id=2"
        cursor.execute(query)
        em = cursor.fetchone()
        while em is not None:
            self.exercise_post_lunch.append(em[1]+" " + em[0] + ":" + em[2])
            em = cursor.fetchone()
        return self.exercise_post_lunch

    def exercises_post_dinner(self):
        cursor = self.db.cursor()
        query = "select e1.exercise_name, e1.time_in_minutes,e1.calories_burned from exercise_list as e1 inner join exercise_group_exercise_name as e2 on e1.exc_id = e2.exc_id where grp_id=3"
        cursor.execute(query)
        em = cursor.fetchone()
        while em is not None:
            self.exercise_post_dinner.append(em[1]+" " + em[0] + ":" + em[2])
            em = cursor.fetchone()
        return self.exercise_post_dinner

    def exercises_normal(self):
        cursor = self.db.cursor()
        query = "select e1.exercise_name, e1.time_in_minutes,e1.calories_burned from exercise_list as e1 inner join exercise_group_exercise_name as e2 on e1.exc_id = e2.exc_id where grp_id=4"
        cursor.execute(query)
        em = cursor.fetchone()
        while em is not None:
            self.exercise_normal.append(em[1]+" " + em[0] + ":" + em[2])
            em = cursor.fetchone()
        return self.exercise_normal

    def exercises_obese(self):
        cursor = self.db.cursor()
        query = "select e1.exercise_name, e1.time_in_minutes,e1.calories_burned from exercise_list as e1 inner join exercise_group_exercise_name as e2 on e1.exc_id = e2.exc_id where grp_id=5"
        cursor.execute(query)
        em = cursor.fetchone()
        while em is not None:
            self.exercise_obese.append(em[1]+" " + em[0] + ":" + em[2])
            em = cursor.fetchone()
        return self.exercise_obese


exercise = Exercise()
exercise_em_list = exercise.exercises_early_morning()
exercise_post_lunch_list = exercise.exercises_post_lunch()
exercise_post_dinner_list = exercise.exercises_post_dinner()
exercise_opt_normal_list = exercise.exercises_normal()
exercise_obese_list = exercise.exercises_obese()
