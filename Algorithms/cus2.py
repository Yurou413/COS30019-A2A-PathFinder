import math
import heapq 
from itertools import count


def custom_search_2(nodes, edges, origin, destinations):

    # Maximum geometric length of any edge
    max_edge_length = 0

    for start, end, cost in edges:
        x1, y1 = nodes[start]
        x2, y2 = nodes[end]

        length = math.hypot(x2 - x1, y2 - y1)
        max_edge_length = max(max_edge_length, length)

    def heuristic(node):
        if not destinations or max_edge_length == 0:
            return 0

        x1, y1 = nodes[node]
        distances = []

        for goal in destinations:
            x2, y2 = nodes[goal]
            distances.append(math.hypot(x2 - x1, y2 - y1))

        # Lower bound on the number of remaining edges
        return math.floor(min(distances) / max_edge_length)

    tie_breaker = count()
    frontier = [
        (heuristic(origin), 0, next(tie_breaker), origin, [origin])
    ]
    best_moves = {origin: 0}
    nodes_created = 1

    while frontier:
        _, moves, _, current, path = heapq.heappop(frontier)

        if moves != best_moves.get(current):
            continue

        if current in destinations:
            return current, nodes_created, path

        for neighbour, edge_cost in sorted(
            graph[current], key=lambda item: item[0]
        ):
            new_moves = moves + 1

            if new_moves < best_moves.get(neighbour, float("inf")):
                best_moves[neighbour] = new_moves

                heapq.heappush(
                    frontier,
                    (
                        new_moves + heuristic(neighbour),
                        new_moves,
                        next(tie_breaker),
                        neighbour,
                        path + [neighbour]
                    )
                )
                nodes_created += 1

    return None, nodes_created, []
