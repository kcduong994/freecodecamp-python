"""
N-Queens Solver Using Depth-First Search
=======================================

This module solves the N-Queens problem with depth-first search and
backtracking.

A solution is represented as a list of column indexes. The value at index
``row`` identifies the column containing the queen for that row.

Example
-------
The solution::

    [1, 3, 0, 2]

represents the board::

    . Q . .
    . . . Q
    Q . . .
    . . Q .
"""


def dfs_n_queens(n):
    """
    Return every valid arrangement of ``n`` queens on an ``n × n`` board.

    Parameters
    ----------
    n : int
        The board dimension and the number of queens to place.

    Returns
    -------
    list[list[int]]
        All valid queen placements in depth-first traversal order.

        Each solution has length ``n``. The value at index ``row`` is the
        zero-based column occupied by the queen in that row.

        An empty list is returned when ``n`` is less than 1 or when no valid
        arrangement exists.

    Notes
    -----
    The search places exactly one queen per row. Therefore, only column and
    diagonal conflicts need to be tracked.

    Two queens share a diagonal when either of these values is equal:

    - ``row - column`` for a main diagonal
    - ``row + column`` for an anti-diagonal
    """

    if n < 1:
        return []

    solutions = []

    # placement[row] stores the selected column for that row.
    placement = []

    # These sets form the conflict state for the current search path.
    columns = set()
    main_diagonals = set()
    anti_diagonals = set()

    def backtrack(row):
        """Extend the current placement from the given row."""

        if row == n:
            # Store a snapshot because placement is mutated during backtracking.
            solutions.append(placement.copy())
            return

        # Ascending column order preserves the deterministic solution order
        # required by the lab tests.
        for column in range(n):
            main_diagonal = row - column
            anti_diagonal = row + column

            if (
                column in columns
                or main_diagonal in main_diagonals
                or anti_diagonal in anti_diagonals
            ):
                continue

            # Choose: reserve this column and both diagonals.
            placement.append(column)
            columns.add(column)
            main_diagonals.add(main_diagonal)
            anti_diagonals.add(anti_diagonal)

            # Explore: place the next queen on the following row.
            backtrack(row + 1)

            # Undo: restore the exact state that existed before this choice.
            placement.pop()
            columns.remove(column)
            main_diagonals.remove(main_diagonal)
            anti_diagonals.remove(anti_diagonal)

    backtrack(0)
    return solutions


def main():
    """Run representative examples."""

    for board_size in (1, 2, 3, 4, 5, 8):
        solutions = dfs_n_queens(board_size)

        print(
            f"{board_size}-Queens: "
            f"{len(solutions)} solution(s)"
        )

        if board_size <= 5:
            print(solutions)


if __name__ == "__main__":
    main()
