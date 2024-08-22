
import os
import json
import requests
import time
from datetime import datetime
import pipes
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
from apiclient import errors
from __config import *


DB_HOST = getAtmanConfigParamValue("PRANA_CARE_MESSAGE_QUEUE_HOST") 
DB_USER = getAtmanConfigParamValue("PRANA_CARE_DATA_DB_USER_NAME")
DB_USER_PASSWORD = getAtmanConfigParamValue("PRANA_CARE_DATA_DB_USER_PASSWD")
DB_NAME = getAtmanConfigParamValue("PRANA_CARE_DATA_DB_NAME")
BACKUP_PATH = getAtmanConfigParamValue("DATABASE_BACK_UP_PATH")
fromaddr = email_name
host = email_host
port = email_port
password = email_password
toaddr = ["adhir.potdar@isanasystems.com"]
DATETIME = time.strftime('%Y%m%d-%H%M%S')
date = datetime.now().strftime("%Y-%m-%d")
TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME
pranacare_file = getAtmanConfigParamValue("DATABASE_BACKUP_FILE_NAME")+"_"+DATETIME+".sql.gz"
DRIVE_FOLDER = getAtmanConfigParamValue("DATABASE_DRIVE_FOLDER")
SCOPES = ['https://www.googleapis.com/auth/drive']
file_path = getAtmanConfigParamValue("PYTHON_SCRIPT_PATH")


def take_backup():
    try:
        if not os.path.exists(TODAYBACKUPPATH):
            os.mkdir(TODAYBACKUPPATH)
        dump = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + DB_NAME + " | gzip -c" +  " > " + pipes.quote(TODAYBACKUPPATH) + "/" + pranacare_file
        os.system(dump)
    except Exception as err:
        print (err)

def upload_to_drive():
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
    file_metadata = {'name': pranacare_file, 'parents':[os.path.basename(DRIVE_FOLDER)]}
    media = MediaFileUpload(TODAYBACKUPPATH+"/"+pranacare_file,mimetype="application/x-gzip")
    file = service.files().create(body=file_metadata,media_body=media,fields='id').execute()
    print('File ID: %s' % file.get('id'))
    print('File uploaded successfully')
    page_token = None
    file_list = []
    while True:
        response = service.files().list(q="name contains 'pranacare_backup_2' and name contains '.sql.gz'",spaces='drive',fields='nextPageToken, files(id, name)', pageToken=page_token, orderBy="createdTime").execute()
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

def send_mail():
    msg = MIMEMultipart()
    # storing the senders email address   
    msg['From'] = fromaddr
    # storing the receivers email address  
    msg['To'] = ", ".join(toaddr) 
    # storing the subject  
    msg['Subject'] = "Pranacare Database Back up " + date
    # string to store the body of the mail 
    body = "Database Backup for " + date +". Click on below link: \n" + DRIVE_FOLDER
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain'))  
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

def job():
    take_backup()
    upload_to_drive()
    time.sleep(60)
    send_mail()
    os.system("rm -r " + TODAYBACKUPPATH)

job()	
