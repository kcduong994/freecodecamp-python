def selection_sort(array):
    """
    Sort a list of numbers from smallest to largest using the selection sort algorithm.

    This function sorts the input list in place, meaning it modifies the original
    list directly instead of creating and returning a new sorted list.

    Selection sort works by:
    1. Moving through the list one position at a time.
    2. Finding the smallest value in the remaining unsorted part of the list.
    3. Swapping that smallest value with the first unsorted position.
    4. Skipping the swap when the smallest value is already in the correct position.

    Parameters:
        array:
            A list of numbers to be sorted.

    Returns:
        The same list object, sorted in ascending order.
    """

    # Move through each position in the list.
    # current_index marks the first position of the unsorted part.
    for current_index in range(len(array)):
        # Assume the current position contains the smallest value.
        minimum_index = current_index

        # Search the remaining unsorted part of the list.
        # The search starts at current_index + 1 because the current position
        # is already being used as the initial minimum.
        for search_index in range(current_index + 1, len(array)):
            # If a smaller value is found, remember its index.
            if array[search_index] < array[minimum_index]:
                minimum_index = search_index

        # Swap only when the minimum value is not already in the current position.
        # This avoids unnecessary swaps, as required by the lab.
        if minimum_index != current_index:
            array[current_index], array[minimum_index] = (
                array[minimum_index],
                array[current_index],
            )

    # Return the same list object after sorting it in place.
    return array
