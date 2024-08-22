from __whatsapp_config import *
from __config import *
import datetime
import sys

if __name__ == "__main__":
    template_file = getJsonTemplate()
    token_file = getTokenTemplate()
    instance_id = token_file.get("instance_id_pranacare", "")
    token = token_file.get("token_pranacare", "")
    header, url, data =  getSendMessageTemplate(template_file)
    _header = json.loads(header)
    _url = url%(instance_id, token)
    user_number = "919993602730"
    service = sys.argv[1]
    message_body_whatsapp = "Hi Vivek,\n \nPranacare %s script stopped at %s \n\nThanks."%(service, datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    _data = data%(user_number, message_body_whatsapp.replace("&", "%26"))
    sentMessage(_data, _url, _header)

