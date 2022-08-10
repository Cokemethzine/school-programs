#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: September 20, 2021
#This program will draw a Rhombus-Flower


#use the stamp feature not making other turtles for when you get back from the gym
import turtle

wn = turtle.Screen()
wn.bgcolor("khaki")

alex = turtle.Turtle()
alex.shape("turtle")
alex.pencolor("black")
alex.pensize(3)
alex.fillcolor("green")


for i in range(6):
    alex.forward(100)
    alex.left(45)
    alex.forward(100)
    alex.left(135)
    alex.stamp()
    alex.forward(100)
    alex.left(45)
    alex.forward(100)
    alex.left(75)


wn.exitonclick()