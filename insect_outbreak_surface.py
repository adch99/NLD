import numpy as np

def fixedpt(r, k, epsilon=1e-2):
    coeffs = np.array([-r/k, r, -(1+r/k), r])
    polys = np.poly1d()
    roots = np.roots(coeffs)
    isReal = (np.abs(roots.imag) < epsilon)
    return roots.real[isReal]

r_val = np.linspace(0, 1, 100)
k_val = np.linspace(0, 40, 100)

r, k = np.meshgrid(r_val, k_val)
x = fixedpt(r, k)
