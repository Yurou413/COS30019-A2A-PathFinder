import heapq
from heuristic import heuristic


def gbfs(nodes, graph, origin, destinations):
    sequence = 0

    frontier = [
        (
            heuristic(nodes, origin, destinations),
            sequence,
            origin,
            [origin]
        )
    ]

    nodes_created = 1

    while frontier:
        h, order, current, path = heapq.heappop(frontier)

        if current in destinations:
            return current, nodes_created, path

        for neighbour, cost in sorted(
            graph.get(current, []), key=lambda edge: edge[0]
        ):
            if neighbour not in path:
                sequence += 1

                new_path = path + [neighbour]
                new_h = heuristic(nodes, neighbour, destinations)

                heapq.heappush(
                    frontier,
                    (new_h, sequence, neighbour, new_path)
                )

                nodes_created += 1

    return None, nodes_created, []