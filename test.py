import pylab
import matplotlib.pyplot as plt
x = pylab.linspace(0, 26, 51)
y = pylab.sin(x)/x
fig, ax = plt.subplots()
ax.spines["left"].set_position(("data", 0))
ax.spines["bottom"].set_position(("data", 0))

# Hide the top and right spines.
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Hide number in the axis
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_yticks([])
ax.set_xticks([])
ax.plot(x, y, '.')
ax.plot([16, 16], [-0.2,0.8],color = 'red', linewidth=1, linestyle='--')
ax.set(xlim=(-0.5, 30), ylim=(-0.5, 1.5))
ax.annotate('TRUNCATION POINT',
            xy=(16, 0), xycoords='data',
            xytext=(0.4, 0.8), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
ax.set_xlabel('TIME', loc = 'right', fontsize = 9)
ax.set_ylabel('IMPULSE RESPONSE', loc = 'top', rotation=90, fontsize = 9)
plt.show()