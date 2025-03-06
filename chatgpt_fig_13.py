import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Define filter parameters
N = 64  # Number of taps (must be even for Type-2)
fs = 10000  # Sampling frequency in Hz
cutoff = 3000  # Cutoff frequency in Hz
M = 3  # Additional parameter for display
BW = 16  # Bandwidth parameter for display
T1 = 0.03095703
T2 = 0.27556998
T3 = 0.74434815

# Create frequency sampling points (0 to Nyquist frequency)
num_frequencies = N // 2 + 1  # Only half the spectrum is specified
H = np.zeros(num_frequencies)  # Magnitude response

# Define the ideal magnitude response (Low-pass characteristics)
cutoff_idx = int(cutoff / (fs / 2) * num_frequencies)  # Cutoff index in frequency domain
print(cutoff_idx)
H[:cutoff_idx] = 1  # Passband (magnitude = 1)
H[cutoff_idx:] = 0  # Stopband (magnitude = 0)
H[16]=T3
H[17]=T2
H[18]=T1
print(H)
# Ensure Type-2 symmetry (Hermitian symmetry)
H_full = np.concatenate([H, H[-2:0:-1].conj()])  # Mirror for negative frequencies

# Compute impulse response using IFFT
h = np.fft.ifft(H_full).real  # Get real coefficients

# Apply shift to make it causal (center at N/2)
h = np.roll(h, N//2)

# Compute frequency response for visualization
w, H_freq = freqz(h, worN=2048, fs=fs)

# Convert to decibels
H_db = 20 * np.log10(abs(H_freq))

# Plot the frequency response
plt.figure(figsize=(7, 5))
plt.plot(w, H_db, 'k')  # Black line as in the original figure
plt.ylim(-220, 20)
plt.xlim(0, 5000)
plt.xlabel("FREQUENCY IN Hz")
plt.ylabel("MAGNITUDE IN dB")
plt.grid()

# Annotate parameters
plt.text(3000, -20, f"BW={BW}\nM={M}\nN={N}", fontsize=12)

# Add title and caption
plt.title("Fig. 25. The frequency response for a type-2 low-pass filter.")

# Show the plot
plt.show()
