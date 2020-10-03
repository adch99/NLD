import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

s = 10
b = 8.0 / 3.0
n0 = 3 # For each of the three coordinates => effectively n0**3
n = 10**7
tspan = (0, 200)
teval = np.linspace(*tspan, n)
nfigs = 4
cmap = plt.get_cmap("jet")

def lorenz(t, v, r):
    x, y, z = v
    dx = s * (y - x)
    dy = r*x -x*z - y
    dz = x*y - b*z
    return np.array([dx, dy, dz])

def varying_r():
    rvals = [10, 22, 24.5, 100, 126.52, 400]
    for r in rvals:
        figs = pregraphing(r)
        # varying_initial_cond(r, figs)
        single_random_point(r, figs) # When you want for only one random point
        postgraphing(r, figs)

def single_random_point(r, figs):
    pos0 = np.random.uniform(-50, 50, size=(3,))
    varying_integration_len(r, pos0, figs, key=None)


def varying_initial_cond(r, figs):
    # Create grid of initial conditions
    x0vals = y0vals = z0vals = (r/10)*np.linspace(-1, 1, n0)

    # One could optimize this instead of having three nested
    # Python loops over them, but its a one time operation
    # and far from being the most computationally expensive
    # one. Plus it's just 64 loops for now.
    for i, x0 in enumerate(x0vals):
        for j, y0 in enumerate(y0vals):
            for k, z0 in enumerate(z0vals):
                pos0 = np.array([x0, y0, z0])
                varying_integration_len(r, pos0, figs, key=i+j+k)

def varying_integration_len(r, pos0, figs, key=None):
    # For now let's skip this.
    run(r, pos0, figs, key=key)

def run(r, pos0, figs, key=None):
    # Solve the DE first
    np.set_printoptions(formatter={"float": "{: 7.2f}".format}, suppress=True, precision=2)
    print("Solving for r=", r, " and pos=", pos0, "...")
    sol = solve_ivp(lorenz, tspan, pos0, t_eval=teval, args=(r,))
    if sol.success:
        grapher(r, pos0, sol, figs, key=key)
    else:
        print(f"Integration for r={r}, pos0={pos0} failed: {sol.message}")

def grapher(r, pos0, sol, figs, key=None):
    t = sol.t
    x, y, z = sol.y
    pos0string = np.array2string(pos0, precision=3, suppress_small=True,
        separator="_", formatter={"float": "{: 7.2f}".format})
    label = pos0string # Add integration length etc later if needed
    axes = [fig.gca() for fig in figs]
    args = [(t, x), (t, y), (x, y), (x, y, z)]

    if key is not None:
        color = cmap(key/n0**3)
    else:
        color = None

    for i in range(nfigs):
         axes[i].plot(*args[i], label=pos0string, color=color, alpha=0.9)

def pregraphing(r):
    figs = [plt.figure(figsize=(20, 10)) for i in range(nfigs)]
    axes = [fig.gca() for fig in figs[:-1]]
    axes.append(figs[-1].gca(projection="3d"))
    xlabels = [r"$t$", r"$t$", r"$x$", r"$x$"]
    ylabels = [r"$x$", r"$y$", r"$y$", r"$y$"]
    titlesuffixes = [r"$x$ vs $t$", r"$y$ vs $t$", r"$y$ vs $x$", "3d plot"]
    titles = [f"r = {r} " + suffix for suffix in titlesuffixes]
    for i in range(nfigs):
         axes[i].set_xlabel(xlabels[i])
         axes[i].set_ylabel(ylabels[i])
         axes[i].set_title(titles[i])
    return figs

def postgraphing(r, figs):
    axes = [fig.gca() for fig in figs]
    filenameprefixes = ["xvst", "yvst", "xvsy"]
    for i in range(nfigs-1):
         # axes[i].legend()
         figs[i].savefig(f"plots/{filenameprefixes[i]}_r={r}.png")
         plt.close(fig=figs[i])

if __name__ == "__main__":
    varying_r()
    # r = 100
    # figs = pregraphing(r)
    # single_random_point(r, figs)
    # postgraphing(r, figs)
    plt.close()
