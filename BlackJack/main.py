############### Blackjack Project #####################
from art import logo
import random
from replit import clear
wins = 0
losses = 0
def handTotal(hand):
  total = 0
#  for i in hand:
#    total += i
  for i in range(0,len(hand)):
    total += hand[i]
  return total
  
def deal(hand,times):
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  for i in range(0,times):
    hand.append(random.choice(cards))
    if hand[len(hand)-1] == 11 and handTotal(hand) > 21:
      hand[len(hand)-1] = 1
      
#def computerHandDeal():
#  while handTotal(computerHand) <= 16:
#    deal(computerHand,1)

def winnerDeterminer(computerHand,userHand):
  global wins
  global losses
  if handTotal(userHand) > 21:
    losses +=1
    return "You went over, you Lose!"
  elif handTotal(computerHand) > 21:
    wins +=1
    return "Opponent went over, you Win!"
  elif handTotal(computerHand) == 21:
    losses +=1
    return "Opponent got BlackJack, you Lose!"
  elif handTotal(userHand) == 21:
    wins +=1
    return "You got BlackJack, you Win!"
  elif handTotal(computerHand) == handTotal(userHand):
    return "Draw!"
  elif handTotal(computerHand) > handTotal(userHand):
    losses +=1
    return "Opponent got closer to 21, you Lose!"
  else:
    wins +=1
    return "You got closer to 21, you Win!"
  

def game():
  global wins
  global losses
  clear()
  print(logo)
  computerHand = []
  userHand = []
  print(f"You have {wins} wins and {losses} losses\n")
  shouldContinue = True
  deal(userHand,2)
  deal(computerHand,2)
  while handTotal(userHand) <= 20 and shouldContinue == True:
    print(f"\nYour cards: {userHand}, current score: {handTotal(userHand)}\nComputer's first card: {computerHand[0]}")
    if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "n" or handTotal(userHand) >= 20:
      shouldContinue = False
    else:
      deal(userHand,1)
  while handTotal(computerHand) <= 16:
    deal(computerHand,1)
  print(f"\nYour final hand: {userHand}, final score: {handTotal(userHand)}\nComputer's final hand: {computerHand}") 
  print(winnerDeterminer(computerHand,userHand))
  if input("\nDo you want to play again?: ").lower() == 'y':
    game()
  
  
  
if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    game()






