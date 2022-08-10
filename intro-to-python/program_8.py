#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: September 24, 2021
#This program will  prints out the numbers 2-20 incrementing by 2. Next to each number, print out the number + 10

twos = list(range(2, 22, 2))

for i in twos:
    print("current value: ", i, "| value+10: ", int(i) + 10)