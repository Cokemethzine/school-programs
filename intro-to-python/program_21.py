#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: October 7, 2021
#This program will create an image of khaki and rosy horizontal and vertical stripes.

import matplotlib.pyplot as plt
import numpy as np

size_input = int(input("Enter the size: "))
output_file_input = input("Enter output file: ")

img = np.ones((size_input, size_input, 3))

img[1::2, :] =  [240/256, 230/256, 0.5490196347236633]
img[:, 1::2] = [0.729411780834198, 143/256, 143/256]


plt.imshow(img)             
plt.show()

plt.imsave(output_file_input, img)