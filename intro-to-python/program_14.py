#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: October 4, 2021
#This program will ask user for hexcode and then use the hex code to stamp 4 turtles of that color into a square

import turtle
user_color = input("Please enter a 6-digit Hexadecimal number: ")

wn = turtle.Screen()


nour = turtle.Turtle()
nour.shape("turtle")
nour.color("#" + user_color)

for i in range(4):
    nour.left(90)
    nour.forward(100)
    nour.stamp()







wn.exitonclick()
