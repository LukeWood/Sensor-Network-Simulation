from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(0, projection='3d')
n = 100

xs = randrange(n, 23, 32)
ys = randrange(n, 0, 100)
zs = randrange(n, zlow, zhigh)
ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
