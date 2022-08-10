#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: September 29, 2021
#This program will

import turtle
wm = turtle.Screen()

turtle.colormode(255)
nour = turtle.Turtle()
nour.shape("turtle")


nour.backward(100)


for i in range(255, 0,-10):
     nour.forward(10)
     nour.pensize(255-i)
     nour.color(255,i,0)

nour.pensize(0)
nour.penup()
nour.color(0, 0, 0)

for i in range(255, 0, -10):
    nour.backward(10)

nour.right(90)
nour.pendown()

for i in range(255, 0,-10):
     nour.forward(10)
     nour.pensize(255-i)
     nour.color(255,i,0)


wm.exitonclick()