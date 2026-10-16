import re

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