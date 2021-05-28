import random
import os

#print (10)
#print (10, 20, "test")

PLAYER_NAME = os.getenv("PLAYER_NAME")
print (PLAYER_NAME)

print ("------------START----------------")
print("WELCOME",PLAYER_NAME,"TO ROCK, PAPER, SCISSORS GAME!")

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
    print ("-------------END-----------------")
    exit()

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE:", computer_choice)

#adopted from JanZielonka in Slack. Thanks so much to Jan for saving me so much time.

if user_choice == "rock":
    if computer_choice == "rock":
        print("IT'S A TIE")
    elif computer_choice == "paper":
        print("PAPER BEATS ROCK, THE COMPUTER WON...")
    elif computer_choice == "scissors":
        print("ROCK BEATS SCISSORS! CONGRATS!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("PAPER BEATS ROCK. YOU WON! CONGRATS!")
    elif computer_choice == "paper":
        print("IT'S A TIE")
    elif computer_choice == "scissors":
        print("SCISSORS CUT PAPER. THE COMPUTER WON...")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("ROCK BEATS SCISSORS, THE COMPUTER WON...")
    elif computer_choice == "paper":
        print("SCISSORS CUT PAPER. YOU WON! CONGRATS!")
    elif computer_choice == "scissors":
        print("IT'S A TIE")

print("THIS IS THE END OF OUR GAME. PLEASE TRY AGAIN")
print ("-------------END-----------------")

