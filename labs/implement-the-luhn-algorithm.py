def verify_card_number(numbers):
    """
    Verify whether a card number is valid using the Luhn algorithm.

    The function accepts a string of digits. The string may also contain spaces
    or dashes, which are removed before validation.

    The Luhn algorithm works by:
    1. Starting from the right side of the number.
    2. Leaving the rightmost digit unchanged because it is the check digit.
    3. Doubling every other digit.
    4. Subtracting 9 from doubled values greater than 9.
    5. Adding all digits together.
    6. Checking whether the total is divisible by 10.

    Parameters:
        numbers:
            A string representing the card number to validate.

    Returns:
        "VALID!" if the card number passes the Luhn check.
        "INVALID!" if the card number fails the Luhn check.
    """

    # Remove dashes from card numbers such as "4111-1111-1111-1111".
    cleaned_number = numbers.replace("-", "")

    # Remove spaces from card numbers such as "1234 5678 9012 3456".
    cleaned_number = cleaned_number.replace(" ", "")

    # Store the checksum total.
    total = 0

    # Reverse the number so the rightmost digit becomes the first digit.
    # This makes it easier to skip the check digit at index 0.
    reversed_number = cleaned_number[::-1]

    # Process each digit from right to left.
    for index, digit in enumerate(reversed_number):
        # Convert the digit from a string to an integer before doing arithmetic.
        number = int(digit)

        # After reversing, every odd index represents a digit that must be doubled.
        # Index 0 is the original rightmost check digit, so it is not doubled.
        if index % 2 == 1:
            number = number * 2

            # If doubling creates a two-digit number, subtract 9 to reduce it.
            # This is equivalent to adding the two digits together.
            if number > 9:
                number = number - 9

        # Add the processed digit to the checksum total.
        total = total + number

    # A valid Luhn number has a checksum total divisible by 10.
    if total % 10 == 0:
        return "VALID!"

    return "INVALID!"
