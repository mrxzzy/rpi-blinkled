#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
from datetime import datetime

def ledon():
  GPIO.output(13,GPIO.HIGH)

def ledoff():
  GPIO.output(13,GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.OUT)

count = 0
while count < 3:
  ledon()
  time.sleep(0.1)
  ledoff()
  time.sleep(0.1)
  count = count + 1

now = datetime.now().year
while now <= 2020:
  ledon()
  time.sleep(0.3)
  ledoff()
  time.sleep(0.3)
  now = datetime.now().year

ledon()
