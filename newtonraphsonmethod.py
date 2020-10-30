# Newton's method

def approx(x, f, df):
    return x - f(x)/df(x)

def g(x):
    return x**2 - 4

def dg(x):
    return 2*x

def main():
    x = 90
    epsilon = 1e-3
    iters = 0
    diff = 1
    while diff > epsilon:
        xnew = approx(x, g, dg)
        diff = abs(x - xnew)
        x = xnew
        iters += 1
        print(f"Iteration: {iters}\tApprox: {x}")
    print(f"Final Answer: {x}")
    return x

if __name__ == "__main__":
    main()
