#!/bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# Configure ddns config file:
servicename="boulderhalle_status"
servicefile="/lib/systemd/system/boulderhalle_status.service"
servicescrip="$SCRIPTPATH/boulderhalle_status.py"


cat >> $servicefile <<- EOM
[Unit]
Description="$servicename"
#After=multi-user.target

[Service]
Type=simple
WorkingDirectory=$SCRIPTPATH
User=pi
ExecStart=/usr/bin/python3 "$servicescrip"
Restart=always

[Install]
WantedBy=multi-user.target
EOM

sudo systemctl daemon-reload
sudo systemctl enable boulderhalle_status.service
sudo systemctl start boulderhalle_status.service
