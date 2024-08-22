import sys
import json
from __whatsapp_config import *

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("python __whatsapp_getqr_code.py <instance_id>")
    else:
        instance_id = sys.argv[1]
        template_file = getJsonTemplate()
        token_file = getTokenTemplate()
        token_list = getToken(token_file)
        for token in token_list:
            if token.get(instance_id) is not None:
                token_id = token.get(instance_id)
            else:
                token_id = None
        if token_id != None:
            header, url = getQrCodeTemplate(template_file) 
            _header = json.loads(header)
            _url = url%(instance_id, token_id)
            getQrCode(_url, _header, instance_id)

