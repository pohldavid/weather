#! /usr/bin/python3

import datetime
import pylunar

location = {'lat':(17, 30, 5), 'lon':(-88, 12, 12)}
location_name = 'Belize City'

# convert local to UTC -> looks like 
UTC_datetime = datetime.datetime.utcnow()
UTC_s = UTC_datetime.strftime("%s")

print(UTC_s.split('-')[0])



observation_time = (2021, 2, 10, 13, 00, 0)

mi = pylunar.MoonInfo(location['lat'], location['lon'])

mi.update(observation_time)
#mi.update((2021, 7, 19, 1, 45, 0))

today = datetime.datetime.today()
print('today: ', today)

print('year: ', today.year)

now = datetime.datetime.now()
print('now: ', now)

print(now.year, now.month, now.day, now.hour, now.minute, now.second)

print(mi.age())
print(mi.fractional_phase())
print(mi.phase_name(),'\n')


print("improve this script -> requires UTC date/time : calculate this from local time")
print("calculate azimuth, elevation, etc.")