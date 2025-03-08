import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
x = np.linspace(0, 10, 100)
w1 = -0.5 * x + 8
w2 = -0.4 * x + 6
w3 = -0.1 * x + 5
w4 = 0.2 * x + 2
w5 = 0.6 * x - 1

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 4))

# Plot lines
ax.plot(x, w1, color='black')
ax.plot(x, w2, color='black')
ax.plot(x, w3, color='black')
ax.plot(x, w4, color='black')
ax.plot(x, w5, color='black')

# Remove border
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Draw arrows at the edges
ax.annotate("", xy=(10.5, 0), xytext=(-0.5, 0),
            arrowprops=dict(arrowstyle="->", color="black", lw=1.5))
ax.annotate("", xy=(0, 9), xytext=(0, -2),
            arrowprops=dict(arrowstyle="->", color="black", lw=1.5))

# Remove ticks
ax.set_xticks([])
ax.set_yticks([])

# Labels for axes
ax.text(10.5, -0.3, "VALUE OF TRANSITION COEFFICIENT", fontsize=12, ha='center', va='center')
ax.text(-0.5, 9.5, r"$H(e^{j\omega T})$", fontsize=12, ha='center', va='center', rotation=90)

# Annotate labels at the start of each line
ax.text(x[0], w1[0], r'$\omega_1$', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
ax.text(x[0], w2[0], r'$\omega_2$', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
ax.text(x[0], w3[0], r'$\omega_3$', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
ax.text(x[0], w4[0], r'$\omega_4$', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
ax.text(x[0], w5[0], r'$\omega_5$', fontsize=12, verticalalignment='bottom', horizontalalignment='right')

# Show plot
plt.show()
