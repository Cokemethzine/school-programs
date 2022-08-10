#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: September 29, 2021
#This program will draw a shade of yellow hearts

import turtle
wn = turtle.Screen()


turtle.colormode(255)	
tess = turtle.Turtle()		
tess.shape("turtle")
wn = turtle.Screen()

tess.penup()
tess.left(60)
tess.pendown()

for i in range(0, 255, 10):
     tess.forward(10)
     tess.pensize(i)
     tess.color(i, i , 0) #(225, 225, 0) = yellow

tess.pensize(0)
tess.penup()
tess.color(0, 0, 0)


for i in range(255, 0, -10):
     tess.backward(10)


tess.left(60)
tess.pendown()

for i in range(0, 255, 10):
     tess.forward(10)
     tess.pensize(i)
     tess.color(i, i, 0)


wn.exitonclick()