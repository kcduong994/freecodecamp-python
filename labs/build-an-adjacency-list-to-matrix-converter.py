"""
Adjacency List to Matrix Converter
==================================

This module converts an adjacency-list representation of an unweighted
graph into an adjacency matrix.

An adjacency list stores each node as a dictionary key and stores the
connected nodes in a list.

Example:

{
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2],
}

An adjacency matrix is a square two-dimensional list where:

- matrix[i][j] == 1 means an edge exists from node i to node j.
- matrix[i][j] == 0 means no edge exists from node i to node j.

The function supports both directed and undirected graphs, depending on
how the connections are written in the input adjacency list.
"""


def adjacency_list_to_matrix(adj_list):
    """
    Convert an adjacency list into an adjacency matrix.

    Parameters
    ----------
    adj_list : dict[int, list[int]]
        A dictionary representing an unweighted graph.

        Each dictionary key represents a node, and the corresponding
        list contains the nodes directly connected to that node.

        Example:

        {
            0: [1, 2],
            1: [2],
            2: [0, 3],
            3: [2],
        }

    Returns
    -------
    list[list[int]]
        A square adjacency matrix.

        The value at matrix[i][j] is:

        - 1 if an edge exists from node i to node j
        - 0 if no edge exists from node i to node j

    Notes
    -----
    This implementation assumes that:

    - Node labels are consecutive integers.
    - Node numbering starts at 0.
    - Every node appears as a key in the adjacency-list dictionary.
    """

    # The number of dictionary keys determines the number of nodes
    # in the graph.
    #
    # Example:
    # {0: [...], 1: [...], 2: [...]} contains three nodes.
    number_of_nodes = len(adj_list)

    # Create a square matrix filled with zeros.
    #
    # The outer list comprehension creates one row for each node.
    # The inner list comprehension creates one column for each node.
    #
    # For three nodes, the initial matrix is:
    #
    # [
    #     [0, 0, 0],
    #     [0, 0, 0],
    #     [0, 0, 0],
    # ]
    matrix = [
        [0 for _ in range(number_of_nodes)]
        for _ in range(number_of_nodes)
    ]

    # Traverse every node and its neighboring nodes.
    #
    # Example:
    # node = 0
    # neighbors = [1, 2]
    #
    # This means that the graph contains the directed edges:
    #
    # 0 -> 1
    # 0 -> 2
    for node, neighbors in adj_list.items():

        # Process every neighbor connected to the current node.
        for neighbor in neighbors:

            # Mark the corresponding matrix position as 1.
            #
            # matrix[node][neighbor] represents the edge:
            #
            # node -> neighbor
            matrix[node][neighbor] = 1

    # Print each matrix row on a separate line, as required by the lab.
    #
    # Printing the entire matrix directly would display all rows on
    # one line, while the exercise explicitly requires one row per line.
    for row in matrix:
        print(row)

    # Return the completed adjacency matrix so it can be reused,
    # tested, or stored by the calling code.
    return matrix
