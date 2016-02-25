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

port = "/dev/cu.usbmodem1421"
baudrate = 9600
angle = [0, 90, 45, -45, "LCP", "RCP"]
ser = serial.Serial(port, baudrate)

while (i < 1):
    count = 0
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "LMP-data-" + timestr + ".txt"

    while (count < num_of_measurements):
        time.sleep(2)

        ser.flush()
        ser.write('1')
        time.sleep(1)

        measurement = ser.readline()

        print "Measurement: ", measurement

        if(os.path.isfile(filename)):
            target = open(filename, 'ab')
        else:
            target = open(filename, 'w')

        target.write(measurement)

        target.close()
        count = count + 1

    ser.flush()
    ser.write('2')
    i = i + 1

get_stokes_chip(filename)
