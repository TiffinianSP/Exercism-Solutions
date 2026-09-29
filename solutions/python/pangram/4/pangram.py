"""A module to find out if a sentence is a pangram."""
from string import ascii_lowercase
def is_pangram(sentence):
    """A function to find out if a sentence is a pangram."""
    alphabet = set(ascii_lowercase)
    return alphabet.issubset(sentence.lower())