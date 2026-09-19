def equilateral(sides):
    if len(sides) != 3:
        return False
    first_side = sides[0]
    second_side = sides[1]
    third_side = sides[2]
    
    if  first_side + second_side > third_side and second_side + third_side > first_side and first_side + third_side > second_side:
        if first_side == second_side and second_side == third_side:
            return True
        return False
    return False

def isosceles(sides):
    if len(sides) != 3:
        return False
    first_side = sides[0]
    second_side = sides[1]
    third_side = sides[2]
    
    if  first_side + second_side > third_side and second_side + third_side > first_side and first_side + third_side > second_side:
        if first_side == second_side or second_side == third_side or first_side == third_side:
            return True
        return False
    return False


def scalene(sides):
    if len(sides) != 3:
        return False
    first_side = sides[0]
    second_side = sides[1]
    third_side = sides[2]
    
    if  first_side + second_side > third_side and second_side + third_side > first_side and first_side + third_side > second_side:
        if first_side != second_side and second_side != third_side and first_side != third_side:
            return True
        return False
    return False