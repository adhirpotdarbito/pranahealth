import csv
from __db_config import *

def insert_custom_config(admin_id, meeting_type, meeting_config_file):
    with open(meeting_config_file,'rt') as f:
        meeting_credentials = json.load(f)

        cursor = db.cursor()
        query = "INSERT INTO admin_online_meeting_config(admin_id, meeting_type, meeting_credentials) VALUES(%s, %s, %s)"
        cursor.execute(query, (int(admin_id), meeting_type, json.dumps(meeting_credentials)))
        db.commit()
                
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print ("python insert_meeting_config.py <admin_id> <meeting_type> <meeting_config_file>")
    else:
        admin_id = sys.argv[1]
        meeting_type = sys.argv[2]
        meeting_config_file = sys.argv[3]
        init_db()
        db = get_db()
        try:
            insert_custom_config(admin_id, meeting_type, meeting_config_file)
            close_db()
        except Exception as err:
            print err
            db.rollback()
            close_db()
