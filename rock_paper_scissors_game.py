#Name: Samuel Awud
#Date: Feb 10, 2023
#Rock Paper Scissor Game

import random

print("Welcome to the gameRock, Paper, Scissors ")
print("Rules of the game")
print("If player chooses Rock and the other chooses Scissor, Rock wins.")
print("If player chooses Scissors and the other chooses Paper, Scissors wins.")
print("If player chooses Paper and the other chooses Rock, Paper wins.")
print("If both players make the same choice, it's a tie.")
print("Enter -1 to quit the game")
#function  that analyzes the user input/choice
def userChoice ():
    print("R-P-S game....")
    print("Choose 1 for rock")
    print("Choose 2 for paper")
    print("Choose 3 for scissors")
    userInput = int(input("Choose your choice : "))
    if userInput==1:
        print("you choose rock")
        return "rock"
    elif userInput==2:
        print("you choose paper")
        return "paper"
    elif userInput==3:
        print("you choose scissors")
        return "scissors"
    else:
        print("invalid input, choose a number from 1 to 3.")
        return -1
#function  that determines the computer choice
def comp_choice():
    comp_choice=random.choice([1, 2, 3])# random choice of the computer
    if comp_choice==1:
        print("Computer chooses rock")
        return "rock"
    elif comp_choice==2:
        print("Computer chooses paper")
        return "paper"
    else:
        print("Computer chooses scissors")
        return "scissors"  
 # Function that check for the winner of the game

def game():
    userInput=userChoice()
    compChoice=comp_choice()
    if userInput==-1:
        return
    
    if compChoice=="rock":
        if userInput=="rock":
            print("The game is tie!")
        elif userInput=="paper":
            print("You are the winner!")
        else:
            print("The winner is computer!")
    elif compChoice=="paper":
        if userInput=="rock":
            print("The winner is computer!")
        elif userInput=="paper":
            print("The game is tie!")
        else:
            print("You are the winner!")
    elif compChoice=="scissors":
        if userInput=="scissors":
            print("You Won!")
        elif userInput=="paper":
            print("Computer Won!")
        else:
            print("The game is tie!")
    else:
        return -1
        
# main
def main():
    #userChoice()
    game()

main()
'''
For this assignment, I took a deep dive into the requirements for the 
Rock, Paper, Scissors game. I broke the process down into smaller steps 
and wrote functions for each one, then called them all in the main function 
to make the game work. 
To make sure everything was working as it should, 
I tested the program a few times by giving it different inputs. I also 
tried to input some invalid data to make sure the error message was 
displayed properly.
Overall, I learned a lot about how to create a simple game using functions
and random numbers in Python. In the future, I'd love to take on a new 
challenge and try building the same game with different logic or 
incorporating some advanced features.'''
