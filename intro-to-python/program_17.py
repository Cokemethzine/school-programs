#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: October 7, 2021
#This program will


import turtle

num_stamps = int(input("Enter number of stamps the turtle will print: "))
l = turtle.Turtle()
l.shape("circle")
turtle.colormode(255)
l.penup()
steps, red, green, blue = 10, 186, 164, 145
l.color(red, green, blue)

for i in range(num_stamps):
    l.stamp()
    steps += 2

    if red + 3 <= 255 and green + 3 <= 255 and blue + 3 <= 255:
        red, green, blue = red + 3, green + 3, blue + 3
        
    l.color(red, green, blue) 
    l.forward(steps)
    l.right(24)