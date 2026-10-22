## COS30019-A2A-PathFinder
Assignment 2A-Tree Based Search
## Team
Team ID: Sushi

Members:

1. Vivian Yee Shan THEN (104396350)
2. Hui Ming TANG (104399731)
3. Yu Rou YAP (105805297)
4. Violet Grace Jia Yun LIM (105806698)
## Overview

PathFinder finds a path from a starting node to one of the destination nodes. The graph has directed edges with different costs.

The program has six search methods.

| Method | Algorithm |
|---|---|
| DFS | Depth-First Search |
| BFS | Breadth-First Search |
| GBFS | Greedy Best-First Search |
| AS | A* Search |
| CUS1 | Uniform-Cost Search |
| CUS2 | A* Search Using Move Count |

## Requirements

- Python 3
- No extra Python packages are needed.

## Folder Structure

```text
project/
├── search.py
├── problem.py
├── heuristic.py
├── README.md
├── test-results.txt
├── Algorithms/
│   ├── dfs.py
│   ├── bfs.py
│   ├── gbfs.py
│   ├── astar.py
│   ├── cus1.py
│   └── cus2.py
└── problems/
    ├── PathFinder-test-1.txt
    ├── ...
    └── PathFinder-test-16.txt
```

| File or folder | Purpose |
|---|---|
| `search.py` | Runs the selected search method and prints the result |
| `problem.py` | Reads the problem file and builds the graph |
| `heuristic.py` | Contains the shared heuristic for GBFS and A* |
| `Algorithms/` | Contains the six search methods |
| `problems/` | Contains the test files |
| `test-results.txt` | Stores the recorded test results |

## How to Run

1. Download and extract the project ZIP.
2. Open the folder containing `search.py`.
3. Click the folder address bar, type `cmd` and press Enter.
4. Run the program using this format:

```text
python search.py <filename> <method>
```

For example:

```text
python search.py problems/PathFinder-test-1.txt AS
```

### Commands for All Six Methods

```text
python search.py problems/PathFinder-test-1.txt DFS
python search.py problems/PathFinder-test-1.txt BFS
python search.py problems/PathFinder-test-1.txt GBFS
python search.py problems/PathFinder-test-1.txt AS
python search.py problems/PathFinder-test-1.txt CUS1
python search.py problems/PathFinder-test-1.txt CUS2
```

Change the filename to run another test case.

## Input Format

Each problem file has four sections.

```text
Nodes:
1: (0,0)
2: (1,0)
3: (2,0)
Edges:
(1,2): 3
(2,3): 2
Origin:
1
Destinations:
3
```

| Section | Meaning |
|---|---|
| `Nodes:` | Lists the node IDs and their coordinates |
| `Edges:` | Lists the directed edges and their costs |
| `Origin:` | Gives the starting node |
| `Destinations:` | Lists the possible destination nodes |

Edges have a direction. For example, `(1,2): 3` means travelling from node 1 to node 2 costs 3. It does not mean you can travel from node 2 to node 1.

Use semicolons to separate multiple destinations:

```text
Destinations:
5; 4
```

The search stops when it reaches any one of them.

### Input Limits

The program accepts nonnegative whole numbers for node IDs, coordinates and edge costs.

It checks that the starting node, destination nodes and nodes used in edges exist.

Some wrongly written node or edge lines may be skipped without an error message. Follow the input format carefully.

## Output Format

When a destination is reached, the output has this format:

```text
filename method
goal nodes_created
path
```

Example:

```text
problems/PathFinder-test-1.txt AS
5 8
2 -> 3 -> 5
```

| Output | Meaning |
|---|---|
| `problems/PathFinder-test-1.txt` | The test file used |
| `AS` | The selected search method |
| `5` | The destination reached |
| `8` | The number of search entries created |
| `2 -> 3 -> 5` | The path from the start to the destination |

The number of created entries includes the starting entry. The same graph node can be counted more than once if it is reached through different paths.

This is not the number of different graph nodes or expanded nodes.

If no destination can be reached, the program prints the filename and method, followed by:

```text
No solution found.
```

## How the Methods Work

| Method | Basic idea |
|---|---|
| DFS | Follows one branch deeply before trying another branch |
| BFS | Searches one level at a time to find the fewest moves |
| GBFS | Chooses an entry using its estimated remaining cost |
| AS | Uses the cost travelled so far plus an estimated remaining cost |
| CUS1 | Chooses the entry with the lowest cost travelled so far |
| CUS2 | Uses the moves taken so far plus an estimate of the remaining moves |

BFS and CUS2 find a path with the fewest moves. This may not be the cheapest path.

DFS and GBFS do not always find the cheapest path.

CUS1 finds the cheapest path when edge costs are nonnegative. A* also found minimum-cost paths in the recorded tests, but its current Euclidean heuristic does not guarantee this for every graph.

## Implementation Notes

### Neighbour Order

Neighbours are added in increasing node-ID order.

DFS adds them to its stack in reverse order so that smaller IDs are processed first.

### A* Tie-Breaking

A* uses this priority queue entry:

```python
(f, sequence, node, g, path)
```

When two entries have the same `f` score, the entry added first is processed first.

### Cycle Handling

DFS, BFS, GBFS and A* do not revisit a node already in the current path.

CUS1 and CUS2 use dictionaries to keep the best cost or move count found for each node. Entries that do not improve the stored value are skipped.

### Shared Heuristic

GBFS and A* use the straight-line distance to the nearest destination as their heuristic. GBFS selects entries using this estimate, while A* adds it to the cost travelled so far. CUS2 uses its own heuristic based on the estimated number of remaining moves.

### CUS2 Heuristic

CUS2 has its own heuristic inside `cus2.py`.

It divides the straight-line distance to the nearest goal by the longest geometric edge length, then rounds down:

```text
floor(distance to nearest goal / longest geometric edge length)
```

If the longest edge length is zero, it returns zero.

This estimates the remaining moves. CUS2 uses move count rather than total edge cost.

## Testing

There are 16 test files in the `problems` folder.

The recorded results are saved in `test-results.txt`.

| Test cases | Methods tested | Number of runs |
|---|---|---|
| 1–15 | DFS, BFS, GBFS, AS, CUS1 and CUS2 | 90 |
| 16 | AS only | 1 |
| **Total** | | **91** |

Case 14 has an unreachable destination. Therefore, `No solution found.` is the expected result.

### Test 16 — A* Tie-Breaking

Test 16 checks whether A* uses the order entries were added when two entries on different branches have the same score.

Run:

```text
python search.py problems/PathFinder-test-16.txt AS
```

Expected output:

```text
problems/PathFinder-test-16.txt AS
9 5
1 -> 2 -> 9
```

### Running the Recorded Tests Again

Open a Windows Command Prompt in the project folder.

Run this command to test all six methods on cases 1–15:

```bat
(for /L %i in (1,1,15) do @for %m in (DFS BFS GBFS AS CUS1 CUS2) do @python search.py problems/PathFinder-test-%i.txt %m) > test-results.txt 2>&1
```

Then run this command to add the A* result for case 16:

```bat
python search.py problems/PathFinder-test-16.txt AS >> test-results.txt 2>&1
```

The first command replaces the old results file. The second command adds the new result at the end.

To view the results:

```text
notepad test-results.txt
```

These commands are for typing directly into Command Prompt. If they are saved in a `.bat` file, use `%%i` and `%%m` instead of `%i` and `%m`.

## Known Limitations and Items to Confirm

| Item | Current situation |
|---|---|
| Euclidean heuristic | Straight-line distance may overestimate the remaining cost because edge costs are not always based on geometric distance. A* is therefore not guaranteed to find the cheapest path for every graph. |
| CUS1 and CUS2 | They use global dictionaries to reduce repeated searches. We still need to confirm whether this is allowed under the tree-based search requirement. |
| Input values | Negative numbers and decimal numbers are not supported. |
| Input errors | Some wrongly written node or edge lines may be skipped without an error message. |
| Test 16 | Only AS has a recorded result for this case. |
