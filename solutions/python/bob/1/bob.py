def response(hey_bob):
    is_whitespace = ""
    if hey_bob == "":
        return "Fine. Be that way!"
    for char in hey_bob:
        if not char.isspace():
            is_whitespace = ""
            break
        is_whitespace = "is whitespace"
    if is_whitespace == "is whitespace":
        return "Fine. Be that way!"
    has_letters = "No"
    if any(character.isalpha() for character in hey_bob):
        has_letters = "Yes"
    hey_bob_clean = hey_bob.strip()
    question_mark = hey_bob_clean[-1]
    all_caps = hey_bob.upper()
    if question_mark == "?" and all_caps == hey_bob and has_letters == "Yes":
        return "Calm down, I know what I'm doing!"
    if question_mark == "?":
        return "Sure."
    if all_caps == hey_bob and has_letters == "Yes":
        return "Whoa, chill out!"
    return "Whatever."
    