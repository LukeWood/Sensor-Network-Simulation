from rgg.generate_graphs import unit_square_graph
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

N=20
#to get R=.4, N=20, we set A=pi*20*(.4^2)
A=10.05

def draw_uncolored(adj_list, positions):
    colors = []
    from_list = []
    to_list = []
    G = nx.Graph()
    for index, position in enumerate(positions):
        G.add_node(index, pos=position)
    for node, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    nx.draw(G, node_color="blue")
    plt.show()

if __name__ == "__main__":
    adj_list, positions = unit_square_graph(N, A, return_positions=True)
    draw_uncolored(adj_list, positions)
