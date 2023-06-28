def add_numbers(val_a, val_b):
    # Convert the input strings to integers
    num_a = int(val_a)
    num_b = int(val_b)

    # Add the numbers together
    result = num_a + num_b

    # Convert the result back to a string and return it
    return str(result)

# Test cases
print(add_numbers("5", "5"))
print(add_numbers("100", "0"))
print(add_numbers("-5", "5"))
print(add_numbers("-10", "-5"))
