import csv
from __db_config import *


def insert_dietician():
    with open('dietician_data.csv','rt') as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            name=row[0]
            email=row[1]
            password=row[2]
            gender=row[3]
            city=row[4] 
            contact=row[5] 
            cursor = db.cursor()
            query ="SELECT * FROM users WHERE email='%s'"%(email);
            get_data = cursor.execute(query)
            if int(get_data) == 0:
                cursor = db.cursor()
                query = "INSERT INTO users(name, email, password, gender, contact, city, country, role, status, accepted_tc) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (name,email,password,gender,contact,city,"India","DIETITION_ACL",1,1))
                print ("dietician added")
            else:
                print("user already present")
    db.commit()
                
init_db()
db = get_db()
try:
    insert_dietician()
    close_db()
except Exception as err:
    print err
    db.rollback()
    close_db()
