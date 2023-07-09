from computer import computers_choice
from man import user_choice

def menu():
    print("Choose a sign: \n 1. rock \n 2. scissors \n 3. paper")
menu()

def score():
    rock = open("rock.txt").read()
    scissors = open("scissors.txt").read()
    paper = open("paper.txt").read()
    computers_win = 0
    men_win = 0
    for i in range(3):
        n = user_choice()
        choice = computers_choice()

        """
        If the user is the winner
        """
        if (n == 1 and choice == scissors) or (n == 2 and choice == paper) or (n == 3 and choice == rock):
            print("YOU WIN THIS ROUND")
            men_win +=1


        """
        If the computer is the winner
        """
        if (n == 1 and choice == paper) or (n == 2 and choice == rock) or (n == 3 and choice == scissors):
            print("YOU LOSE THIS ROUND")
            #HIER GEWINNT MASCHINE
            computers_win +=1


    if men_win > computers_win :
        print("Congrats, you've won!")
    else:
        print("Sorry, you lost!")
score()

