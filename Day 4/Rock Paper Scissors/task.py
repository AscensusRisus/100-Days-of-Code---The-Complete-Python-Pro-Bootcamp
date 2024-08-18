import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock, Paper, Scissors Game!")
number_input = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n")
choices = [rock, paper, scissors]
computers_choice = choices[random.randint(0, 2)]
players_choice = choices[int(number_input)]
if players_choice == computers_choice:
    print(f"Your choice:\n{players_choice}\nComputers choice:\n{computers_choice}\nIt is draw!")
elif players_choice == rock:
    if computers_choice == paper:
        print(f"Your choice:\n{players_choice}\nComputers choice:\n{computers_choice}\nYou lose!")
    else:
        print(f"Your choice:\n{players_choice}\nComputers choice:\n{computers_choice}\nYou win!")
elif players_choice == paper:
    if computers_choice == rock:
        print(f"Your choice:\n{players_choice}\nComputers choice:\n{computers_choice}\nYou win!")
    else:
        print(f"Your choice:\n{players_choice}\nComputers choice:\n{computers_choice}\nYou lose!")
elif players_choice == scissors:
    if computers_choice == rock:
        print(f"Your choice:\n{players_choice}\nComputers choice:\n{computers_choice}\nYou lose!")
    else:
        print(f"Your choice:\n{players_choice}\nComputers choice:\n{computers_choice}\nYou win!")
else:
    print("You must type 0, 1 or 2")





