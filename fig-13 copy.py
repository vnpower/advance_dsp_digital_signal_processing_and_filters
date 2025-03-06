from scipy import interpolate, fft, signal
import matplotlib.pyplot as plt
import numpy as np

N = 16
H = np.zeros(N)
H[0] = 1
n= np.arange(0, N, 1)
w = 2*np.pi*n/N
fig, ax = plt.subplots()
Fs = 10000   # Sample rate, Hz
fs = np.arange(0, Fs, 1)*N/Fs
wf = 2*np.pi*fs/N

h = np.zeros(N)
for n in np.arange(N):
    h[n] = H[0] / N
    for k in np.arange(N):
        h[n] = h[n] + H[k]*np.exp(-1j*k*np.pi/N) * np.sin(n*N/2)/np.sin(n/2 - np.pi*k/N)
    h = h * np.exp(-1j*n*(N-1)/2)
    return h

h = freq_res(w)

h = np.real(h)
print(h)
ax.plot(w, 20*np.log(abs(h)), 'r')
# ax.plot(nf, hf, 'r')
plt.show()