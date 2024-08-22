import os
import csv
from __db_config import *

def insertAdminProfile(db):
    with open('/opt/atman/bin/admin_profile.csv','rt') as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            admin_id = row[0]
            try:
                os.system("sudo /bin/cp " + row[5] + " /var/lib/mysql-files/")
                profile_picture = os.path.basename(row[5])
            except Exception:
                profile_picture = "NULL"
            profile_picture_filename = row[10]
            city = row[6]
            cursor = db.cursor()
            query = "select admin_id from admin_profile WHERE admin_id=%d"%int(admin_id)
            get_query = cursor.execute(query)
            if get_query == 0:
                query = "INSERT INTO admin_profile(admin_id, city, profile_picture, profile_picture_filename) VALUES(%s,%s,LOAD_FILE(%s),%s)"
                cursor.execute(query, (int(admin_id), str(city), '/var/lib/mysql-files/' + profile_picture, str(profile_picture_filename)))
                print("Profile Picture Inserted")
            else:
                query = "UPDATE admin_profile set profile_picture=LOAD_FILE(%s), profile_picture_filename=%s WHERE admin_id=%s"
                cursor.execute(query, ('/var/lib/mysql-files/' + profile_picture, str(profile_picture_filename), int(admin_id)))
                print("Profile Picture Updated")
            db.commit()
            cursor.close()
            db.close()
            os.system("sudo /bin/rm /var/lib/mysql-files/" + profile_picture)


init_db()
db = get_db()
insertAdminProfile(db)
