#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: November 17, 2021
#This program will ask the program that asks the user for the name of a CSV file and create markers for all the NYC WIFI Hotspot locotions.

import folium
import pandas as pd

user_input = input("Please enter the of the input file: ")
user_output = input("Please enter the name of the output file: ")
borough = input("Please enter the name of the borough: ")

ny = pd.read_csv(user_input)
mapNYC = folium.Map(location=[40.75,-74.125])
wifi = ny.groupby("City").get_group(borough)

for index,row in wifi.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = ["Location"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapNYC)

mapNYC.save(outfile = user_output)
