import numpy as np
from scipy.integrate import solve_ivp as solve
import matplotlib.pyplot as plt

def f(t, phi, k): return k - np.sin(phi)

phi0 = np.array([np.pi/4])
kvals = [1.0, 1.5, 0.5]
tspan = (0, 10)
teval = np.linspace(*tspan, 100)

fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)

for k in kvals:
    sol = solve(f, tspan, phi0, t_eval=teval, args=(k,))
    t = sol.t
    phi = sol.y.flatten()
    ax1.plot(t, phi, label="k = %f" % k)
    ax2.plot(t, np.sin(phi), label="k = %f" % k)


ax1.set_xlabel("t")
ax1.set_ylabel(r"\phi")
ax2.set_ylabel(r"sin(\phi)")
ax1.set_yticks(np.arange(0, 10, np.pi/2))
ax1.legend()
ax2.legend()
plt.show()
