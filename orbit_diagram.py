import numpy as np
import matplotlib.pyplot as plt

# General orbit diagram plotter
# copied from logistic_map_orbit_diagram.py

rspan = (1, 5)
rsample_size = 1000
xspan = (0, 1)
# If the abs(x) goes beyond this value,
# we reject the orbit as being unstable
# and count as going to infinity
xupper_bound = 100

def f(x, r):
    return r*np.minimum(x, 1-x)

def get_orbit(r, sample_size=100, skip_transient=5000):
    x = np.random.uniform(*xspan)
    for i in range(skip_transient):
        x = f(x, r)
        if abs(x) > xupper_bound:
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
        plt.scatter(rarray, orbit, marker="o", color="#2e3440", s=0.5)
    plt.xlabel("r")
    plt.ylabel("x*")
    plt.title("Orbit Diagram")

if __name__ == "__main__":
    main()
    plt.show()
