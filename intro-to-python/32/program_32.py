#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: October 29, 2021
#This program will

import pandas as pd
import matplotlib.pyplot as plt

input_user = input("Enter name of input file: ")
output_user = input("Enter name of output file: ")

bar = pd.read_csv(input_user)
group_states = bar.groupby("state")
group_seconds = group_states["duration (seconds)"].mean() 

grouped_data = group_seconds.sort_values(ascending=False)[:10]

grouped_data.plot.bar()

plt.xlabel("State")
plt.ylabel("Seconds")

fig = plt.gcf()
fig.savefig(output_user)
