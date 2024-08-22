import sys
from __db_config import * 

gender = ""
height = 0
weight = 0
waist = 0 
bmi_user = 0
whtr_user = 0
ibw_user = 0
ideal_height_user = 0
total_num_user = []
body_param_details = []

def numUsers(db):
    cursor = db.cursor()
    query = "SELECT id FROM user_body_param"
    cursor.execute(query)
    num_user = cursor.fetchone()
    if len(sys.argv) == 1:
        while num_user is not None:
            total_num_user.append(num_user[0])
            num_user = cursor.fetchone()
    else:
        total_num_user.append(int(sys.argv[1]))    
    return total_num_user

def get_body_param(db, user_id):
    try: 
        global gender, height, weight, waist, bmi_user, whtr_user, ideal_height_user, ibw_user
        cursor = db.cursor()
        query_1 = "SELECT gender, email FROM users WHERE id=%d"%int(user_id)
        query_2 = "SELECT height, weight, waist, bmi, waist_height_ratio, ideal_body_weight, ideal_height FROM user_body_param WHERE id=%d"%int(user_id)
        cursor.execute(query_2) 
        body_param = cursor.fetchall()
        cursor.execute(query_1)
        user_gender = cursor.fetchall()
        gender = user_gender[0][0]
        mail = user_gender[0][1]
        print "user mail: ",mail
        height = body_param[0][0]
        weight = body_param[0][1]
        waist = body_param[0][2]
        bmi_user = body_param[0][3]
        whtr_user = body_param[0][4]
        ibw_user = body_param[0][5]
        ideal_height_user = body_param[0][6]
    except Exception as err:
        print("user_id not found")
        exit()

def calculate_bmi(height, weight):
    return round((weight/height**2)*10000,2)

def calculate_ibw(height, gender):
    if gender == "Male":
        if height >= 152:    
            return round(50.0 + 2.3 * ((height/2.54) - 60))
        else:
            return round((height**2*1.65)/1000)
    else:
        if height >= 152:
            return round(45.5 + 2.3 * (height/2.54 - 60))
        else:
            return round((height**2*1.65)/1000)

def average_height(gender):
    if gender == "Male":
        return 165.1
    else:
        return 152.4
        
def cal_whtr(waist, height):
    return round(waist/height,2) 

def update_body_param(db):
    try:
        cursor = db.cursor()
        for user_id in total_num_user:
            get_body_param(db, user_id)
            bmi = calculate_bmi(height, weight)
            ibw = calculate_ibw(height, gender)
            whtr = cal_whtr(waist, height)
            avg_height = average_height(gender)
            if bmi_user == 0:
                query = "UPDATE user_body_param set bmi=%f WHERE id=%d"%(float(bmi), int(user_id))
                cursor.execute(query)  
                db.commit()
                print ("bmi updated: ", bmi)
            if whtr_user == 0:
                query = "UPDATE user_body_param set waist_height_ratio=%f WHERE id=%d"%(float(whtr), int(user_id))
                cursor.execute(query)  
                db.commit()
                print ("whtr updated: ", whtr)
            if ideal_height_user == 0:
                query = "UPDATE user_body_param set ideal_height=%f WHERE id=%d"%(float(avg_height), int(user_id))
                cursor.execute(query)  
                db.commit()
                print ("ideal height updated: ", avg_height)
            if ibw_user == 0:
                query = "UPDATE user_body_param set ideal_body_weight=%f WHERE id=%d"%(float(ibw), int(user_id))
                cursor.execute(query)  
                db.commit()
                print ("Ideal body weight updated: ", ibw)
            print (" ")
            print ("==========================================")
            print (" ")

    except Exception as err:
        db.rollback()
        print (err) 
    finally:
        cursor.close()
        db.close()
               

if __name__ == "__main__":
    init_db()
    db = get_db()
    numUsers(db)
    update_body_param(db)
