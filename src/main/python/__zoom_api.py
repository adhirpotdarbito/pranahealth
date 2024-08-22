'''
  
    Copyright (C) 2018-2020 Isana Systems India Private Limited

    This source code is owned and maintained by Isana Systems India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of Isana Systems India Private Limited.

'''

import sys
import json
import logging
import requests
import base64
import random
import string
from __db_config import *

confidential_data = ""
query = ""
meeting_metadata = ""
m_query = ""
m_query_update = ""

def getZoomApiConfigJson():
    with open("/opt/atman/config/pranacare_zoom_api_call_config.json", "rb") as json_file:
        config_json = json.load(json_file)
    return config_json

def getZoomClientId(config_json):
    client_id = config_json.get("client_id", "")
    return client_id
      
def getZoomClientSecret(config_json):
    client_secret = config_json.get("client_secret", "")
    return client_secret
      
def getZoomDevRedirectUrl(config_json):
    dev_redirect_url = config_json.get("dev_redirect_url", "")
    return dev_redirect_url
      
def getZoomProdRedirectUrl(config_json):
    prod_redirect_url = config_json.get("prod_redirect_url", "")
    return prod_redirect_url
      
def getZoomApiHeader(config_json, bearer=0):
    if bearer == 0:
        api_header = config_json.get("api_header", "")
    else:
        api_header = config_json.get("api_header_bearer", "")
    return api_header
      
def getZoomAccessTokenUrl(config_json):
    access_token_url = config_json.get("access_token_url", "")
    return access_token_url
      
def getZoomRefreshTokenUrl(config_json):
    access_token_url = config_json.get("refresh_token_url", "")
    return access_token_url
      
def getZoomProfileUrl(config_json):
    profile_url = config_json.get("profile_url", "")
    return profile_url
      
def getZoomScheduleMeetingUrl(config_json):
    schedule_meeting_url = config_json.get("schedule_meeting_url", "")
    return schedule_meeting_url
      
def getZoomMeetingSchedulePayload(config_json):
    meeting_schedule_payload = config_json.get("meeting_schedule_payload", "")
    return meeting_schedule_payload
      
def getZoomDeleteMeetingUrl(config_json):
    delete_meeting_url = config_json.get("delete_meeting_url", "")
    return delete_meeting_url
      
def getZoomAuthorizeUrl(config_json):
    authorize_url = config_json.get("authorize_url", "")
    return authorize_url

def getConfidentialDataJson(config_json):
    confidential_data_json = config_json.get("confidential_data", "")
    return confidential_data_json

def getMeetingDataJson(config_json):
    meeting_data_json = config_json.get("meeting_data", "")
    return meeting_data_json

def getConfidentialDataUpdateQuery(config_json):
    confidential_data_update_query = config_json.get("update_confidential_data", "")
    return confidential_data_update_query

def getProfileDataUpdateQuery(config_json):
    profile_data_update_query = config_json.get("update_profile_data", "")
    return profile_data_update_query
    
def getMeetingUrlUpdateQuery(config_json):
    meeting_url_update_query = config_json.get("update_meeting_url", "")
    return meeting_url_update_query
    
def getMeetingDataUpdateQuery(config_json):
    meeting_data_update_query = config_json.get("update_meeting_data", "")
    return meeting_data_update_query
    
def getMeetingDataQuery(config_json):
    meeting_data_query = config_json.get("query_meeting_data", "")
    return meeting_data_query
    
def getBase64ClientIdSecret(config_json):
    base64_output = ""
    try:
        client_id = getZoomClientId(config_json)
        #print client_id
        client_secret = getZoomClientSecret(config_json)
        #print client_secret
        base64_input = client_id + ":" + client_secret
        #print base64_input
        encodedBytes = base64.b64encode(base64_input.encode("utf-8"))
        #print encodedBytes
        #base64_output = str(encodedBytes, "utf-8")
        base64_output = str(encodedBytes)
        #print base64_output
    except Exception as e:
        #print ("Error in zoom api access token retrieval -" + str(e))
        base64_output = ""

    return base64_output

def getZoomAccessToken(auth_code):
    access_token = ""
    refresh_token = ""
    try:
        #print ("Parsing the josn file.")
        config_json = getZoomApiConfigJson()
        #print ("Parsed the josn file.")
        #print config_json

        global confidential_data
        confidential_data = getConfidentialDataJson(config_json)
        global query
        query = getConfidentialDataUpdateQuery(config_json)

        base64_client_id_secret = getBase64ClientIdSecret(config_json)
        api_header = getZoomApiHeader(config_json)
        #print api_header
        _api_header = api_header%(base64_client_id_secret)
        #print _api_header
        api_header_json = json.loads(_api_header)
        print api_header_json
        prod_redirect_url = getZoomProdRedirectUrl(config_json)
        #print prod_redirect_url
        access_token_url = getZoomAccessTokenUrl(config_json)
        #print access_token_url
        _access_token_url = access_token_url%(auth_code, prod_redirect_url)
        print _access_token_url

        response = requests.post(_access_token_url, headers=api_header_json)
        #print requests.Response()
        #print response
        if response.status_code == 200:
            logging.info("Access token retrived successfully")
            print ("Access token retrived successfully - status code: " + str(response.status_code))
            #print ("Access Token data: ")
            #print response.content
            #print response.text
            api_output = response.json()
            print api_output
            access_token = api_output.get("access_token", "")
            refresh_token = api_output.get("refresh_token", "")
        else:
            logging.info("Error while retrieving access token - " + str(response.status_code))
            print ("Error while retrieving access token - " + str(response.status_code))
            print response.content
            access_token = ""
            refresh_token = ""

    except Exception as e:
        print ("Error in zoom api access token retrieval -" + str(e))
        access_token = ""
        refresh_token = ""

    return access_token, refresh_token

def refreshZoomAccessToken(cur_refresh_token):
    access_token = ""
    refresh_token = ""
    try:
        #print ("Parsing the josn file.")
        config_json = getZoomApiConfigJson()
        #print ("Parsed the josn file.")
        #print config_json

        global confidential_data
        confidential_data = getConfidentialDataJson(config_json)
        global query
        query = getConfidentialDataUpdateQuery(config_json)

        base64_client_id_secret = getBase64ClientIdSecret(config_json)
        api_header = getZoomApiHeader(config_json)
        #print api_header
        _api_header = api_header%(base64_client_id_secret)
        #print _api_header
        api_header_json = json.loads(_api_header)
        print api_header_json
        prod_redirect_url = getZoomProdRedirectUrl(config_json)
        #print prod_redirect_url
        refresh_token_url = getZoomRefreshTokenUrl(config_json)
        #print refresh_token_url
        _refresh_token_url = refresh_token_url%(cur_refresh_token)
        print _refresh_token_url

        response = requests.post(_refresh_token_url, headers=api_header_json)
        #print requests.Response()
        #print response
        if response.status_code == 200:
            logging.info("Access token refreshed successfully")
            print ("Access token refreshed successfully - status code: " + str(response.status_code))
            #print ("Access Token data: ")
            #print response.content
            #print response.text
            api_output = response.json()
            print api_output
            access_token = api_output.get("access_token", "")
            refresh_token = api_output.get("refresh_token", "")
        else:
            logging.info("Error while refreshing access token - " + str(response.status_code))
            print ("Error while refreshing access token - " + str(response.status_code))
            print response.content
            access_token = ""
            refresh_token = ""

    except Exception as e:
        print ("Error in zoom api access token refresh -" + str(e))
        access_token = ""
        refresh_token = ""

    return access_token, refresh_token

def getProfile(access_token):
    profile_data = ""
    try:
        #print ("Parsing the josn file.")
        config_json = getZoomApiConfigJson()
        #print ("Parsed the josn file.")
        #print config_json

        global query
        query = getProfileDataUpdateQuery(config_json)

        api_header = getZoomApiHeader(config_json, 1)
        #print api_header
        _api_header = api_header%(access_token)
        #print _api_header
        api_header_json = json.loads(_api_header)
        print api_header_json
        prod_redirect_url = getZoomProdRedirectUrl(config_json)
        #print prod_redirect_url
        profile_url = getZoomProfileUrl(config_json)
        print profile_url

        response = requests.get(profile_url, headers=api_header_json)
        #print requests.Response()
        #print response
        if response.status_code == 200:
            logging.info("Profile retrieved successfully")
            print ("Profile retrieved successfully - status code: " + str(response.status_code))
            #print ("Proflile data: ")
            #print response.content
            #print response.text
            profile_data = response.json()
        else:
            logging.info("Error while retrieving profile - " + str(response.status_code))
            print ("Error while retrieving profile - " + str(response.status_code))
            print response.content
            profile_data = ""

    except Exception as e:
        print ("Error in zoom api profile retrieval -" + str(e))
        profile_data = ""

    return profile_data

def scheduleMeeting(access_token, topic, start_time, duration, agenda, password):
    meeting_url = ""
    meeting_id = ""
    try:
        #print ("Parsing the josn file.")
        config_json = getZoomApiConfigJson()
        #print ("Parsed the josn file.")
        #print config_json

        global meeting_metadata
        meeting_metadata = getMeetingDataJson(config_json)
        global query
        query = getMeetingUrlUpdateQuery(config_json)
        global m_query_update
        m_query_update = getMeetingDataUpdateQuery(config_json)
        global m_query
        m_query = getMeetingDataQuery(config_json)

        api_header = getZoomApiHeader(config_json, 1)
        #print api_header
        _api_header = api_header%(access_token)
        #print _api_header
        api_header_json = json.loads(_api_header)
        print api_header_json
        prod_redirect_url = getZoomProdRedirectUrl(config_json)
        #print prod_redirect_url
        schedule_meeting_url = getZoomScheduleMeetingUrl(config_json)
        print schedule_meeting_url
        _schedule_meeting_url = schedule_meeting_url%("me")
        print _schedule_meeting_url
        api_payload = getZoomMeetingSchedulePayload(config_json)
        _api_payload = api_payload%(topic, start_time, duration, agenda, password)
        print _api_payload
        #api_payload_json = json.loads(_api_payload)
        #print api_payload_json

        response = requests.post(_schedule_meeting_url, headers=api_header_json, data=_api_payload)
        #response = requests.post(_schedule_meeting_url, headers=api_header_json, data=api_payload_json)
        #print requests.Response()
        #print response
        if response.status_code == 201:
            logging.info("Meeting scheduled successfully")
            print ("Meeting scheduled successfully - status code: " + str(response.status_code))
            #print ("Meeting data: ")
            #print response.content
            #print response.text
            meeting_data = response.json()
            meeting_url = meeting_data.get("join_url", "")
            meeting_id = meeting_data.get("id", "")
        else:
            logging.info("Error while scheduling meeting - " + str(response.status_code))
            print ("Error while scheduling meeting - " + str(response.status_code))
            print response.content
            meeting_url = ""
            meeting_id = ""

    except Exception as e:
        print ("Error in zoom api meeting scheduling -" + str(e))
        meeting_url = ""
        meeting_id = ""

    return meeting_url, meeting_id

def deleteMeeting(access_token, meeting_id):
    deletion_status = ""
    try:
        #print ("Parsing the josn file.")
        config_json = getZoomApiConfigJson()
        #print ("Parsed the josn file.")
        #print config_json

        api_header = getZoomApiHeader(config_json, 1)
        #print api_header
        _api_header = api_header%(access_token)
        #print _api_header
        api_header_json = json.loads(_api_header)
        print api_header_json
        prod_redirect_url = getZoomProdRedirectUrl(config_json)
        #print prod_redirect_url
        delete_meeting_url = getZoomDeleteMeetingUrl(config_json)
        print delete_meeting_url
        _delete_meeting_url = delete_meeting_url%(meeting_id)
        print _delete_meeting_url

        response = requests.delete(_delete_meeting_url, headers=api_header_json)
        #print requests.Response()
        #print response
        if response.status_code == 204:
            logging.info("Meeting deletion successfully")
            print ("Meeting deleted successfully - status code: " + str(response.status_code))
            #print ("Meeting data: ")
            #print response.content
            print response.text
            deletion_status = "Success"
        else:
            logging.info("Error while deleting meeting - " + str(response.status_code))
            print ("Error while deleting meeting - " + str(response.status_code))
            print response.content
            deletion_status = "Failed"

    except Exception as e:
        print ("Error in zoom api meeting scheduling -" + str(e))
        deletion_status = "Failed"

    return deletion_status

def loadMeetingUrl(admin_id, appointment_id, meeting_id, meeting_url):

    try:
        init_db()
        db = get_db()
        cursor = db.cursor()

        global query
        _query = query%(meeting_url, appointment_id)
        #print _query

        cursor.execute(_query)

        global meeting_metadata
        global m_query
        global m_query_update

        _mquery = m_query%(admin_id)
        cursor.execute(_mquery)
        current_meetings = cursor.fetchone()
        current_mmeting_data = current_meetings[0]
        current_mmeting_data_dict = {}
        if current_mmeting_data == None or current_mmeting_data == "NULL":
            current_mmeting_data_dict[meeting_url] = meeting_id
        else:
            current_mmeting_data_dict = json.loads(current_mmeting_data)
            current_mmeting_data_dict[meeting_url] = meeting_id

        meeting_metadata = json.dumps(current_mmeting_data_dict)    

        _m_query_update = m_query_update%(meeting_metadata, admin_id)
        #print _m_query_update
        cursor.execute(_m_query_update)

        db.commit()
        close_db()
    except Exception as err:
        print err
        db.rollback()
        close_db()

def loadProfileData(admin_id, profile_data):

    try:
        init_db()
        db = get_db()
        cursor = db.cursor()

        global query
        _query = query%(json.dumps(profile_data), admin_id)
        #print _query

        cursor.execute(_query)
        db.commit()
        close_db()
    except Exception as err:
        print err
        db.rollback()
        close_db()

def loadConfidentialData(admin_id, access_token, refresh_token):
    
    try:
        init_db()
        db = get_db()
        cursor = db.cursor()

        global confidential_data
        global query
        #print confidential_data
        _confidential_data = confidential_data%(access_token, refresh_token) 
        #print _confidential_data
        _query = query%(_confidential_data, admin_id)
        #print _query

        cursor.execute(_query)
        db.commit()
        close_db()
    except Exception as err:
        print err
        db.rollback()
        close_db()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print ("python __zoom_api.py <opcode> <auth_code>|<refresh_token>|<access_token>|<user_id>")
    else:
        opcode = sys.argv[1] 
        if opcode == "access_token":
            auth_code = sys.argv[2]
            access_token, refresh_token = getZoomAccessToken(auth_code)
            print ("Access Token: " + access_token)
            print ("Refresh Token: " + refresh_token)
            if len(sys.argv) == 4:
                admin_id = sys.argv[3]
                loadConfidentialData(admin_id, access_token, refresh_token)
        elif opcode == "refresh_token":
            cur_refresh_token = sys.argv[2]
            access_token, refresh_token = refreshZoomAccessToken(cur_refresh_token)
            print ("Access Token: " + access_token)
            print ("Refresh Token: " + refresh_token)
            if len(sys.argv) == 4:
                admin_id = sys.argv[3]
                loadConfidentialData(admin_id, access_token, refresh_token)
        elif opcode == "profile":
            access_token = sys.argv[2]
            profile_data = getProfile(access_token)
            print ("Profile Data: " + str(profile_data))
            if len(sys.argv) == 4:
                admin_id = sys.argv[3]
                loadProfileData(admin_id, profile_data)
        elif opcode == "schedule_meeting":
            access_token = sys.argv[2]
            topic = "Consultation Appointment"
            #start_time = "2020-05-29T12:00:00"
            #duration = "30"
            start_time = sys.argv[3]
            duration = sys.argv[4]
            agenda = "Consultation"
            password = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(9))
            meeting_url, meeting_id = scheduleMeeting(access_token, topic, start_time, duration, agenda, password) 
            print ("Meeting URL: " + meeting_url)
            print ("Meeting Id: " + str(meeting_id))
            admin_id = sys.argv[5]
            appointment_id = sys.argv[6]
            loadMeetingUrl(admin_id, appointment_id, str(meeting_id), meeting_url)
        elif opcode == "delete_meeting":
            access_token = sys.argv[2]
            meeting_id = sys.argv[3]
            status = deleteMeeting(access_token, meeting_id)
            print ("Meeting Deletion Status: " + status)
