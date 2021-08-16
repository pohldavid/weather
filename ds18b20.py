#! /usr/bin/python3

'''

see usage of ds18b20 here
https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/#:~:text=The%20DS18B20%20temperature%20sensor%20is,wire%20for%20the%20data%20signal.

'''
# this file is diffferent for each use case 
#one_wire_file = '/sys/bus/w1/devices/28-3c01a8168ea2/w1_slave'
#one_wire_file = '/sys/bus/w1/devices/00-c00000000000/w1_slave'
one_wire_file = '/sys/bus/w1/devices/28-0301a279045a/w1_slave'
'''

file is of the form:

c4 01 55 05 7f a5 a5 66 bc : crc=bc YES
c4 01 55 05 7f a5 a5 66 bc t=28250

'''
'''
temperature in Celcius is the last string in the last line of the file:
t=28250
'''

with open(one_wire_file, "r") as file:

    for last_line in file:
        pass

print(last_line)

temperature = last_line.split()[-1] # grab the temperature term from the lst line of the file

no_decimal_celcius = temperature.split('=')[-1] # remove the 't='

celcius = float(no_decimal_celcius[0:2] + '.' + no_decimal_celcius[2:]) #slice and add decimal after second digit; cast type to float (close enough)
fahrenheit = (celcius*9/5)+32

print('Celcius:' , celcius, ' Fahrenheit: ', fahrenheit) 




