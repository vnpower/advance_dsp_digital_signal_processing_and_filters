import matplotlib.pyplot as plt

""" fig = plt.figure()
fig.add_subplot(1, 2, 1, colspan)   #top and bottom left
fig.add_subplot(3, 2, 2)   #top right
fig.add_subplot(3, 2, 4)   #bottom right 
fig.add_subplot(3, 2, 6)   #bottom right  """

fig = plt.figure(layout="constrained")

""" ax1 = plt.subplot2grid((4, 8), (0, 0), colspan=5, rowspan=4)
ax2 = plt.subplot2grid((4, 8), (0, 5), colspan=3)
ax3 = plt.subplot2grid((4, 8), (1, 5), colspan=3)
ax4 = plt.subplot2grid((4, 8), (2, 5), colspan=3)
ax4 = plt.subplot2grid((4, 8), (3, 5), colspan=3) """

ax1 = plt.subplot2grid((8, 19), (0, 0), colspan=12, rowspan=8)
ax2 = plt.subplot2grid((8, 19), (0, 12), colspan=6, rowspan=2)
ax3 = plt.subplot2grid((8, 19), (2, 12), colspan=6, rowspan=2)
ax4 = plt.subplot2grid((8, 19), (4, 12), colspan=6, rowspan=2)
ax5 = plt.subplot2grid((8, 19), (6, 12), colspan=6, rowspan=2)

plt.show()