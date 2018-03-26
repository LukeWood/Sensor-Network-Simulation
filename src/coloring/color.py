def color_graph(ordering, adj_list):
    coloring = [-1 for _ in ordering]
    for node in ordering:
        color = 0
        used_colors = set([coloring[neighbor] for neighbor in adj_list[node]])
        while color in used_colors:
            color = color + 1
        coloring[node] = color
    return coloring

def compute_ordering(adj_list, lengths_when_removed_returned=False):
    ordering = []
    max_degree = max(map(lambda x: len(x), adj_list))
    length_to_nodes = {}
    for i in range(max_degree+1):
        length_to_nodes[i] = set()
    length_to_nodes[-1] = set()
    node_to_length = [len(node) for node in adj_list]
    lengths_when_removed = [-1 for _ in adj_list]

    for i, node in enumerate(adj_list):
        l = len(node)
        length_to_nodes[l].add(i)

    while len(ordering) != len(adj_list):
        index = 0
        while len(length_to_nodes[index]) == 0:
            index=index + 1
        for node in length_to_nodes[index]: break
        ordering.append(node)
        lengths_when_removed[node] = node_to_length[node]
        for neighbor in adj_list[node]:
            l = node_to_length[neighbor]
            if neighbor in length_to_nodes[l]:
                node_to_length[l] = node_to_length[neighbor]-1
                length_to_nodes[l].remove(neighbor)
                length_to_nodes[l-1].add(neighbor)
        length_to_nodes[index].remove(node)
    if lengths_when_removed_returned:
        return ordering, lengths_when_removed
    else:
        return ordering
