def equilateral(sides):
    if len(sides) != 3:
        return False
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if  a + b > c and b + c > a and a + c > b:
        if a == b and b == c:
            return True
        return False
    return False

def isosceles(sides):
    if len(sides) != 3:
        return False
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if  a + b > c and b + c > a and a + c > b:
        if a == b or b == c or a == c:
            return True
        return False
    return False


def scalene(sides):
    if len(sides) != 3:
        return False
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if  a + b > c and b + c > a and a + c > b:
        if a != b and b != c and a != c:
            return True
        return False
    return False