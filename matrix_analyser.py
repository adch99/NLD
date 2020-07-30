import numpy as np

# Matrix Analysis
epsilon = 1e-3
A = np.matrix([[-4, 12], [-3, 11]])

det = np.linalg.det(A)
trace = np.trace(A)

eigenvals, eigenvecs = np.linalg.eig(A)

print("Values")
print("------")
print("{0:12} = {1:6.2f}".format("Determinant", det))
print("{0:12} = {1:6.2f}".format("Trace", trace))
print("{0:12} = {1:6.2f}".format("Tr^2 - 4*Det", trace**2 - 4*det))
print()
print("Eigenvalue - Eigenvector")
print("------------------------")

# print(eigenvecs)

formatter = {"float": "{:5.2f}".format}

for i in range(len(eigenvals)):
    with np.printoptions(precision=2, suppress=True, formatter=formatter):
        val = eigenvals[i]
        vec = np.asarray(eigenvecs.T[i]).flatten()
        # print(vec.shape)
        if np.abs(vec[0]) > epsilon: # I want to know the slope
            vec = vec/vec[0]  # from the eigenvector
        print("{0}) {1:5.2f} - {2:}".format(i+1, val, vec))
