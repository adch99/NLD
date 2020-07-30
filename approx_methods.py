import math

def f(x):
    return -x

def euler(x_n, step):
    return x_n + f(x_n)*step

def euler_imp(x_n, step):
    guess = euler(x_n, step)
    return x_n + (f(x_n) + f(guess))*step/2

def evaluate(t, t0, x0, estimator, step):
    x = x0
    numsteps = (t - t0) / step
    try:
        int(numsteps)
    except ValueError:
        print("t-t0 must be a multiple of the step size!")
        return None

    for i in range(int(numsteps)):
        x = estimator(x, step)

    return x

print("Euler")
for n in range(0, 5):
    value = evaluate(1, 0, 1, euler, 10**-n)
    print("%d: %f" % (n, value))

print("Expected Value: %f" % (1/math.e))

print("Improved Euler")
for n in range(0, 5):

    value = evaluate(1, 0, 1, euler_imp, 10**-n)
    print("%d: %f" % (n, value))

print("Expected Value: %f" % (1/math.e))
