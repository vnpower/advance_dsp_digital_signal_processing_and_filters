import numpy as np
import matplotlib.pyplot as plt

# Define Line 1 (through A, B, C)
x1 = np.linspace(0.06, 0.6, 100)
y1 = 0.75 * x1 + 0.64  # Linear equation for Line 1

# Define Line 2 (through D, E, F)
x2 = np.linspace(0.15, 0.28, 100)
y2 = 4.8 * x2 - 0.42  # Linear equation for Line 2

# Define points on the respective lines
points = {
    "A": (0.48, 0.75*0.48+0.64),  # Lies on Line 1
    "B": (0.4, 0.75 * 0.4 + 0.64),  # Lies on Line 1
    "C": (0.21, 0.75 * 0.21 + 0.64),  # Lies on Line 1
    "D": (0.254, 4.8 * 0.254 - 0.42),  # Lies on Line 2
    "E": (0.24, 4.8 * 0.24 - 0.42),  # Lies on Line 2
    "F": (0.21, 4.8 * 0.21 - 0.42),  # Lies on Line 2
}

# Create the plot
fig, ax = plt.subplots(figsize=(5, 5))

# Plot the lines
ax.plot(x1, y1, 'k', label="Line 1")
ax.plot(x2, y2, 'k', label="Line 2")

# Plot and label points
for label, (x, y) in points.items():
    ax.plot(x, y, 'ko')  # Black dots
    ax.text(x, y-0.04, label, fontsize=10, verticalalignment='bottom')

# Labels and formatting
ax.set_xlabel(r"$T_1$", fontsize=12)
ax.set_ylabel(r"$T_2$", fontsize=12)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.2)
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(["0.0", "1.0"])
ax.set_yticklabels(["0.0", "1.0"])

# Move spines to create origin at (0,0)
ax.spines["left"].set_position(("data", 0))
ax.spines["bottom"].set_position(("data", 0))
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add arrows at the ends of axes
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

plt.show()
