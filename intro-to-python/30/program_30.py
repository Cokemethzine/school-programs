#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: October 27, 2021
#This program will ask the input of of a file , then print the average rating and print the lowest rating

from numpy import sin
import pandas as pd

#Read in the csv file.
rating = pd.read_csv('ramenRatings.csv')
rating["Stars"] = pd.to_numeric(rating["Stars"], downcast="float")

groupedData = rating.groupby('Style')

print("The average stars per serving style:",groupedData['Stars'].mean())

singapore = rating.groupby('Country').get_group('Singapore')
id = singapore['Stars'].idxmin()
print(f'{singapore["Brand"][id]} has the lowest rating in {rating["Country"][id]} with {rating["Stars"][id]} stars')