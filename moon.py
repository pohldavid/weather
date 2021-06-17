#! /usr/bin/python3

import datetime
import pylunar

#import pytz
location = {'lat':(17, 30, 5), 'lon':(-88, 12, 12)}
location_name = 'Belize City'

# pylunar takes UTC time as a tuple
UTC_now = datetime.datetime.utcnow()

observation_time = (UTC_now.year, UTC_now.month, UTC_now.day, UTC_now.hour, UTC_now.minute, UTC_now.second)

mi = pylunar.MoonInfo(location['lat'], location['lon'])

mi.update(observation_time)

now = datetime.datetime.now()

print(f'Observation time: {now:%Y-%m-%d %H:%M}')

print(f'Moon age: {mi.age():0.2f} days')

print(f'Moon phase: {(mi.fractional_phase())*100.0:0.2f} %')

print(f'Moon phase name: {mi.phase_name()}')

print(f'Azimuth: {mi.azimuth():0.2f}')

print(f'Altitude: {mi.altitude():0.2f}')

print(f'Earth Distance: {mi.earth_distance():,.2f} km [{mi.earth_distance()*0.62137:,.2f} mi]')

print('Rise Set Times: ',mi.rise_set_times('America/Chicago'))
#print(f'Rise Set Times: {mi.rise_set_times('America/Chicago')}')
print('Add Rise/Set Times')
