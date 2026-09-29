"""Module to check if a phrase is an isogram."""
def is_isogram(phrase):
    """Function to check if a phrase is an isogram."""
    cleaned = [char.lower() for char in phrase if char.isalpha()]
    return len(cleaned) == len(set(cleaned))