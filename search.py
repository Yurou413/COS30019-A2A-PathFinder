
import sys
import re
from collections import deque


def read_problem(filename):
    nodes = {}
    edges = []
    origin = None
    destinations = []
    section = None

    with open(filename, "r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()

            if not line:
                continue

            if line == "Nodes:":
                section = "nodes"
                continue
            elif line == "Edges:":
                section = "edges"
                continue
            elif line == "Origin:":
                section = "origin"
                continue
            elif line == "Destinations:":
                section = "destinations"
                continue

            if section == "nodes":
                match = re.fullmatch(
                    r"(\d+):\s*\((\d+),\s*(\d+)\)", line
                )
                if match:
                    node = int(match.group(1))
                    x = int(match.group(2))
                    y = int(match.group(3))
                    nodes[node] = (x, y)

            elif section == "edges":
                match = re.fullmatch(
                    r"\((\d+),\s*(\d+)\):\s*(\d+)", line
                )
                if match:
                    start = int(match.group(1))
                    end = int(match.group(2))
                    cost = int(match.group(3))
                    edges.append((start, end, cost))

            elif section == "origin":
                origin = int(line)

            elif section == "destinations":
                destinations = [
                    int(value.strip()) 
                    for value in line.split(";") # Splits the text wherever it finds a semicolon.
                    if value.strip() # Remove whitespace around each value.
                ]

    if not nodes: # If the nodes dictionary is empty.
        raise ValueError("No nodes found in the input file.")

    if origin not in nodes: # Checks whether the origin exists in the dictionary.
        raise ValueError("Origin is missing or invalid.")

    # Checks whether the destination list is empty.
    # Checks whether at least one destination does not exist in the graph.
    if not destinations or any(d not in nodes for d in destinations):
        raise ValueError("Destinations are missing or invalid.")

    # Creates a dictionary containing every node, with an initially empty list of heighbours.
    graph = {node: [] for node in nodes}

    # Loops through every edge in the list.
    for start, end, cost in edges:
        if start not in nodes or end not in nodes:
            raise ValueError("An edge refers to an unknown node.")

        # Adds the neighbour and edge cost to the starting node's adjacency list.
        graph[start].append((end, cost))

    # Loops through by node ID, from smallest to largest.
    for node in graph:
        # Sort using the first item of each edge tuple, which is the neighbour's node ID.
        graph[node].sort(key=lambda edge: edge[0]) 

    return nodes, graph, origin, destinations


# Depth-First Search
def dfs(graph, origin, destinations):
    # Each stack entry contains the current node and its path.
    stack = [(origin, [origin])] # The initial node is 2, so one search node has been created.
    nodes_created = 1

    while stack:
        current, path = stack.pop()

        if current in destinations:
            return current, nodes_created, path

        # Add neighbouring nodes to the stack.
        for neighbour, cost in reversed(graph[current]):
            # Avoid revisiting a node on the current path.
            if neighbour not in path:
                stack.append((neighbour, path + [neighbour]))
                nodes_created += 1

    return None, nodes_created, []
    # 5, 7 means goal node 5 was found after 7 search nodes had been created.


def bfs(graph, origin, destinations):
    # Each queue entry contains the current node and its path.
    queue = deque([(origin, [origin])])
    nodes_created = 1

    while queue:
        current, path = queue.popleft() # popleft() removes the node entered the queue first.

        if current in destinations:
            return current, nodes_created, path

        for neighbour, cost in graph[current]:
            # Avoid revisiting a node on the current path.
            if neighbour not in path:
                queue.append((neighbour, path + [neighbour]))
                nodes_created += 1

    return None, nodes_created, []


def main():
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        return

    filename = sys.argv[1]
    method = sys.argv[2].upper()

    try:
        nodes, graph, origin, destinations = read_problem(filename)

        if method == "DFS":
            goal, count, path = dfs(graph, origin, destinations)
        elif method == "BFS":
            goal, count, path = bfs(graph, origin, destinations)
        else:
            print("Unsupported method. Use DFS or BFS.")
            return

        if goal is None:
            print(f"{filename} {method}")
            print("No solution found.")
        else:
            print(f"{filename} {method}")
            print(f"{goal} {count}")
            print(" -> ".join(map(str, path)))

    except (OSError, ValueError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
