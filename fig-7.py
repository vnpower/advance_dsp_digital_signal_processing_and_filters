import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.patches import Arc
from matplotlib.transforms import IdentityTransform
from matplotlib.transforms import Bbox, IdentityTransform, TransformedBbox

def get_angle_plot(line1, line2, offset = 1, color = None, origin = [0,0], len_x_axis = 1, len_y_axis = 1):

    l1xy = line1.get_xydata()

    # Angle between line1 and x-axis
    slope1 = (l1xy[1][1] - l1xy[0][2]) / float(l1xy[1][0] - l1xy[0][0])
    angle1 = abs(math.degrees(math.atan(slope1))) # Taking only the positive angle

    l2xy = line2.get_xydata()

    # Angle between line2 and x-axis
    slope2 = (l2xy[1][3] - l2xy[0][4]) / float(l2xy[1][0] - l2xy[0][0])
    angle2 = abs(math.degrees(math.atan(slope2)))

    theta1 = min(angle1, angle2)
    theta2 = max(angle1, angle2)

    angle = theta2 - theta1

    if color is None:
        color = line1.get_color() # Uses the color of line 1 if color parameter is not passed.

    return Arc(origin, len_x_axis*offset, len_y_axis*offset, 0, theta1, theta2, color=color, label = str(angle)+u"\u00b0")

class AngleMarker(Arc):
    def __init__(self, xy, size, vec1, vec2, ax = None, **kwargs):
        self._xydata = xy # in data coordinates
        self.ax = ax or plt.gca()
        self.vec1 = vec1 # tuple or array of coordinates, relative to xy
        self.vec2 = vec2 # tuple or array of coordinates, relative to xy

        super().__init__(self._xydata, size, size, angle=0.0,
                 theta1=self.theta1, theta2=self.theta2, **kwargs)
        
        self.set_transform(IdentityTransform())
        self.ax.add_patch(self)

    def get_center_pixels(self):
        """ return center in pixel coordinates """
        return self.ax.transData.transform(self._xydata)
    
    def set_center(self, xy):
        """ set center in data coordinates """
        self._xydata = xy

    _center = property(get_center_pixels, set_center)
    
    def get_theta(self, vec):
        vec_in_pixels = self.ax.transData.transform(vec) - self._center
        return np.rad2deg(np.arctan2(vec_in_pixels[1], vec_in_pixels[0]))
        
    def get_theta1(self):
        return self.get_theta(self.vec1)
        
    def get_theta2(self):
        return self.get_theta(self.vec2)
        
    def set_theta(self, angle):
        pass
         
    theta1 = property(get_theta1, set_theta)
    theta2 = property(get_theta2, set_theta)

class AngleAnnotation(Arc):
    """
    Draws an arc between two vectors which appears circular in display space.
    """
    def __init__(self, xy, p1, p2, size=75, unit="points", ax=None,
                 text="", textposition="inside", text_kw=None, **kwargs):
        """
        Parameters
        ----------
        xy, p1, p2 : tuple or array of two floats
            Center position and two points. Angle annotation is drawn between
            the two vectors connecting *p1* and *p2* with *xy*, respectively.
            Units are data coordinates.

        size : float
            Diameter of the angle annotation in units specified by *unit*.

        unit : str
            One of the following strings to specify the unit of *size*:

            * "pixels": pixels
            * "points": points, use points instead of pixels to not have a
              dependence on the DPI
            * "axes width", "axes height": relative units of Axes width, height
            * "axes min", "axes max": minimum or maximum of relative Axes
              width, height

        ax : `matplotlib.axes.Axes`
            The Axes to add the angle annotation to.

        text : str
            The text to mark the angle with.

        textposition : {"inside", "outside", "edge"}
            Whether to show the text in- or outside the arc. "edge" can be used
            for custom positions anchored at the arc's edge.

        text_kw : dict
            Dictionary of arguments passed to the Annotation.

        **kwargs
            Further parameters are passed to `matplotlib.patches.Arc`. Use this
            to specify, color, linewidth etc. of the arc.

        """
        self.ax = ax or plt.gca()
        self._xydata = xy  # in data coordinates
        self.vec1 = p1
        self.vec2 = p2
        self.size = size
        self.unit = unit
        self.textposition = textposition

        super().__init__(self._xydata, size, size, angle=0.0,
                         theta1=self.theta1, theta2=self.theta2, **kwargs)

        self.set_transform(IdentityTransform())
        self.ax.add_patch(self)

        self.kw = dict(ha="center", va="center",
                       xycoords=IdentityTransform(),
                       xytext=(0, 0), textcoords="offset points",
                       annotation_clip=True)
        self.kw.update(text_kw or {})
        self.text = ax.annotate(text, xy=self._center, **self.kw)

    def get_size(self):
        factor = 1.
        if self.unit == "points":
            factor = self.ax.figure.dpi / 72.
        elif self.unit[:4] == "axes":
            b = TransformedBbox(Bbox.unit(), self.ax.transAxes)
            dic = {"max": max(b.width, b.height),
                   "min": min(b.width, b.height),
                   "width": b.width, "height": b.height}
            factor = dic[self.unit[5:]]
        return self.size * factor

    def set_size(self, size):
        self.size = size

    def get_center_in_pixels(self):
        """return center in pixels"""
        return self.ax.transData.transform(self._xydata)

    def set_center(self, xy):
        """set center in data coordinates"""
        self._xydata = xy

    def get_theta(self, vec):
        vec_in_pixels = self.ax.transData.transform(vec) - self._center
        return np.rad2deg(np.arctan2(vec_in_pixels[1], vec_in_pixels[0]))

    def get_theta1(self):
        return self.get_theta(self.vec1)

    def get_theta2(self):
        return self.get_theta(self.vec2)

    def set_theta(self, angle):
        pass

    # Redefine attributes of the Arc to always give values in pixel space
    _center = property(get_center_in_pixels, set_center)
    theta1 = property(get_theta1, set_theta)
    theta2 = property(get_theta2, set_theta)
    width = property(get_size, set_size)
    height = property(get_size, set_size)

    # The following two methods are needed to update the text position.
    def draw(self, renderer):
        self.update_text()
        super().draw(renderer)

    def update_text(self):
        c = self._center
        s = self.get_size()
        angle_span = (self.theta2 - self.theta1) % 360
        angle = np.deg2rad(self.theta1 + angle_span / 2)
        r = s / 2
        if self.textposition == "inside":
            r = s / np.interp(angle_span, [60, 90, 135, 180],
                                          [3.3, 3.5, 3.8, 4])
        self.text.xy = c + r * np.array([np.cos(angle), np.sin(angle)])
        if self.textposition == "outside":
            def R90(a, r, w, h):
                if a < np.arctan(h/2/(r+w/2)):
                    return np.sqrt((r+w/2)**2 + (np.tan(a)*(r+w/2))**2)
                else:
                    c = np.sqrt((w/2)**2+(h/2)**2)
                    T = np.arcsin(c * np.cos(np.pi/2 - a + np.arcsin(h/2/c))/r)
                    xy = r * np.array([np.cos(a + T), np.sin(a + T)])
                    xy += np.array([w/2, h/2])
                    return np.sqrt(np.sum(xy**2))

            def R(a, r, w, h):
                aa = (a % (np.pi/4))*((a % (np.pi/2)) <= np.pi/4) + \
                     (np.pi/4 - (a % (np.pi/4)))*((a % (np.pi/2)) >= np.pi/4)
                return R90(aa, r, *[w, h][::int(np.sign(np.cos(2*a)))])

            bbox = self.text.get_window_extent()
            X = R(angle, r, bbox.width, bbox.height)
            trans = self.ax.figure.dpi_scale_trans.inverted()
            offs = trans.transform(((X-s/2), 0))[0] * 72
            self.text.set_position([offs*np.cos(angle), offs*np.sin(angle)])

fig, ([ax1, ax2], [ax3, ax4]) = plt.subplots(nrows=2, ncols=2)
a = np.arange(1) + 1j*np.arange(6,11)
b = np.exp(1j*np.pi/3)
N1=8
k1=np.arange(N1)
c = np.exp(1j*2*np.pi*k1/N1)
Drawing_uncolored_circle = plt.Circle( (0, 0 ),
                                      1 ,
                                      fill = False )
Drawing_uncolored_circle2 = plt.Circle( (0, 0 ),
                                      1 ,
                                      fill = False )
Drawing_uncolored_circle3 = plt.Circle( (0, 0 ),
                                      1 ,
                                      fill = False )
Drawing_uncolored_circle4 = plt.Circle( (0, 0 ),
                                      1 ,
                                      fill = False )

# Hide number in the axis
ax1.set_yticklabels([])
ax1.set_xticklabels([])
ax1.set_yticks([])
ax1.set_xticks([])
# Hide the top and right spines.
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
""" ax1.spines["left"].set_visible(False)
ax1.spines["bottom"].set_visible(False) """
ax1.plot(1, 0, ">k", transform=ax1.get_yaxis_transform(), clip_on=False)
ax1.plot(0, 1, "^k", transform=ax1.get_xaxis_transform(), clip_on=False)
ax1.spines["left"].set_position(("data", 0))
ax1.spines["bottom"].set_position(("data", 0))
ax1.set_xlim(-1.2, 1.2)
ax1.set_ylim(-1.2, 1.2)
#
#ax1.add_artist( Drawing_uncolored_circle )
#ax1.scatter(b.real,b.imag)
ax1.scatter(c.real,c.imag)
ax1.add_artist( Drawing_uncolored_circle )
ax1.plot([0, c[1].real], [0, c[1].imag], 'r')
#ax1.plot([2,.5,1],[0,.2,1])
# am = AngleMarker((.5,.2), 100, (0,0), (1,1), ax=ax1)
am1 = AngleAnnotation((0, 0), (1, 0), (c[1].real, c[1].imag), ax=ax1, size=75, text=r"$\theta$")
ax1.text(-1.1, -1.1, '(A)', fontsize = 9)


# Hide number in the axis
ax2.set_yticklabels([])
ax2.set_xticklabels([])
ax2.set_yticks([])
ax2.set_xticks([])
# Hide the top and right spines.
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
""" ax2.spines["left"].set_visible(False)
ax2.spines["bottom"].set_visible(False) """
ax2.plot(1, 0, ">k", transform=ax2.get_yaxis_transform(), clip_on=False)
ax2.plot(0, 1, "^k", transform=ax2.get_xaxis_transform(), clip_on=False)
ax2.spines["left"].set_position(("data", 0))
ax2.spines["bottom"].set_position(("data", 0))
ax2.set_xlim(-1.2, 1.2)
ax2.set_ylim(-1.2, 1.2)
#
#ax2.add_artist( Drawing_uncolored_circle )
#ax2.scatter(b.real,b.imag)
ax2.scatter(c.real,c.imag)
ax2.add_artist( Drawing_uncolored_circle2 )
ax2.plot([0, c[1].real], [0, c[1].imag], 'r')
#ax2.plot([2,.5,1],[0,.2,1])
# am = AngleMarker((.5,.2), 100, (0,0), (1,1), ax=ax2)
am2 = AngleAnnotation((0, 0), (1, 0), (c[1].real, c[1].imag), ax=ax2, size=75)
c_b = np.exp(1j*2*np.pi*(k1+1/2)/N1)
ax2.scatter(c_b.real,c_b.imag)
ax2.plot([0, c_b[0].real], [0, c_b[0].imag], 'r')
am2a = AngleAnnotation((0, 0), (1, 0), (c_b[0].real, c_b[0].imag), ax=ax2, size=75, text=r"$\theta / 2$")
ax2.text(-1.1, -1.1, '(B)', fontsize = 9)


N3=9
k3=np.arange(N3)
c3 = np.exp(1j*2*np.pi*k3/N3)
# Hide number in the axis
ax3.set_yticklabels([])
ax3.set_xticklabels([])
ax3.set_yticks([])
ax3.set_xticks([])
# Hide the top and right spines.
ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)
""" ax3.spines["left"].set_visible(False)
ax3.spines["bottom"].set_visible(False) """
ax3.plot(1, 0, ">k", transform=ax3.get_yaxis_transform(), clip_on=False)
ax3.plot(0, 1, "^k", transform=ax3.get_xaxis_transform(), clip_on=False)
ax3.spines["left"].set_position(("data", 0))
ax3.spines["bottom"].set_position(("data", 0))
ax3.set_xlim(-1.2, 1.2)
ax3.set_ylim(-1.2, 1.2)
#
#ax3.add_artist( Drawing_uncolored_circle )
#ax3.scatter(b.real,b.imag)
ax3.scatter(c3.real,c3.imag)
ax3.add_artist( Drawing_uncolored_circle3 )
ax3.plot([0, c3[1].real], [0, c3[1].imag], 'r')
#ax3.plot([2,.5,1],[0,.2,1])
# am = AngleMarker((.5,.2), 100, (0,0), (1,1), ax=ax3)
am3 = AngleAnnotation((0, 0), (1, 0), (c3[1].real, c3[1].imag), ax=ax3, size=75, text=r"$\theta$")
ax3.text(-1.1, 1.1, '(C)', fontsize = 9)


N4=9
k4=np.arange(N4)
c4 = np.exp(1j*2*np.pi*(k4+1/2)/N4)
c4o = np.exp(1j*2*np.pi*k4/N4)
# Hide number in the axis
ax4.set_yticklabels([])
ax4.set_xticklabels([])
ax4.set_yticks([])
ax4.set_xticks([])
# Hide the top and right spines.
ax4.spines["top"].set_visible(False)
ax4.spines["right"].set_visible(False)
""" ax4.spines["left"].set_visible(False)
ax4.spines["bottom"].set_visible(False) """
ax4.plot(1, 0, ">k", transform=ax4.get_yaxis_transform(), clip_on=False)
ax4.plot(0, 1, "^k", transform=ax4.get_xaxis_transform(), clip_on=False)
ax4.spines["left"].set_position(("data", 0))
ax4.spines["bottom"].set_position(("data", 0))
ax4.set_xlim(-1.2, 1.2)
ax4.set_ylim(-1.2, 1.2)
#
#ax4.add_artist( Drawing_uncolored_circle )
#ax4.scatter(b.real,b.imag)
ax4.scatter(c4o.real,c4o.imag)
ax4.scatter(c4.real,c4.imag)

ax4.add_artist( Drawing_uncolored_circle4 )
ax4.plot([0, c4[0].real], [0, c4[0].imag], 'r')
#ax4.plot([2,.5,1],[0,.2,1])
# am = AngleMarker((.5,.2), 100, (0,0), (1,1), ax=ax4)
am4 = AngleAnnotation((0, 0), (1, 0), (c4[0].real, c4[0].imag), ax=ax4, size=75, text=r"$\theta / 2$")
ax4.text(-1.1, 1.1, '(D)', fontsize = 9)

plt.show()
