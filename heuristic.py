def heuristic(nodes, node, destinations):
    x, y = nodes[node]
    return min(
        ((x - nodes[goal][0]) ** 2 + (y - nodes[goal][1]) ** 2) ** 0.5
        for goal in destinations
    )