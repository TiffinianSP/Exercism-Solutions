"""Module to translate a number from one base to another."""
def rebase(input_base, digits, output_base):
    """Function to translate a number from one base to another."""
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    total = 0
    for digit in digits:
        if not 0 <= digit < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        total = total * input_base + digit
    if total == 0: 
        return [0]
    output_base_digits = []
    while total > 0:
        output_base_digits.append(total % output_base)
        total = total // output_base
    return output_base_digits[::-1]