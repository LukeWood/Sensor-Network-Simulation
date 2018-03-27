from coloring import compute_ordering, color_graph
from generate_graphs import unit_square_graph
from generate_graphs import unit_disc_graph
from generate_graphs import unit_sphere_graph
from generate_graphs import adjacency_list_from_node_list
import matplotlib.pyplot as plt

def coloring_histogram(coloring, graph_topology=""):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    plt.clf()
    max_color = max(coloring)
    yvals = [0 for _ in range(max_color+1)]
    for d in coloring:
        yvals[d] = yvals[d] + 1
    ax = sns.barplot(x=list(range(max_color+1)), y=yvals)
    plt.title("")
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    plt.title("Frequencies of Colors for Topology %s, N=16000, A=64" % graph_topology)
    name="../results/%s/coloring/color_distribution.png" % graph_topology
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(base=5))
    plt.savefig(name, bbox_inches="tight")

N = 16000
A = 64

fns = [
    ("square",unit_square_graph),
    ("disc", unit_disc_graph),
    ("sphere", unit_sphere_graph)
]

for topology, fn in fns:
    plt.clf()
    nodes = fn(N, A)
    alist = adjacency_list_from_node_list(nodes)
    ordering = compute_ordering(alist)
    coloring = color_graph(ordering, alist)
    coloring_histogram(coloring, graph_topology=topology)
