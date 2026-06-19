def pin_extractor(poems):
    # Store the extracted PIN code from each poem.
    secret_codes = []

    # Process each poem in the input list.
    for poem in poems:
        secret_code = ''

        # Split the poem into separate lines.
        lines = poem.split('\n')

        # Each line hides one digit of the PIN.
        # The line index determines which word should be used.
        for line_index, line in enumerate(lines):
            words = line.split()

            # If the target word exists, use its length as the next digit.
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))

            # If the target word does not exist, use 0.
            else:
                secret_code += '0'

        # Add the completed PIN for this poem to the result list.
        secret_codes.append(secret_code)

    return secret_codes


poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))
