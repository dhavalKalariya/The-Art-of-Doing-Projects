# Rock, paper and Scissors game
import random
print("Welcome to a game of Rock, Paper, Scissors")

rounds = int(input("How many rounds would you like to play: "))

player_score = 0
computer_score = 0
picks = ["rock","paper","scissors"]

for round in range(1,rounds+1):

    print("\nRound "+str(round))
    print("Player: "+str(player_score)+"\tComputer: "+str(computer_score))
    #gather player input
    player_pick = input("Time to pick...rock, paper, scissors: ").lower()
    if player_pick not in picks:
        print("This is not a valid game options!")
        computer_score += 1
        print("Computer gets the point!")
        
    else: 
        
      #pick the random input for the computer
        computer_pick = random.randint(0,2)
        if computer_pick == 0:
            computer_pick = "rock"
        elif computer_pick == 1:
            computer_pick = "paper"
        else:
            computer_pick = "scissors"
    #compare players input and computer input

        if player_pick == computer_pick:
            print("\tComputer: "+str(computer_pick))
            print("\tPlayer: "+str(player_pick))
            print("\tIt is a tie, how boring!")
            print("\tThis round was a tie.")

        elif player_pick == "rock" and computer_pick == "paper":
            print("\tComputer: "+str(computer_pick))
            print("\tPlayer: "+str(player_pick))
            print("\tPaper covers rock!")
            print("\tComputer wins round "+str(round)+".")
            computer_score += 1

        elif player_pick == "paper" and computer_pick == "rock":
            print("\tComputer: "+str(computer_pick))
            print("\tPlayer: "+str(player_pick))
            print("\tPaper covers rock!")
            print("\tYou wins round "+str(round)+".")
            player_score += 1

        elif player_pick == "scissors" and computer_pick == "paper":
            print("\tComputer: "+str(computer_pick))
            print("\tPlayer: "+str(player_pick))
            print("\tScissors cut paper!")
            print("\tYou wins round "+str(round)+".")
            player_score += 1

        elif player_pick == "paper" and computer_pick == "scissors":
            print("\tComputer: "+str(computer_pick))
            print("\tPlayer: "+str(player_pick))
            print("\tScissors cut paper!")
            print("\tComputer wins round "+str(round)+".")
            computer_score += 1
    
        elif player_pick == "scissors" and computer_pick == "rock":
            print("\tComputer: "+str(computer_pick))
            print("\tPlayer: "+str(player_pick))
            print("\trock break scissors!")
            print("\tComputer wins round "+str(round)+".")
            computer_score += 1

        elif player_pick == "rock" and computer_pick == "scissors":
            print("\tComputer: "+str(computer_pick))
            print("\tPlayer: "+str(player_pick))
            print("\trock break scissors!")
            print("\tYou wins round "+str(round)+".")
            player_score += 1

        

print("Final Game Results")
print("\tRounds Played: "+str(rounds))
print("\tPlayer Score: "+str(player_score))
print("\tComputer Score: "+str(computer_score))
if computer_score > player_score:
    print("Winner: Computer :-( ")
elif computer_score < player_score:
    print("Winner: You :D ")
else:
    print("The game is tied")