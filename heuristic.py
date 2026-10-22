import math

def heuristic(nodes, node, destinations):
    x1, y1 = nodes[node]

    # Find the estimated distance to the nearest destination
    distances = []

    for destination in destinations:
        x2, y2 = nodes[destination]

        distance = math.sqrt(
            (x2 - x1) ** 2 + (y2 - y1) ** 2
        )

        distances.append(distance)

    return min(distances)
