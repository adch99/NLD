import numpy as np
import matplotlib.pyplot as plt

rspan = (3.3, 4)
rsample_size = 1000

def f(x, r):
    return r*x*(1-x)

def get_orbit(r, sample_size=100, skip_transient=300):
    x = np.random.uniform(0,1)
    for i in range(skip_transient):
        x = f(x, r)
        if abs(x) > 10:
            return np.array([])

    samples = []
    for i in range(sample_size):
        samples.append(x)
        x = f(x, r)
    orbit = np.array(list(set(samples)))
    return orbit

def main():
    rvals = np.linspace(*rspan, rsample_size)
    fig, ax = plt.subplots(nrows=1, ncols=1)
    for r in rvals:
        orbit = get_orbit(r)
        rarray = np.zeros(orbit.shape) + r
        plt.scatter(rarray, orbit, marker="o", color="black", s=0.5)
    plt.xlabel("r")
    plt.ylabel("x*")
    plt.title("Orbit Diagram")

if __name__ == "__main__":
    main()
    plt.show()
