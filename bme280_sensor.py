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
    data = f"{timestamp.stamp()} Humidity {humidity:03.2f} % Pressure {pressure:03.2f} InHg Temperature {temperature:03.1f} F"
    print( data)
#    print(f"{timestamp.stamp()} Humidity {humidity:03.2f} % Pressure {pressure:03.2f} InHg Temperature {temperature:03.1f} F")
    with open("data.txt", "a") as outfile:
        outfile.write(str(data))
        outfile.close()
	
    sleep(15)
