import serial
import sys
import time
import datetime
import os.path
import numpy as np
from get_stokes import get_stokes_chip

print "============================================================================="
print "Light Measuring Polarimeter (LMP)"
print "A simple program to record values from a photosensor transmitting serial data"
print "============================================================================="
# print "How many measurements? ",
num_of_measurements = 7
i = 0

port = "COM4"
baudrate = 9600
angle = [0, 90, 45, -45, "LCP", "RCP"]
ser = serial.Serial(port, baudrate)

while (i < 1):
    count = 0
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "LMP-data-" + timestr + ".txt"

    while (count < num_of_measurements):
        time.sleep(2)
        # print "Measurement Angle: ",
        # angle = angle[count];

        ser.flush()
        ser.write('1')
        time.sleep(1)

        measurement = ser.readline()

        print "Measurement: ", measurement

        if(os.path.isfile(filename)):
            target = open(filename, 'ab')
        else:
            target = open(filename, 'w')

        # target.write(angle)
        # target.write('\t')
        target.write(measurement)

        target.close()
        count = count + 1

    ser.flush()
    ser.write('2')
    i = i + 1

# with open(filename) as f:
#     x = f.readlines
# # data = np.loadtxt(filename)
#
# # x = data[0]
# pH = x[1]
# pV = x[2]
# p45  = x[3]
# p135 = x[4]
# pR =  x[5]
# pL = x[6]
#
# get_stokes_chip(pH, pV, p45, p135, pR, pL)