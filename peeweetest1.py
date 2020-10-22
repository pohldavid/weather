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

for i in range(10):
    current_day=date.today()
    current_time=str(datetime.now().time()).split('.')[0] # h:m:s decimal seconds removed
    this_reading = Readings(temperature='100'+str(i), humidity = '50', pressure = '29', day = current_day, reading_time = current_time )
    this_reading.save()

    print(this_reading.temperature)
    print(this_reading.day)
    print(this_reading.reading_time)

