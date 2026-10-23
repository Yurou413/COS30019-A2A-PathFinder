import math


def get_cost_scale(nodes, graph):
    ratios = []

    for start, neighbours in graph.items():
        for end, cost in neighbours:
            if cost < 0:
                raise ValueError("Edge costs must be nonnegative.")

            length = math.dist(nodes[start], nodes[end])

            if length > 0:
                ratios.append(cost / length)

    return min(ratios) if ratios else 0.0


def heuristic(nodes, node, destinations, cost_scale):
    if cost_scale == 0:
        return 0.0

    nearest_distance = min(
        math.dist(nodes[node], nodes[goal])
        for goal in destinations
    )

    return cost_scale * nearest_distance