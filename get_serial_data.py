import serial
import sys
import time
import datetime
import os.path

print "============================================================================="
print "Light Measuring Polarimeter (LMP)"
print "A simple program to record values from a photosensor transmitting serial data"
print "============================================================================="
# print "How many measurements? ",
num_of_measurements = 3

port = "COM4"
baudrate = 9600
count = 0
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "LMP-data-" + timestr

ser = serial.Serial(port, baudrate)


while (count < num_of_measurements):

    print "Measurement Angle: ",
    angle = raw_input()

    ser.flush()
    ser.write('1')
    time.sleep(1)

    measurement = ser.readline()
    print "Measurement: ", measurement

    # ts = time.time()
    # date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    # filename = "LMP", date


    if(os.path.isfile(filename)):
        target = open(filename, 'ab')
    else:
        target = open(filename, 'w')

    target.write(angle)
    target.write('\t')
    target.write(measurement)
    # target.write('\n')

    target.close()
    count = count + 1
