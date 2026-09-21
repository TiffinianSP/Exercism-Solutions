"""Module to find out what a number would be in the Raindrop sequence."""
def convert(number):
    """Function to find out what a number would be in the Raindrop sequence."""
    result = ""
    if number % 3 == 0:
        result = result + "Pling"
    if number % 5 == 0:
        result = result + "Plang"
    if number % 7 == 0:
        result = result + "Plong"
    if not (number % 3 == 0 or number % 5 == 0 or number % 7 == 0):
        result = str(number)
    return result
    