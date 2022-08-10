#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: October 6, 2021
#This program will ask the user which conversion they would want to do. As well as do the conversion for them.


user_input = input("Please enter the conversion you want to do:\n'a' for Light-Year to Parsec conversion \n'b' for Parsec to Light-Year conversion \nYour selection: ")

if user_input == "a":
    number_input = input("Please enter a number of Light-Years: ")
    parsecs = float(number_input)/3.26156 
    print(str(number_input) + " Light-Years is equal to " + str(parsecs) + " Parsecs.")

elif user_input == "b":
    number_input_2 = input("Please Enter a number of Parsecs: ")
    light_years = float(number_input_2) * 3.26156
    print(str(number_input_2) + " Parsecs is equal to " + str(light_years) + " Light-Years")
else:
    print("Invalid input!")

