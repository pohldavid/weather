#! /usr/bin/python3

from astral import LocationInfo
#from astral import now, today
import datetime
from pytz import timezone
#import pytz
from astral.sun import sun

central = timezone("US/Central")

city = LocationInfo("Pohl Barn", "USA", "US/Central", 29.2829243, -96.8658090) # barn coordinates from google maps

print((
    f"Information for {city.name}/{city.region}\n"
    f"Timezone: {city.timezone}\n"
    f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
))

today = datetime.datetime.today()

tomorrow = today + datetime.timedelta(days=1)

sun_today = sun(city.observer, today, tzinfo=city.timezone)
sun_tomorrow = sun(city.observer, tomorrow, tzinfo=city.timezone)

print(today.strftime("Today, %A %B %d, %Y"))
print("-"*30)
print((
    f'Dawn:    {sun_today["dawn"].strftime("%H:%M:%S")}\n'
    f'Sunrise: {sun_today["sunrise"].strftime("%H:%M:%S")}\n'
    f'Noon:    {sun_today["noon"].strftime("%H:%M:%S")}\n'
    f'Sunset:  {sun_today["sunset"].strftime("%H:%M:%S")}\n'
    f'Dusk:    {sun_today["dusk"].strftime("%H:%M:%S")}\n'
))

print(tomorrow.strftime("Tomorrow, %A %B %d, %Y"))
print("-"*30)
print((
    f'Dawn:    {sun_tomorrow["dawn"].strftime("%H:%M:%S")}\n'
    f'Sunrise: {sun_tomorrow["sunrise"].strftime("%H:%M:%S")}\n'
    f'Noon:    {sun_tomorrow["noon"].strftime("%H:%M:%S")}\n'
    f'Sunset:  {sun_tomorrow["sunset"].strftime("%H:%M:%S")}\n'
    f'Dusk:    {sun_tomorrow["dusk"].strftime("%H:%M:%S")}\n'
))


localized_now =  central.localize(datetime.datetime.now())

print(localized_now.strftime("Time now:  %H:%M:%S"))

time_till_dawn = sun_tomorrow["dawn"] - localized_now
seconds_till_dawn = time_till_dawn.total_seconds()

print(seconds_till_dawn)


    

