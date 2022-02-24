#RoShamBo! v_0.1
    #RoShamBo! is a simple rock-paper-scissors program. The computer randomly selects rock, paper, or scissors
    #and competes against you, the player. 
import random 


print("Hello! Welcome to RoShamBo! Let's play! \n")

while True:
    PlayerChoice = input("rock, paper, or scissors? ")

    ProgramChoice = ""
    randomRoll = (random.randrange(1, 4))
    if randomRoll == 1:
        ProgramChoice = "rock"
    if randomRoll == 2:
        ProgramChoice = "paper"
    if randomRoll == 3:
        ProgramChoice = "scissors"
    
    print("I choose...",ProgramChoice,)
    if ProgramChoice == PlayerChoice:
        print("Stalemate! \n")

    elif ProgramChoice == "rock" and PlayerChoice == "scissors":
        print("I win! \n")

    elif ProgramChoice == "paper" and PlayerChoice == "rock":
        print("I win! \n")

    elif ProgramChoice == "scissors" and PlayerChoice == "paper":
        print("I win! \n")
    
    else:
        print("You win! \n")

    continue

