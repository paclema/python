#!/bin/bash


# Configure ddns config file:
servicename="boulderhalle_status"
servicefile="/lib/systemd/system/boulderhalle_status.service"
servicescrip="/home/pi/seleniumInstall/python/scraping/boulderhalle_status.py"

cat >> $servicefile <<- EOM
[Unit]
Description="$servicename"
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/usr/bin/python3 "$servicescrip"
StandardInput=tty-force

[Install]
WantedBy=multi-user.target
EOM

sudo systemctl daemon-reload
sudo systemctl enable boulderhalle_status.service
sudo systemctl start boulderhalle_status.service
