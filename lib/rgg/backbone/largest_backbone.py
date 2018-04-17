
def largest_backbone(adj_list):
    visited = {}
    largest_backbone = []
    for node_index, node in enumerate(adj_list):
        if node_index in visited or node == False: continue
        current_backbone = []
        stack = [node_index]
        while len(stack) != 0:
            current_node = stack.pop()
            if current_node in visited: continue
            visited[current_node] = True
            current_backbone.append(current_node)
            for neighbor in adj_list[current_node]:
                stack.append(neighbor)
        if len(current_backbone) > len(largest_backbone):
            largest_backbone = current_backbone
    return largest_backbone
