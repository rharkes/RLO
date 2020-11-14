"""
A simple v-t graph of a falling object with air resistance
In python with matplotlib
"""
from matplotlib import pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

# run a simulation of a falling object
t = [0.0]  # a list with the timepoints
v = [0.0]  # a list with the velocities
dt = 0.001  # seconds
t_end = 2  # simulation time
a = 9.81  # free faling acceleration
c = 0.2  # a = F/m = (.5*rho*A*cw*v**2)/m  put all constants in c.
while t[-1] < t_end:  # check last value of t
    t.append(t[-1] + dt)
    a = 9.81 - c * (v[-1] ** 2)
    v.append(v[-1] + a * dt)

# start plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(t, v)
plt.xlim([0, 3])
plt.ylim([0, 10])
# extra control over the ticks:
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
plt.grid(b=True, which='major', axis='both', alpha=1, color=[0, 0, 0])
plt.grid(b=True, which='minor', axis='both', alpha=0.5, color=[0, 0, 0])
plt.minorticks_on()
# label the axis
plt.xlabel('tijd (s)')
plt.ylabel('snelheid (m/s)')
plt.show()
fig.savefig("falling.png", dpi=600)