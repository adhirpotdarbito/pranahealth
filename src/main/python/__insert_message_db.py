import json
import datetime
from __user_queue_data import *
from __message_queue import *
from __message import *
from __config import *
from __db_config import *

class InsertData(QueueData):
    """
        Class for Inserting Message Queue data to the mysql database
    """
    def __init__(self):
        super(InsertData, self).__init__()
        # initialize database
        init_db()
        global db
        db = get_db()
        db.ping(True)

    def callback(self, ch, method, properties, body):
        print (body)
        self.processingFunction(body) 

    def processingFunction(self, message_recieved):
        """
           Function to process message queue data and to store and update in the database tables.
        """
        data = {}
        message = {}
        message_recieved = json.loads(message_recieved)
        data["id"] = message_recieved.get("user_id")
        data["parameter_type"] = message_recieved.get("parameter_type")
        data["message"] = message_recieved.get("message")
        user_id = message_recieved.get("user_id")
        #admin_id = message_recieved.get("message", {}).get("adminId")
        admin_id = message_recieved.get("admin_id")

        try:
            db.ping(True)
        except:
            init_db()
            db = get_db()

        # create cursor object
        cursor = db.cursor()
        if message_recieved.get("parameter_type") == "User Misc Data":
            query_misc = json.loads(message_recieved.get("message", {}).get("miscData",{}))
            if query_misc.get("Summary_Setting") or query_misc.get("Trends_Setting"):
                return
            data["body_params"] = query_misc.get("Anthropometry", {})
            data["glucose"] = query_misc.get("BioChemical", {}).get("Diabetic_Profile", {})
            data["cardiac"] = query_misc.get("BioChemical", {}).get("Lipid_Profile", {})
            data["blood_pressure"] = query_misc.get("BioChemical", {}).get("Blood_Pressure", {})
            data["ls_habit"] = query_misc.get("Lifestyle", {})

            # insert body parameters data to user_body_param table from misc data recieved from queue
            try:
                bod = json.loads(message_recieved.get("message", {}).get("miscData",{})).get("Personal_History", {}).get("dob", {}).get("measure", 0)
                bod = int("".join(bod.split("-")))
            except Exception:
                bod = 0
            try:
                height = float(data.get("body_params",{}).get("body_measurements", {}).get("heightNew", 0))
            except Exception:
                height = 0
            try:
                weight = float(data.get("body_params",{}).get("body_measurements", {}).get("weight", 0).get("measure", 0))
            except Exception:
                weight = 0
            try:
                waist = float(data.get("body_params",{}).get("body_measurements", {}).get("waist").get("measure", 0))
            except Exception:
                waist = 0
            try:
                hip = float(data.get("body_params",{}).get("body_measurements", {}).get("hips").get("measure", 0))
            except Exception:
                hip = 0
            try:
                bmi = float(data.get("body_params",{}).get("body_measurements", {}).get("bmi", 0).get("measure", 0))
            except Exception:
                bmi = 0
            try:
                whr = float(data.get("body_params",{}).get("body_measurements", {}).get("whr", 0).get("measure", 0))
            except Exception:
                whr = 0
            try:
                whtr = float(data.get("body_params",{}).get("body_measurements", {}).get("whtr", 0).get("measure", 0))
            except Exception:
                whtr = 0
            try:
                ibw = float(data.get("body_params",{}).get("body_measurements", {}).get("ibw", 0).get("measure", 0))
            except Exception:
                ibw = 0
            #ideal_height = data.get("body_params",{}).get("body_measurements", {}).get("idealHeight", 0)
            query = "INSERT INTO user_body_param(id, height, weight, bod, waist, hip_size, bmi, waist_hip_ratio, waist_height_ratio, ideal_body_weight) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE bod=%s, height=%s, weight=%s, waist=%s, hip_size=%s, bmi=%s, waist_hip_ratio=%s, waist_height_ratio=%s, ideal_body_weight = %s"
            cursor.execute(query, (int(user_id), height, weight, bod, waist*2.54, hip*2.54, bmi, whr, whtr, ibw, bod, height, weight, waist*2.54, hip*2.54, bmi, whr, whtr, ibw))  #execute query from cursor object
            db.commit()  #commit to the database
            print("Updated body params")

            # insert cardiac data to user_cr_risk table from misc data recieved from queue
            try:
                tot_chol = int(data.get("cardiac").get("totalCholestrol", 0).get("measure", 0))
            except Exception:
                tot_chol = 0
            try:
                hdl_chol = int(data.get("cardiac").get("hdl", 0).get("measure", 0))
            except Exception:
                hdl_chol = 0
            try:
                ldl_chol = int(data.get("cardiac").get("ldl", 0).get("measure", 0))
            except Exception:
                ldl_chol = 0
            #trigly = int(data.get("cardiac").get("triglycerides", 0).get("measure", 0))
            try:
                non_hdl = int(data.get("cardiac").get("nonHdlCholestrol", 0).get("measure", 0))
            except Exception:
                non_hdl = 0
            try:
                bp_treated = data.get("cardiac").get("bpTreated", "").get("measure", "")
            except Exception:
                bp_treated = False
            if bp_treated == True:
                bp_treated = "Yes"
            else:
                bp_treated = "No"
            query = "INSERT INTO user_cr_risk(id, tc_mg_dl, hdl_mg_dl, bp_treated, non_hdl_cholesterol) VALUES(%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE tc_mg_dl=%s, hdl_mg_dl=%s,bp_treated=%s,non_hdl_cholesterol=%s"
            cursor.execute(query, (int(user_id), tot_chol, hdl_chol, bp_treated, non_hdl, tot_chol, hdl_chol, bp_treated, non_hdl)) #execute query from cursor object
            db.commit() #commit to the database
            print ("Updated Cardiac data")

            # insert blood pressure parameter to user_cr_risk table from misc data recieved from queue
            try:
                sbp = int(data.get("blood_pressure").get("systolicBloodPressure", 0).get("measure", 0))
            except Exception:
                sbp = 0
            try:
                dbp = int(data.get("blood_pressure").get("diastolicBloodPressure", 0).get("measure", 0))
            except Exception:
                dbp = 0
            query = "INSERT INTO user_cr_risk(id, sbp_mm_hg, dp_mm_hg) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE sbp_mm_hg=%s, dp_mm_hg=%s"
            cursor.execute(query, (int(user_id), sbp, dbp, sbp, dbp))  #execute query from cursor object 
            db.commit() # commit to the database
            # insert glucose data to user_glucose_Risk table from misc data recieved from queue
            try: 
                glucose_fast = int(data.get("glucose").get("bloodSugarFasting", 0).get("measure", 0))
            except Exception:
                glucose_fast = 0
            try:
                glucose_pp = int(data.get("glucose").get("bloodSugarPostLunch", 0).get("measure", 0))
            except Exception:
                glucose_pp = 0
            try:
                hba1c = float(data.get("glucose").get("glycosylated", 0).get("measure", 0))            
            except Exception:
                hba1c = 0
            try:
                mpg = int(data.get("glucose").get("meanPlasmaGlucose", 0).get("measure", 0))
            except Exception:
                mpg = 0
            try:
                insulin = float(data.get("glucose").get("insulinFasting", 0).get("measure", 0))
            except Exception:
                insulin = 0
            try: 
                sugar_treated = data.get("glucose").get("sugarTreated", "").get("measure", "")
            except Exception:
                sugar_treated = False 
            if sugar_treated == True:
                sugar_treated = "Yes"
            else:
                suger_treated = "No"
            query = "INSERT INTO user_glucose_risk(id, glucose_fasting, glucose_pp, hba1c, mpg, sugar_treated, fasting_insulin) VALUES(%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE glucose_fasting=%s,glucose_pp=%s, hba1c=%s, mpg=%s, sugar_treated=%s, fasting_insulin=%s"
            cursor.execute(query, (int(user_id), glucose_fast, glucose_pp, hba1c, mpg, sugar_treated, insulin, glucose_fast, glucose_pp, hba1c, mpg, sugar_treated, insulin)) #execute query from cursor object
            db.commit() #commit to the database
            print ("Updated glucose data")

            # insert lifestyle habits parameter to user_ls_habit from misc data recieved from queue
            try:
                smoker = data.get("ls_habit").get("smoking", None).get("options", None)
                if smoker == "yes":
                    smoker = "regular"
                else:
                    smoker = "n.a."
            except Exception:
                smoker = "n.a."

            try:
                alcohol = data.get("ls_habit").get("alchohol", None).get("options", None)
                if alcohol == "yes":
                    alcohol = "regular"
                else:
                    alcohol = "n.a."
            except Exception:
                alcohol = "n.a."

            try:
                stress = data.get("ls_habit").get("stress", None).get("options", None)
                if stress == "yes":
                    stress = "regular"
                else:
                    stress = "n.a."
            except Exception:
                stress = "n.a."

            #junk_food = data.get("ls_habit").get("junkFood", None).get("options", None)
            #if junk_food == "yes":
            #    junk_food = "regular"
            #else:
            #    junk_food = "n.a."

            junk_food = "n.a."

            try:
                exercise = data.get("ls_habit").get("exercise", None).get("options", None)
                if exercise == "yes":
                    exercise  = "regular"
                else:
                    exercise = "n.a."
            except Exception:
                exercise = "n.a."

            try:
                sleep = data.get("ls_habit").get("sleepHours", None).get("duration", None)
            except Exception:
                sleep = 0

            query = "INSERT INTO user_ls_habit(id, smoker, alcoholic, stress, junk_food_lover, regular_exercise, sleep_hrs) VALUES(%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE smoker=%s, alcoholic=%s, stress=%s, junk_food_lover=%s, regular_exercise=%s, sleep_hrs=%s"
            #execute query from cursor object and commit to the database
            cursor.execute(query, (int(user_id), smoker, alcohol, stress, junk_food, exercise, sleep, smoker, alcohol, stress, junk_food, exercise, sleep))
            db.commit()
            # Insert and Update user_history_data and user_data_update
            current_date = int(datetime.datetime.now().strftime("%Y%m%d"))
            try:
                self.updateData(current_date, user_id, admin_id, "User Body Parameters", "dob", dob)
                self.updateData(current_date, user_id, admin_id, "User Body Parameters", "height", height)
                self.updateData(current_date, user_id, admin_id, "User Body Parameters", "weight", weight)
                self.updateData(current_date, user_id, admin_id, "User Body Parameters", "waist", waist)
                self.updateData(current_date, user_id, admin_id, "User Body Parameters", "Hip Size", hip)
                self.updateData(current_date, user_id, admin_id, "User Body Parameters", "BMI", bmi)
                self.updateData(current_date, user_id, admin_id, "User Body Parameters", "Waist Hip Ratio", whr)
                self.updateData(current_date, user_id, admin_id, "User Body Parameters", "Waist Height Ratio", whtr)
                self.updateData(current_date, user_id, admin_id, "User Body Parameters", "Ideal Body Weight", ibw)
                self.updateData(current_date, user_id, admin_id, "User Cardiac Data", "tcMgDl", tot_chol)
                self.updateData(current_date, user_id, admin_id, "User Cardiac Data", "hdlMgDl", hdl_chol)
                self.updateData(current_date, user_id, admin_id, "User Cardiac Data", "non-hdl Cholesterol", non_hdl)
                self.updateData(current_date, user_id, admin_id, "User Cardiac Data", "sbpMmHg", sbp)
                self.updateData(current_date, user_id, admin_id, "User Cardiac Data", "dpMmHg", dbp)
                self.updateData(current_date, user_id, admin_id, "User Glucose Data", "glucoseFasting", glucose_fast)
                self.updateData(current_date, user_id, admin_id, "User Glucose Data", "glucosePp", glucose_pp)
                self.updateData(current_date, user_id, admin_id, "User Glucose Data", "hba1c", hba1c)
                self.updateData(current_date, user_id, admin_id, "User Glucose Data", "mpg", mpg)
            except Exception:
                pass
        
    def updateData(self, time_key, user_id, admin_id, parameter_type, parameter_name, parameter_value):
        # check if current parameter value equals to the table parameter value and current date equals table date for that parameter
        if parameter_value == self.getUserDataValue(user_id, admin_id, parameter_type, parameter_name)[0] and time_key == self.getUserDataValue(user_id, admin_id, parameter_type, parameter_name)[1]:
            return      
            #print ("Do not insert or update")
        else:
            if parameter_value not in  ["0", "0.0"]:  # check if parameter values is not empty
                if time_key == self.getUserDataValue(user_id, admin_id, parameter_type, parameter_name)[1]:  # check current date with parameter date from table
                    self.deleteuserHistoryData(user_id, admin_id, parameter_type, parameter_name, time_key)  # delete the previous from history table
                    self.updateUserHistory(time_key, user_id, admin_id, parameter_type, parameter_name, parameter_value) # insert latest in user history table 
                    self.updateUserData(time_key, user_id, admin_id, parameter_type, parameter_name, parameter_value)  # update latest in user data table
                else:  # insert and update to user history and user data table
                    self.updateUserHistory(time_key, user_id, admin_id, parameter_type, parameter_name, parameter_value)
                    self.updateUserData(time_key, user_id, admin_id, parameter_type, parameter_name, parameter_value)
                    

    def updateUserData(self, time_key, user_id, provider_id, parameter_type, parameter_name, parameter_value):
        cursor = db.cursor()
        query = "SELECT user_id, provider_id, parameter_type, parameter_name FROM user_data_update WHERE user_id=%s AND provider_id=%s AND parameter_type=%s AND parameter_name=%s"   
        get_data = cursor.execute(query, (int(user_id), int(provider_id), parameter_type, parameter_name))
        if get_data == 0:
            query = "INSERT INTO user_data_update(time_key, user_id, provider_id, parameter_type, parameter_name, parameter_value) VALUES(%s, %s, %s, %s, %s, %s)" 
            cursor.execute(query, (time_key, int(user_id), int(provider_id), parameter_type, parameter_name, str(parameter_value)))
            db.commit()
        else:
            query = "UPDATE user_data_update set time_key=%s, parameter_value=%s WHERE user_id=%s AND provider_id=%s AND parameter_type=%s AND parameter_name=%s" 
            cursor.execute(query, (time_key, str(parameter_value), int(user_id), int(provider_id), parameter_type, parameter_name))
            db.commit()

 
    def updateUserHistory(self, time_key, user_id, provider_id, parameter_type, parameter_name, parameter_value):
        cursor = db.cursor()
        query = "INSERT INTO user_history_data(time_key, user_id, provider_id, parameter_type, parameter_name, parameter_value) VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (time_key, int(user_id), int(provider_id), parameter_type, parameter_name, str(parameter_value)))
        db.commit()
    
    def deleteuserHistoryData(self, user_id, provider_id, parameter_type, parameter_name, date):
        cursor = db.cursor()
        query = "DELETE FROM user_history_data WHERE user_id=%s AND provider_id=%s AND Parameter_type=%s AND parameter_name=%s AND time_key=%s"
        cursor.execute(query, (int(user_id), int(provider_id), parameter_type, parameter_name, date))
        db.commit()

    def getUserDataValue(self, user_id, provider_id, parameter_type, parameter_name):
        try:
            cursor = db.cursor()
            query = "SELECT parameter_value, time_key from user_data_update WHERE user_id=%s AND provider_id=%s AND parameter_type=%s AND parameter_name=%s"
            cursor.execute(query,(int(user_id), int(provider_id), parameter_type, parameter_name))
            value = cursor.fetchone()
            return value[0], value[1]
        except Exception as err:
            return 0, 0    

    def consumeUserData(self):
        super(InsertData, self).consumeUserData() 
        try: 
            # call module name and message queue object from config file.
            module = __import__(getAtmanConfigParamValue("MESSAGE_QUEUE_FILE_NAME"))
            message_queue = getattr(module, getAtmanConfigParamValue("MESSAGE_QUEUE_CLASS"))()
            message_queue.connectServer()
            message_queue.createChannel()
            callback = self.callback
            message_queue.consumeData(callback, queue_name_db) 
        except Exception as err:
            print (err)
            print ("===========================================")


