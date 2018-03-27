from coloring import compute_ordering
from generate_graphs import unit_square_graph
from generate_graphs import unit_disc_graph
from generate_graphs import unit_sphere_graph
from generate_graphs import adjacency_list_from_node_list
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

N = 16000
A = 32

fns = [
    ("square",unit_square_graph),
    ("disc", unit_disc_graph),
    ("sphere", unit_sphere_graph)
]

for topology, fn in fns:
    nodes = fn(N, A)
    alist = adjacency_list_from_node_list(nodes)
    ordering, degrees_when_removed = compute_ordering(alist, lengths_when_removed_returned=True)
    degrees = list(map(lambda node: len(node), alist))
    max_degree = max(degrees)

    densities = [0 for _ in range(max_degree + 1)]
    for degree in degrees:
        densities[degree] = densities[degree] + 1
    densities_when_removed = [0 for _ in range(max_degree + 1)]
    for degree in degrees_when_removed:
        densities_when_removed[degree] = densities_when_removed[degree] + 1

    x=list(range(max_degree + 1))
    plt.scatter(x, densities, alpha=.5)
    plt.scatter(x, densities_when_removed, alpha=.5)
    plt.xlabel("Degrees")
    plt.ylabel("Frequency")
    plt.title("Degrees vs Degrees When Removed From Graph")
    plt.legend(["Degrees","Degrees When Placed In SLVO"])
    plt.savefig("../results/%s/coloring/degree_frequencies.png" % topology)
