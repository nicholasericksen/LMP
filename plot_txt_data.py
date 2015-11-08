from __future__ import division
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
#here will be the loop to take data readings on each keystroke
#readings will be then saved in a .txt file for processing

data = np.loadtxt('data-set-1.txt')

x = data[:,0]
y = data[:,1]

#first guess at curve before fitting
offset = np.mean(data)
amplitude = 3*np.std(data)/(np.sqrt(2))
phase = 0
freq = .02

curve_guess = amplitude*np.sin(freq*x + phase) + offset

z = np.polyfit(x, y, 6)
f = np.poly1d(z)

x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

x_radians = x * np.pi / 180
print x_radians
y_actual = 2 * np.sin( 4 * (x_radians - 0.4799655 )) + 3
print y_actual
integrandA = y_actual
integrandB = y_actual*np.sin(2*x_radians)
integrandC = y_actual*np.cos(4*x_radians)
integrandD = y_actual*np.sin(4*x_radians)

A = 2 * (1/np.pi) * integrate.simps(integrandA, x_radians)
B = 2 * (2/np.pi) * integrate.simps(integrandB, x_radians)
C = 2 * (2/np.pi) * integrate.simps(integrandC, x_radians)
D = 2 * (2/np.pi) * integrate.simps(integrandD, x_radians)

print A
print B
print C
print D

S1 = 2 * C
S2 = 2 * D
S3 = B
S0 = A - C
# S0 = np.sqrt(S1**2 + S2**2 + S3**2)

norm_stokes_S0 = S0/S0
norm_stokes_S1 = S1/S0
norm_stokes_S2 = S2/S0
norm_stokes_S3 = S3/S0

unit_norm_denominator = np.sqrt(S1**2 + S2**2 + S3**2)
unit_norm_S0 = S0 / unit_norm_denominator
unit_norm_S1 = S1 / unit_norm_denominator
unit_norm_S2 = S2 / unit_norm_denominator
unit_norm_S3 = S3 / unit_norm_denominator

print "S0: " , unit_norm_S0
print "S1: " , unit_norm_S1
print "S2: " , unit_norm_S2
print "S3: " , unit_norm_S3

plt.plot(x, y, 'ro', x_new, y_new)
plt.plot(x, y_actual, 'bo')

plt.title('Light Measuring Polarimetry')
plt.xlabel('Measurement Angles')
plt.ylabel('Intensity')

plt.show()

#initalize plotting
fig = plt.figure()
ax = fig.gca(projection='3d')


#draw poincare sphere
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z)
ax.scatter(unit_norm_S1, unit_norm_S2, unit_norm_S3, color="g", s=100)

plt.xlabel('S1')
plt.ylabel('S2')

plt.show()
