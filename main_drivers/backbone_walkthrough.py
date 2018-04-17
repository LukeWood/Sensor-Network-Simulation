from rgg.generate_graphs import unit_square_graph
from rgg.coloring import compute_ordering, color_graph
from rgg.backbone import find_backbones
import networkx as nx
import matplotlib.pyplot as plt

N=20
A=10

adj_list, positions = unit_square_graph(N, A, return_positions=True)
ordering, degs_whem_removed = compute_ordering(adj_list)
coloring = color_graph(ordering, adj_list)

backbones = find_backbones(coloring, adj_list)

def draw_colored(backbone, positions, coloring):
    plt.clf()
    colors = ['#6A1B9A', '#D50000', '#AEEA00', '#00B0FF', '#00B8D4', '#00BFA5', '#00C853', '#DD2C00', '#FFFF00']
    G = nx.Graph()
    color_map = [colors[color%len(colors)] for color, node in zip(coloring, backbone) if node != False]

    should_be_nodes = []
    for node_index, node in enumerate(backbone):
        if node == False:
            continue
        G.add_node(node_index)
        should_be_nodes.append(node_index)

        for neighbor in node:
            G.add_edge(node_index, neighbor)

    pos = {}
    for node_index, position in enumerate(positions):
        if backbone[node_index] == False:
            continue
        pos[node_index] = position

    plt.title("Backbone of a WSN with N=%d, A=%d" % (N, A))
    nx.draw(G, pos=pos, node_color=color_map)
    plt.savefig("../results/backbone/backbone_display.png", bbox_inches="tight")

draw_colored(backbones[0], positions, coloring)
