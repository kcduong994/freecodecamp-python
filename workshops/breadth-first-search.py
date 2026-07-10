"""
Breadth-First Search Parentheses Generator
==========================================

This module generates every valid combination of balanced parentheses
for a given number of pairs.

The solution uses a breadth-first search (BFS) approach. Each state in
the queue stores:

1. The current parentheses string.
2. The number of opening parentheses used.
3. The number of closing parentheses used.

A new state is added only when it can still lead to a valid balanced
parentheses sequence.
"""


def gen_parentheses(pairs):
    """
    Generate all valid combinations of balanced parentheses.

    Parameters
    ----------
    pairs : int
        The number of matching parentheses pairs to generate.

    Returns
    -------
    list[str] | str
        A list containing every valid balanced-parentheses combination.

        If ``pairs`` is not an integer, the function returns:

        ``'The number of pairs should be an integer'``

        If ``pairs`` is less than 1, the function returns:

        ``'The number of pairs should be at least 1'``

    Notes
    -----
    The function uses breadth-first search.

    Each queue item is a tuple with the structure:

    ``(current, opens_used, closes_used)``

    where:

    - ``current`` is the parentheses string built so far.
    - ``opens_used`` is the number of opening parentheses used.
    - ``closes_used`` is the number of closing parentheses used.
    """

    # Validate that the number of pairs is an integer.
    #
    # This prevents unsupported values such as strings, lists,
    # or floating-point numbers from entering the BFS process.
    if not isinstance(pairs, int):
        return 'The number of pairs should be an integer'

    # At least one pair is required to generate a valid sequence.
    if pairs < 1:
        return 'The number of pairs should be at least 1'

    # Initialize the BFS queue with one empty state.
    #
    # The tuple contains:
    #
    # 1. The current string
    # 2. The number of opening parentheses used
    # 3. The number of closing parentheses used
    #
    # At the beginning, no parentheses have been added.
    queue = [('', 0, 0)]

    # Store every complete and valid parentheses combination.
    result = []

    # Continue processing states until the queue becomes empty.
    #
    # A non-empty list evaluates to True, while an empty list
    # evaluates to False.
    while queue:

        # Remove the oldest state from the front of the queue.
        #
        # Using pop(0) gives the queue first-in-first-out behavior,
        # which is the defining traversal order of breadth-first search.
        current, opens_used, closes_used = queue.pop(0)

        # A complete sequence must contain exactly twice as many
        # characters as the number of pairs.
        #
        # For example:
        #
        # pairs = 3
        # required length = 6
        if len(current) == 2 * pairs:

            # Every state reaching this length is valid because
            # invalid states are never added to the queue.
            result.append(current)

        else:
            # Add an opening parenthesis when the maximum allowed
            # number of opening parentheses has not been reached.
            if opens_used < pairs:

                # Create a new BFS state after adding '('.
                #
                # The opening-parenthesis count increases by one,
                # while the closing-parenthesis count stays unchanged.
                queue.append(
                    (
                        current + '(',
                        opens_used + 1,
                        closes_used,
                    )
                )

            # Add a closing parenthesis only when there are more
            # opening parentheses than closing parentheses.
            #
            # This condition prevents invalid prefixes such as:
            #
            # ")"
            # "())"
            #
            # A closing parenthesis must always match an opening
            # parenthesis that has already been added.
            if closes_used < opens_used:

                # Create a new BFS state after adding ')'.
                #
                # The opening-parenthesis count stays unchanged,
                # while the closing-parenthesis count increases by one.
                queue.append(
                    (
                        current + ')',
                        opens_used,
                        closes_used + 1,
                    )
                )

    # Return every valid balanced-parentheses sequence discovered
    # during the breadth-first traversal.
    return result


def main():
    """Run example demonstrations of the BFS generator."""

    print(gen_parentheses(2))
    print(gen_parentheses(3))


if __name__ == '__main__':
    main()
