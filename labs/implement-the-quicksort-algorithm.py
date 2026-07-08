def quick_sort(numbers):
    """
    Sort a list of integers from least to greatest using the quicksort algorithm.

    This function returns a new sorted list and does not modify the original
    input list.

    Quicksort works by:
    1. Choosing a pivot value.
    2. Splitting the input list into three groups:
       - values less than the pivot
       - values equal to the pivot
       - values greater than the pivot
    3. Recursively sorting the smaller and greater groups.
    4. Combining the sorted groups into one final sorted list.

    Parameters:
        numbers:
            A list of integers to be sorted.

    Returns:
        A new list containing the same integers in ascending order.
    """

    # Base case:
    # A list with 0 or 1 element is already sorted.
    #
    # numbers[:] creates a shallow copy so the function returns a new list
    # instead of directly returning the original input list.
    if len(numbers) <= 1:
        return numbers[:]

    # Choose the first element as the pivot.
    # The pivot is used as the reference value for partitioning the list.
    pivot = numbers[0]

    # Values smaller than the pivot will be stored here.
    less_than_pivot = []

    # Values equal to the pivot will be stored here.
    # This is important for preserving duplicate values correctly.
    equal_to_pivot = []

    # Values greater than the pivot will be stored here.
    greater_than_pivot = []

    # Partition the list into three groups based on comparison with the pivot.
    for number in numbers:
        if number < pivot:
            less_than_pivot.append(number)
        elif number == pivot:
            equal_to_pivot.append(number)
        else:
            greater_than_pivot.append(number)

    # Recursively sort the lower and higher partitions.
    # The equal partition is already sorted because all values in it are the same.
    #
    # The final result is a new list:
    # sorted smaller values + pivot-equal values + sorted greater values.
    return (
        quick_sort(less_than_pivot)
        + equal_to_pivot
        + quick_sort(greater_than_pivot)
    )
