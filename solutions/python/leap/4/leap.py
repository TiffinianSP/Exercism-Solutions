def leap_year(year):
    """Module to check if a year is a leap year or not."""

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False
        