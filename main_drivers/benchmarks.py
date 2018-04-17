from rgg.coloring import compute_ordering, color_graph, valid_coloring
from rgg.generate_graphs import unit_square_graph
from rgg.generate_graphs import unit_disc_graph
from rgg.generate_graphs import unit_sphere_graph
from rgg.backbone import find_potential_backbones, largest_backbone
from time import process_time

benchmarks = [
    (1,  1000,    32, "Square", unit_square_graph),
    (2,  8000,    64, "Square", unit_square_graph),
    (3,  16000,   32, "Square", unit_square_graph),
    (4,  64000,   64, "Square", unit_square_graph),
    (5,  64000,   128,"Square", unit_square_graph),
    (6,  128000,  64, "Square", unit_square_graph),
    (7,  128000,  128,"Square", unit_square_graph),
    (8,  8000,    64, "Disc",   unit_disc_graph),
    (9,  64000,   64, "Disc",   unit_disc_graph),
    (10, 64000,   128,"Disc",   unit_disc_graph),
    (12, 32000,   128,"Sphere", unit_sphere_graph),
    (11, 16000,   64, "Sphere", unit_sphere_graph),
    (13, 64000,   128,"Sphere", unit_sphere_graph)
]

def draw_backbone(backbones, positions, coloring, A, N, topology):
    if topology == "Sphere":
        positions = list(map(lambda x: (x[0], x[1]), positions))
    import matplotlib.pyplot as plt
    import networkx as nx
    plt.clf()
    fig, axes = plt.subplots(1, 2)
    x = 0
    y = 0
    colors = ['#6A1B9A', '#D50000', '#AEEA00', '#00B0FF', '#00B8D4', '#00BFA5', '#00C853', '#DD2C00', '#FFFF00']

    first_round=[]
    second_round=[]
    for current_backbone in backbones:
        G = nx.Graph()
        zorder={}
        current_backbone_set = set(filter(lambda x: x != False, map(lambda c: c[0] if c[1] != False else False, enumerate(current_backbone))))
        for node_index, node in enumerate(current_backbone):
            if node == False:
                G.add_node(node_index)
                zorder[node_index] = -1
                continue
            G.add_node(node_index)
            zorder[node_index] = 21
            for neighbor in node:
                if neighbor in current_backbone_set:
                    G.add_edge(node_index, neighbor)

        pos = {}
        for node_index, position in enumerate(positions):
            pos[node_index] = position

        color_map = [colors[coloring[x]%len(colors)] if current_backbone[x] != False else "#CCCCCC" for x in G.node]
        nx.draw(G, pos=pos, node_color=color_map, ax=axes[x], node_size=2500/(N*N))
        pathcollection = nx.draw_networkx_edges(G, pos=pos, zorder=20, node_color=color_map, ax=axes[x], node_size=2500/(N*N))
        pathcollection.zorder = 20
        x = x + 1
    plt.suptitle("Two Biggest Backbones of RGG N=%d, A=%d, Topology=%s" % (N, A, topology))
    plt.savefig("../results/backbone/backbone_%d_%d_%s.png" % (N, A, topology), bbox_inches="tight")

with open("../results/shared/coloring/coloring_data.csv", "w+") as f:
    f.write("Benchmark,N,A,R,Topology,Avg. Degree,Min Degree,Max Degree,When Removed,Colors,Largest Color,Runtime\n")
    for benchmark, N, A, topology, fn in benchmarks:
        print("Running benchmark %d" % benchmark)
        start = process_time()
        adj_list,positions, R = fn(N, A, return_radius=True, return_positions=True)
        ordering, degrees_when_removed = compute_ordering(adj_list)
        coloring = color_graph(ordering, adj_list)
        potential_backbones = find_potential_backbones(coloring, adj_list)

        largest_backbones = list(map(largest_backbone, potential_backbones))

        end = process_time()

        largest_backbone_adj_lists = []
        for potential_backbones2, backbone in zip(potential_backbones, largest_backbones):
            backbone_set = set(backbone)
            potential_backbones2 = list(map(lambda item: item[1] if item[0] in backbone_set else False, enumerate(potential_backbones2)))
            largest_backbone_adj_lists.append(potential_backbones2)

        flatten = lambda l: [item for sublist in l for item in sublist]
        largest_backbone_adj_lists.sort(key=lambda backbone: -len(flatten(filter(lambda n: n!=False,backbone))))
        draw_backbone(largest_backbone_adj_lists[:2], positions, coloring, N, A, topology)

        num_colors = max(coloring)
        max_degree_when_removed = max(degrees_when_removed)
        min_degree = min(map(lambda node: len(node),adj_list))
        max_degree = max(map(lambda node: len(node),adj_list))
        avg_degree = sum(map(lambda node: len(node),adj_list))/len(adj_list)
        color_counts = [0 for _ in range(num_colors + 1)]

        for color in coloring:
            color_counts[color] = color_counts[color] + 1
        largest_color = max(color_counts)
        runtime = end - start

        f.write("%d,%d,%d,%.6f,%s,%d,%d,%d,%d,%d,%d,%.6f" % (benchmark, N, A, R, topology,avg_degree,min_degree,max_degree, max_degree_when_removed, num_colors,largest_color, runtime))
        f.write("\n")
        f.flush()
