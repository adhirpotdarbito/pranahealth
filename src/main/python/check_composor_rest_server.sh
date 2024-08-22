#!/bin/bash
SERVICE="composer-rest-server -c admin@pranacare-network -n never -u true -d log -w true"
if pgrep -f "$SERVICE" >/dev/null
then
echo "$SERVICE script for composer rest server is running. Time: $(date)."
else
echo "$SERVICE script for composer rest server stopped at $(date)."
echo "Starting $SERVICE daemon for composer rest server. Time: $(date)." 
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
nvm use 8.16.0
nohup composer-rest-server -c admin@pranacare-network -n never -u true -d log -w true &
/usr/bin/python /opt/atman/bin/send_whatsapp_alert.py "$SERVICE"
fi
