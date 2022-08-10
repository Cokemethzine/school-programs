#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: October 22, 2021
#This program will display covid cases

import matplotlib.pyplot as plt
import pandas as pd

user_input = input("Enter borough name:")
user_output = input("Enter output name: ")

pop = pd.read_csv('covidCases.csv')

print("Min:",pop[user_input].min())
print("Max:",pop[user_input].max())
print("Mean:",pop[user_input].mean())
print("Median:",pop[user_input].median())
print("Standard Deviation:",pop[user_input].std())

pop = pd.read_csv('covidCases.csv')
pop['Fraction'] = pop[user_input]/pop['Case Count']
pop.plot(x = 'Date of Interest', y = 'Fraction')

fig = plt.gcf()
fig.savefig(user_output)

