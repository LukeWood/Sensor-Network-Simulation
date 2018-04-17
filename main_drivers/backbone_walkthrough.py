from rgg.generate_graphs import unit_square_graph
from rgg.coloring import compute_ordering, color_graph
from rgg.backbone import find_backbones
import networkx as nx
import matplotlib.pyplot as plt

N=20
A=10.05

adj_list, positions = unit_square_graph(N, A, return_positions=True)
ordering, degs_whem_removed = compute_ordering(adj_list)
coloring = color_graph(ordering, adj_list)

backbones = find_backbones(coloring, adj_list)
