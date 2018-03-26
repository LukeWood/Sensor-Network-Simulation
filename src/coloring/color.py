def smallest_last_vertex_ordering(adj_list):
    lengths_to_nodes = []
    nodes_to_lengths = {}
    for node_num,row in enumerate(adj_list):
        length = len(row)
        while length >= len(lengths_to_nodes):
            lengths_to_nodes.append(set())
        lengths_to_nodes[length].add(node_num)
        nodes_to_lengths[node_num] = length
    return lengths_to_nodes, nodes_to_lengths

def color_graph(adj_list):
    lengths_to_nodes, nodes_to_lengths = smallest_last_vertex_ordering(adj_list)
    max_degree = len(lengths_to_nodes)
    colors = [-1 for _ in adj_list]
    count = 0
    while count < len(adj_list):
        index = 0
        while index < len(lengths_to_nodes) and len(lengths_to_nodes[index]) == 0:
            index = index + 1
        if index == len(lengths_to_nodes):
            break
        for node in lengths_to_nodes[index]: break
        neighbors = adj_list[node]
        used_colors = set([colors[neighbor] for neighbor in neighbors])
        current_color = 0
        while current_color in used_colors:
            current_color+=1
        colors[node] = current_color
        for neighbor in neighbors:
            length = nodes_to_lengths[neighbor]
            nlength = length-1
            nodes_to_lengths[neighbor] = nlength
            if neighbor in lengths_to_nodes[length]:
                lengths_to_nodes[length].remove(neighbor)
                lengths_to_nodes[nlength].add(neighbor)
        lengths_to_nodes[index].remove(node)
        count + 1
    return max(colors)
