from art import logo
print(logo)

def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}
def calculator():
  num1 = float(input("\n\nWhat's the first number?: "))
  for i in operations:
      print(i)
  keepGoing = True
  while keepGoing:  
    operation_symbol = input("\nPick an operation: ")
    num2 = float(input("\nWhat's the next number?: \n"))
    answer = operations[operation_symbol](num1,num2)
    print(f"\n{num1} {operation_symbol} {num2} = {answer}")
    num1 = answer
    if input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to calculate again: ").lower() == 'n':
      keepGoing = False
      calculator()

calculator()