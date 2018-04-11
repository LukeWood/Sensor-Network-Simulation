def color_graph(ordering, adj_list):
    coloring = [-1 for _ in ordering]
    for node in ordering:
        color = 0
        used_colors = set([coloring[neighbor] for neighbor in adj_list[node]])
        while color in used_colors:
            color = color + 1
        coloring[node] = color
    return coloring
