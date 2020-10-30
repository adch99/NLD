import sympy as sym
from functools import reduce

cache = {}

# x = sym.Symbol("x")

def f(x, r):
    return r*x*(1-x)

def fn(n, x, r):
    y = x
    for i in range(n):
        y = f(y, r)
    return y

def Rn(n):
    if n in cache.keys():
        return cache[n]
    else:
        r = sym.Symbol("r")
        poly = sym.poly(fn(n, 0.5, r) - 0.5)
        primefactors = sym.primefactors(n)
        for p in primefactors:
            if p != n:
                poly = sym.pexquo(poly, fn(p, 0.5, r) - 0.5)

        print("Expression:", poly)
        print()
        allsols = poly.nroots()
        sols = sym.ConditionSet(r, r>0, allsols)
        cache[n] = sols
        return sols

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def onlyRn(n):
    # if n in cache.keys():
    #     return
    nfactors = factors(n)
    R = Rn(n)
    for p in nfactors:
        if p != n:
            R = R - Rn(p)
            # print(f"Removing Rn({p}): {Rn(p)}")
    return R

def calculate_delta():
    pass
if __name__ == "__main__":
    print("Solutions:", onlyRn(8))
