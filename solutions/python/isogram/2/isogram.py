def is_isogram(phrase):
    cleaned = [char.lower() for char in phrase if char.isalpha()]
    return len(cleaned) == len(set(cleaned))