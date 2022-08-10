#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: November 5, 2021
#This program will ask the user for a CSV of video Games dataset

import pandas as pd
user_input = input("Enter file name: ")

games = pd.read_csv(user_input)

print("There are 16598 total games")

print("The number of games in each genre is")
print(games["Genre"].value_counts())

print("The top 3 publishers are:")
print(games["Publisher"].value_counts()[:3])