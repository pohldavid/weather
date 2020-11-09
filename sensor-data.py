import bme280
import smbus2
from time import sleep
import timestamp
port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

from peewee import *
from datetime import *

db = SqliteDatabase('history.db')

class Readings(Model):


    temperature = CharField()
    humidity = CharField()
    pressure = CharField()
    day = DateField()
    reading_time = TimeField()

    class Meta:
        database = db

db.connect()

db.create_tables([Readings])

for i in range(3):
    bme280_data = bme280.sample(bus,address)
    current_day=date.today()
    current_time=str(datetime.now().time()).split('.')[0] # h:m:s decimal seconds removed
    this_reading = Readings(temperature=bme280_data.temperature, humidity = bme280_data.humidity, pressure = bme280_data.pressure, day = current_day, reading_time = current_time )
    this_reading.save()

    print("peewee ", this_reading.temperature)
    print("peewee ", this_reading.day)
    print("peewee ", this_reading.reading_time)


"""
while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure/33.8639
    temperature = (bme280_data.temperature * 9.0/5.0) +32

    
    
    sleep(15)
"""
