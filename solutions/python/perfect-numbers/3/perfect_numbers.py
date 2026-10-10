"""Module to determine if a number is perfect, abundant or deficient"""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if is_perfect(number):
        return is_perfect(number)
    if is_deficient(number):
        return is_deficient(number)
    return is_abundant(number)
def is_perfect(number):
    total = 0
    for num in range(1, number):
        if number % num == 0:
            total += num
    if total == number:
        return "perfect"
    return ""
def is_abundant(number):
    total = 0
    for num in range(1, number):
        if number % num == 0:
            total += num
    if total > number:
        return "abundant"
    return ""
def is_deficient(number):
    total = 0
    for num in range(1, number):
        if number % num == 0:
            total += num
    if total < number:
        return "deficient"
    return ""