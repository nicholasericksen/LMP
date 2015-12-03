from __future__ import division
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft
from get_stokes import get_stokes_trapz, get_stokes_simps
from scipy import integrate
#here will be the loop to take data readings on each keystroke
#readings will be then saved in a .txt file for processing

data = np.loadtxt('LMP-data-20151130-195009.txt')

x = data[:,0]
y = data[:,1]

x_radians = x * np.pi / 180
# print x_radians
y_actual = 2 * np.sin( 4 * (x_radians - 0.4799655 )) + 3

def integrandA(theta, amp, freq, phi, offset):
    return (1/np.pi)*(amp * np.cos(freq*theta - phi) + offset)

def integrandB(theta, amp, freq, phi, offset):
    return ((2/np.pi)*((amp * np.cos(freq*theta - phi) + offset) * np.sin(2*theta)))

def integrandC(theta, amp, freq, phi, offset):
    return (2/np.pi)*((amp * np.cos(freq*theta - phi) + offset) * np.cos(4*theta))

def integrandD(theta, amp, freq, phi, offset):
    return (2/np.pi)*((amp * np.cos(freq*theta - phi) + offset) * np.sin(4*theta))


amp = 0.413
freq = 4
phi = 20 * np.pi / 180
offset = 0.587

lower_bound = 0
upper_bound = 2 * np.pi

A = integrate.quad(integrandA, lower_bound, upper_bound, args=(amp, freq, phi, offset) )
B = integrate.quad(integrandB, lower_bound, upper_bound, args=(amp, freq, phi, offset) )
C = integrate.quad(integrandC, lower_bound, upper_bound, args=(amp, freq, phi, offset) )
D = integrate.quad(integrandD, lower_bound, upper_bound, args=(amp, freq, phi, offset) )

print "A: ", A[0]
print "B: ", B[0]
print "C: ", C[0]
print "D: ", D[0]

stokes0 = A[0] - C[0]
stokes1 = 2*C[0]
stokes2 = 2*D[0]
stokes3 = B[0]

print "S0: ", stokes0
print "S1: ", stokes1
print "S2: ", stokes2
print "S3: ", stokes3


# print y_actual
# s0, s1, s2, s3 = get_stokes_trapz(x_radians, y)

S0, S1, S2, S3 = get_stokes_simps(x_radians, y)

def curve_fit_into(y):
    # first guess at curve before fitting
    offset = np.mean(y)
    print "offset: ", offset
    amplitude = 3*np.std(y)/(2**0.5)
    print "amplitude: ", amplitude

    # spectrum = fft.fft(data)
    # freq = fft.fftfreq(len(spectrum))
    # print "freq: ", freq
    # plt.plot(freq, abs(spectrum))
    # plt.show()


    # phase = 0
    # freq = .02 #this should be determined by the FFT spectrum
    #
    # curve_guess = amplitude*np.sin(freq*x + phase) + offset
    #
    # z = np.polyfit(x, y, 6)
    # f = np.poly1d(z)
    #
    # x_new = np.linspace(x[0], x[-1], 50)
    # y_new = f(x_new)
curve_fit_into(y)

def draw_data(x, y):
    plt.plot(x, y, 'ro')
    # plt.plot(x, y_actual, 'bo')

    plt.title('Light Measuring Polarimetry')
    plt.xlabel('Measurement Angles')
    plt.ylabel('Intensity')

    plt.show()

draw_data(x, y)




def draw_poincare_sphere(S1, S2, S3):
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

# draw_poincare_sphere(S1, S2, S3)
# draw_poincare_sphere(s1, s2, s3)
