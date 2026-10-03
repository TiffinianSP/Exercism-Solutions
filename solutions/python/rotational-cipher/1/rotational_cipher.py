def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotated_alphabet = alphabet[key:] + alphabet[:key]
    alphabet += alphabet.upper()
    rotated_alphabet += rotated_alphabet.upper()
    translation_table = str.maketrans(alphabet, rotated_alphabet)
    return text.translate(translation_table)