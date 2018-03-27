def valid_coloring(coloring, adj_list):
    for color, neighbors in zip(coloring, adj_list):
        neighbor_colors = set([coloring[neighbor] for neighbor in neighbors])
        if color in neighbor_colors:
            return False
    return True
