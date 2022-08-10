#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: November 17, 2021
#This program will check if the number the user inputs a prefect square
import math

def is_square(positive_int):
    if positive_int < 0:
        return False
    root = math.sqrt(positive_int)
    return positive_int == int(root + 0.5) ** 2

def perfectSquareChecker(num):
    if not (is_square(num)):
        print("Hey, this number isn't even! Try again next time.")
        return

    print("This number is a perfect square, it is the product of:", math.sqrt(num), "squared.")

def main():

    """
    You are provided the above two functions, your job now is to take
    user input and validate it. In other words, take integer input from
    the user, and make sure that it is a perfect square. If it's not,
    you need to keep asking the user for a perfect square until they
    enter one.
    Hint, you should use a while loop to validate input!
    Another hint, you are provided the function (is_square) which will
    check to see if a positive integer is a perfect square or not!
    """
    is_loop_running = True
    while is_loop_running:
         user_input = int(input("Enter a square integer: "))
         perfectSquareChecker(user_input)

    



if __name__ == "__main__":
    main()