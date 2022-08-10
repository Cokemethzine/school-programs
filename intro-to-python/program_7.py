#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: September 24, 2021
#This program will prints each character in the message, and the character corresponding to the unicode + 5.

message = input("Enter a message: ")

for i in message:
    print(i, " shifted by 5 characters is: ", chr(ord(i) + 5))