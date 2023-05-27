Skip to content
Commands
Search

Try Ghostwriter


Help





main.py
Selection deleted
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
game_images = [rock,paper,scissors]
computer_choice = random.randint(0, 2)
user_choice= int(input("Your choise \npress 01 for rock \nPress 02 for paper \nPress 03 scissors\n"))

print("\nYou choose\n")
print(game_images[user_choice])


print("Computer chose:")
print(game_images[computer_choice])


if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")



Ln 56, Col 1 (1073 chars)

History


Enable "Accessible Terminal" in Workspace Settings to use a screen reader with the console.
Booting ReplReady
Replit