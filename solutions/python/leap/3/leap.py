def leap_year(year):
    """Module to check if a year is a leap year or not."""

    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False
        