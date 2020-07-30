import numpy as np
import matplotlib.pyplot as plt

n = 25
a = 10
b = 4

A = np.matrix([[0, 0], [b, a]])

x = y = np.linspace(-2, 2, n)
X, Y = np.meshgrid(x, y)

V = np.zeros((n, n, 2))
V[:, :, 0] = X
V[:, :, 1] = Y

# print("X:")
# print(X)
#
# print("Y:")
# print(Y)
#
# print("V:")
# print(V)
print("V.shape:", V.shape)

dV = np.tensordot(V, A, axes=[2, 1])
dX = dV[:, :, 0]
dY = dV[:, :, 1]
C = dX**2 + dY**2
plt.quiver(X, Y, dX, dY, C, headwidth=2.5, headlength=3)
plt.show()
