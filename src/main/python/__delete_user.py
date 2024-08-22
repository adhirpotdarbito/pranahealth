from __db_config import *
import sys 


def delete_user(email, db): 
    cursor = db.cursor()
    query = "select id from users where email='%s'"%(email)
    cursor.execute(query)
    user_id = cursor.fetchone()[0] 
    try:
        query = "DELETE FROM user_body_param WHERE id=%d"%(user_id)
        cursor.execute(query)
        query = "DELETE FROM user_ls_habit WHERE id=%d"%(user_id)
        cursor.execute(query)
        query = "DELETE FROM user_cr_risk WHERE id=%d"%(user_id)
        cursor.execute(query)
        query = "DELETE FROM user_glucose_risk WHERE id=%d"%(user_id)
        cursor.execute(query)
        query = "DELETE FROM user_medical_reports WHERE user_id=%d"%(user_id)
        cursor.execute(query)
        query = "DELETE FROM user_family_history WHERE id=%d"%(user_id)
        cursor.execute(query)
        query = "DELETE FROM user_medical_data WHERE id=%d"%(user_id)
        cursor.execute(query)
        query = "DELETE FROM user_misc_data WHERE id=%d"%(user_id)
        cursor.execute(query)
        query = "DELETE FROM sessions WHERE user_id=%d"%(user_id)
        cursor.execute(query)
        query = "DELETE FROM user_food_plan_mapping WHERE user_id=%d"%(user_id)
        cursor.execute(query)
        query = "DELETE FROM user_risk_data WHERE user_id=%d"%(user_id)
        cursor.execute(query)
        query = "DELETE FROM user_keys WHERE id=%d"%(user_id)
        cursor.execute(query)
        query = "DELETE FROM user_tracking_ci WHERE user_id=%d"%(user_id)
        cursor.execute(query)
        query = "DELETE FROM user_tracking_cb WHERE user_id=%d"%(user_id)
        cursor.execute(query)
        query = "DELETE FROM users WHERE id=%d"%(user_id)
        cursor.execute(query)
        db.commit()
        print ("Deleted user with email: "+ email)
    except Exception as err:
        print (err)
        db.rollback()
    finally:
        db.close()
   

init_db()
db = get_db() 
if len(sys.argv) < 2:
    print ("try- \npython __user_delete.py <email>")
else:
    email = sys.argv[1]
    delete_user(email, db)
    
