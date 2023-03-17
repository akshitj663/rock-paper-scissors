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

#Write your code below this line 👇
game_images = [rock, paper, scissors]
users_choice = int(input("What do u choose? Type 0  for Rock ,1 for paper  and 2 for scissors "))
print(game_images[users_choice])
computer_choice = random.randint(0,2)
print("computer chooses:")
print(game_images[computer_choice])
if users_choice == 0 and computer_choice == 0:
  print("Its Draw")
if users_choice == 1 and computer_choice == 1:
  print("Its Draw")
if users_choice == 2 and computer_choice == 2:
  print("Its Draw")
if users_choice == 0 and computer_choice == 1:
  print("Computer Wins!")
if users_choice == 0 and computer_choice == 2:
  print("You Wins!")
if users_choice == 1 and computer_choice == 0:
  print("You Wins!")
if users_choice == 1 and computer_choice == 2:
  print("Computer Wins!")
if users_choice == 2 and computer_choice == 0:
  print("Computer Wins!") 
if users_choice == 2 and computer_choice == 1:
  print("You Wins!")