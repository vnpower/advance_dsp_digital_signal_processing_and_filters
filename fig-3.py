import pylab
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import firwin, freqz
from scipy import signal

x = pylab.linspace(0, 15, 20)
y = pylab.sin(x)/x
z = pylab.cos(np.pi*2*x/65)
fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.spines["left"].set_position(("data", 0))
ax1.spines["bottom"].set_position(("data", 0))

# Hide the top and right spines.
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

ax1.plot(1, 0, ">k", transform=ax1.get_yaxis_transform(), clip_on=False)
ax1.plot(0, 1, "^k", transform=ax1.get_xaxis_transform(), clip_on=False)

# Hide number in the axis
ax1.set_yticklabels([])
ax1.set_xticklabels([])
ax1.set_yticks([])
ax1.set_xticks([])
ax1.plot(x, z, 'o', label='WINDOW')
ax1.plot(x, y, '.', label='ORIGINAL IMPULSE RESPONSE')

ax1.legend(loc='upper right')
ax1.set(xlim=(-0.5, 30), ylim=(-0.5, 1.5))
ax1.set_xlabel('TIME', loc = 'right', fontsize = 11)
ax1.set_ylabel('RESPONSE', loc = 'top', rotation=90, fontsize = 11)


# Filter requirements
fs = 1000 # Sample rate, Hz
cutoff = 100 # Desired cutoff frequency, Hz
trans_width = 100 # Width of transition from pass band to stop band, Hz
numtaps = 101 # Size of the FIR filter

# Compute the filter coefficients using the firwin function
taps = firwin(numtaps, cutoff, window='hann', pass_zero=True, fs=fs)

# Compute the frequency response of the filter
w, h = freqz(taps, 1, worN=2000)

# Hide number in the axis
ax2.set_yticklabels([])
ax2.set_xticklabels([])
ax2.set_yticks([])
ax2.set_xticks([])
# Hide the top and right spines.
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

ax2.plot(1, 0, ">k", transform=ax2.get_yaxis_transform(), clip_on=False)
ax2.plot(0, 1, "^k", transform=ax2.get_xaxis_transform(), clip_on=False)
ax2.spines["left"].set_position(("data", 0))
ax2.spines["bottom"].set_position(("data", 0))

#ax2.set_title('Digital filter frequency response')
ax2.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
# ax2.set_ylabel('Amplitude [dB]', color='b')
ax2.set_ylabel('RESPONSE', fontsize = 11)
# ax2.set_xlabel('Frequency [Hz]')
ax2.set_xlabel('FREQUENCY', loc='right', fontsize = 11)
ax2.set_ylim([-0.2, 1.5])
ax2.set_xlim([-5, 0.3*fs])


plt.show()