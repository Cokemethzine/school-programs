#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: November 19, 2021
#This program will create rock papers scissors game

import random 

player_move_over =  3
human_tracker = 0
computer_tracker = 0

while player_move_over > 0:
    if human_tracker >= 2 :
        print("Game finished and winner is: Human" )
        player_move_over = 0
        break
    elif computer_tracker >= 2 :
        print("Game finished and winner is: Computer")
        player_move_over = 0
        break
    
    player_move = int(input("Enter 1 for rock, 2 for paper, or 3 for scissors: "))
    computer_move = random.randint(1, 3)
    winner = ""
    if player_move == 1 and computer_move == 1:
        winner = "draw"
        print("computerMove " + str(computer_move))
        print("Round finished and winner is: " + winner)
    
    elif player_move == 1 and computer_move == 2:
        winner = "computer"
        print("computerMove " + str(computer_move))
        print("Round finished and winner is: " + winner)
        player_move_over = player_move_over - 1
        computer_tracker +=  1
    
    elif player_move == 1 and computer_move == 3:
        winner = "human"
        print("computerMove " + str(computer_move))
        print("Round finished and winner is: " + winner)
        player_move_over -= 1
        human_tracker += 1

    elif player_move == 2 and computer_move == 1:
        winner = "human"
        print("computerMove " + str(computer_move))
        print("Round finished and winner is: " + winner)
        player_move_over = player_move_over - 1
        human_tracker += 1

    elif player_move == 2 and computer_move == 2:
        winner = "draw"
        print("computerMove " + str(computer_move))
        print("Round finished and winner is: " + winner)
        

    elif player_move == 2 and computer_move == 3:
        winner = "computer"
        print("computerMove " + str(computer_move))
        print("Round finished and winner is: " + winner)
        player_move_over = player_move_over - 1
        computer_tracker +=  1


    elif player_move == 3 and computer_move == 1:
        winner = "computer"
        print("computerMove " + str(computer_move))
        print("Round finished and winner is: " + winner)
        player_move_over = player_move_over - 1
        computer_tracker +=  1

    elif player_move == 3 and computer_move == 2:
        winner = "human"
        print("computerMove " + str(computer_move))
        print("Round finished and winner is: " + winner)
        player_move_over = player_move_over - 1
        human_tracker += 1

    elif player_move == 3 and computer_move == 3:
        winner = "draw"
        print("computerMove " + str(computer_move))
        print("Round finished and winner is: " + winner)
    
    else:
        winner = "invalid"
        print("computerMove " + str(computer_move))
        print("Round finished and winner is: " + winner)

    