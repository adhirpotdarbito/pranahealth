import os
import csv
from __db_config import *

def insertAdminProfile(db):
    with open('/opt/atman/bin/admin_profile.csv', "rt") as f:
        data = csv.reader(f)
        next(data)
        for row in data: 
            admin_id = row[0]
            address = row[1]
            experience = row[2]
            specialties = row[3]
            profile_data = row[4]
            try:
                os.system("sudo /bin/cp "+row[5]+" /var/lib/mysql-files/")
                profile_picture = os.path.basename(row[5])
            except Exception:
                profile_picture = "NULL"
            city = row[6]
            country = row[7]
            clinic_details = row[9]
            profile_picture_filename = row[10]
            area = row[12]
            area_list = area.split(",")
            cursor = db.cursor()
            query =  "select admin_id from admin_profile WHERE admin_id=%d"%int(admin_id)
            get_query = cursor.execute(query)
            if get_query == 0:
                query = "INSERT INTO admin_profile(admin_id, address, experience, specialties, profile_data, profile_picture, city, country,clinic_details, profile_picture_filename, area) VALUES(%s,%s,%s,%s,%s,LOAD_FILE(%s),%s,%s,%s,%s,%s)"
                cursor.execute(query,(int(admin_id),str(address),str(experience),str(specialties),str(profile_data),'/var/lib/mysql-files/'+profile_picture,str(city), str(country),str(clinic_details), str(profile_picture_filename), str(area)))
                print("Profile data Inserted.")
                if area_list[0] not in  ["NULL", ""]: 
                    for areas in area_list: 
                        query = "INSERT INTO admin_areas(admin_id,country,city,area) VALUES(%s,%s,%s,%s)"
                        cursor.execute(query, (int(admin_id), str(country), str(city), str(areas)))
                        print(areas + "area inserted.")
            else:
                query = "UPDATE admin_profile set address=%s, experience=%s, specialties=%s, profile_data=%s, profile_picture=LOAD_FILE(%s), city=%s, country=%s,clinic_details=%s, profile_picture_filename=%s WHERE admin_id=%s"
                cursor.execute(query,(str(address),str(experience),str(specialties),str(profile_data),'/var/lib/mysql-files/'+profile_picture,str(city), str(country),str(clinic_details), str(profile_picture_filename), int(admin_id)))
                print ("Profile data Updated.")
            db.commit()
            cursor.close()           
            os.system("sudo /bin/rm /var/lib/mysql-files/"+profile_picture)



init_db()
db = get_db()
insertAdminProfile(db)
db.close()

