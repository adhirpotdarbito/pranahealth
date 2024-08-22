import csv
import sys
from __db_config import *



def insert_patient(dietitian_email, csv_file_name, db):
    input_file = csv.DictReader(open(csv_file_name))
    query = "SELECT id FROM users WHERE email='%s'"%(dietitian_email)
    cursor = db.cursor()
    cursor.execute(query)
    admin_id = cursor.fetchone()[0]
   
    for row in input_file:
        first_name = row.get("First Name").replace(" ","").title()
        last_name = row.get("Last Name","").replace(" ","").title()
        name = first_name + " " + last_name
        email = row.get("Email","").lower()
        if email == "":
            if last_name == "":
                email = first_name.lower() + '@pranacare.co.in'
            else:
                email = first_name.lower() + "." + last_name.lower() + '@pranacare.co.in'
        gender = row.get("Gender","").replace(" ", "").title()
        city = row.get("City").title()
        if city == "":
            city = "Pune"
        contact = row.get("Contact", "")
        password = row.get("Password","")
        if password == "":
            password = first_name.lower()+"@123"
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE email='%s'"%(email)
        if (cursor.execute(query)) == 1:
            query = "UPDATE users set name=%s, email=%s, password=%s, gender=%s, city=%s, country=%s, contact=%s, status=%s WHERE email=%s"
            cursor.execute(query,(name, email, password, gender, city, "India", contact, 2, email))
            print (name + " updated successfully.")
            db.commit()
        else:
            query = "INSERT INTO users(name, email, password, gender, city, country, contact, status) VALUES(%s, %s, %s, %s, %s, %s, %s,%s)"
            cursor.execute(query, (name,email,password,gender,city,"India",contact, 2))
            db.commit() 
            print (name + " added successfully.")
            query = "SELECT id FROM users WHERE email='%s'"%(email)
            cursor.execute(query)
            user_id = cursor.fetchone()[0]
            query = "INSERT INTO admin_patient_mapping(patient_id, admin_id, patient_type) VALUES(%s,%s,%s)" 
            cursor.execute(query, (user_id,admin_id,"New Patient"))
            db.commit()
    


if __name__=="__main__":
    if len(sys.argv) < 3:
        print ("try:\npython __insert_patients.py <dietitian_mail> <csv_file_name>")
    else:
        try:
            dietitian_email = sys.argv[1]
            csv_file_name = sys.argv[2]
            init_db()
            db = get_db()
            insert_patient(dietitian_email, csv_file_name, db)
        except Exception as err:
            print (err)
            db.rollback()
        finally:
            close_db()
            
