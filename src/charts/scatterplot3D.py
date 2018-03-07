from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def scatterplot3D(nodes):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xs = [node.dims[0] for node in nodes]
    ys = [node.dims[1] for node in nodes]
    zs = [node.dims[2] for node in nodes]
    ax.scatter(xs, ys, zs)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()
