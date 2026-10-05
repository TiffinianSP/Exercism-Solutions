"""Module to find out the score of a dart based on the given coordinates and size of dartboard."""
import math
def score(x_coord, y_coord):
    """Function to find out the score of a dart based on the given coordinates and size of dartboard."""
    hypo = math.hypot(abs(x_coord), abs(y_coord))
    if hypo <= 1: return 10
    if hypo <= 5: return 5
    if hypo <= 10: return 1
    return 0