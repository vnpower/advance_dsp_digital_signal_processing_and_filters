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

Gk = np.zeros(N)
Gk[0:BW] = 1
Gk[BW] = T3
Gk[BW+1] = T2
Gk[BW+2] = T1
Gk[N-BW-2] = -T1
Gk[N-BW-1] = -T2
Gk[N-BW] = -T3
Gk[(N-BW+1):N] = -1

# Compute h(n) by IFFT
h = np.fft.ifft(Hk)
h = np.real(h)

def h_n_imres(n):
    h_i = Gk[0]/N
    for k in range(1, int(N/2-1)):
        h_i += (1/N)*2*Gk[k]*np.cos(np.pi*k/N+2*np.pi/N*k*n)
    return h_i

h = h_n_imres(n)

fig = plt.figure(layout="constrained")
ax1 = plt.subplot2grid((8, 19), (0, 0), colspan=12, rowspan=8)
ax2 = plt.subplot2grid((8, 19), (0, 12), colspan=6, rowspan=2)
ax3 = plt.subplot2grid((8, 19), (2, 12), colspan=6, rowspan=2)
ax4 = plt.subplot2grid((8, 19), (4, 12), colspan=6, rowspan=2)
ax5 = plt.subplot2grid((8, 19), (6, 12), colspan=6, rowspan=2)

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
H_f = 20*np.log10(abs(Hf))
[w1, w2, w3, w4] = np.split(w, 4)
[H_f1, H_f2, H_f3, H_f4] = np.split(H_f, 4)
Hf1 = np.fft.rfft(h_r, n=int(16*N))
# ax.plot(nn, h_r,)
# ax.stem(freq, np.abs(h_f), 'b', markerfmt=" ", basefmt="-b")
# ax1.plot(w[0:1250], 20*np.log10(abs(Hf[0:1250])), 'r', linewidth=0.5)
#ax1.plot(w[0:1250], H_f[0:1250], 'r', linewidth=0.5)
ax2.plot(w1, H_f1, 'b', linewidth=1)
# ax.plot(nf, hf, 'r')
ax2.axes.set_ylim(-0.002, 0.002)
# ax1.axes.set_ylabel('MAGNITUDE IN DB')
ax2.axes.set_xlim(0, 1250)
ax2.set_yticks(np.arange(-0.002, 0.003, 0.001))  # Set label locations
ax2.set_xticks(np.arange(0, 1251, 250))
ax2.set_title('EXPANDED FREQUENCY RESPONSE', fontsize = 9)

ax3.plot(w2, H_f2, 'b', linewidth=1)
# ax.plot(nf, hf, 'r')
#ax2.axes.set_ylim(-3, 1)
# ax1.axes.set_ylabel('MAGNITUDE IN DB')
ax3.axes.set_ylabel('MAGNITUDE IN DB')
ax3.axes.set_xlim(1250, 2500)
ax3.set_yticks(np.arange(-3, 2, 1))  # Set label locations
ax3.set_xticks(np.arange(1250, 2750, 250))

ax4.plot(w3, H_f3, 'b', linewidth=1)
ax4.axes.set_xlim(2500, 3750)
ax4.set_ylim(-200, 0)
ax4.set_yticks(np.arange(-200, 1, 40))  # Set label locations
ax4.set_xticks(np.arange(2500, 4000, 250))

ax5.plot(w4, H_f4, 'b', linewidth=1)
ax5.axes.set_xlim(3750, 5000)
ax5.set_ylim(-160, -80)
ax5.set_yticks(np.arange(-160, -79, 20))  # Set label locations
ax5.set_xticks(np.arange(3750, 5001, 250))
ax5.axes.set_xlabel('FREQUENCY IN Hz')

ax1.plot(w, 20*np.log10(abs(Hf)), 'r', linewidth=0.5)
# ax.plot(nf, hf, 'r')
ax1.text(3500, 10, 'BW = 16', fontsize = 9)
ax1.text(3500, 0, 'M = 3', fontsize = 9)
ax1.text(3500, -10, 'N = 64', fontsize = 9)
ax1.axes.set_ylim(-180, 25)
ax1.axes.set_ylabel('MAGNITUDE IN DB')
ax1.axes.set_xlabel('FREQUENCY IN Hz')
ax1.axes.set_xlim(0, 5000)
y_ticks = np.arange(-180, 40, 20)
ax1.set_yticks(y_ticks)  # Set label locations

plt.show()