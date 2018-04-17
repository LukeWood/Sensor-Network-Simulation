def top_four_colors(color_frequencies):
    def custom_cmp(val):
        return -val[1]
    item_with_freqs = list(color_frequencies.items())
    item_with_freqs.sort(key=custom_cmp)
    top_four = item_with_freqs[:4]
    top_colors = []
    for color, _size in top_four:
        top_colors.append(color)
    return top_colors

def color_frequencies(coloring):
    from functools import reduce
    def increment_color(frequency_table, color):
        frequency_table[color] = frequency_table[color]+1 if color in frequency_table else 1
        return frequency_table
    return reduce(increment_color, coloring, {})

def possible_backbones(top_colors):
    from itertools import combinations
    return list(combinations(top_colors, r=2))

def find_backbones(coloring, adj_list):
    top_colors = top_four_colors(color_frequencies(coloring))
    backbone_colors = possible_backbones(top_colors)

    backbones = []
    for color_combination in backbone_colors:
        color_set = set(color_combination)
        adj_list_width_false_nodes = []
        for node,color in zip(adj_list, coloring):
            if color in color_set:
                adj_list_width_false_nodes.append(node)
            else:
                adj_list_width_false_nodes.append(False)
        adj_list_with_updated_edges = []
        for node in adj_list_width_false_nodes:
            if node == False:
                adj_list_with_updated_edges.append(False)
                continue
            new_node = []
            for edge in node:
                if coloring[edge] in color_set:
                    new_node.append(edge)
                else:
                    pass
            adj_list_with_updated_edges.append(new_node)
        backbones.append(adj_list_with_updated_edges)
    return backbones
