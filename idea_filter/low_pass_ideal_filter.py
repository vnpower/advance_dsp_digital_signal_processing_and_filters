import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(nrows=6)
# Move the left and bottom spines to x = 0 and y = 0, respectively.
ax1.spines["left"].set_position(("data", 0))
ax1.spines["bottom"].set_position(("data", 0))
# Hide the top and right spines.
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

# Draw arrows (as black triangles: ">k"/"^k") at the end of the axes.  In each
# case, one of the coordinates (0) is a data coordinate (i.e., y = 0 or x = 0,
# respectively) and the other one (1) is an axes coordinate (i.e., at the very
# right/top of the axes).  Also, disable clipping (clip_on=False) as the marker
# actually spills out of the axes.
ax1.plot(1, 0, ">k", transform=ax1.get_yaxis_transform(), clip_on=False)
ax1.plot(0, 1, "^k", transform=ax1.get_xaxis_transform(), clip_on=False)

# Hide number in the axis
ax1.set_yticklabels([])
ax1.set_xticklabels([])
ax1.set_yticks([])
ax1.set_xticks([])


# initialize x and y coordinates 
x1 = [-0.5, -0.5, 0.5, 0.5, 3, 3, 4, 4] 
y1 = [0, 1, 1, 0, 0, 1, 1, 0] 

# set the title of a plot 
# ax1.set_title('AX1 TITLE', position=(1, 2), ha='left', va='center', fontsize=5, color='red')
ax1.text(5.6, 1.1, '(A)', fontsize = 9)
ax1.text(5.6, 0.7, 'LOW-PASS', fontsize = 9)
ax1.text(5.6, 0.3, 'DESIGN', fontsize = 9)

# Set title of x-axis and y-axis
ax1.set_xlabel('FREQUENCY', loc = 'right', fontsize = 9)
ax1.set_ylabel('MAGNITUDE', loc = 'top', rotation=0, fontsize = 9)

# plot scatter plot with x and y data 
ax1.scatter([-1.2, -1, -0.8, 4.2, 4.5, 4.7], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5], s=1) 
  
# plot with x and y data 
ax1.plot(x1, y1)
ax1.plot([0, 0], [-0.7,1.2],color = 'red')
ax1.plot([3.5, 3.5], [-0.7,1.2],color = 'red')

ax1.annotate("", xy=(0, -0.5), xytext=(3.5, -0.5), textcoords=ax1.transData, arrowprops=dict(arrowstyle='<->'))
# ax1.annotate("", xy=(0, -0.5), xytext=(3.5, -0.5), textcoords=ax1.transData, arrowprops=dict(arrowstyle='|-|'))
bbox=dict(fc="white", ec="none")
ax1.text(3.5/2, -0.6, "1/T", ha="center", va="center", bbox=bbox, fontsize = 9)

#ax1.plot(6, 0)
ax1.set(xlim=(-1.5, 5.5), ylim=(-0.7, 1.7))

#----------------------------------------------
# Move the left and bottom spines to x = 0 and y = 0, respectively.
ax2.spines["left"].set_position(("data", 0))
ax2.spines["bottom"].set_position(("data", 0))
# Hide the top and right spines.
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

# Hide number in the axis
ax2.set_yticklabels([])
ax2.set_xticklabels([])
ax2.set_yticks([])
ax2.set_xticks([])


# initialize x and y coordinates 
x2 = [-1, -0.75, -0.75, 0.75, 0.75, 2.75, 2.75, 4.25, 4.25, 4.5] 
y2 = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1] 

# set the title of a plot 
# ax2.set_title('ax2 TITLE', position=(1, 2), ha='left', va='center', fontsize=5, color='red')
ax2.text(5.6, 1.1, '(B)', fontsize = 9)
ax2.text(5.6, 0.7, 'HIGH-PASS', fontsize = 9)
ax2.text(5.6, 0.3, 'DESIGN', fontsize = 9)

# plot scatter plot with x and y data 
ax2.scatter([-1.2, -1, -0.8, 4.7, 4.9, 5.1], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5], s=1) # s=1 is the size of the dot
  
# plot with x and y data 
ax2.plot(x2, y2)
ax2.plot([0, 0], [-0.7,1.2],color = 'red', linewidth=0.5)
ax2.plot([3.5, 3.5], [-0.7,1.2],color = 'red', linewidth=0.5)
ax2.plot([3.5/2, 3.5/2], [-0.7,1.2],color = 'red', linewidth=0.5, linestyle='--')

ax2.annotate("", xy=(0, -0.5), xytext=(3.5/2, -0.5), textcoords=ax2.transData, arrowprops=dict(arrowstyle='<->'))
ax2.annotate("", xy=(3.5/2, -0.5), xytext=(3.5, -0.5), textcoords=ax2.transData, arrowprops=dict(arrowstyle='<->'))
bbox=dict(fc="white", ec="none")
ax2.text(3.5/4, -0.6, "1/2T", ha="center", va="center", bbox=bbox, fontsize = 9)
ax2.text(3.5*3/4, -0.6, "1/2T", ha="center", va="center", bbox=bbox, fontsize = 9)

ax2.set(xlim=(-1.5, 5.5), ylim=(-0.7, 1.7))

#----------------------------------------------
#----------------------------------------------
# Move the left and bottom spines to x = 0 and y = 0, respectively.
ax3.spines["left"].set_position(("data", 0))
ax3.spines["bottom"].set_position(("data", 0))
# Hide the top and right spines.
ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)

# Hide number in the axis
ax3.set_yticklabels([])
ax3.set_xticklabels([])
ax3.set_yticks([])
ax3.set_xticks([])

# initialize x and y coordinates 
x3 = [-0.75, -0.75, -0.25, -0.25, 0.25, 0.25, 0.75, 0.75, 2.75, 2.75, 3.25, 3.25, 3.75, 3.75, 4.25, 4.25] 
y3 = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0] 

# set the title of a plot 
ax3.text(5.6, 1.1, '(C)', fontsize = 9)
ax3.text(5.6, 0.7, 'BAND-PASS', fontsize = 9)
ax3.text(5.6, 0.3, 'DESIGN', fontsize = 9)

# plot scatter plot with x and y data 
ax3.scatter([-1.2, -1, -0.8, 4.7, 4.9, 5.1], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5], s=1) # s=1 is the size of the dot
  
# plot with x and y data 
ax3.plot(x3, y3)
ax3.plot([0, 0], [-0.7,1.2],color = 'red', linewidth=0.5)
ax3.plot([3.5, 3.5], [-0.7,1.2],color = 'red', linewidth=0.5)

ax3.set(xlim=(-1.5, 5.5), ylim=(-0.7, 1.7))

#----------------------------------------------
#----------------------------------------------
# Move the left and bottom spines to x = 0 and y = 0, respectively.
ax4.spines["left"].set_position(("data", 0))
ax4.spines["bottom"].set_position(("data", 0))
# Hide the top and right spines.
ax4.spines["top"].set_visible(False)
ax4.spines["right"].set_visible(False)

# Hide number in the axis
ax4.set_yticklabels([])
ax4.set_xticklabels([])
ax4.set_yticks([])
ax4.set_xticks([])


# initialize x and y coordinates 
x4 = [-1, -0.75, -0.75, -0.5, -0.5, 0.5, 0.5, 0.75, 0.75, 2.75, 2.75, 3, 3, 4, 4, 4.25, 4.25, 4.5] 
y4 = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1] 

# set the title of a plot 
ax4.text(5.6, 1.1, '(D)', fontsize = 9)
ax4.text(5.6, 0.7, 'BAND-', fontsize = 9)
ax4.text(5.6, 0.3, 'ELIMINATION', fontsize = 9)
ax4.text(5.6, -0.1, 'DESIGN', fontsize = 9)

# plot scatter plot with x and y data 
ax4.scatter([-1.2, -1, -0.8, 4.7, 4.9, 5.1], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5], s=1) # s=1 is the size of the dot
  
# plot with x and y data 
ax4.plot(x4, y4)
ax4.plot([0, 0], [-0.7,1.2],color = 'red', linewidth=0.5)
ax4.plot([3.5, 3.5], [-0.7,1.2],color = 'red', linewidth=0.5)

ax4.set(xlim=(-1.5, 5.5), ylim=(-0.7, 1.7))

#----------------------------------------------

#----------------------------------------------
# Move the left and bottom spines to x = 0 and y = 0, respectively.
ax5.spines["left"].set_position(("data", 0))
ax5.spines["bottom"].set_position(("data", 0))
# Hide the top and right spines.
ax5.spines["top"].set_visible(False)
ax5.spines["right"].set_visible(False)

# Hide number in the axis
ax5.set_yticklabels([])
ax5.set_xticklabels([])
ax5.set_yticks([])
ax5.set_xticks([])

ax5.set_ylabel('IMAGINARY', loc = 'top', rotation=0, fontsize = 9)

# initialize x and y coordinates 
x5 = [-0.75, 1.75, 1.75, 4.25] 
y5 = [-0.25, 0.5, -0.5, 0.25] 

# set the title of a plot 
# ax5.text(5.6, 1.1, '(E)', fontsize = 9)
ax5.text(5.6, 0.7, '(E)', fontsize = 9)
ax5.text(5.6, 0.3, 'DIFFERENTIATOR', fontsize = 9)

# plot scatter plot with x and y data 
ax5.scatter([-1.2, -1, -0.8, 4.7, 4.9, 5.1], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5], s=1) # s=1 is the size of the dot
  
# plot with x and y data 
ax5.plot(x5, y5)
ax5.plot([0, 0], [-0.7,1.2],color = 'red', linewidth=0.5)
ax5.plot([3.5, 3.5], [-0.7,1.2],color = 'red', linewidth=0.5)

ax5.set(xlim=(-1.5, 5.5), ylim=(-0.7, 1.7))

#----------------------------------------------

#----------------------------------------------
# Move the left and bottom spines to x = 0 and y = 0, respectively.
ax6.spines["left"].set_position(("data", 0))
ax6.spines["bottom"].set_position(("data", 0))
# Hide the top and right spines.
ax6.spines["top"].set_visible(False)
ax6.spines["right"].set_visible(False)

# Hide number in the axis
ax6.set_yticklabels([])
ax6.set_xticklabels([])
ax6.set_yticks([])
ax6.set_xticks([])

ax6.set_ylabel('PHASE', loc = 'top', rotation=0, fontsize = 9)

# initialize x and y coordinates 
x6 = [-1, 0, 0, 1.75, 1.75, 3.5, 3.5, 4.25] 
y6 = [-0.5, -0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5] 

# set the title of a plot 
ax6.text(5.6, 1.1, '(F)', fontsize = 9)
ax6.text(5.6, 0.7, 'HILBERT', fontsize = 9)
ax6.text(5.6, 0.3, 'TRANSFORMER', fontsize = 9)

# plot scatter plot with x and y data 
ax6.scatter([-1.2, -1, -0.8, 4.7, 4.9, 5.1], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5], s=1) # s=1 is the size of the dot
  
# plot with x and y data 
ax6.plot(x6, y6)
ax6.plot([0, 0], [-0.7,1.2],color = 'red', linewidth=0.5)
ax6.plot([3.5, 3.5], [-0.7,1.2],color = 'red', linewidth=0.5)

ax6.set(xlim=(-1.5, 5.5), ylim=(-0.7, 1.7))

#----------------------------------------------

plt.show()