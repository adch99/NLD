import numpy as np
import matplotlib.pyplot as plt

# ------------------------------- #
# Parameters for making the plot  #
# ------------------------------- #

n = 40 # Number of points per x and y axis
logscale = True # Denote vector magnitude by log-scale colouring
polar = False # Plot in polar coordinates

# Set both 0 for a slope plot. Leave at default unless it clogs the plot.
headwidth = 2 # Arrow head length (default: 2)
headlength = 3 # Arrow head width (default: 3)

xlims = (-3, 3)
ylims = (-3, 3)

# plt.set_cmap("jet")

# Declare your parameters here.

# ---------------------- #
# Put the functions here #
# ---------------------- #

def fx(x, y):
    return -x/(x**2 + y**2)

def fy(x, y):
    return -y/(x**2 + y**2)

def fr(r, θ):
    return r*(1 - r**2)*((r*np.sin(θ))**2 + ((r*np.cos(θ))**2 - 1)**2)

def ft(r, θ):
    return ((r*np.sin(θ))**2 + ((r*np.cos(θ))**2 - 1)**2)

# ------------------------- #
# End of user configuration #
# ------------------------- #

if polar == True:
    def fx(x, y):
        r = np.sqrt(x**2 + y**2)
        θ = np.arctan2(y , x)
        return fr(r, θ)*np.cos(θ) - r*np.sin(θ)*ft(r, θ)

    def fy(x, y):
        r = np.sqrt(x**2 + y**2)
        θ = np.arctan2(y, x)
        return fr(r, θ)*np.sin(θ) + r*np.cos(θ)*ft(r, θ)
    # ax = plt.subplot(111, projection="polar")

x = np.linspace(*xlims, n)
y = np.linspace(*ylims, n)
X, Y = np.meshgrid(x, y)
dX = fx(X, Y)
dY = fy(X, Y)
dl = np.sqrt(dX**2 + dY**2)
dX_norm = dX / dl
dY_norm = dY / dl

if logscale:
    colours = np.log(dl)
else:
    colours = dl

plt.quiver(X, Y, dX_norm, dY_norm, colours, headwidth=headwidth, headlength=headlength, angles="xy")
plt.colorbar()
plt.tight_layout()
plt.figure()
plt.streamplot(X, Y, dX, dY, color=colours)
plt.colorbar()
plt.tight_layout()
plt.show()
