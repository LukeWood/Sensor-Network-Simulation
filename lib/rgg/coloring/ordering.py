def first_of_set(s):
    if len(s) == 0:
        raise ValueError("Empty set given to function 'first_of_set/1'")
    for item in s: break
    return item

def compute_ordering(adj_list):
    ordering = []
    max_degree = max(map(lambda x: len(x), adj_list))
    length_to_nodes = {}

    for i in range(max_degree+1):
        length_to_nodes[i] = set()
    length_to_nodes[-1] = set()

    node_to_length = [len(node) for node in adj_list]
    lengths_when_removed = [-1 for _ in adj_list]

    for i, node in enumerate(adj_list):
        degree = len(node)
        length_to_nodes[degree].add(i)

    while len(ordering) != len(adj_list):
        index = 0
        while len(length_to_nodes[index]) == 0:
            index=index + 1
        node = first_of_set(length_to_nodes[index])
        ordering.append(node)
        lengths_when_removed[node] = node_to_length[node]
        for neighbor in adj_list[node]:
            neighbor_len = node_to_length[neighbor]
            if neighbor in length_to_nodes[neighbor_len]:
                node_to_length[neighbor] = neighbor_len-1
                length_to_nodes[neighbor_len].remove(neighbor)
                length_to_nodes[neighbor_len-1].add(neighbor)
        length_to_nodes[index].remove(node)
    return ordering[::-1], lengths_when_removed
