from rgg.coloring import compute_ordering
from rgg.generate_graphs import unit_square_graph
from rgg.generate_graphs import unit_disc_graph
from rgg.generate_graphs import unit_sphere_graph
from rgg.generate_graphs import adjacency_list_from_node_list
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

N = 1000
A = 32

fns = [
    ("square",unit_square_graph),
    ("disc", unit_disc_graph),
    ("sphere", unit_sphere_graph)
]

for topology, fn in fns:
    plt.clf()
    alist = fn(N, A)
    ordering, degrees_when_removed = compute_ordering(alist)
    degrees = list(map(lambda node: len(node), alist))

    plt.plot(degrees)
    ax = plt.plot(degrees_when_removed)
    plt.xlabel("Degrees")
    plt.ylabel("Frequency")
    plt.title("Degrees vs Degrees When Removed From Graph, N=16000, A=32")
    plt.legend(["Degrees","Degrees When Placed In SLVO"])
    plt.savefig("../results/%s/coloring/degree_frequencies.png" % topology, bbox_inches="tight")
