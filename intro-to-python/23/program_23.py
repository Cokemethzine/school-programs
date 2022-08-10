#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: October 18, 2021
#This program will count of the white pixels and subtract the difference.

#This program loads an image, counts the number of pixels that are
#nearly white as an estimate for snow pack.

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

file_1 = input("Enter first file name: ")
file_2 = input("Enter second image file: ")
threshold = input("Enter threshold of white pixels: ")

ca = plt.imread(file_1)
cb = plt.imread(file_2)  #Read in image
countSnow = 0
countSnow_2 = 0            #Number of pixels that are almost white
t = float(threshold)                #Threshold for almost white-- can adjust between 0.0 and 1.0

#For every pixel:
for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          #Check if red, green, and blue are > t:
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
               countSnow = countSnow + 1

for i in range(cb.shape[0]):
     for j in range(cb.shape[1]):
          #Check if red, green, and blue are > t:
          if (cb[i,j,0] > t) and (cb[i,j,1] > t) and (cb[i,j,2] > t):
               countSnow_2 = countSnow_2 + 1

print("Snow count of first image: ", countSnow)
print("Snow count of second image: ", countSnow_2)
print("Difference between first and second image:", countSnow - countSnow_2)