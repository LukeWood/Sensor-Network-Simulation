from rgg.coloring import compute_ordering, color_graph
from rgg.generate_graphs import unit_square_graph
import seaborn as sns
import matplotlib.pyplot as plt
N = 16000
As = [
    10, 32, 64, 96, 128, 156, 196, 256 
]

random_ys = []
svlo_ys = []

for A in As:
    adj_list = unit_square_graph(N, A)
    ordering, degs_whem_removed = compute_ordering(adj_list)
    coloring_random = color_graph(range(0, len(adj_list)), adj_list)
    coloring_slvo = color_graph(ordering, adj_list)
    random_ys.append(max(coloring_random))
    svlo_ys.append(max(coloring_slvo))

data={
    "x":As,
    "Random":random_ys,
    "SVLO": svlo_ys
}

plt.plot('x', 'Random', data=data)
plt.plot('x', 'SVLO', data=data)

plt.legend(["Random", "SVLO"])
plt.title("Random Ordering vs Shortest Vertex Last Ordering, N=16000")
plt.xlabel("A")
plt.ylabel("Colors Used")
plt.savefig("../results/comparison/number_colors.png")
