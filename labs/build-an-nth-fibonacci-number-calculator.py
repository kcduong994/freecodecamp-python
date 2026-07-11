"""
Nth Fibonacci Number Calculator
===============================

This module computes Fibonacci numbers using bottom-up dynamic programming.

The sequence starts with:

    F(0) = 0
    F(1) = 1

Each later value is defined as:

    F(n) = F(n - 1) + F(n - 2)
"""


def fibonacci(n):
    """
    Return the n-th Fibonacci number.

    Parameters
    ----------
    n : int
        A non-negative index in the Fibonacci sequence.

    Returns
    -------
    int
        The Fibonacci number at index ``n``.

    Notes
    -----
    The implementation uses bottom-up dynamic programming. Previously
    computed values are stored in ``sequence`` and reused instead of
    recalculating overlapping subproblems.

    Time complexity is O(n), and auxiliary space complexity is O(n).
    """

    # The first two values are the dynamic-programming base cases.
    sequence = [0, 1]

    if n < 2:
        return sequence[n]

    # Build the sequence incrementally until F(n) has been computed.
    for _ in range(2, n + 1):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[n]


def main():
    """Run representative Fibonacci calculations."""

    test_indexes = (0, 1, 2, 3, 5, 10, 15)

    for index in test_indexes:
        print(f"F({index}) = {fibonacci(index)}")


if __name__ == "__main__":
    main()
