def merge_sort(array):
    """
    Sort a list in ascending order using the merge sort algorithm.

    The function modifies the original list in place.

    Merge sort works in two main phases:
    1. Divide the list into two smaller halves.
    2. Recursively sort each half and merge them back in sorted order.

    Parameters:
        array:
            The list of numbers to be sorted.

    Returns:
        None.
        The original list is updated directly.
    """

    # Base case:
    # A list with 0 or 1 element is already sorted, so no further work is needed.
    if len(array) <= 1:
        return

    # Find the middle index of the list.
    # Integer division is used because list indexes must be whole numbers.
    middle_point = len(array) // 2

    # Split the list into left and right halves.
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Recursively sort the left half.
    merge_sort(left_part)

    # Recursively sort the right half.
    merge_sort(right_part)

    # Index for reading values from the left sorted half.
    left_array_index = 0

    # Index for reading values from the right sorted half.
    right_array_index = 0

    # Index for writing sorted values back into the original array.
    sorted_index = 0

    # Compare values from both halves while both still have remaining elements.
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        # If the current value in the left half is smaller,
        # place it into the original array.
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1

        # Otherwise, place the current value from the right half
        # into the original array.
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1

        # Move to the next position in the original array.
        sorted_index += 1

    # If there are leftover values in the left half,
    # copy them into the original array.
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    # If there are leftover values in the right half,
    # copy them into the original array.
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


# This block runs only when the file is executed directly.
# It will not run if the file is imported as a module.
if __name__ == "__main__":
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]

    print("Unsorted array: ")
    print(numbers)

    merge_sort(numbers)

    print("Sorted array: ")
    print(numbers)
