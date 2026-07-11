"""
Depth-First Search Algorithm
============================

This module implements depth-first search (DFS) for an undirected graph
represented by an adjacency matrix.

Depth-first search explores one path as deeply as possible before
backtracking to visit other unvisited branches.

The implementation uses a stack, which follows the Last-In-First-Out
(LIFO) principle.
"""


def dfs(undirected_adj_matrix, node_label):
    """
    Return all nodes reachable from a given starting node.

    Parameters
    ----------
    undirected_adj_matrix : list[list[int]]
        A square adjacency matrix representing an undirected graph.

        Each matrix entry has the following meaning:

        - ``1`` indicates that an edge exists between two nodes.
        - ``0`` indicates that no direct edge exists.

        For example:

        [
            [0, 1, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
        ]

    node_label : int
        The numeric label of the starting node.

        Valid node labels range from ``0`` to ``n - 1``, where ``n`` is
        the number of nodes in the graph.

    Returns
    -------
    list[int]
        A list containing every node reachable from the starting node,
        in depth-first traversal order.

    Notes
    -----
    This implementation assumes that:

    - The graph is undirected.
    - The adjacency matrix is square.
    - Node labels are consecutive integers starting from 0.
    - The starting node is a valid matrix index.
    """

    # Initialize the stack with the starting node.
    #
    # A stack follows Last-In-First-Out behavior, so the most recently
    # added node is processed first.
    stack = [node_label]

    # Store nodes that have already been visited.
    #
    # This prevents the algorithm from processing the same node
    # repeatedly and avoids infinite loops in graphs containing cycles.
    visited = []

    # Continue until there are no remaining nodes to process.
    while stack:

        # Remove and return the most recently added node.
        #
        # Using pop() without an index removes the final list element,
        # which gives the list stack-like LIFO behavior.
        current = stack.pop()

        # Process the node only if it has not already been visited.
        if current not in visited:

            # Record the current node as visited.
            visited.append(current)

            # Inspect every possible neighbor of the current node.
            #
            # The row at undirected_adj_matrix[current] describes all
            # direct connections from the current node.
            #
            # enumerate() provides:
            #
            # - neighbor: the numeric label of a possible neighboring node
            # - connected: 1 when an edge exists, otherwise 0
            for neighbor, connected in enumerate(
                undirected_adj_matrix[current]
            ):

                # Add a neighboring node to the stack only when:
                #
                # 1. A direct edge exists.
                # 2. The neighboring node has not already been visited.
                if connected == 1 and neighbor not in visited:
                    stack.append(neighbor)

    # Return every node discovered from the starting node.
    return visited


def main():
    """Run example depth-first search demonstrations."""

    connected_graph = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0],
    ]

    disconnected_graph = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
    ]

    print(dfs(connected_graph, 1))
    print(dfs(connected_graph, 3))
    print(dfs(disconnected_graph, 3))
    print(dfs(disconnected_graph, 0))


if __name__ == '__main__':
    main()
