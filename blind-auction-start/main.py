from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
moreBids = True
auction = {}
while moreBids:
  name = input("\nWhat is your name?\n")
  auction[name] = round(float(input("\nHow much do you want to bid?\n$")),2)
  if input("\nAre there any other bidders? Yes or No\n").lower() == "no":
    moreBids = False
  else:
    clear()
highestBidderAmt = 0
highestBidderName = ""
for i in auction:
  if auction[i] > highestBidderAmt:
    highestBidderAmt = auction[i]
    highestBidderName = i
print(f"The Winner of the Auction is {highestBidderName} with a bid of ${highestBidderAmt}")
