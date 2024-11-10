import numpy as np
import matplotlib.pyplot as plt

X = np.linspace((3 * -np.pi),(3 *  np.pi), 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.figure(figsize=(15,5))

plt.plot(X,C, color='orange',
         linewidth=1.5,
         linestyle='--',
         marker='o',
         label='cos(x)')

plt.plot(X,S,
         color='purple',
         linewidth=1.5,
         linestyle=':',
         marker='o',
         label='sin(x)')

plt.axhline(y=0, color='black', linewidth=0.5)

plt.xticks( [-3*np.pi, -5/2*np.pi, -2*np.pi, -3/2*np.pi, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3/2*np.pi, 2*np.pi, 5/2*np.pi, 3*np.pi],
            [r'$-3\pi$', r'$-5\pi/2$', r'$-2\pi$', r'$-3\pi/2$', r'$-\pi$',
             r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$',
             r'$3\pi/2$', r'$2\pi$', r'$5\pi/2$', r'$3\pi$'])
plt.yticks([-1, 0, +1])

plt.legend(loc='upper left')
plt.show()