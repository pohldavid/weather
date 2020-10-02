#!/usr/bin/env python3

import matplotlib.pyplot as plt

def make_X_Axis_Label():
    x_label = []
    for h in range(8):
        x_label.append(str(h)+"AM")
    return x_label

# x = ['Maths', 'Physics', 'Chemistry']


x =  make_X_Axis_Label()

y1 = [95, 88, 45, 65, 87, 90, 46, 75]


plt.plot(x, y1, label="Temperature \u00b00F")

y2 = [67, 45, 56, 55, 45, 56, 60, 62]


plt.plot(x, y2, label="Humidity %")


y3 = [28.87, 29.92, 29.90, 29.91, 29.92, 29.92, 29.90, 28.90]

plt.plot(x, y3, label="Pressure inHg")

#plt.xlabel('Time')
#plt.ylabel('Value')

plt.title('BME_280 Humidity, Temperature, Pressure')

plt.legend()

plt.show()

