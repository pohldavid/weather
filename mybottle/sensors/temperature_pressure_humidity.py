from fake import bme280
from fake import smbus2
from datetime import datetime
from datetime import date

port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus, address)


def read():
    reading = bme280.sample(bus,address)
    day = date.today().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    data = ({"temperature" : reading.temperature,
             "humidity" : reading.humidity,
             "pressure" : reading.pressure,
             "day" : day, "time" : time})

    return data



if __name__ == "main":
    read()

