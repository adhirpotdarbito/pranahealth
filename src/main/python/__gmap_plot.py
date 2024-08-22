'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

import sys
import gmplot
import psycopg2
from __doctors import *

# latitute/longitude list
# TBD we may get lat long from address using google API
lat_list = []
long_list = []

def get_doc_location(db, doctor):
    doc_lat_long = []

    cursor = db.cursor()
    try:
        query_str = ("select latitude,longitude from lat_long where doc_id=%s" %str(doctor[0]))
        cursor.execute(query_str)
        lat_long = cursor.fetchall()
        for i in range(len(lat_long)):
            doc_lat_long.append(lat_long[i][0])
            doc_lat_long.append(lat_long[i][1])
    except Exception as err:
        print (Exception, err)
        print ("Unexpected error: prepare_doc_location_for_disease" , sys.exc_info()[0])

    cursor.close()
    return doc_lat_long

def prepare_doc_location_for_disease(db,disease_name):
    cursor = db.cursor()
    # get the list of doctors for disease_name
    doctor_list = get_doctor_list_for_disease(disease_name)
    doc_idx = 0
    while doc_idx <len(doctor_list):
        # get doctor entry
        doctor_entry = doctor_list[doc_idx]
        try:
            query_str = ("select latitude,longitude from lat_long where doc_id=%s" %str(doctor_entry[0]))
            cursor.execute(query_str)
            latitude = []
            longitude = []
            lat_long = cursor.fetchall()
            # Transform the the fetched latitude and longitude data into two separate lists
            for i in range(len(lat_long)):
                latitude.append(lat_long[i][0])
                longitude.append(lat_long[i][1])
            lat_list.append(latitude)
            long_list.append(longitude)
        except Exception as err:
            print (Exception, err)
            print ("Unexpected error: prepare_doc_location_for_disease" , sys.exc_info()[0])
            cursor.close()
            return(-1)

        # go to next doctor in list
        doc_idx = doc_idx +1
    cursor.close()
    return 0

def plot_doctors_loc_gmap():
    # init gmplot
    if (len(lat_list) > 0):
        latitude = lat_list[0]
        longitude = long_list[0]
        gmap = gmplot.GoogleMapPlotter(latitude[0],longitude[0],13)
    else:
        return

    pos = 0
    while (pos < len(lat_list)):
        latitude = lat_list[pos]
        longitude = long_list[pos]
        gmap.marker(float(latitude[0]),float(longitude[0]) , 'cornflowerblue')
        pos = pos +1
    gmap.draw('doc_locations.html')

def get_lat_list_doctors():
    return lat_list

def get_long_list_doctors():
    return long_list
