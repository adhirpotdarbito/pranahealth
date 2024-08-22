#!/bin/bash
SERVICE="/usr/bin/python /opt/atman/bin/__insert_update_misc.py"
if pgrep -f "$SERVICE" >/dev/null
then
echo "$SERVICE script for database insertion is running. Time: $(date)."
else
echo "$SERVICE script for database insertion stopped at $(date)."
echo "Starting $SERVICE daemon for database insertion. Time: $(date)." 
nohup /usr/bin/python /opt/atman/bin/__insert_update_misc.py &
fi
