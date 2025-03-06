from scipy import interpolate, fft, signal
import matplotlib.pyplot as plt
import numpy as np

numtaps = 19
fL1 = 100
fL2 = 200
fH1 = 500
fH2 = 600
fs  = 1600
Bl  = 2
Bh  = 2.3

# bands = [0, fL1, fL2, fH1, fH2, fs/2]
# desired = [Bl, 1, Bh]

bands   = [0, 100, 180, 520, 600, fs/2]
desired = [1.966,1.966,0.980,0.980,2.225,2.225]

# interpolate desired response at equally spaced frequency points
interpolator = interpolate.interp1d(bands, desired)
N = 1024
fsampling = np.linspace(0, fs/2, N)
sampled = interpolator(fsampling)
# take the inverse FFT
y = fft.fftshift(fft.irfft(sampled))
# truncate response to keep numtaps coefficients
n1 = N-numtaps//2
n2 = n1 + numtaps
y = y[n1:n2]

plt.plot(bands, desired, 'k', linewidth=2)
plt.show()
# plt.plot(f, np.abs(h), 'b')