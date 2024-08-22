'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

import MySQLdb
from __config import *
# global database obj
db = None

# Object to hold all the constant values
class _Const(object):

    PRANA_CARE_DATA_DB_NAME = getAtmanConfigParamValue('PRANA_CARE_DATA_DB_NAME')
    PRANA_CARE_DATA_DB_USER_NAME = getAtmanConfigParamValue('PRANA_CARE_DATA_DB_USER_NAME')
    PRANA_CARE_DATA_DB_USER_PASSWD = getAtmanConfigParamValue('PRANA_CARE_DATA_DB_USER_PASSWD')

def init_db():
    global db
    CONST = _Const()
    try:
        db = MySQLdb.connect("localhost", CONST.PRANA_CARE_DATA_DB_USER_NAME, CONST.PRANA_CARE_DATA_DB_USER_PASSWD, CONST.PRANA_CARE_DATA_DB_NAME)
    except Exception as err:
        print (Exception, err)
        print "Unable to connect pranacare DB."
        exit(-1)

def get_db():
    global db
    return db;

def close_db():
    global db
    db.close()
