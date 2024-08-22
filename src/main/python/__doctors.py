'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

import sys
from __users import *

# doctor[disease] --> all doctor details specialization on disease
doctors = {}

# doctors = {} key/value pair
# you can access all the doctors for disease X
# doctor[X]
def prepare_doctor_details_per_disease(db,disease_name):
    # open cursor object
    cursor = db.cursor()
    try:
        query_str = "select d_cat from disease where name='%s'" %disease_name
        cursor.execute(query_str)
        d_cat = cursor.fetchone()
        query_str = "select id,name,address,phone,rating from doctors where d_cat=%d" %d_cat[0]
        query_str = query_str + " and city='%s'" %get_user_city()
        cursor.execute(query_str)
        doc = cursor.fetchone()
        doctor = []
        while doc is not None:
            doctor.append(doc)
            doc = cursor.fetchone()
        # list of all doctors who has the speciality for disease
        doctors[disease_name] = doctor
    except Exception as err:
        print (Exception, err)
        print("Unexpected error: prepare_doctor_details", sys.exc_info()[0])
        cursor.close()
        return (-1)
    # close cursor object
    cursor.close()
    return 0

def get_doctor_list_for_disease(disease_name):
    return doctors[disease_name]
