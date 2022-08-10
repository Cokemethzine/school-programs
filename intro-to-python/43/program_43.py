#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: November 15, 2021
#This program will write a program that ask the user the names of a CSV file and then creat a map with markers for all the NY attractions

import folium
import pandas as pd

user_input = input("Enter CSV file name: ")
user_output = input("Enter output file: ")

ny = pd.read_csv(user_input)
ny_attractions = folium.Map(location=[40.768731, -73.964915], )

for index,row in ny.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["NAME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(ny_attractions)

ny_attractions.save(outfile = user_output)