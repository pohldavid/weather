#! /usr/bin/python3
from gpiozero import MotionSensor,Button,OutputDevice
from datetime import datetime
from subprocess import call, check_output
import picamera
import time
import os

pir = MotionSensor(14)
btn_reboot = Button(21, hold_time=1)
btn_shutdown = Button(20, hold_time=1)
relay = OutputDevice(27, active_high=False, initial_value=False)

temp = check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
date = check_output("date")
print(str(temp) +" " + str(date) + ' >> temp.txt')

def reboot():
    print("rebooting")
    os.system("sudo reboot")

def shutdown():
    print("shutting down")
    os.system("sudo poweroff")

print('Starting')

# Wait an initial duration to PIR to settle
time.sleep(1)
while True:
    if btn_reboot.is_pressed:
        print("reboot")
        reboot()
    elif btn_shutdown.is_pressed:
        print("shutdown")
        shutdown()
    elif pir.motion_detected:
        relay.on()
        print('Motion detected')
        print('Beginning capture')
        ts = '{:%Y%m%d-%H%M%S}'.format(datetime.now())
        with picamera.PiCamera() as cam:
            cam.vflip = True
            cam.resolution=(1024,768)
            cam.annotate_background = picamera.Color('black')
            cam.capture('/home/pi/pig-cam/stills/PiggyCam'+str(datetime.now())+'.jpg')
            cam.start_recording('/home/pi/pig-cam/videos/video.h264')
            start = datetime.now()
            while (datetime.now() - start).seconds < 5:
                cam.annotate_text = "Pir Piggy Cam v 1.1"+datetime.now().strftime('%d-%m-%y %H:%M:%S')
                cam.wait_recording(0.2)
            cam.stop_recording()
        time.sleep(5)
        timestamp = datetime.now().strftime('%d-%m-%y_%H-%M-%S')
        input_video = "/home/pi/pig-cam/videos/video.h264"
        output_video = "/home/pi/pig-cam/videos/{}.mp4".format(timestamp)
        print("output_video: ", output_video)
        call(["MP4Box", "-add", input_video, output_video])
        time.sleep(10)
        print('Motion Ended')
        relay.off()
    
    else:
        pass
        
            
        


