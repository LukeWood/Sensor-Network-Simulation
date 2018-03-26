def smallest_last_vertex_ordering(adj_list):
    lengths_to_nodes = []
    nodes_to_length = {}
    for node_num,row in enumerate(adj_list):
        length = len(row)
        while length > len(nodes_to_lengths):
            lengths_to_nodes.append(set())
        lengths_to_nodes[length].add(node_num)
        nodes_to_lengths[node_num] = length
    return lengths_to_nodes, nodes_to_length

def color_graph(adj_list):
    lengths_to_nodes, nodes_to_length = smallest_last_vertex_ordering(adj_list)
    max_degree = len(lengths_to_nodes)
    index = 0
    colors = [False for _ in adj_list]
    while index < max_degree:
        node = next(iter(lengths_to_nodes[index]))
        neighbors = adj_list[node]
        used_colors = set([colors[neighbor] for neighbor in neighbors])
        current_color = 0
        while current_color in used_colors:
            current_color+=1
        colors[node] = current_color

        for neighbor in neighbors:
            length = nodes_to_length[neighbor]
            lengths_to_nodes[length].remove(neighbor)
            lengths_to_nodes[length-1].add(neighbor)
            nodes_to_length[neighbor] = length-1

    return colors
