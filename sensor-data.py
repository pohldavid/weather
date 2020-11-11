import bme280
import smbus2
from time import sleep
import timestamp
from peewee import *
from datetime import *

port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus, address)

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


# mock-up to test db read write
for i in range(3):
    bme280_data = bme280.sample(bus,address)
    current_day = date.today()
    current_time = datetime.now().strftime("%H:%M:%S")
    this_reading = Readings(
        temperature=bme280_data.temperature,
        humidity=bme280_data.humidity,
        pressure=bme280_data.pressure,
        day=current_day,
        reading_time=current_time)
    this_reading.save()

    print("peewee day", this_reading.day)
    print("peewee reading_time", this_reading.reading_time)
    print("peewee temperature ", this_reading.temperature)
    print("peewee pressure", this_reading.pressure)
    print("peewee humidity", this_reading.humidity)
    
