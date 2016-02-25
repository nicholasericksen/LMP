import numpy as np
from scipy import integrate

def get_stokes_trapz(theta, I):
    signal0 = I
    signal1 = signal0*np.sin(2*theta)
    signal2 = signal0*np.cos(4*theta)
    signal3 = signal0*np.sin(4*theta)

    # print "signal1 = ", signal1
    # print "signal2 = ", signal2
    # print "signal3 = ", signal3

    denom = float(2*len(I))/360

    area0 = np.trapz(signal0)
    area1 = np.trapz(signal1)
    area2 = np.trapz(signal2)
    area3 = np.trapz(signal3)

    A = area0/np.pi
    B = -area1*2/np.pi
    C = area2*2/np.pi
    D = area3*2/np.pi

    stokes0 = ((A-C))
    stokes1 = (2*C)
    stokes2 = (2*D)
    stokes3 = (B)

    stokes0p = np.sqrt(stokes1**2 + stokes2**2 + stokes3**2)

    s0 = stokes0/stokes0p
    s1 = stokes1/stokes0p
    s2 = stokes2/stokes0p
    s3 = stokes3/stokes0p

    DOP = stokes0p/(stokes0)

    print "S0 (trapzoidal): ", s0
    print "S1 (trapzoidal): ", s1
    print "S2 (trapzoidal): ", s2
    print "S3 (trapzoidal): ", s3
    print "DOP: ", DOP

    return s0, s1, s2, s3

def get_stokes_simps(theta, I):
    theta = np.array(theta)
    print "theta = ", theta
    I = np.array(I)
    print "I = ", I

    n1 = np.sin(2*theta)
    n2 = np.cos(4*theta)
    n3 = np.sin(4*theta)

    print "n1 ", n1
    print "n2 ", n2
    print "n3 ", n3


    integrandA = I
    integrandB = I*np.sin(2*theta)
    integrandC = I*np.cos(4*theta)
    integrandD = I*np.sin(4*theta)

    print "integrandA ", integrandA
    print "integrandB ", integrandB
    print "integrandC ", integrandC
    print "integrandD ", integrandD

    A = (2/np.pi) * integrate.simps(integrandA, theta)
    B = -(4/np.pi) * integrate.simps(integrandB, theta)
    C = (4/np.pi) * integrate.simps(integrandC, theta)
    D = (4/np.pi) * integrate.simps(integrandD, theta)

    print "============================="
    print "A: " , A
    print "B: ", B
    print "C: ", C
    print "D: ", D
    # print "theta: ", theta

    stokes0 = A - C
    stokes1 = 2 * C
    stokes2 = 2 * D
    stokes3 = B
    # S0 = np.sqrt(S1**2 + S2**2 + S3**2)

    stokes0p = np.sqrt(stokes1**2 + stokes2**2 + stokes3**2)

    # S0 = stokes0/stokes0p
    # S1 = stokes1/stokes0p
    # S2 = stokes2/stokes0p
    # S3 = stokes3/stokes0p
    DOP = np.sqrt(stokes1**2 + stokes2**2 + stokes3**2) / (stokes0)
    print "DOP", DOP

    # S0 = stokes0 / DOP
    # S1 = stokes1 / DOP
    # S2 = stokes2 / DOP
    # S3 = stokes3 / DOP
    #
    S0_un = stokes0
    S1_un = stokes1
    S2_un = stokes2
    S3_un = stokes3
    S0 = stokes0 / stokes0
    S1 = stokes1 / stokes0
    S2 = stokes2 / stokes0
    S3 = stokes3 / stokes0



    # unit_norm_S0 = S0 / unit_norm_denominator
    # unit_norm_S1 = S1 / unit_norm_denominator
    # unit_norm_S2 = S2 / unit_norm_denominator
    # unit_norm_S3 = S3 / unit_norm_denominator


    print "S0 (un): " , S0_un
    print "S1 (un): " , S1_un
    print "S2 (un): " , S2_un
    print "S3 (un): " , S3_un

    print "S0 (Simpsons): " , S0
    print "S1 (Simpsons): " , S1
    print "S2 (Simpsons): " , S2
    print "S3 (Simpsons): " , S3

    return S0, S1, S2, S3


# filename = 'results/EX-02.04.16/LMP-data-20160204-183739-Horizontal.txt'

def read_file(filename):
    infile = open(filename)
    data_set = infile.read().splitlines()
    infile.close()

    return data_set



def get_stokes_chip(filename):

    data = read_file(filename)
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

    print "DOP", DOP

    S0p = DOP * S0

    S0n = S0p /S0p
    S1n = S1 / S0p
    S2n = S2 / S0p
    S3n = S3 / S0p

    print "S0 (chip): " , S0n
    print "S1 (chip): " , S1n
    print "S2 (chip): " , S2n
    print "S3 (chip): " , S3n

    # return S0p, S1n, S2n, S3n

# get_stokes_chip(pH, pV, p45, p135, pR, pL)
