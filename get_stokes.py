import numpy as np

def get_stokes(theta, I):
    signal0 = I
    signal1 = signal0*np.sin(2*theta)
    signal2 = signal0*np.cos(4*theta)
    signal3 = signal0*np.sin(4*theta)

    print "signal1 = ", signal1
    print "signal2 = ", signal2
    print "signal3 = ", signal3

    denom = float(2*len(I))/360

    area0 = np.trapz(signal0)/denom
    area1 = np.trapz(signal1)/denom
    area2 = np.trapz(signal2)/denom
    area3 = np.trapz(signal3)/denom

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

    return s0, s1, s2, s3
