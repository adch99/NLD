import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.integrate import solve_ivp

x = y = np.linspace(-4, 4, 10)

def f(t, v):
    x, y = v
    fx = -y**2
    fy = x
    return np.array([fx, fy])

def jac(t, v):
    x, y = v
    return np.array([[y, x], [2*x, -1]])

fig = plt.figure()
ax = plt.gca()
mpl.style.use("seaborn")
cycle = plt.cycler("color", mpl.cm.Blues_r(np.linspace(0,0.5,5)))
ax.set_prop_cycle(cycle)

tspan = (0, 10)
tvals = np.linspace(0, 10, 100)
print("tvals:", tvals)

for i in range(len(x)):
    for j in range(len(y)):
        r0 = np.array([x[i], y[j]])

        sol = solve_ivp(f, tspan, r0, t_eval=tvals)
        if sol.status != 0:
            print(f"Status: {sol.status} Message: {sol.message}")
        xsol, ysol = sol.y
        plt.plot(xsol, ysol, alpha=0.8)

plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.show()
