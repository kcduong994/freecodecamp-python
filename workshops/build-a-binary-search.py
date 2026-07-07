def binary_search(search_list, value):
    # Store the values checked during the search process.
    # This helps show the path taken by the binary search algorithm.
    path_to_target = []

    # The search starts from the first index of the list.
    low = 0

    # The search ends at the last index of the list.
    high = len(search_list) - 1

    # Continue searching while the current search range is valid.
    while low <= high:
        # Find the middle index of the current search range.
        mid = (low + high) // 2

        # Get the value stored at the middle index.
        value_at_middle = search_list[mid]

        # Record the middle value that was checked.
        path_to_target.append(value_at_middle)

        # If the middle value is the target value,
        # return the search path and the index where the value was found.
        if value == value_at_middle:
            return path_to_target, f'Value found at index {mid}'

        # If the target value is greater than the middle value,
        # ignore the left half and continue searching on the right side.
        elif value > value_at_middle:
            low = mid + 1

        # If the target value is less than the middle value,
        # ignore the right half and continue searching on the left side.
        else:
            high = mid - 1

    # If the loop ends without finding the value,
    # return an empty path and a not-found message.
    return [], 'Value not found'


# Search for 3 in a sorted list.
# The value exists in the list.
print(binary_search([1, 2, 3, 4, 5], 3))

# Search for 4 in another sorted list.
# The value exists in the list.
print(binary_search([1, 2, 3, 4, 5, 9], 4))

# Search for 10 in a sorted list.
# The value does not exist in the list.
print(binary_search([1, 3, 5, 9, 14, 22], 10))
