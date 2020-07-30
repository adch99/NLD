import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

def f(x, r):
    return r - x - np.exp(-x)

def fprime(x, r):
    return -1 + np.exp(-x)

def bif_diagram(f, fprime, r_range, num_samples=10):
    r_samples = np.linspace(*r_range, num_samples)
    for r in r_samples:
        x0 = 5
        result = root(f, x0, jac=fprime, args=(r))
        print(result.x)

bif_diagram(f, fprime, (3, 4))
