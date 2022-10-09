import random

rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
scissors = "scissors"
rock = "rock"
paper = "paper"

list_of_signs = (scissors, rock, paper)
game_on = True


def check_winner():
    computer = random.choice(list_of_signs)
    if player == "scissors" and computer == "paper":
        print(f"{scissors_art}\n VS\n{paper_art}\nPlayer won!")
    elif player == "paper" and computer == "scissors":
        print(f"{paper_art}\n VS\n{scissors_art}\nComputer won!")
    elif player == "rock" and computer == "paper":
        print(f"{rock_art}\n VS\n{paper_art}\nComputer won!")
    elif player == "paper" and computer == "rock":
        print(f"{paper_art}\n VS\n{rock_art}\nPlayer won!")
    elif player == "scissors" and computer == "rock":
        print(f"{scissors_art}\n VS\n{rock_art}\nComputer won!")
    elif player == "rock" and computer == "scissors":
        print(f"{rock_art}\n VS\n{scissors_art}\nPlayer won!")
    else:
        print("Please provide a correct sign!")

"""*********************GAME*********************"""

print("Welcome to Rock, Paper, Scissors")

while game_on:
    player = input("Choose Rock, Paper or Scissors\n").lower()
    check_winner()
    play_again = input("Do you want to play more? 'y' or 'n'\n")
