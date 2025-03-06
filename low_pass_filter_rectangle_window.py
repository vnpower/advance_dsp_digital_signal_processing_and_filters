
import numpy as np
from scipy.signal import firwin, freqz
import matplotlib.pyplot as plt

# Filter requirements
fs = 1000 # Sample rate, Hz
cutoff = 100 # Desired cutoff frequency, Hz
trans_width = 100 # Width of transition from pass band to stop band, Hz
numtaps = 101 # Size of the FIR filter

# Compute the filter coefficients using the firwin function
taps = firwin(numtaps, cutoff, window='rectangular', pass_zero=True, fs=fs)

# Compute the frequency response of the filter
w, h = freqz(taps, 1, worN=2000)

# Plot the frequency response
fig, ax1 = plt.subplots()
#ax1.set_title('Digital filter frequency response')
ax1.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
# ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_ylabel('AMPLITUDE')
# ax1.set_xlabel('Frequency [Hz]')
ax1.set_xlabel('FREQUENCY')
ax1.set_ylim([-0.05, 1.5])
ax1.set_xlim([0, 0.3*fs])
ax1.grid()

plt.show()