import random

game = input("What game would you like to play?\n1. Rock, Paper, Scissors\n")

while game == "1":
    player1 = input("Take your pick:\n1.Rock\n2.Paper\n3.Scissors\n")
    x = "Rock Paper Scissors"
    y = x.split()
    if player1 == "1" or "2" or "3":
        npc = random.choice(y)
        print("Computer chooses " + npc)
    if player1 == "1" or "Rock" and npc == "Paper" or player1 == "2" or "Paper" and npc == "Scissors" or player1 == "3" or "Scissors" and npc == "Rock":
        print("You Lost!")
    elif player1 == "1" or "Rock" and npc == "Scissors" or player1 == "2" or "Paper" and npc == "Rock" or player1 == "3" or "Scissors" and npc == "Paper":
        print("You Won!")
    elif player1 == "1" or "Rock "and npc == "Rock" or player1 == "2" or "Paper" and npc == "Paper" or player1 == "3" or "Scissors" and npc == "Scissors":
        print("Its a draw!")

    game = input("\nPress 1 to play again: ")
