import numpy as np
import matplotlib.pyplot as plt

# Define parameters
N = 16
BW = 2
M = 3
T1, T2, T3 = 0.1, 0.5, 0.8  # Example threshold values

# Frequency response Hk
Hk = np.zeros(N)
Hk[:BW] = 1
Hk[BW] = T3
Hk[BW+1] = T2
Hk[BW+2] = T1
Hk[-BW-2] = T1
Hk[-BW-1] = T2
Hk[-BW] = T3
Hk[-BW+1:] = 1

# Plot
fig, ax = plt.subplots(figsize=(8, 4))
k = np.arange(N)

ax.plot(k, Hk, 'ko', markersize=5)  # Markers for points
ax.hlines([T1, T2, T3], 0, N-1, linestyles='dashdot', colors='k', linewidth=1)  # Dashed levels
#ax.hlines(1, 0, BW-1, colors='k', linewidth=2)  # BW range

ax.vlines(0, 1, 1.15, colors='k', linewidth=1)  # BW vertical line
ax.vlines(1, 1, 1.15, colors='k', linewidth=1)  # M vertical line

ax.vlines(BW, T3, 1, colors='k', linewidth=1)  # BW vertical line
ax.vlines(BW+M-1, T1, 1, colors='k', linewidth=1)  # M vertical line

# Labels and annotations
ax.text(0.3, 1, 'BW', fontsize=10, verticalalignment='bottom')
ax.text(BW + 1, 0.9, 'M', fontsize=10, verticalalignment='bottom')
ax.text(7, 1.05, 'N = 16\nBW = 2\nM = 3', fontsize=12, verticalalignment='top')

ax.annotate("", xy=(0, 1.1), xytext=(1, 1.1), textcoords=ax.transData, arrowprops=dict(arrowstyle='<->'))
ax.annotate("", xy=(BW, 0.9), xytext=(BW+M-1, 0.9), textcoords=ax.transData, arrowprops=dict(arrowstyle='<->'))

ax.set_xticks(np.arange(0, N, 1))
ax.set_yticks([0, T1, T2, T3, 1])
ax.set_yticklabels(["0.0", "T1", "T2", "T3", "1.0"])
ax.set_xlabel("k", loc='right')
ax.set_ylabel("H_k")

# Hide top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.show()
