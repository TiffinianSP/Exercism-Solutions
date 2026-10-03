def is_valid(isbn):
    isbn_list = []
    for char in isbn:
        if char != "-":
            isbn_list.append(char)
    if len(isbn_list) != 10:
        return False
    
    for item in isbn_list:
        if item == "X" and isbn_list.index(item) == 9:
            index = isbn_list.index(item)
            isbn_list[index] = 10
        elif item.isalpha() == True:
            return False
    total = 0
    counter = 0
    for number in isbn_list:
        total += int(number) * (10 - counter)
        counter += 1
    return total % 11 == 0