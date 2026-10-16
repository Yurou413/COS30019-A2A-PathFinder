import heapq

from heuristic import heuristic

def astar(nodes, graph, origin, destinations):
    # Priority queue: (f, node, sequence, g, path)
    frontier = []
    sequence = 0

    start_h = heuristic(nodes, origin, destinations)
    heapq.heappush(
        frontier, (start_h, origin, sequence, 0, [origin])
    )

    nodes_created = 1

    while frontier:
        f, current, _, g, path = heapq.heappop(frontier)

        # Check whether a destination has been reached
        if current in destinations:
            return current, nodes_created, path

        # Expand neighbours in ascending node-number order
        for neighbour, edge_cost in sorted(
            graph.get(current, []), key=lambda edge: edge[0]
        ):
            # Avoid cycles within the current path
            if neighbour not in path:
                new_g = g + edge_cost
                new_h = heuristic(nodes, neighbour, destinations)
                new_f = new_g + new_h
                new_path = path + [neighbour]

                sequence += 1

                heapq.heappush(
                    frontier,
                    (
                        new_f,
                        neighbour,
                        sequence,
                        new_g,
                        new_path
                    )
                )

                nodes_created += 1

    return None, nodes_created, []