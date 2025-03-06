from scipy import interpolate, fft, signal
import matplotlib.pyplot as plt
import numpy as np

BW = 16
M = 3
T1 = 0.03095703
T2 = 0.27556998
T3 = 0.74434815
""" 
STEP-1:
Given N, the designer must determine how fine an interpolation should be used. 
For the designs we investigated, where N varied from 15 to 256, we found that 16 N sample values of H(ejwT) lead to reliable computations and results; i.e., 16 to 1 interpolation was used. 
"""
N = 64

""" 
STEP-2:
Given the set of N values of Hk, the FFT is used to compute h(n), the inverse DFT of Hk.
For both N odd and N even the set Hk which was used was real and symmetric;
therefore h(n) is real in all cases and symmetric for N odd. 
"""
n= np.arange(0, N, 1)
print(n)
# Given Hk
Hk = np.zeros(N)
Hk[0:BW] = 1
Hk[BW] = T3 # T3
Hk[BW+1] = T2 # T2
Hk[BW+2] = T1 # T1
Hk[N-BW-2] = T1 # T1
Hk[N-BW-1] = T2 # T2
Hk[N-BW] = T3 # T3
Hk[(N-BW+1):N] = 1
# print(Hk)

# Compute h(n) by IFFT
h = np.fft.ifft(Hk)
h = np.real(h)

fig, ax = plt.subplots()

"""  In order to obtain values of the interpolated frequency response one of two procedures is followed.
Either a) h(n) is rotated by N/2 samples ( N even) or
[(N- 1)/2] samples ( N odd) to remove the sharpedges of
the impulse response, and then 15 N zero-valued samples
are symmetrically placed around theimpulse response [as
illustrated in Fig. 9(A)]; or b) h(n) is split around the
(N/2)nd sample value, and 15 N zero-valued samples are
placed between the two pieces of the impulse response
[as illustratedin Fig. 9(B)]. The zero-augmentedsequences
of Fig. 9(A) and (B) are transformed using the FFT to
give the interpolated frequency responses. These two
procedures can easily be shown to yield identical results,
the differences being primarily computational ones. """

# Step 3: Rotate and join
HR = np.floor(16*N)
h_r = np.zeros(HR)
# h_r[(int(15*N/2)):(int(17*N/2))] = h
h1 = h[0:(int(N/2)+1):1]
h1 = h1[::-1]
h2 = h[(int(N/2+1)):N]
h2 = h2[::-1]
# h12 = np.concatenate((h1, h2))
h_r[int(15*N/2):(int(16*N/2)+1)] = h1
h_r[int(16*N/2)+1:int(17*N/2)] = h2
# print(h_r)

w, Hf = signal.freqz(h_r, [1], fs=10000)
Hf1 = np.fft.rfft(h_r, n=int(16*N))
f_Hf1 = np.arange(0, 5000, 5000/len(Hf1))
print(len(Hf1))
print(len(Hf))

Hf2 = np.fft.fft(h_r, n=int(16*N))
f_Hf2 = np.arange(0, 10000, 10000/len(Hf2))

# ax.plot(nn, h_r,)
# ax.stem(freq, np.abs(h_f), 'b', markerfmt=" ", basefmt="-b")
ax.plot(w, 20*np.log10(abs(Hf)), 'r', linewidth=0.5)
ax.plot(f_Hf1, 20*np.log10(abs(Hf1)), 'b', linewidth=0.5)
ax.plot(f_Hf2, 20*np.log10(abs(Hf2)), 'g', linewidth=0.5)
# ax.plot(nf, hf, 'r')
ax.text(3500, 10, 'BW = 16', fontsize = 9)
ax.text(3500, 0, 'M = 3', fontsize = 9)
ax.text(3500, -10, 'N = 64', fontsize = 9)
ax.axes.set_ylim(-180, 25)
ax.axes.set_ylabel('MAGNITUDE IN DB')
ax.axes.set_xlabel('FREQUENCY IN Hz')
ax.axes.set_xlim(0, 5000)
y_ticks = np.arange(-180, 40, 20)
ax.set_yticks(y_ticks)  # Set label locations
plt.show()