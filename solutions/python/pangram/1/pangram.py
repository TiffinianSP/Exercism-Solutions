"""A module to find out if a sentence is a pangram."""
def is_pangram(sentence):
    """A function to find out if a sentence is a pangram."""
    return all(char in sentence.lower() for char in "qwertyuiopasdfghjklzxcvbnm")
        

