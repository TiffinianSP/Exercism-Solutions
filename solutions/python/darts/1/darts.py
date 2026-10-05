import math
def score(x, y):
    x, y = abs(x), abs(y)
    hypo = math.hypot(x, y)
    if hypo <= 1:
        return 10
    if hypo <= 5:
        return 5
    if hypo <= 10:
        return 1
    return 0