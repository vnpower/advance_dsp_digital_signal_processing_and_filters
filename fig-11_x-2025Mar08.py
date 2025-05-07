import numpy as np
import matplotlib.pyplot as plt

# Define x-axis range (transition coefficient values)
x = np.linspace(0, 13, 100)
x1 = np.linspace(0.5, 10, 100)
x2 = np.linspace(1, 11.5, 100)
x3 = np.linspace(1.5, 12, 100)
x4 = np.linspace(2, 12.5, 100)
x5 = np.linspace(5, 13, 100)

# Define five different lines representing different ω values
y1 = -0.75 * x1 + 8
y2 = -0.4 * x2 + 6.5
y3 = -0.15 * x3 + 4
y4 = 0.3 * x4 + 1.5
y5 = 0.8 * x5 - 3

# Create the plot
fig, ax = plt.subplots(figsize=(6, 4))

ax.plot(x1, y1, 'k', label=r'$\omega_1$')
ax.plot(x2, y2, 'k', label=r'$\omega_2$')
ax.plot(x3, y3, 'k', label=r'$\omega_3$')
ax.plot(x4, y4, 'k', label=r'$\omega_4$')
ax.plot(x5, y5, 'k', label=r'$\omega_5$')

# Annotate the ω values at the left side of the graph
ax.text(x1[0], y1[0], r'$\omega_1$', fontsize=12, verticalalignment='bottom')
ax.text(x2[0], y2[0], r'$\omega_2$', fontsize=12, verticalalignment='bottom')
ax.text(x3[0], y3[0], r'$\omega_3$', fontsize=12, verticalalignment='bottom')
ax.text(x4[0], y4[0]+0.2, r'$\omega_4$', fontsize=12, verticalalignment='bottom')
ax.text(x5[0]-0.5, y5[0], r'$\omega_5$', fontsize=12, verticalalignment='bottom')

# Labels and formatting
ax.set_xlabel("VALUE OF TRANSITION COEFFICIENT", fontsize=10)
ax.set_ylabel(r"$H(e^{j\omega T})$", fontsize=10)



ax.spines["left"].set_position(("data", 0))
ax.spines["bottom"].set_position(("data", 0))
# Hide the top and right spines.
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add arrows at the end of axes

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Hide number in the axis
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_yticks([])
ax.set_xticks([])

plt.show()
