#! /usr/bin/python3
import bme280
import smbus2

from datetime import datetime
from subprocess import call, check_output
import picamera
import time
import os

port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)
bme280_data = bme280.sample(bus,address)
humidity  = bme280_data.humidity
pressure  = bme280_data.pressure/33.8639
temperature = (bme280_data.temperature * 9.0/5.0) +32




temp = check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
date = check_output("date")
print(str(temp) +" " + str(date))

cam = picamera.PiCamera()
cam.vflip = True
cam.hflip=True
cam.rotation = 270

cam.resolution=(1024,768)
cam.annotate_background = picamera.Color('black')
cam.start_preview()
time.sleep(2)
cam.annotate_text = "Weather " + str(temperature) +datetime.now().strftime('%d-%m-%y %H:%M:%S')
cam.capture('/home/pi/weather/stills/'+str(datetime.now())+'.jpg')

timestamp = datetime.now().strftime('%d-%m-%y_%H-%M-%S')
        
            
        


