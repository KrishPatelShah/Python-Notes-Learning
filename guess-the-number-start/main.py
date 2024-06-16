from art import logo
import random
from replit import clear

def game():
  clear()
  print(logo)
  secretNumber = random.randint(1,100)
  print("Welcome to the Number Guessing Game\nI'm thinking of Number between 1 and 100\n")
  if input("Type 'easy' for EASY MODE and 'hard' for HARD MODE: ").lower() == "easy":
    numberOfGuesses = 10
  else:
    numberOfGuesses = 5
  print("You have " + str(numberOfGuesses) +" attempts to guess the NUMBER I'm THINKING OF\n")
  gameOver = False
  while not gameOver:
    guess = int(input("Make a Guess: "))
    if guess == secretNumber:
      print("\nYou got it! The answer was " + str(secretNumber))
      gameOver = True
    elif guess > secretNumber:
      numberOfGuesses -=1
      print("Too High")
    else:
      numberOfGuesses -=1
      print("Too Low")
  
    if numberOfGuesses == 0 :
      gameOver = True
      print(f"\nYou've Run ot of Guesses, YOU LOSE. The answer was " + str(secretNumber))
    elif gameOver == False:
      print(f"Guess again.\nYou have {numberOfGuesses} remaining to guess the number.\n")
  if input("\nDo you want to play again? yes or no: ").lower() == "yes":
    game()
  else:
    clear()
    print("Good Bye!")
  
game()