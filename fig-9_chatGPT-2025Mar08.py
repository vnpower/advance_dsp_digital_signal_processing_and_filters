import numpy as np
import matplotlib.pyplot as plt

def generate_impulse_response(N=16):
    """Generate a sample impulse response h(n) as a sinc function."""
    n = np.arange(-N//2, N//2)
    h = np.sinc(n / 4)  # Example sinc function
    return n, h

def method_A(h, N):
    """Rotate h(n) and add zero-padding symmetrically."""
    h_rotated = np.roll(h, N//2)
    h_padded = np.pad(h_rotated, (15*N//2, 15*N//2), mode='constant')
    return h_padded

def method_B(h, N):
    """Split h(n) and add zero-padding in between."""
    half_N = N//2
    h_split = np.hstack((h[:half_N], np.zeros(15*N), h[half_N:]))
    return h_split

# Parameters
N = 16
n, h = generate_impulse_response(N)

# Compute both methods
h_A = method_A(h, N)
h_B = method_B(h, N)

# Plotting
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Method A visualization
axes[0].stem(np.arange(len(h_A)), h_A, basefmt=" ")
axes[0].set_title("Method A: Rotated and Zero-Padded")
axes[0].set_xlabel("n")
axes[0].set_ylabel("h(n)")
axes[0].grid()

# Method B visualization
axes[1].stem(np.arange(len(h_B)), h_B, basefmt=" ")
axes[1].set_title("Method B: Split and Zero-Padded")
axes[1].set_xlabel("n")
axes[1].grid()

plt.tight_layout()
plt.show()
