#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: October 15, 2021
#This program will follow the pseudocode

import turtle

wm = turtle.Screen()
turtle.colormode(255)
nour = turtle.Turtle()
nour.pensize(5)
wm.bgcolor("khaki")

for i in range(36):
    nour.pencolor(0, i * 7, 0)
    nour.forward(10)
    nour.left(10)
    for i in range(4):
        nour.left(90)
        nour.forward(300)
        nour.backward(50)



wm.exitonclick()