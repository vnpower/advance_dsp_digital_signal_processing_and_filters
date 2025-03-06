from scipy import interpolate, fft, signal
import matplotlib.pyplot as plt
import numpy as np

N = 16
M = 3
BW = 3
T1 = 0.2
T2 = 0.7
T3 = 0.9

n= np.arange(0, N, 1) # n = 0 to N-1
Hk = np.zeros(N)
Hk[0:BW] = 1
Hk[BW] = T3
Hk[BW+1] = T2
Hk[BW+2] = T1
Hk[N-BW-2] = T1
Hk[N-BW-1] = T2
Hk[N-BW] = T3
Hk[(N-BW+1):N] = 1

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
k = np.fft.ifft(Hk)
k = np.real(k)
#print(k)
fig, ax = plt.subplots()

def h_n_impluse_response(n):
    h_n = np.zeros(N)
    for i in n:
        h_n[i] = Gk[0]/N
        for k in range(1, int(N/2-1)):
            h_n[i] += (1/N)*2*Gk[k]*np.cos(np.pi*k/N+2*np.pi/N*k*i)
    return h_n
def h_n_imres(n):
    h_i = Gk[0]/N
    for k in range(1, int(N/2-1)):
        h_i += (1/N)*2*Gk[k]*np.cos(np.pi*k/N+2*np.pi/N*k*n)
    return h_i

# h = h_n_impluse_response(n)
h = h_n_imres(n)
ax.plot(n, h, 'r', linewidth=1)
ax.plot(n, h, '.')
#ax.plot(n, k, 'b', linewidth=0.5)
ax.set_xticks(np.arange(0, N, 1))
ax.plot([7.5, 7.5], [-0.1, 0.5], 'k--', linewidth=0.5)
ax.axes.set_ylabel('Impulse Response, h(n)')
ax.axes.set_xlabel('n', loc='right')
ax.annotate('SYMMETRY ORIGIN',
            xy=(7.5, 0.2), xycoords='data',
            xytext=(0.4, 0.8), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
#ax.plot(n, k, '.')
# Hide number in the axis
ax.set_yticklabels([])
#ax.set_xticklabels([])
ax.set_yticks([])
#ax.set_xticks([])
# Hide the top and right spines.
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
ax.spines["left"].set_position(("data", 0))
ax.spines["bottom"].set_position(("data", 0))


plt.show()