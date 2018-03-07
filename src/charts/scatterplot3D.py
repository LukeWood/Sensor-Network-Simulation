from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def scatterplot3D(nodes):
    fig = plt.figure()
    ax = fig.add_subplot(0, projection='3d')

    xs = []
    ys = []
    zs = []
    ax.scatter(xs, ys, zs)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()
