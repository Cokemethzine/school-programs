#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: October 27, 2021
#This program will ask the user to input file and output file and then make a plot and store it

import pandas as pd
import matplotlib.pyplot as plt

input_user = input("Enter name of input file: ")
output_user = input("Enter name of output file: ")

pop = pd.read_csv(input_user)
pop['Fraction Single Adults'] = pop['Total Single Adults in Shelter']/pop['Total Individuals in Shelter']
pop.plot(x = "Date of Census", y = "Fraction Single Adults")

fig = plt.gcf()
fig.savefig(output_user)

