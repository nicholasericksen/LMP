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
num_of_measurements = 18

port = "/dev/cu.usbmodem1421"
baudrate = 9600
count = 0

timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "LMP-data-" + timestr + ".txt"

ser = serial.Serial(port, baudrate)

while (count < num_of_measurements):
    print "Measurement Angle: ",
    angle = raw_input()

    ser.flush()
    ser.write('3')
    time.sleep(1)

    measurement = ser.readline()
    print "Measurement: ", measurement

    if(os.path.isfile(filename)):
        target = open(filename, 'ab')
    else:
        target = open(filename, 'w')

    target.write(angle)
    target.write('\t')
    target.write(measurement)

    target.close()
    count = count + 1
