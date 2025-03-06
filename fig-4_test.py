import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
N = 16
BW = 3
#b = np.array([1, 1, 1, 1]) / N
b = np.ones(N) / N
b1=b+np.pi
b2=np.concatenate((b,b1))
#b[BW:(N-BW)] = 0
w, h = signal.freqz(b, worN=16)
h1 = h[::-1]
h2 = np.concatenate((h, h1))

plt.figure()
plt.title('Filter response')
#plt.plot(w , np.abs(h), 'b')
plt.plot(b2, np.abs(h2), 'b')
plt.grid()
plt.show()