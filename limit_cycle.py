import numpy as np
from scipy.integrate import solve_ivp as solve
import matplotlib.pyplot as plt
import matplotlib as mpl

def f(t, v, k): 
    r, theta = v
    return np.array([r*(1 - r**2) + k*r*np.cos(theta), 1])

def approx(theta, k):
    return 1 - k*(np.sin(theta) + np.cos(theta))/2

v0 = np.array([1, np.pi])
kvals = np.linspace(0.1, 0.5, 2)
tspan = (0, 10)
teval = np.linspace(*tspan, 100)
kwargs = {"projection": "polar"}
figt, axt = plt.subplots(nrows=2, sharex=True)
figp, axp = plt.subplots(subplot_kw=kwargs)
colours = [mpl.cm.PuOr(k) for k in np.linspace(0, 1, len(kvals))] 
for i in range(len(kvals)):
    k = kvals[i]
    sol = solve(f, tspan, v0, t_eval=teval, args=(k,))
    t = sol.t
    r, theta = sol.y
    print(sol.y.shape)
    theta_approx = np.linspace(theta.min(), theta.max(), 100)
    r_approx = approx(theta_approx, k)
    axt[0].plot(t, r, label="k = %.2f" % k, color=colours[i])
    axt[1].plot(t, theta, label="k = %.2f" % k, color=colours[i])
    axp.plot(theta, r, label="k = %.2f" % k, color=colours[i])
    axp.plot(theta_approx, r_approx, label="k = %.2f approx" % k, color=colours[i], linestyle="-.")


axt[0].set_xlabel("t")
axt[0].set_ylabel("r")
axt[1].set_ylabel(r"$\theta$")
axt[0].legend()
axt[1].legend()
axp.legend()
plt.show()
