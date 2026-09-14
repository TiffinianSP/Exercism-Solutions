"""Module to find out the number of wheat on a chessboard square and the total amount of wheat on a chessboard, according to the famous wheat and chessboard puzzle"""
def square(number):
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    return (2 ** 64) - 1