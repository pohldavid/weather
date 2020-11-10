from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Reading(Model):
    temperature = CharField()
    humidity = CharField()
    pressure = CharField()
    day = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.

        
        

db.connect()

db.create_tables([Person, Pet, Reading])

something = Reading(temperature='100', humidity = '50', pressure = '29', day=date(1960, 1, 15))
something.save()

uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
uncle_bob.save() # bob is now stored in the database

chuy = Pet(name='Chuy', birthday=date(1960, 1, 15))
chuy.save() 

# Returns: 1

grandma = Person.select().where(Person.name == 'Bob').get()

print(grandma.name)

print(something.temperature)
