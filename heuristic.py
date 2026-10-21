def heuristic(nodes, node, destinations):
    # A zero heuristic never overestimates the remaining path cost.
    return 0