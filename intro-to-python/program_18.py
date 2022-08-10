#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: October 7, 2021
#This program will

import matplotlib.pyplot as plt
import numpy as np


""" img = np.zeros((30, 30, 3))

img[:6, :, (0, 2)] = 1
img[:, :6, (0,2)] = 1
img[15:21, :,(0,2)] = 1
img[:21, 25:, (0,2)] = 1 """
num = 20
img = np.ones((num,num,3))  
img[::2,::2,0:2] = 0

plt.imshow(img)             
plt.show()
plt.imsave("logo.png", img)
