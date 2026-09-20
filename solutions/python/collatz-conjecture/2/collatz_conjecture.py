"""Module to check how many steps it requires for a number to reach 1 in the collatz conjecture"""
def steps(number):
    """Module to check how many steps it requires for a number to reach 1 in the collatz conjecture"""
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            counter += 1
        else:
            number = 3 * number + 1
            counter += 1
    return counter