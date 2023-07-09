
import random

"""
Computerul face o alegere random
Omul face o alegere de la tastatura
Apoi comparam alegerea omului cu alegerea computerului

"""

def computers_choice():
    rock = open("rock.txt").read()
    scissors = open("scissors.txt").read()
    paper = open("paper.txt").read()
    L = [rock, scissors, paper]
    choice = random.choice(L)
    print("The computer chooses:\n", choice)
    return choice



def mensch_choice():
    print("Choose a sign: \n 1. rock \n 2. scissors \n 3. paper")
    print("Meine choice ist:")
    rock = open("rock.txt").read()
    scissors = open("scissors.txt").read()
    paper = open("paper.txt").read()
    n = int(input())

    if n == 1:
        print(rock)

    if n == 2:
        print(scissors)
    if n == 3:
        print(paper)
    if n!=1 and n!=2 and n!=3:
        print("invalid choice")
    return n


def score():
    rock = open("rock.txt").read()
    scissors = open("scissors.txt").read()
    paper = open("paper.txt").read()
    computers_win = 0
    men_win = 0
    while men_win < 2 and computers_win < 2:
        n = mensch_choice()
        choice = computers_choice()

        if (n == 1 and choice == scissors) or (n == 2 and choice == paper) or (n == 3 and choice == rock):
            print("YOU WIN")
            #HIER GEWINNT MENSCH
            men_win +=1


        elif (n == 1 and choice == paper) or (n == 2 and choice == rock) or (n == 3 and choice == scissors):
            print("YOU LOSE")
            #HIER GEWINNT MASCHINE
            computers_win +=1


    if men_win > computers_win :
        print("Ai castigat ba")
    else:
        print("Te-o batut calculatoru")
score()

