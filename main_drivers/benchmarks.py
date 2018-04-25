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
    (11, 16000,   64, "Sphere", unit_sphere_graph),
    (12, 32000,   128,"Sphere", unit_sphere_graph),
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

with open("../results/benchmarks/full_benchmark.csv", "w+") as f:
    headers = ["Benchmark","N","A","R","Topology","Num Edges","Avg. Degree","Min Degree",
        "Max Degree","Average Degree When Removed","Colors","Largest Color", "Terminal Clique Size",
        "Backbone Order","Backbone Size","Backbone Domination",
        "Number of Backbone Faces",
        "Generation Runtime (Seconds)", "Coloring Runtime (Seconds)", "Backbone Runtime (Seconds)", "Total Runtime (Seconds)"]
    f.write(",".join(headers)+"\n")
    for benchmark, N, A, topology, fn in benchmarks:
        print("Running benchmark %d" % benchmark)
        start_generation = process_time()
        adj_list,positions, R = fn(N, A, return_radius=True, return_positions=True)
        end_generation = process_time()
        start_coloring = end_generation
        ordering, degrees_when_removed, terminal_clique_size = compute_ordering(adj_list, return_terminal_clique_size=True)
        coloring = color_graph(ordering, adj_list)
        end_coloring = process_time()
        start_backbone = end_coloring
        potential_backbones = find_potential_backbones(coloring, adj_list)
        end_backbone = process_time()

        largest_backbones = list(map(largest_backbone, potential_backbones))
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

        runtime = end_backbone - start_generation
        coloring_runtime = end_coloring - start_coloring
        generation_runtime = end_generation - start_generation
        backbone_runtime = end_backbone - start_backbone
        number_one_backbone=largest_backbone_adj_lists[0]
        backbone_order = len(flatten(filter(lambda x: x != False, number_one_backbone)))
        backbone_size = len(list(filter(lambda x: x!=False, number_one_backbone)))
        backbone_nodes = []
        backbone_edges = []
        for node, neighbors in enumerate(number_one_backbone):
            if neighbors == False:
                continue
            backbone_nodes.append(node)
            backbone_edges.append(neighbors)

        dominated_nodes = set()
        for node in backbone_nodes:
            dominated_nodes.add(node)
            for neighbor in adj_list[node]:
                dominated_nodes.add(neighbor)
        backbone_domination=len(dominated_nodes)/len(adj_list)

        num_faces = "N/A"
        if topology == "Sphere":
            num_edges = sum(map(lambda node: len(node),backbone_edges))
            num_faces = 2 + num_edges - len(backbone_nodes)
            num_faces = str(num_faces)

        from math import sqrt
        from math import pi
        if topology == "Square":
            R=sqrt(A /(N * pi))
        elif topology == "Disc":
            R=sqrt(A/N)
        elif topology == "Sphere":
            R=sqrt(2*A/N)

        f.write("%d,%d,%d,%.6f," % (benchmark, N, A, R))
        f.write("%s,%d,%.6f,%d,%d," % (topology, avg_degree*N,avg_degree,min_degree,max_degree))
        f.write("%d,%d,%d,%d,%d," % (max_degree_when_removed, num_colors,largest_color, terminal_clique_size, backbone_order))
        f.write("%d,%.6f,%s,%.6f," % (backbone_size, backbone_domination, num_faces,generation_runtime))
        f.write("%.6f,%.6f,%.6f" %(coloring_runtime, backbone_runtime, runtime))
        f.write("\n")
        f.flush()
