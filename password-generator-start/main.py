#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print(str(len(letters)))
print(str(len(symbols)))
print(str(len(numbers)))
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


randomLetters = []
randomSymbols = []
randomNumbers = []

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for i in range(0,nr_letters):
  randomLetters += letters[random.randint(0,51)]

for i in range(0,nr_symbols):
  randomSymbols += symbols[random.randint(0,8)]

for i in range(0,nr_numbers):
  randomNumbers += numbers[random.randint(0,9)]



everything = randomLetters + randomSymbols + randomNumbers

randomEverything = []
randomNumber = 0
for i in range(0,len(everything)):
  randomNumber = random.randint(0,len(everything)-1)
  randomEverything += everything[randomNumber]
  everything.pop(randomNumber)
  
  
stringVers = ""
for i in randomEverything:
  stringVers += i
print(str(stringVers))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P