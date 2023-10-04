#!/bin/bash

echo "copying timelapse script.."
cp blinkled.py /usr/local/bin/
echo "copying systemd unit.."
mkdir /etc/systemd/system/blinkled.target.wants
cp blinkled.service /etc/systemd/system/
cp blinkled.target /etc/systemd/system/

echo "enabling units and reloading configs.."
systemctl daemon-reload
systemctl isolate blinkled.target
ln -sf /etc/systemd/system/blinkled.target /etc/systemd/system/default.target
systemctl enable blinkled.service

echo "chmod scripts.."
chmod 755 /usr/local/bin/blinkled.py

