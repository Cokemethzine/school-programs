#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: September 28, 2021
#This program will shift the input value 13 spaces



code = input("Enter a word: ")

code_2 = ""

shift = 13 
max_unicode = ord("Z")
min_unicode = ord("A")



for i in code:
    unicode_letter = ord(i) # made a variable to turn the inputed character into unicode
    if unicode_letter + shift > 90: #checking weather if it would need to reset to A
        current_shift = max_unicode - unicode_letter #for the letters that go over Z we figure out how many shifted spaces are left
        reminder_shift = shift - current_shift #reminding shift for A, made the value into a variable
        shifted_letter = reminder_shift + min_unicode - 1 #shifting the reminder from A, we had to subtract 1 since it already counts at A
        final_letter_unicode = chr(shifted_letter) #turning the final letter into its character
        code_2 = code_2 + final_letter_unicode # to put it in a single line
    else:
        final_letter_unicode = chr(unicode_letter + shift) #when the letters did not go over Z, shifted it regular
        code_2 = code_2 + final_letter_unicode #put it in a single line
print(code_2) #printed code outside of for loop

