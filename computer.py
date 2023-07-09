import random


"""
Computer chooses a sign at random
"""

def computers_choice():
    rock = open("rock.txt").read()
    scissors = open("scissors.txt").read()
    paper = open("paper.txt").read()
    L = [rock, scissors, paper]
    choice = random.choice(L)
    print("The computer chooses:\n", choice)
    return choice