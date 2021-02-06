#!/usr/bin/pyenv

import datetime
import pylunar

mi = pylunar.MoonInfo((17, 30, 5), (-88, 12, 12))

mi.update((2021, 2, 5, 22, 00, 0))
#mi.update((2021, 7, 19, 1, 45, 0))

today = datetime.datetime.today()
print('today: ', today)

print('year: ', today.year)


now = datetime.datetime.now()
print('now: ', now)

print(now.year, now.month, now.day, now.hour, now.minute, now.second)

print("\U+1F312")


print(mi.age())
print(mi.fractional_phase())
print(mi.phase_name())
print('unicode charater for moon')
