#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: September 27, 2021
#This program will reverse the phrase and reverse the last letters of what the user inputs

phrase = input("Enter a phrase: ")
phrase_2 = phrase.split()
reversed_phrase = ""
last_letter_phrase = ""


for i in phrase:
    reversed_phrase = i + reversed_phrase
print("Reversed phrase: " + reversed_phrase)


for l in phrase_2:
    last_letter_phrase = l[0] + last_letter_phrase
print("Last letter of reversed words: " + last_letter_phrase.upper())

