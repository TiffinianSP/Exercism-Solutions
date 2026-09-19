def is_armstrong_number(number):
    """Function that shows if a number is an Armstrong number or not"""
    digits = [int(d) for d in str(number)]
    num_of_digits = len(digits)
    total = 0
    counter = 0
    for i in digits:
        counter = i ** num_of_digits
        total += counter
    if total == number:
        return True
    return False
