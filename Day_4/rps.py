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
import random

user = int(
    input("Type 0 to pick Rock, 1 to pick Paper, and 2 to pick scissors : \n"))
move = [rock, paper, scissors]
outcome = random.randint(0, 2)
print(f"You chose {move[user]}")
print(f"Computer chose {move[outcome]}")
if move[outcome] == move[user]:
    print("This is a draw")
elif move[outcome] == 0 and move[user] == 2:
    print("You lose :(")
elif move[outcome] == 1 and move[user] == 0:
    print("You lose :(")
elif move[outcome] == 2 and move[user] == 1:
    print("You lose :(")
else:
    print("You win :)")
