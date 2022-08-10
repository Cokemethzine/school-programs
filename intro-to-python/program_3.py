#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: September 17, 2021
#This program will have one variable change the background color, one variable draw a square and another variable draw a equilateral triangle.

import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("khaki")


tess = turtle.Turtle()
tess.color("darkblue")
tess.pensize(5)

alex = turtle.Turtle()
alex.color("violet")
alex.pensize(5)

for i in range(4):
    tess.forward(100)
    tess.left(90)

alex.left(90)
alex.forward(100)

alex.right(30)
alex.forward(100)
alex.right(120)
alex.forward(100)
alex.right(120)
alex.forward(100)

wn.exitonclick()
