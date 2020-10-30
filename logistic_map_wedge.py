import sympy as sym
import numpy as np

def f(x, r):
    return r*x*(1-x)

def fn(n, x, r):
    y = x
    for i in range(n):
        y = f(y, r)
    return y

def getIntersection():
    x = np.random.uniform(0, 1)
    r = sym.Symbol("r")
    polys = [sym.Poly(fn(i, x, r)) for i in range(2, 10)]
    sol = sym.solve(polys, r)
    print(sol)

def manual():
    r = sym.Symbol("r")
    eq = sym.Eq(1 - 1/r, r**3/4 - r**4/16 - r**5/16 + r**6/32 - r**7/256)
    sol = sym.solveset(eq, r)
    print(list(sol)[2].evalf())

if __name__ == "__main__":
    # getIntersection()
    manual()
