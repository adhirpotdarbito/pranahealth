from __db_config import *
from __config import *
import smtplib
import json
import csv
import os
import pickle
from datetime import datetime
from collections import OrderedDict
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
from apiclient import errors

diet_patient_map = OrderedDict()
diet_patient_result = []
SCOPES = ['https://www.googleapis.com/auth/drive']
DRIVE_FOLDER = getAtmanConfigParamValue("DIETITIAN_PATIENT_LIST_DRIVE_FOLDER")
file_name = getAtmanConfigParamValue("DIETITIAN_PATIENT_LIST_FILE_NAME")+"_" + datetime.now().strftime("%d-%m-%Y") + ".csv"
file_path = getAtmanConfigParamValue("PYTHON_SCRIPT_PATH")
fromaddr = email_name
toaddr = ["adhir.potdar@isanasystems.com"]
host = email_host
port = email_port
password = email_password


def get_patient_dietition(db, diet_patient_map):
    cursor = db.cursor()
    query = "select u.name as Dietitian, count(a.patient_id) as Num_Patients from users u, admin_patient_mapping a where u.role in ('DIETITION_ACL', 'DIETITION_MIN_ROLE') and u.id = a.admin_id and u.name not like '%isana%' and u.id not in (302, 240, 279, 307, 576, 536, 1771, 1770, 1175, 1232, 2130, 1868) and u.name not like 'Adhir%' group by u.name order by Num_Patients desc"
    cursor.execute(query)
    get_data =cursor.fetchone()
    while get_data is not None:
        diet_patient_map["Dietition Name"] = get_data[0]
        diet_patient_map["Number of Patient"] = get_data[1]
        diet_patient_result.append(diet_patient_map)
        diet_patient_map = OrderedDict()
        get_data = cursor.fetchone()
    try:
        with open(file_path+file_name, 'w+') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=["Dietition Name", "Number of Patient"])
            writer.writeheader()
            for data in diet_patient_result:
                writer.writerow(data)
        print('File created successfully: %s' % file_name)
    except IOError:
        print("I/O error") 

    return 0

def upload_to_drive(file_name):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(file_path+'token.pickle'):
        with open(file_path+'token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                file_path+'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(file_path+'token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    file_metadata = {'name': file_name, 'parents':[os.path.basename(DRIVE_FOLDER)]}
    media = MediaFileUpload(file_path+file_name,mimetype="text/csv")
    file = service.files().create(body=file_metadata,media_body=media,fields='id').execute()
    print('File ID: %s' % file.get('id'))
    print('File uploaded to drive successfully')
    page_token = None
    file_list = []
    while True:
        response = service.files().list(q="name contains 'Dietition_Patient_count' and name contains '.csv'",spaces='drive',fields='nextPageToken, files(id, name)', pageToken=page_token, orderBy="createdTime").execute()
        for file in response.get('files', []):
            # Process change
            file_list.append(file.get('id'))
            #print 'Found file: %s (%s)' % (file.get('name'), file.get('id'))
        file_list.reverse()
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    try:
        for _id in file_list[14:]:
            service.files().delete(fileId=_id).execute()
    except errors.HttpError, error:
        pass
 
def send_email(file_name):
    try:
        msg = MIMEMultipart()
        # storing the senders email address   
        msg['From'] = fromaddr
        # storing the receivers email address  
        msg['To'] = ", ".join(toaddr)
        # storing the subject  
        msg['Subject'] = "Dietition and Patient List " + datetime.now().strftime("%d-%m-%Y")
        # string to store the body of the mail 
        body = "Hi, \n\nKindly PFA the list of dietitions and there patients for " + datetime.now().strftime("%d-%m-%Y") + ".\n\nThanks,\nTeam Pranacare."
        # attach the body with the msg instance 
        msg.attach(MIMEText(body, 'plain'))
        # open the file to be sent  
        filename = file_name
        attachment = open(file_path+filename, "rb")
        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream')
        # To change the payload into encoded form 
        p.set_payload((attachment).read())
        # encode into base64 
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        # attach the instance 'p' to instance 'msg' 
        msg.attach(p)
        # creates SMTP session 
        server = smtplib.SMTP(host, port)
        # start TLS for security 
        server.starttls()
        # Authentication 
        server.login(fromaddr, password)
        # Converts the Multipart msg into a string 
        text = msg.as_string()
        # sending the mail 
        server.sendmail(fromaddr, toaddr, text)
        print("file send successfully")
        server.quit()
    except Exception as e:
        print (e)
        pass

try:
    init_db()
    db = get_db()
    get_patient_dietition(db, diet_patient_map)
    upload_to_drive(file_name)
    send_email(file_name)
    os.system("/bin/rm "+file_path + file_name)
    print("File removed locally")
    print("======================")
    close_db()
except Exception as err:
    print err
