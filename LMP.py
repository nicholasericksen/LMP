import serial
import sys
import time
import datetime
import os.path
import numpy as np

class LMP():
    def __init__(self, port="/dev/cu.usbmodem1421", baudrate=9600):
        self.ser = serial.Serial(port, baudrate)
        
    def sensor(self):
        self.ser.flush()
        self.ser.write('3')

        time.sleep(1)
        measurement = self.ser.readline()
        print "Voltage: ", measurement

    def read_file(self, filename):
        infile = open(filename)
        data_set = infile.read().splitlines()
        infile.close()

        return data_set

    def stokesclassical(self, filename):
        data = self.read_file(filename)
        data = [float(i) for i in data]

        pH = data[1]
        pV = data[2]
        p45 = data[3]
        p135 = data[4]
        pR = data[5]
        pL = data[6]

        S0 = pH + pV
        S1 = pH - pL
        S2 = p45 - p135
        S3 = pR - pL

        DOP = np.sqrt(S1**2 + S2**2 + S3**2) / S0

        print ""
        print "=========================================="
        print "DOP", DOP

        S0p = DOP * S0

        S0n = S0p /S0p
        S1n = S1 / S0p
        S2n = S2 / S0p
        S3n = S3 / S0p

        print "S0: " , S0n
        print "S1: " , S1n
        print "S2: " , S2n
        print "S3: " , S3n
        print "=========================================="

        return S0n, S1n, S2n, S3n

    def pSphere(self, S1, S2, S3):
        #initalize plotting
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
        x = np.cos(u)*np.sin(v)
        y = np.sin(u)*np.sin(v)
        z = np.cos(v)
        ax.plot_wireframe(x, y, z)
        ax.scatter(S1, S2, S3, color="g", s=100)

        plt.xlabel('S1')
        plt.ylabel('S2')

        plt.show()

    def classical(self):
        num_of_measurements = 7
        i = 0

        angle = [0, 90, 45, -45, "LCP", "RCP"]

        while (i < 1):
            count = 0
            timestr = time.strftime("%Y%m%d-%H%M%S")
            filename = "LMP-data-" + timestr + ".txt"

            while (count < num_of_measurements):
                time.sleep(2)

                self.ser.flush()
                self.ser.write('1')
                time.sleep(1)

                measurement = self.ser.readline()

                print "Measurement: ", measurement

                if(os.path.isfile(filename)):
                    target = open(filename, 'ab')
                else:
                    target = open(filename, 'w')

                target.write(measurement)

                target.close()
                count = count + 1

            self.ser.flush()
            self.ser.write('2')
            i = i + 1

        self.stokesclassical(filename)
