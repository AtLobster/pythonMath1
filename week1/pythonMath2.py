from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr
import matplotlib as mpl

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

angles = np.array([30, 45, 60, 90, 120, 150, 180, 270])
angles_rad = np.deg2rad(angles)
colors = np.array(['red', 'green', 'blue', 'orange', 'purple', 'brown', 'pink', 'gray'])

text = [f'${angle}°$' for angle in angles]

x = np.cos(angles_rad)
y = np.sin(angles_rad)

plt.scatter(x, y, color=colors, marker='X')


for i in range(len(angles)):
    plt.annotate(text[i],
                xy=(x[i], y[i]), xycoords='data',
                xytext=(+30, +5), textcoords='offset points', fontsize=12,
                color=colors[i],
                arrowprops=dict(arrowstyle="->",
                               connectionstyle="arc3,rad=0",
                               color=colors[i]))

plt.show()