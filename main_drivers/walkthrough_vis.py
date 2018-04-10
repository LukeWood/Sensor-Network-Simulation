from rgg.generate_graphs import unit_square_graph
from rgg.coloring import compute_ordering, color_graph
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

N=20
#to get R=.4, N=20, we set A=pi*20*(.4^2)
A=10.05

def draw_uncolored(adj_list, positions):
    plt.clf()
    G = nx.Graph()
    for index, position in enumerate(positions):
        G.add_node(index, pos=position)
    for node, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    nx.draw(G, node_color="blue")
    plt.title("Uncolored Unit Square Graph with N=20, R=.4")
    plt.savefig("../results/walkthrough/uncolored.png", bbox_inches="tight")

def draw_colored(adj_list, positions, coloring):
    plt.clf()
    colors = ['#6A1B9A', '#D50000', '#AEEA00', '#00B0FF', '#00B8D4', '#00BFA5', '#00C853', '#DD2C00', '#FFFF00']
    G = nx.Graph()
    color_map = [colors[color] for color in coloring]
    for node, position in enumerate(positions):
        G.add_node(node, pos=position)
    for node, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    nx.draw(G, node_color=color_map, with_labels=True)
    plt.title("Uncolored Unit Square Graph with N=20, R=.4")
    plt.savefig("../results/walkthrough/colored.png", bbox_inches="tight")


if __name__ == "__main__":
    adj_list, positions = unit_square_graph(N, A, return_positions=True)
    ordering, degrees_when_removed = compute_ordering(adj_list)
    coloring = color_graph(ordering, adj_list)
    draw_uncolored(adj_list, positions)
    draw_colored(adj_list, positions, coloring)
