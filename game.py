
print("rock, paper, scissors, shoot!")

import random
#print (10)
#print (10, 20, "test")

user_choice = input ("PLEASE CHOOSE ONE OF THE FOLLOWING: 'rock', 'paper', 'scissors'")

print ("YOU SELECTED", user_choice)

#validate that user choice is valid, if not valid present end of program message
#Operators:
#and
#or

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, INVALID INPUT. PLEASE TRY AGAIN")
    exit()

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE:", computer_choice)

print("THIS IS THE END OF OUR GAME. PLEASE TRY AGAIN")

