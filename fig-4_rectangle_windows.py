import pylab
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import firwin, freqz

fig, ax = plt.subplots()

# Filter requirements
fs = 10000 # Sample rate, Hz
cutoff = 2000 # Desired cutoff frequency, Hz
trans_width = 200 # Width of transition from pass band to stop band, Hz
numtaps = 16 # Size of the FIR filter

k = np.arange(0, numtaps)
wk = 2*np.pi*k/numtaps
Hk = np.zeros(numtaps)

Hk[0] = 1
Hk[1] = 1
Hk[2] = 1
Hk[3] = 1
Hk[numtaps-1] = 1
Hk[numtaps-2] = 1
Hk[numtaps-3] = 1

# Compute the filter coefficients using the firwin function
taps = firwin(numtaps, cutoff, window='rectangular', pass_zero=True, fs=fs)

# Compute the frequency response of the filter
w, h = freqz(taps, [1], worN=fs)
w_k, h_k = freqz(taps, [1], worN=[wk])


w1 = w + np.pi
w2 = np.concatenate((w, w1))
h1 = h[::-1]
h2 = np.concatenate((h, h1))

#print(w)
# Hide number in the axis
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_yticks([])
ax.set_xticks([])
# Hide the top and right spines.
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
ax.spines["left"].set_position(("data", 0))
ax.spines["bottom"].set_position(("data", 0))

#ax2.set_title('Digital filter frequency response')
ax.plot(w2, np.abs(h2), 'b')
#ax.plot(wk, Hk, '.')
ax.plot(w_k, np.abs(h_k), '.')
#ax.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
# ax2.set_ylabel('Amplitude [dB]', color='b')
ax.set_ylabel('RESPONSE', fontsize = 11)
# ax2.set_xlabel('Frequency [Hz]')
ax.set_xlabel('FREQUENCY', loc='right', fontsize = 11)
#ax2.set_ylim([-0.2, 1.5])
#ax2.set_xlim([-5, 0.3*fs])


plt.show()