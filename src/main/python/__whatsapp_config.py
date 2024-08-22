import json
import logging
import requests

def getTokenTemplate():
    with open("/opt/atman/config/pranacare_whatsapp_chatapi_config.json", "rb") as json_file:
        json_token = json.load(json_file)
    return json_token

def getJsonTemplate():
    with open("/opt/atman/config/whatsapp_chatapi_call.json", "rb") as json_file:
        json_template = json.load(json_file)
    return json_template

def getToken(token_template):
    instance = token_template.get("instance_token", [])
    return instance
      
def getQrCodeTemplate(json_template):
    header = json_template.get("get_qr_code_header", "")
    url = json_template.get("get_qr_code_url", "")
    return header, url

def getSendMessageTemplate(json_template):
    header = json_template.get("send_message_header", "")
    url = json_template.get("send_message_url", "")
    data = json_template.get("send_message_body", "")
    return header, url, data

def getSendFileTemplate(json_template):
    header = json_template.get("send_message_header", "")
    url = json_template.get("send_file_url", "")
    data = json_template.get("send_file_body", "")
    return header, url, data

def getSendContactTemplate(json_template):
    header = json_template.get("send_message_header", "")
    url = json_template.get("send_contact_url", "")
    data = json_template.get("send_contact_body", "")
    return header, url, data

def getPdfContent(json_template):
    content_pdf = json_template.get("pdf_content", "")
    return content_pdf  

def getQrCode(url, header, instance_id):
    response = requests.get(url, headers=header, allow_redirects=True)
    open(instance_id+".png","wb").write(response.content)


def sentMessage(data, url, header):
    try:
        response = requests.post(url, headers=header, data=data)
        print response
        if response.status_code == 200:
            logging.info("Whatsapp sent successfully")
            print ("Whatsapp sent successfully")
        else:
            logging.info("Error sending Whatsapp with response code - " + str(response.status_code))
            print ("Whatsapp not sent")
    except Exception as e:
        print ("Error in sending whatsapp -" + e)
        pass
