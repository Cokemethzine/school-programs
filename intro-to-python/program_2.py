#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: September 14, 2021
#This program draws a nonagon

import turtle

wn = turtle.Screen()

nonagon = turtle.Turtle()

for i in range(9):
    nonagon.forward(100)
    nonagon.left(40)

wn.exitonclick()