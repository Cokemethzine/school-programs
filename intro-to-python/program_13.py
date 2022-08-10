#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: September 29, 2021
#This program will ask user to input a list of books and their author and then the code will state the title followed by the initials of the author.


book = input("Enter a list of books and their authors:")

author_N_book_list = book.split(";")

for book in author_N_book_list:
    book_words = book.split("-")
    book_title = book_words[0].strip()
    
    # getting author intials 
    book_author = book_words[1]
    author_name_list = book_author.split(" ")
    first_name = author_name_list[1][:1]
    last_name = author_name_list[2][:1]
    

    # outputting final results
    output = book_title + " by " + first_name +"." + last_name + "."


    print(output)
print("Thank you for using my book organizer!")

def name():
    pass






