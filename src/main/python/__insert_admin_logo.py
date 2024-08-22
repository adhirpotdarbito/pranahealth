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
                os.system("sudo /bin/cp "+row[8]+" /var/lib/mysql-files/")
                large_logo = os.path.basename(row[8])
            except Exception:
                large_logo = "NULL"
            large_logo_filename = row[11]
            city = row[6]
            cursor = db.cursor()
            query = "select admin_id from admin_profile WHERE admin_id=%d"%int(admin_id)
            get_query = cursor.execute(query)
            if get_query == 0:
                query = "INSERT INTO admin_profile(admin_id, city, large_logo, large_logo_filename) VALUES(%s,%s,LOAD_FILE(%s),%s)"
                cursor.execute(query,(int(admin_id),str(city),'/var/lib/mysql-files/'+large_logo, str(large_logo_filename)))
                print("Logo Inserted")

            else:
                query = "UPDATE admin_profile set large_logo=LOAD_FILE(%s), large_logo_filename=%s WHERE admin_id=%s"
                cursor.execute(query,('/var/lib/mysql-files/'+large_logo, str(large_logo_filename), int(admin_id)))
                print("Logo Updated")
            db.commit()
            cursor.close()
            db.close()
            os.system("sudo /bin/rm /var/lib/mysql-files/"+large_logo)


init_db()
db = get_db()
insertAdminProfile(db)
