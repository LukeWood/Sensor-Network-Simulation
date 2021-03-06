from rgg.generate_graphs import unit_square_graph
from rgg.coloring import compute_ordering, color_graph
from rgg.backbone import find_potential_backbones, largest_backbone
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

N=20
#to get R=.4, N=20, we set A=pi*20*(.4^2)
A=10.05

def first_of_set(s):
    if len(s) == 0:
        raise ValueError("Empty set given to function 'first_of_set/1'")
    for item in s: break
    return item

def compute_ordering(adj_list):
    ordering = []
    max_degree = max(map(lambda x: len(x), adj_list))
    length_to_nodes = {}
    for i in range(max_degree + 1):
        length_to_nodes[i] = set()
    length_to_nodes[-1] = set()
    node_to_length = [len(x) for x in adj_list]
    for i, node in enumerate(adj_list):
        degree = len(node)
        length_to_nodes[degree].add(i)

    removed = [False for x in adj_list]
    ordering_states = []
    while len(ordering) != len(adj_list):

        current_state = []
        for index, is_removed in enumerate(removed):
            if is_removed:
                current_state.append(False)
            else:
                current_state.append([n for n in adj_list[index] if not removed[n]])
        ordering_states.append(current_state)

        index = 0
        while len(length_to_nodes[index]) == 0:
            index=index + 1
        node = first_of_set(length_to_nodes[index])
        ordering.append(node)
        for neighbor in adj_list[node]:
            neighbor_len = node_to_length[neighbor]
            if neighbor in length_to_nodes[neighbor_len]:
                node_to_length[neighbor] = neighbor_len-1
                length_to_nodes[neighbor_len].remove(neighbor)
                length_to_nodes[neighbor_len-1].add(neighbor)
        length_to_nodes[index].remove(node)
        removed[node] = True

    current_state = []
    for index, is_removed in enumerate(removed):
        if is_removed:
            current_state.append(False)
        else:
            current_state.append(adj_list[index])
    ordering_states.append(current_state)
    return ordering[::-1], ordering_states

def draw_ordering_graph(ordering_states, positions):
    nodes = {}
    plot_index=0
    fig, axes = plt.subplots(4, 5)
    x = 0
    y = 0
    for state in ordering_states[:-1]:
        G = nx.Graph()
        pos = {}
        for index, position in enumerate(positions):
            if state[index] is False:
                continue
            pos[index]=position
            G.add_node(index, pos=position, size=1)
        for node, neighbors in enumerate(state):
            if neighbors is False:
                continue
            for neighbor in neighbors:
                G.add_edge(node, neighbor)
        nx.draw(G, pos=pos,node_color="blue", ax=axes[y, x], node_size=50)
        if x == 4:
            x = 0
            y = y + 1
        else:
            x = x + 1
    plt.suptitle("Visualization of the removal of nodes during SLVO")
    plt.savefig("../results/walkthrough/ordering.png", bbox_inches="tight")


def draw_coloring_graph(adj_list, coloring_order, positions, coloring):
    colors = ['#6A1B9A', '#D50000', '#AEEA00', '#00B0FF', '#00B8D4', '#00BFA5', '#00C853', '#DD2C00', '#FFFF00']
    nodes = {}
    plot_index=0
    fig, axes = plt.subplots(4, 5)
    x = 0
    y = 0
    node_colors=["#000000" for node in positions]
    G = nx.Graph()
    pos = {}
    for index, position in enumerate(positions):
        pos[index]=position
        G.add_node(index, pos=position, size=1)
    for node, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    for node in coloring_order:
        node_colors[node] = colors[coloring[node]]
        nx.draw(G, pos=pos,node_color=node_colors, ax=axes[y, x], node_size=50)
        if x == 4:
            x = 0
            y = y + 1
        else:
            x = x + 1
    plt.suptitle("Coloring of Graph during SLVO Coloring")
    plt.savefig("../results/walkthrough/coloring.png", bbox_inches="tight")

def draw_uncolored(adj_list, positions):
    plt.clf()
    G = nx.Graph()
    pos = {}
    for index, position in enumerate(positions):
        G.add_node(index)
        pos[index] = position

    for node, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    plt.title("UnColored Unit Square Graph with N=20, R=.4")
    nx.draw(G, pos=pos)
    plt.savefig("../results/walkthrough/uncolored.png", bbox_inches="tight")

def draw_colored(adj_list, positions, coloring):
    plt.clf()
    colors = ['#6A1B9A', '#D50000', '#AEEA00', '#00B0FF', '#00B8D4', '#00BFA5', '#00C853', '#DD2C00', '#FFFF00']
    G = nx.Graph()
    color_map = [colors[color] for color in coloring]
    pos={}
    for node, position in enumerate(positions):
        G.add_node(node, pos=position)
        pos[node] = position


    for node, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    plt.title("Colored Unit Square Graph with N=20, R=.4")
    nx.draw(G, pos=pos, node_color=color_map)
    plt.savefig("../results/walkthrough/final_colored.png", bbox_inches="tight")

def draw_all_backbones(backbones, positions, coloring):
    fig, axes = plt.subplots(2, 3)
    x = 0
    y = 0
    colors = ['#6A1B9A', '#D50000', '#AEEA00', '#00B0FF', '#00B8D4', '#00BFA5', '#00C853', '#DD2C00', '#FFFF00']

    for current_backbone in backbones:
        G = nx.Graph()
        color_map = {}

        for node_index, node in enumerate(current_backbone):
            if node == False:
                G.add_node(node_index)
                continue
            G.add_node(node_index)
            for neighbor in node:
                G.add_edge(node_index, neighbor)

        pos = {}
        for node_index, position in enumerate(positions):
            pos[node_index] = position

        color_map = [colors[coloring[x]] if current_backbone[x] != False else "#CCCCCC" for x in G.node]
        nx.draw(G, pos=pos,node_color=color_map, ax=axes[y, x], node_size=50)
        if x == 2:
            x = 0
            y = y + 1
        else:
            x = x + 1
    plt.suptitle("Potential Backbones of Graph with N=20, R=.4")
    plt.savefig("../results/walkthrough/potential_backbones.png", bbox_inches="tight")


def draw_largest_backbones(backbones, positions, coloring):
    fig, axes = plt.subplots(2, 3)
    x = 0
    y = 0
    colors = ['#6A1B9A', '#D50000', '#AEEA00', '#00B0FF', '#00B8D4', '#00BFA5', '#00C853', '#DD2C00', '#FFFF00']

    for current_backbone in backbones:
        G = nx.Graph()
        color_map = {}

        for node_index, node in enumerate(current_backbone):
            if node == False:
                G.add_node(node_index)
                continue
            G.add_node(node_index)
            for neighbor in node:
                G.add_edge(node_index, neighbor)

        pos = {}
        for node_index, position in enumerate(positions):
            pos[node_index] = position

        color_map = [colors[coloring[x]] if current_backbone[x] != False else "#CCCCCC" for x in G.node]
        nx.draw(G, pos=pos,node_color=color_map, ax=axes[y, x], node_size=50)
        if x == 2:
            x = 0
            y = y + 1
        else:
            x = x + 1
    plt.suptitle("Largest Backbones Sorted By # Edges of Graph with N=20, R=.4.")
    plt.savefig("../results/walkthrough/largest_backbones.png", bbox_inches="tight")



def draw_dominations(backbones, positions, coloring, adj_list):
    fig, axes = plt.subplots(2, 3)
    x = 0
    y = 0
    colors = ['#6A1B9A', '#D50000', '#AEEA00', '#00B0FF', '#00B8D4', '#00BFA5', '#00C853', '#DD2C00', '#FFFF00']

    for current_backbone in backbones:
        G = nx.Graph()
        color_map = {}
        dominated_nodes = set()

        for node_index, node in enumerate(current_backbone):
            G.add_node(node_index)
            if node == False:
                continue
            dominated_nodes.add(node_index)
            for neighbor in adj_list[node_index]:
                G.add_edge(node_index, neighbor)
                dominated_nodes.add(neighbor)
        pos = {}
        for node_index, position in enumerate(positions):
            pos[node_index] = position

        color_map = [colors[coloring[x]] if current_backbone[x] != False else "#0000FF" if x in dominated_nodes else "#CCCCCC" for x in G.node]

        nx.draw(G, pos=pos,node_color=color_map, ax=axes[y, x], node_size=50)
        if x == 2:
            x = 0
            y = y + 1
        else:
            x = x + 1
    plt.suptitle("Backbone Dominations for N=20, R=.4.")
    plt.savefig("../results/walkthrough/backbone_dominations.png", bbox_inches="tight")


if __name__ == "__main__":
    adj_list, positions = unit_square_graph(N, A, return_positions=True)
    ordering, ordering_states = compute_ordering(adj_list)
    coloring = color_graph(ordering, adj_list)

    draw_uncolored(adj_list, positions)
    draw_colored(adj_list, positions, coloring)

    draw_ordering_graph(ordering_states, positions)
    draw_coloring_graph(adj_list, ordering, positions, coloring)

    backbones = find_potential_backbones(coloring, adj_list)
    draw_all_backbones(backbones, positions, coloring)

    largest_backbones = list(map(largest_backbone, backbones))
    largest_backbone_adj_lists = []
    for potential_backbones, largest_backbone in zip(backbones, largest_backbones):
        backbone_set = set(largest_backbone)
        potential_backbones = list(map(lambda item: item[1] if item[0] in backbone_set else False, enumerate(potential_backbones)))
        largest_backbone_adj_lists.append(potential_backbones)

    flatten = lambda l: [item for sublist in l for item in sublist]
    largest_backbone_adj_lists.sort(key=lambda backbone: -len(flatten(filter(lambda n: n!=False,backbone))))

    draw_largest_backbones(largest_backbone_adj_lists, positions, coloring)

    draw_dominations(largest_backbone_adj_lists, positions, coloring, adj_list)
