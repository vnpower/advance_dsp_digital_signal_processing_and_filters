# Frequency sampling design of linear phase FIR filter 
import matplotlib.pyplot as plt 
from scipy import signal 
import numpy as np 

Fs = 8000 # Sampling Rate = 8kHz 
N = 20 # Filter Order 
# Create index n vector 
n = np.arange(0, N,1) 
# Frequency vector 
w = n*2*np.pi/N 
# Linear Phase = -k*w 
k = np.floor((N-1)/2) 

# Define Ideal Lowpass Magnitude Response 
M = np.ones(N) 
M[2:18]=0 
D = M*np.exp(-1j*k*w) 

# Compute the impulse response h[n] by IFFT 
h = np.fft.ifft(D) 
h = np.real(h) 

# Plot the Magnitude Response 
w, h = signal.freqz(h, [1], fs=2000)
fig = plt.figure() 
ax1 = fig.add_subplot(1, 1, 1) 
ax1.set_title('Lowpass Filter Desing by Frequency Sampling', color='b') 
ax1.plot(w, abs(h), 'r') 
ax1.set_ylabel('Magnitude') 
ax1.set_xlabel('Frequency [Hz]') 
ax1.grid() 
plt.axis('tight') 
plt.show()