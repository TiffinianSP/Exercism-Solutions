"""Module to check if an isbn-10 is valid."""
def is_valid(isbn):
    """Function to check if an isbn-10 is valid."""
    clean_isbn = isbn.replace("-", "")
    if len(clean_isbn) != 10:
        return False
    total = 0
    for index, char in enumerate(clean_isbn):
        if char.isdigit():
            total += int(char) * (10 - index)
        elif char == "X" and index == 9:
            total += 10 * 1
        else:
            return False
    return total % 11 == 0