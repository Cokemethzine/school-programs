#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: November 12, 2021
#This program will write a program that uses folium to make a map of New York City


import folium


mapNYC = folium.Map(location=[40.75,-74.125], zoom_start=10)

folium.Marker(location = [40.7420577, -74.0101494], popup = "Little Island").add_to(mapNYC)

mapNYC.save(outfile='nycMap.html')

