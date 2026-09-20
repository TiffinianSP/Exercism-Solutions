"""Module that checks what Bob will respond to an input."""
def response(hey_bob):
    """Function that checks what Bob will respond to an input."""
    hey_bob_clean = hey_bob.strip()
    if not hey_bob_clean:
        return "Fine. Be that way!"
    
    has_letters = "No"
    if any(character.isalpha() for character in hey_bob):
        has_letters = "Yes"
    question_mark = hey_bob_clean[-1]
    all_caps = hey_bob.upper()
    if question_mark == "?" and all_caps == hey_bob and has_letters == "Yes":
        return "Calm down, I know what I'm doing!"
    if question_mark == "?":
        return "Sure."
    if all_caps == hey_bob and has_letters == "Yes":
        return "Whoa, chill out!"
    return "Whatever."
    