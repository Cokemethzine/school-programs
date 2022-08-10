#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: October 29, 2021
#This program will display the superbowl

import pandas as pd
import matplotlib.pyplot as plt

input_user = input("Enter name of input file: ")
output_user = input("Enter name of output file: ")
pop = pd.read_csv(input_user)
pop["Date"] = pd.to_datetime(pop["Date"].apply(str))

pop['% Points'] = pop['Winner Pts']/ (pop['Winner Pts'] + pop['Loser Pts']) * 100

pop.plot(x = 'Date', y = '% Points')

fig = plt.gcf()
fig.savefig(output_user)