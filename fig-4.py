import pylab
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import firwin, freqz
from scipy import signal

x = pylab.linspace(0, 26, 51)
y = pylab.sin(x)/x
fig, ax = plt.subplots()
ax.spines["left"].set_position(("data", 0))
ax.spines["bottom"].set_position(("data", 0))

# Hide the top and right spines.
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Hide number in the axis
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_yticks([])
ax.set_xticks([])

BW = 2
M = 3
T1 = 0.03095703
T2 = 0.27556998
T3 = 0.74434815
""" 
STEP-1:
Given N, the designer must determine how fine an interpolation should be used. 
For the designs we investigated, where N varied from 15 to 256, we found that 16 N sample values of H(ejwT) lead to reliable computations and results; i.e., 16 to 1 interpolation was used. 
"""
N = 16

""" 
STEP-2:
Given the set of N values of Hk, the FFT is used to compute h(n), the inverse DFT of Hk.
For both N odd and N even the set Hk which was used was real and symmetric;
therefore h(n) is real in all cases and symmetric for N odd. 
"""
n= np.arange(0, N, 1)
print(n)
# Given Hk
Hk = np.zeros(N)
Hk[0:BW] = 1
Hk[BW] = T3 # T3
Hk[BW+1] = T2 # T2
Hk[BW+2] = T1 # T1
Hk[N-BW-2] = T1 # T1
Hk[N-BW-1] = T2 # T2
Hk[N-BW] = T3 # T3
Hk[(N-BW+1):N] = 1
# print(Hk)

Gk = np.zeros(N)
Gk[0:BW] = 1
Gk[BW] = T3
Gk[BW+1] = T2
Gk[BW+2] = T1
Gk[N-BW-2] = -T1
Gk[N-BW-1] = -T2
Gk[N-BW] = -T3
Gk[(N-BW+1):N] = -1

# Compute h(n) by IFFT
h = np.fft.ifft(Hk)
h = np.real(h)

def h_n_imres(n):
    h_i = Gk[0]/N
    for k in range(1, int(N/2-1)):
        h_i += (1/N)*2*Gk[k]*np.cos(np.pi*k/N+2*np.pi/N*k*n)
    return h_i

h = h_n_imres(n)

# Compute h(n) by IFFT
#h = np.fft.ifft(Hk)
h = np.real(h)


# Step 3: Rotate and join
HR = np.floor(16*N)
h_r = np.zeros(HR)
# h_r[(int(15*N/2)):(int(17*N/2))] = h
h1 = h[0:(int(N/2)+1):1]
h1 = h1[::-1]
h2 = h[(int(N/2+1)):N]
h2 = h2[::-1]
# h12 = np.concatenate((h1, h2))
h_r[int(15*N/2):(int(16*N/2)+1)] = h1
h_r[int(16*N/2)+1:int(17*N/2)] = h2
# print(h_r)

w, Hf = signal.freqz(h, [1], fs=10000)
ax.plot(w, np.abs(Hf), 'r', linewidth=0.5)

plt.show()