def number_pattern(n):
    """
    Generate a space-separated sequence of numbers from 1 to n.

    Args:
        n (int): Positive integer indicating the end of the sequence.

    Returns:
        str: Numbers from 1 to n separated by spaces.
    """

    # Validate the input type.
    if not isinstance(n, int):
        return 'Argument must be an integer value.'

    # Validate that the number is positive.
    if n < 1:
        return 'Argument must be an integer greater than 0.'

    # Store the generated pattern.
    pattern = ''

    # Generate numbers from 1 to n.
    for number in range(1, n + 1):
        pattern += str(number)

        # Avoid adding a trailing space.
        if number != n:
            pattern += ' '

    return pattern


# Example usage
print(number_pattern(4))
print(number_pattern(12))
