"""
Shortest Path Algorithm Workshop
================================

This program implements Dijkstra's shortest-path algorithm using an
adjacency matrix.

The algorithm calculates:

1. The shortest distance from a starting node to every reachable node.
2. The actual sequence of nodes forming each shortest path.

Important limitation:
Dijkstra's algorithm requires all edge weights to be non-negative.
"""

# Positive infinity represents the absence of a direct connection
# between two nodes in the adjacency matrix.
INF = float("inf")


# Adjacency matrix representing the weighted graph.
#
# Each row and column corresponds to a node:
#
#     0, 1, 2, 3, 4, 5
#
# matrix[i][j] represents the weight of the edge from node i to node j.
#
# A value of:
# - 0 means the node is connected to itself.
# - INF means there is no direct edge between the two nodes.
# - Any positive number represents the edge weight.
adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]


def shortest_path(matrix, start_node, target_node=None):
    """
    Find the shortest paths from a starting node using Dijkstra's algorithm.

    Parameters
    ----------
    matrix : list[list[float]]
        A square adjacency matrix representing the weighted graph.

    start_node : int
        The index of the node where the search begins.

    target_node : int | None, optional
        A specific destination node.

        When target_node is provided, the function displays only the
        shortest path to that node.

        When target_node is None, the function displays the shortest
        paths to all reachable nodes.

    Returns
    -------
    None
        The function prints the shortest distances and paths directly.

    Notes
    -----
    This implementation assumes that:

    - The graph contains no negative edge weights.
    - The matrix is square.
    - Node numbers correspond to matrix indices.
    """

    # Determine the number of nodes in the graph.
    n = len(matrix)

    # Initialize the known distance to every node as infinity.
    #
    # At the beginning, no routes have been discovered.
    distances = [INF] * n

    # The distance from the starting node to itself is always zero.
    distances[start_node] = 0

    # Store the path used to reach each node.
    #
    # Initially, each path contains only its corresponding node.
    # The paths will be replaced whenever a shorter route is found.
    paths = [[node_no] for node_no in range(n)]

    # Track whether each node has already been permanently processed.
    visited = [False] * n

    # Dijkstra's algorithm processes at most n nodes.
    for _ in range(n):

        # Start each search with no selected node and an infinite
        # minimum distance.
        min_distance = INF
        current = -1

        # Find the unvisited node with the smallest known distance
        # from the starting node.
        for node_no in range(n):
            if (
                not visited[node_no]
                and distances[node_no] < min_distance
            ):
                min_distance = distances[node_no]
                current = node_no

        # If no reachable unvisited node remains, the algorithm
        # has completed its work.
        if current == -1:
            break

        # Mark the selected node as permanently processed.
        #
        # Its shortest distance is now considered final.
        visited[current] = True

        # Examine every possible neighbor of the current node.
        for node_no in range(n):

            # Retrieve the direct edge weight from the current node
            # to the candidate neighboring node.
            distance = matrix[current][node_no]

            # Process the node only when:
            #
            # 1. A direct edge exists.
            # 2. The neighboring node has not been finalized.
            if distance != INF and not visited[node_no]:

                # Calculate the distance to the neighboring node
                # through the current node.
                new_distance = distances[current] + distance

                # Relaxation step:
                #
                # If the newly discovered route is shorter than the
                # previously known route, update both the distance
                # and the corresponding path.
                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance

                    # Copy the path to the current node and append
                    # the neighboring node to form the new route.
                    paths[node_no] = paths[current] + [node_no]

    # Decide which results should be displayed.
    #
    # If a target node was supplied, process only that node.
    # Otherwise, process every node in the graph.
    targets = (
        [target_node]
        if target_node is not None
        else range(n)
    )

    # Display the calculated shortest-path results.
    for node_no in targets:

        # Do not print:
        #
        # 1. A path from the starting node to itself.
        # 2. Nodes that cannot be reached from the starting node.
        if node_no == start_node or distances[node_no] == INF:
            continue

        # Convert each integer node number in the path into a string.
        #
        # This generator produces one converted node at a time.
        string_path = (str(node) for node in paths[node_no])

        # Join the node numbers into a readable route.
        #
        # Example:
        # [0, 2, 3] becomes "0 -> 2 -> 3".
        path = " -> ".join(string_path)

        # Display the final distance and complete shortest path.
        print(
            f"\n{start_node}-{node_no} "
            f"distance: {distances[node_no]}\n"
            f"Path: {path}"
        )


def main():
    """
    Run demonstration examples for the shortest-path algorithm.
    """

    print("Shortest paths from node 0 to all reachable nodes:")
    shortest_path(adj_matrix, 0)

    print("\nShortest path from node 0 to node 5:")
    shortest_path(adj_matrix, 0, 5)


# Run the demonstration only when this file is executed directly.
#
# This prevents main() from running automatically if the module is
# imported into another Python file.
if __name__ == "__main__":
    main()
