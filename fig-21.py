import matplotlib.pyplot as plt
import numpy as np

N = 16
Fs = 10000
n = np.arange(0, N, 1)
T = 1/Fs
k = np.arange(0, N, 1)
fk = np.arange(0, Fs, 1)
wk = k/N*Fs
x = np.linspace(-2*np.pi, 2*np.pi, 100)
x1 = x + 1/3*np.pi
x2 = x - 1/3*np.pi
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(x, np.sinc(x))
ax1.plot(x, np.sinc(x2), dashes=[1, 1])
ax2.plot(x, np.sinc(x))
ax2.plot(x, np.sinc(x1), dashes=[1, 1])
ax2.plot(x, np.sinc(x2), dashes=[6, 2])

# Hide number in the axis
ax1.set_yticklabels([])
ax1.set_xticklabels([])
ax1.set_yticks([])
ax1.set_xticks([])
# Hide the top and right spines.
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.spines["bottom"].set_visible(False)
ax1.spines["left"].set_visible(False)
ax1.text(-6, -0.3, '(A)', fontsize = 9)

# Hide number in the axis
ax2.set_yticklabels([])
ax2.set_xticklabels([])
ax2.set_yticks([])
ax2.set_xticks([])
# Hide the top and right spines.
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.spines["bottom"].set_visible(False)
ax2.spines["left"].set_visible(False)
ax2.text(-6, 0.5, '(B)', fontsize = 9)

plt.show()