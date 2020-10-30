import numpy as np
import matplotlib.pyplot as plt
# This program plots and saves the long-term behaviour
# of the Henon map.

# Parameters
a = 1.4
b = 0.3

# Sample Sizes
ntransient = 0
nsamples = 10**5

def henon(v):
    x, y = v
    return np.array([y + 1 - a*x**2, b*x])

def run(pos0, ntransient, nsamples):
    pos = pos0
    samples = np.zeros((nsamples, 2))
    for i in range(ntransient):
        pos = henon(pos)

    for i in range(nsamples):
        pos = henon(pos)
        samples[i] = pos

    return samples

def grapher(samples):
    x, y = samples.T
    plt.scatter(x, y, s=0.75)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Henon map for a = {a} and b = {b}")

if __name__ == "__main__":
    pos0 = np.array([0, 0])
    samples = run(pos0, ntransient, nsamples)
    grapher(samples)
    print(samples.shape)
    plt.savefig("plots/henon_map.png")
    plt.show()
