import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

R = 2
I0 = 12
mu0 = 4 * np.pi * 1e-7
C0 = mu0 / (4 * np.pi)
N = 50
x, y =np.meshgrid(np.linspace(-5, 5, N), np.linspace(-5, 5, N))

xa, ya = 0, R
xb, yb = 0, -R  # 两个圆环导线在坐标的位置

r1 = np.sqrt((x - xa) ** 2 + (y - ya) ** 2)
r2 = np.sqrt((x - xb) ** 2 + (y - yb) ** 2)

Bx1 = -C0 * I0 * (y - ya) / r1 ** 3
By1 = C0 * I0 * (x - xa) / r1 ** 3

Bx2 = -C0 * I0 * (y - yb) / r2 ** 3
By2 = C0 * I0 * (x - xb) / r2 ** 3

Bx = Bx1 - Bx2
By = By1 - By2
B = np.sqrt(Bx ** 2 + By ** 2)

fig, ax = plt.subplots()
ax.streamplot(x, y, Bx, By, density=2, arrowsize=1.5, linewidth=1)
ax.scatter([xa, xb], [ya, yb], s=50, c='blue')
plt.show()

x = np.outer(np.linspace(-0.5, 0.5, 50), np.ones(50))
y = x.copy().T
az = plt.axes(projection='3d')
az.plot_surface(x, y, B, rstride=1, cstride=1,cmap='rainbow', alpha=0.9)
plt.show()
