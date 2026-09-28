"""Module to translate a piece of text into pig latin."""
import re
def translate(text):
    """Function to translate a piece of text into pig latin."""
    def translate_word (word):
        if re.match(r"^([aeiou]|xr|yt)", word):
            return word + "ay"
        match_with_qu = re.match(r"^([^aeiou]*qu)(.*)", word)
        if match_with_qu:
            return match_with_qu.group(2) + match_with_qu.group(1) + "ay"
        match_with_y = re.match(r"^([^aeiou]+)(y.*)", word)
        if match_with_y:
            return match_with_y.group(2) + match_with_y.group(1) + "ay"
        match_with_const = re.match(r"^([^aeiou]+)(.*)", word)
        if match_with_const:
            return match_with_const.group(2) + match_with_const.group(1) + "ay"
        return word + "ay"
    return " ".join(translate_word(word) for word in text.split())
        
            