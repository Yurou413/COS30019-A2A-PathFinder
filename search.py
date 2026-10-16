
import sys

from problem import read_problem
from Algorithms.dfs import dfs
from Algorithms.bfs import bfs
from Algorithms.gbfs import gbfs
from Algorithms.astar import astar


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
        elif method == "GBFS":
            goal, count, path = gbfs(nodes, graph, origin, destinations)
        elif method == "AS":
            goal, count, path = astar(nodes, graph, origin, destinations)
        else:
            print("Unsupported method. Use DFS, BFS, GBFS or A Star.")
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
