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
game = [rock,paper,scissors]
userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print("\nYou pick\n" + game[userInput] )
computer = random.randint(0,2)
print("\nComputer chooses:\n" + game[computer])
if computer == userInput:
  print("\nIt's a draw")
elif computer == 0:
  if userInput == 1:
    print("\nYou Win since Paper beats Rock")
  else:
    print("\nComputer Wins since Rock beats Scissors")
elif computer == 1:
  if userInput == 2:
    print("\nYou Win since Scissors beats Paper")
  else:
    print("\nComputer Wins since Rock beats Scissors")
else:
  if userInput == 0:
    print("\nYou Win since Rock beats Scissors")
  else:
    print("\nComputer Wins since Scissors beats Paper")