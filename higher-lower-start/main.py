from game_data import data
import art
import random
from replit import clear

game = True
score = 0
while game:
  if score == 0:
    print(art.logo)
    compareA = random.randint(0,len(data)-1)
    compareADict = data[compareA]
    data.pop(compareA)
  followerCountA = int(compareADict["follower_count"])
  print("\nCompare A: " + (compareADict["name"]) + ", a " + (compareADict["description"]) + ", from " + (compareADict["country"]) + ".")
  print(art.vs)
  compareB = random.randint(0,len(data)-1)
  followerCountB = int(data[compareB]["follower_count"])
  print("\nAgainst B: " + (data[compareB]["name"]) + ", a " + (data[compareB]["description"]) + ", from " + (data[compareB]["country"]) + ".\n")
  answer = input("\nWho has more followers? Type 'A' or 'B': ").lower()
  clear()
  print(art.logo)
  if answer == 'a' and followerCountA > followerCountB:
    score +=1
    print("You're right! Current score: " + str(score))
    print((data[compareB]["name"]) + " has " + str(followerCountB) + " followers")
    print((compareADict["name"]) + " has " + str(followerCountA) + " followers")
  elif answer == 'b' and followerCountA < followerCountB:
    score +=1
    print("You're right! Current score: " + str(score))
    print((data[compareB]["name"]) + " has " + str(followerCountB) + " followers")
    print((compareADict["name"]) + " has " + str(followerCountA) + " followers")
    compareADict = data[compareB]
  else: 
    print("Sorry, that's wrong. Final score: " + str(score))
    game = False
    print((data[compareB]["name"]) + " has " + str(followerCountB) + " followers")
    print((compareADict["name"]) + " has " + str(followerCountA) + " followers")
  data.pop(compareB)
