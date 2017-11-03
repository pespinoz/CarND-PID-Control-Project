import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt
plt.interactive(True)


var = pd.read_csv('output_data.txt', sep=',', header=None, names=['delta_t', 'cte', 'speed', 'angle', 'steer'])

delta_t = np.array(var.delta_t)
for i in range(len(var.delta_t)):
    time = np.cumsum(delta_t[:i+1])

################################################################

fig = plt.figure(figsize=(14, 8))

plt.subplot(2, 2, 1)
plt.plot(time, var.cte, color='k')
plt.xlabel('time in s', fontsize=12)
plt.ylabel('cross-track error in m??', fontsize=12)
plt.show()

plt.subplot(2, 2, 2)
plt.plot(time, var.speed, color='k')
plt.xlabel('time in s', fontsize=12)
plt.ylabel('speed in m/s', fontsize=12)
plt.show()

plt.subplot(2, 2, 3)
plt.plot(time, var.angle, color='k')
plt.xlabel('time in s', fontsize=12)
plt.ylabel('angle in rad??', fontsize=12)
plt.show()

plt.subplot(2, 2, 4)
plt.plot(time, var.steer, color='k')
plt.xlabel('time in s', fontsize=12)
plt.ylabel('steering angle in rad??', fontsize=12)
plt.show()

#fig.savefig('figures/py_vs_px.jpg', dpi=None, facecolor='w', edgecolor='w',
#            orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches='tight',
#            pad_inches=0.1, frameon=None)

