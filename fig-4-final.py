# Frequency sampling design of linear phase FIR filter 
import matplotlib.pyplot as plt 
from scipy import signal 
import numpy as np 

Fs = 10000 # Sampling Rate = 8kHz 
N = 16 # Filter Order 
# Create index n vector 
n = np.arange(0, N,1) 
# Frequency vector 
w = n*2*np.pi/N
wk = w 
# Linear Phase = -k*w 
k = np.floor((N-1)/2) 

# Define Ideal Lowpass Magnitude Response 
M = np.ones(N) 
M[4:13]=0 
D = M*np.exp(-1j*k*w) 

# Compute the impulse response h[n] by IFFT 
h = np.fft.ifft(D) 
h = np.real(h) 

wk, hk = signal.freqz(h, [1], worN=wk)

# Plot the Magnitude Response 
w, h = signal.freqz(h, [1], worN=Fs)
w1 = w + np.pi
w2 = np.concatenate((w, w1))
h1 = h[::-1]
h2 = np.concatenate((h, h1))


fig = plt.figure() 
ax1 = fig.add_subplot(1, 1, 1) 
#ax1.set_title('Lowpass Filter Desing by Frequency Sampling', color='b') 
ax1.plot(w2, abs(h2), 'r') 
ax1.plot(wk, abs(hk), '.')
ax1.set_ylabel('MAGNIITUDE') 
ax1.set_xlabel('FREQUENCY') 
#ax1.grid() 
ax1.axes.set_ylim([0, 1.2])
ax1.axes.set_xlim([0, 2*np.pi])
# Hide number in the axis
ax1.set_yticklabels([])
ax1.set_xticklabels([])
ax1.set_yticks([])
ax1.set_xticks([])
# Hide the top and right spines.
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

ax1.plot(1, 0, ">k", transform=ax1.get_yaxis_transform(), clip_on=False)
ax1.plot(0, 1, "^k", transform=ax1.get_xaxis_transform(), clip_on=False)
ax1.spines["left"].set_position(("data", 0))
ax1.spines["bottom"].set_position(("data", 0))
plt.axis('tight') 
plt.show()