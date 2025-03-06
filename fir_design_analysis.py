import matplotlib.pyplot as plt
import scipy.signal as sig
import numpy as np
from math import pi

plt.close('all')

# Design IIR butterworth filter
Fs = 1000;
n = 5;
fc = np.array([100, 300]);

w_c = 2*fc/Fs;
[b,a] = sig.butter(n, w_c,btype='lowpass')

# Frequency response
[w,h] = sig.freqz(b,a,worN = 2000)
w = Fs*w/(2*pi)

h_db = 20*np.log10(abs(h))

plt.figure()
plt.plot(w, h_db)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude(dB)')
plt.grid('on')
