import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt
plt.interactive(True)


var = pd.read_csv('output_data.txt', sep=',', header=None,
                  names=['delta_t', 'cte', 'speed', 'angle', 'steer', 'speed_target', 'throttle'])

delta_t = np.array(var.delta_t)
for i in range(len(var.delta_t)):
    time = np.cumsum(delta_t[:i+1])

################################################################

fig = plt.figure(figsize=(14, 8))

plt.subplot(2, 3, 1)
plt.plot(time, var.cte, color='k')
plt.xlabel('time [s]', fontsize=12)
plt.ylabel('cross-track error [m??]', fontsize=12)
plt.show()

plt.subplot(2, 3, 2)
plt.plot(time, var.speed, color='k')
plt.xlabel('time [s]', fontsize=12)
plt.ylabel('speed [mph]', fontsize=12)
plt.show()

plt.subplot(2, 3, 3)
plt.plot(time, var.angle, color='k')
plt.xlabel('time [s]', fontsize=12)
plt.ylabel('steering angle [degrees]', fontsize=12)
plt.show()

plt.subplot(2, 3, 4)
plt.plot(time, var.steer, color='k')
plt.xlabel('time [s]', fontsize=12)
plt.ylabel('steering angle [norm units]', fontsize=12)
plt.show()

plt.subplot(2, 3, 5)
plt.plot(time, var.speed_target, color='k')
plt.xlabel('time [s]', fontsize=12)
plt.ylabel('speed target [mph]', fontsize=12)
plt.show()

plt.subplot(2, 3, 6)
plt.plot(time, var.throttle, color='k')
plt.xlabel('time [s]', fontsize=12)
plt.ylabel('throttle [norm units]', fontsize=12)
plt.show()

fig.savefig('summary.jpg', dpi=None, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches='tight',
            pad_inches=0.1, frameon=None)

################################################################

fig = plt.figure(figsize=(14, 8))

plt.subplot(2, 1, 1)
plt.plot(time, var.cte, color='k')
plt.xlabel('time [s]', fontsize=12)
plt.ylabel('cross-track error', fontsize=12)
plt.show()

plt.subplot(2, 1, 2)
plt.plot(time, var.angle, color='k')
plt.xlabel('time [s]', fontsize=12)
plt.ylabel('steering angle [degrees]', fontsize=12)
plt.show()

fig.savefig('cte_and_steering.jpg', dpi=None, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches='tight',
            pad_inches=0.1, frameon=None)

################################################################

fig = plt.figure(figsize=(14, 8))

plt.subplot(2, 1, 1)
plt.plot(time, var.speed, color='k')
plt.xlabel('time [s]', fontsize=12)
plt.ylabel('speed [mph]', fontsize=12)
plt.show()

plt.subplot(2, 1, 2)
plt.plot(time, var.throttle, color='k')
plt.xlabel('time [s]', fontsize=12)
plt.ylabel('throttle [norm. units]', fontsize=12)
plt.show()

fig.savefig('speed_and_throttle.jpg', dpi=None, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches='tight',
            pad_inches=0.1, frameon=None)
