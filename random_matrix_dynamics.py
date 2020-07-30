import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numba import jit, prange

n = 100000
epsilon = 1e-3


# saddle = 0
# node = 0
# degenerate = 0
# nonisolated = 0
# centre = 0
# spiral = 0
# stable = 0
# neutral = 0
# unstable = 0

# def is_stable(t, d):
#     if d > -epsilon and t > epsilon:
#         return True
#
# def is_neutral(t, d):
#     if d > -epsilon and -epsilon < t < epsilon:
#         return True


@jit(nopython=True, parallel=True)
def monte_carlo(n, data):
    for i in prange(n):
        M = np.random.uniform(size=(2,2), high=1, low=-1)
        # M = np.random.normal(size=(2,2), loc=0.0, scale=1.0)
        t = np.trace(M)
        d = np.linalg.det(M)

        data[i, 0] = d
        data[i, 1] = t

    return data
        # classifier = np.zeros(3)

        # if d < -epsilon:
        #     saddle += 1 # saddle point
        #     # classifier[]
        #     continue
        #
        # elif -epsilon < d < epsilon:
        #     nonisolated += 1 # non-isolated fixed point
        #
        #     if is_stable(t, d): stable += 1 # stable non-iso fixed pt
        #     elif is_neutral(t, d): neutral += 1 # neutral non-iso fixed pt = 0 map
        #     else: unstable += 1 # unstable non-iso fixed pt
        #     continue
        #
        # else: # d > epsilon
        #     S = t**2 - 4 * d
        #
        #     if S > epsilon:
        #         node += 1 # Node
        #         if is_stable(t, d): stable += 1 # Stable Node
        #         else: unstable += 1 # Unstable Node
        #
        #     elif -epsilon < S < epsilon:
        #         degenerate += 1 # Stars and degenerate nodes
        #         if is_stable(t, d): stable += 1 # stable degenerate node/star
        #         elif is_neutral(t, d): neutral += 1 # The 0 map
        #         else: unstable += 1 # unstable degenerate node/star
        #
        #     else: # S < -epsilon
        #         if is_stable(t, d):
        #             spiral += 1 # stable spiral
        #             stable += 1
        #         elif is_neutral(t, d): # neutral centre
        #             centre += 1
        #             neutral += 1
        #         else:
        #             spiral += 1 # unstable spiral
        #             unstable += 1

# print("Stable:", 100*stable/n)
# print("Unstable:", 100*unstable/n)
# print("Neutral:", 100*neutral/n)
# print("Spiral:", 100*spiral/n)
# print("Centre:", 100*centre/n)
# print("Non-Isolated:", 100*nonisolated/n)
# print("Saddle:", 100*saddle/n)
# print("Node:", 100*node/n)
# print("Degenerate:", 100*degenerate/n)

data = np.empty((n,2), dtype=np.float32)
data = monte_carlo(n, data)
df = pd.DataFrame(data=data, columns=["det", "trace"])
sns.jointplot(x="det", y="trace", data=df, kind="hex")
plt.show()
