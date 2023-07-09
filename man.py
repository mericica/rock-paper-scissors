"""
The user can choose between rock, paper or scissors
"""

def user_choice():
    print("I choose:")
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