import sys
from __config import *
from __db_config import *
from datetime import datetime, timedelta
    
def insertBookingDetails(db, dietitian_email, patient_email, start_time, end_time, duration, start_date, end_date, day):
    _start_date = datetime.strptime(start_date,"%Y%m%d")
    _end_date = datetime.strptime(end_date,"%Y%m%d")
    admin_id = getAdminId(db, dietitian_email)
    user_id = getPatientId(db, patient_email)
    _start_time = datetime.strptime(start_time[:2] + ":" + start_time[2:], '%H:%M')
    _end_time = datetime.strptime(end_time[:2] + ":" + end_time[2:], '%H:%M') 
    while _start_date < _end_date:
        if _start_date.strftime("%a").upper() == day:
            while _start_time < _end_time:
                try:
                    cursor = db.cursor()
                    query = "INSERT INTO patient_appointments(admin_id, patient_id, date, time_slot, status) VALUES(%s,%s,%s,%s,%s)"
                    cursor.execute(query, (int(admin_id), int(user_id), int(_start_date.strftime("%Y%m%d")), "".join(_start_time.time().strftime('%H:%M').split(":")), "booked"))
                except Exception as err:
                    print (err)
                    db.rollback()
                finally:
                    db.commit()
                    print ("Appointment Bookings Added For "+day)
                _start_time = _start_time + timedelta(minutes=int(duration))
            _start_time = datetime.strptime(start_time[:2] + ":" + start_time[2:], '%H:%M')
        _start_date = _start_date + timedelta(days=1)   
            

def getAdminId(db, dietitian_email):
    cursor = db.cursor()
    query = "select id from users where email='%s'"%(dietitian_email)
    cursor.execute(query)
    get_id = cursor.fetchone()
    adminId = get_id[0]
    return adminId

def getPatientId(db, patient_email):
    cursor = db.cursor()
    query = "select id from users where email='%s'"%(patient_email)
    cursor.execute(query)
    get_id = cursor.fetchone()
    patientId = get_id[0]
    return patientId

    
if __name__  == "__main__":
    init_db()
    db = get_db() 
    if len(sys.argv) < 9:
        print ("Arguments must be of length 9")
        print ("python __book_appointment.py <dietitian_email> <user_email> <start_time-HHMM> <end_time-HHMM> <duration-MM> <start_date-YYYYMMDD> <end_date-YYYYMMDD> <DAY- MON>")
    else:
        dietitian_email = sys.argv[1]
        patient_email = sys.argv[2]
        start_time = sys.argv[3]
        end_time = sys.argv[4]
        duration = sys.argv[5]
        start_date = sys.argv[6]
        end_date = sys.argv[7]
        day = sys.argv[8]
        insertBookingDetails(db, dietitian_email, patient_email, start_time, end_time, duration, start_date, end_date, day)

