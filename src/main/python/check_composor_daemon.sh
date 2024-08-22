#!/bin/bash
SERVICE="/usr/bin/python /opt/atman/bin/__composer_consumer.py"
if pgrep -f "$SERVICE" >/dev/null
then
echo "$SERVICE script for composer consumer is running. Time: $(date)."
else
echo "$SERVICE script for composer consumer stopped at $(date)."
echo "Starting $SERVICE daemon for composer consumer. Time: $(date)." 
nohup /usr/bin/python /opt/atman/bin/__composer_consumer.py &
fi

