"""Module to find out the score of a dart based on the given coordinates and size of dartboard."""
import math
def score(x, y):
    """Function to find out the score of a dart based on the given coordinates and size of dartboard."""
    hypo = math.hypot(abs(x), abs(y))
    if hypo <= 1:
        return 10
    if hypo <= 5:
        return 5
    if hypo <= 10:
        return 1
    return 0