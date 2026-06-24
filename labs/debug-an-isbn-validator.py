# ==========================================================
# Debug an ISBN Validator
#
# Goal:
# Fix the existing ISBN validator so it can validate ISBN-10
# and ISBN-13 codes correctly.
#
# Main concepts:
# - input parsing
# - string splitting
# - error handling with try-except
# - early return
# - off-by-one indexing
# - list comprehension
# - ISBN check digit validation
# ==========================================================


# ==========================================================
# Tests 2, 6, 8, 9, 10, 11, 12, 13, 18, 19, 20:
# validate_isbn()
#
# This function receives:
# - isbn: the ISBN code as a string
# - length: the expected ISBN length, either 10 or 13
#
# Why keep isbn as a string?
# ISBN-10 can end with "X", so the whole ISBN should not be
# converted directly to an integer.
# ==========================================================

def validate_isbn(isbn, length):

    # Tests 12-13:
    # Check whether the ISBN code has the exact required length.
    #
    # Why len(isbn)?
    # len() receives only one argument and returns the number
    # of characters in the ISBN string.
    #
    # Example:
    # len("1530051126") -> 10

    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    # Test 9:
    # Fix the off-by-one error.
    #
    # The last character is the given check digit.
    # The other characters are used to calculate the expected check digit.
    #
    # For ISBN-10:
    # isbn = "1530051126"
    # main_digits = "153005112"
    # given_check_digit = "6"

    main_digits = isbn[:length - 1]
    given_check_digit = isbn[length - 1]

    # Convert the main digits from strings to integers.
    #
    # Example:
    # "153005112" -> [1, 5, 3, 0, 0, 5, 1, 1, 2]
    #
    # This does not include the final check digit.

    main_digits_list = [int(digit) for digit in main_digits]

    # Calculate the expected check digit.
    #
    # ISBN-10 and ISBN-13 use different formulas.

    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # Compare the user's check digit with the calculated check digit.
    #
    # If they match, the ISBN is valid.
    # If they do not match, the ISBN is invalid.

    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


# ==========================================================
# Test 3:
# calculate_check_digit_10()
#
# This function calculates the expected check digit for ISBN-10.
#
# Note:
# The detailed ISBN formula is provided by the lab.
# The main debugging task is to make sure the correct digits
# are passed into this function.
# ==========================================================

def calculate_check_digit_10(main_digits_list):

    # Store the weighted sum of the first 9 digits.

    digits_sum = 0

    # Each digit is multiplied by a descending weight.
    #
    # index 0 uses weight 10
    # index 1 uses weight 9
    # index 2 uses weight 8
    # ...
    # index 8 uses weight 2

    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    # Calculate the ISBN-10 check digit.

    result = 11 - digits_sum % 11

    # ISBN-10 special cases:
    # - result 11 becomes "0"
    # - result 10 becomes "X"
    # - other results stay as normal digits

    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)

    return expected_check_digit


# ==========================================================
# Test 4:
# calculate_check_digit_13()
#
# This function calculates the expected check digit for ISBN-13.
# ISBN-13 check digits are always numeric.
# ==========================================================

def calculate_check_digit_13(main_digits_list):

    # Store the weighted sum of the first 12 digits.

    digits_sum = 0

    # ISBN-13 uses alternating weights:
    # - even index: multiply by 1
    # - odd index: multiply by 3

    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3

    # Calculate the ISBN-13 check digit.

    result = 10 - digits_sum % 10

    # ISBN-13 special case:
    # If the result is 10, the check digit is "0".

    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)

    return expected_check_digit


# ==========================================================
# Test 5:
# main()
#
# This function handles user input and controls the program flow.
# ==========================================================

def main():

    # Ask the user to enter an ISBN code and its length.
    #
    # Expected format:
    # ISBN,length
    #
    # Example:
    # 1530051126,10

    user_input = input('Enter ISBN and length: ')

    # Split the input by comma.
    #
    # Example:
    # "1530051126,10" -> ["1530051126", "10"]

    values = user_input.split(',')

    # Tests 6 and 17:
    # Handle input that is not comma-separated.
    #
    # Why len(values) != 2?
    # A valid input must have exactly two parts:
    # - ISBN code
    # - length
    #
    # Why return?
    # If the input format is wrong, the program should stop here.
    # Otherwise, values[1] may cause an IndexError.

    if len(values) != 2:
        print("Enter comma-separated values.")
        return

    # Tests 7 and 16:
    # Convert the length part to an integer.
    #
    # Why try-except?
    # int(values[1]) will raise ValueError if the user enters
    # something like "A" instead of a number.

    try:
        length = int(values[1])
    except ValueError:
        print("Length must be a number.")
        return

    # Store the ISBN code as a string.
    #
    # Do not convert the entire ISBN to int because ISBN-10
    # may end with the letter "X".

    isbn = values[0]

    # Tests 8 and 14:
    # Detect invalid characters inside the ISBN.
    #
    # For ISBN-10:
    # The last character can be "X", so only the characters before
    # the last one must be checked as digits.
    #
    # For ISBN-13:
    # All characters must be digits.
    #
    # This is why the check depends on length.

    if length == 10:
        digits_to_check = isbn[:-1]
    else:
        digits_to_check = isbn

    # Try converting each required character to an integer.
    #
    # If any character is not numeric, int(digit) raises ValueError.
    #
    # Example:
    # int("-") -> ValueError

    try:
        for digit in digits_to_check:
            int(digit)
    except ValueError:
        print("Invalid character was found.")
        return

    # Test 15:
    # The length must be either 10 or 13.
    #
    # If the length is valid, run the ISBN validator.
    # Otherwise, show the required error message.

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')


# ==========================================================
# Test 1:
# The main() call must be commented out.
#
# Why?
# freeCodeCamp tests need to import and run the functions
# without automatically starting the program.
# ==========================================================

# main()
