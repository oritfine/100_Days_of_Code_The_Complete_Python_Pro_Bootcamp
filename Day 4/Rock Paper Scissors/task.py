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

options = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0,2)
print(options[player_choice])
print("Computer chose:")
print(options[computer_choice])
delta = player_choice - computer_choice
if delta == 1 or delta == -2:
    print("You Win!")
elif delta == 0:
    print("Its a Tie!")
else:
    print("You Lose")
