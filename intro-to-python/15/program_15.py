#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: October 5, 2021
#This program will turn the image into yellow

# Import NumPy and Matplotlib
import numpy as np
import matplotlib.pyplot as plt

user_input = input("Enter name of the input file: ")
save_input = input("Enter name of output file: ")
img = plt.imread(user_input)

img[:,:,2] = 0 #getting rid of blue in all rows and colums


plt.imshow(img)             
plt.show()
plt.imsave(save_input, img)  