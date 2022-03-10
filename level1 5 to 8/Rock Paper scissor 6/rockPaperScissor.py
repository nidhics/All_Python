from random import randint # return random integer, here we are importing method,
#  no need write random.randint you can directly write randint
import time

#create a list of play options
t = ["rock", "paper", "scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
#player = False

#while player == False:
#set player to True
player = input("Rock, Paper, Scissors?").lower()
if player == computer:
        print("Tie!")
elif player == "rock":
        if computer == "paper":
            print("computer choses ", computer)
            time.sleep(2)
            print("You lose!", computer, "covers", player)
        else:
            print("computer choses ", computer)
            time.sleep(2)
            print("You win!", player, "smashes", computer)
elif player == "paper":
        if computer == "scissors":
            print("computer choses ", computer)
            time.sleep(2)
            print("You lose!", computer, "cut", player)
        else:
            print("computer choses ", computer)
            time.sleep(2)
            print("You win!", player, "covers", computer)
elif player == "scissors":
        if computer == "rock":
            print("computer choses ", computer)
            time.sleep(2)
            print("You lose...", computer, "smashes", player)
        else:
            print("computer choses ", computer)
            time.sleep(2)
            print("You win!", player, "cut", computer)
else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    # player = False
    # computer = t[randint(0,2)]