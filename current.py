import bme280
import smbus2
from time import sleep
import timestamp
port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure/33.8639
    temperature = (bme280_data.temperature * 9.0/5.0) +32
#    data = f"{timestamp.stamp()} Humidity {humidity:03.2f} % Pressure {pressure:03.2f} InHg Temperature {temperature:03.1f} F </br>"
    current = f"<h1>{timestamp.stamp()}</h1><h1> Humidity {humidity:03.2f} %</h1><h1> Pressure {pressure:03.2f} InHg</h1><h1> Temperature {temperature:03.1f} F</h1> </br>"
    print(current)
#    print(f"<html><h1> {timestamp.stamp()}</h1> Humidity {humidity:03.2f} % Pressure {pressure:03.2f} InHg Temperature {temperature:03.1f} F</html>")
    
    try:
        
        with open("/var/www/html/current.html", "w") as outfile1:
            outfile1.write("<meta http-equiv='refresh' content='15'/> </br>")
            outfile1.write(str(current))
            
    except KeyboardInterrupt:
        print("Later Dude")
        
    finally:

        with open("/var/www/html/current.html", "a") as outfile1:
            outfile1.close()
    
    sleep(15)
