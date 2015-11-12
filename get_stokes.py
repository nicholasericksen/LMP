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
    integrandA = I
    integrandB = I*np.sin(2*theta)
    integrandC = I*np.cos(4*theta)
    integrandD = I*np.sin(4*theta)

    A = (1/np.pi) * integrate.simps(integrandA, theta)
    B = (2/np.pi) * integrate.simps(integrandB, theta)
    C = (2/np.pi) * integrate.simps(integrandC, theta)
    D = (2/np.pi) * integrate.simps(integrandD, theta)

    stokes1 = 2 * C
    stokes2 = 2 * D
    stokes3 = -B
    stokes0 = A - C
    # S0 = np.sqrt(S1**2 + S2**2 + S3**2)

    stokes0p = np.sqrt(stokes1**2 + stokes2**2 + stokes3**2)

    S0 = stokes0/stokes0p
    S1 = stokes1/stokes0p
    S2 = stokes2/stokes0p
    S3 = stokes3/stokes0p


    DOP = np.sqrt(stokes1**2 + stokes2**2 + stokes3**2) / stokes0
    # unit_norm_S0 = S0 / unit_norm_denominator
    # unit_norm_S1 = S1 / unit_norm_denominator
    # unit_norm_S2 = S2 / unit_norm_denominator
    # unit_norm_S3 = S3 / unit_norm_denominator

    print "S0 (Simpsons): " , S0
    print "S1 (Simpsons): " , S1
    print "S2 (Simpsons): " , S2
    print "S3 (Simpsons): " , S3

    return S0, S1, S2, S3
