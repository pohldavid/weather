from fake import bme280
from fake import smbus2
from datetime import datetime
from datetime import date

port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus, address)

def read():

    sample = bme280.sample(bus,address)
    day = date.today()
    time = datetime.now().strftime("%H:%M:%S")
    temperature = sample.temperature
    humidity = sample.humidity
    pressure = sample.pressure
    
    data = {"day":day, "time":time,
            "temperature": temperature, "humidity":humidity,
            "pressure":pressure}
    
    return(data)


