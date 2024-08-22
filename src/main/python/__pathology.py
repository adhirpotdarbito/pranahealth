'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

import sys

# directory for holding pathology tests per disease
pathology_tests = {}

def get_path_tests_for_disease(db,disease_name):
    # open the cursor obj
    cursor = db.cursor()
    try:
        tests = []
        query_str = ("select d_id from disease where name='%s'" %disease_name)
        cursor.execute(query_str)
        d_id = cursor.fetchone()
        query_str = "select tests from path_test where d_id=%s" %d_id
        cursor.execute(query_str)
        path_test = cursor.fetchone()
        tests.append(path_test[0])
        pathology_tests[disease_name] = tests
    except Exception as err:
        print (Exception, err)
        print("Unexpected error: preparation_path_test_details", sys.exc_info()[0])
        cursor.close()
        db.close()
        return -1

    cursor.close()
    return 0

def get_path_tests_per_disease(disease_name):
    return pathology_tests[disease_name]
