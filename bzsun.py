#! /usr/bin/python2
from astral import LocationInfo
import datetime
from astral.sun import sun

# location from termux-location
city = LocationInfo("Belize City", "BZ", "America/Belize",17.5149, -88.2229)
print((
    f"Information for {city.name}/{city.region}\n"
    f"Timezone: {city.timezone}\n"
    f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
    
))

#date=datetime.date(2020, 11, 9)
date=datetime.datetime.today()



s = sun(city.observer, date, tzinfo=city.timezone)

print(date.strftime("%A %d. %B %Y"))
print((
    f'Dawn:    {s["dawn"].strftime("%H:%M:%S %z")}\n'
    f'Sunrise: {s["sunrise"].strftime("%H:%M:%S")}\n'
    f'Noon:    {s["noon"]}\n'
    f'Sunset:  {s["sunset"]}\n'
    f'Dusk:    {s["dusk"]}\n'
))

print(type(s['dawn']))

#29.2829243, -96.8658090
