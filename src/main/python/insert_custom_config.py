import csv
from __db_config import *

def insert_custom_config(admin_id, admin_type, custom_config_file):
    with open(custom_config_file,'rt') as f:
        custom_config_data = json.load(f)

        cursor = db.cursor()
        query = "INSERT INTO admin_patient_custom_config(admin_id, type, custom_config_json) VALUES(%s, %s, %s)"
        cursor.execute(query, (int(admin_id), admin_type, json.dumps(custom_config_data)))
        db.commit()
                
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print ("python insert_custom_config.py <admin_id> <admin_type> <custom_config_file>")
    else:
        admin_id = sys.argv[1]
        admin_type = sys.argv[2]
        custom_config_file = sys.argv[3]
        init_db()
        db = get_db()
        try:
            insert_custom_config(admin_id, admin_type, custom_config_file)
            close_db()
        except Exception as err:
            print err
            db.rollback()
            close_db()
