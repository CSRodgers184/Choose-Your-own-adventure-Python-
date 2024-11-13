from Dice import diceRoll
from MonsterPicker import monster


def main():
  print("Welcome to the Adventure series.")

# Get the user's choice
choice = input("Choose what you would like to do? \n 1) Adventure \n 2) Fight \n 3) Hear rumors in a bar\n")

# Convert the input to an integer (if user input is a number)
try:
    value = int(choice)
except ValueError:
    print("Invalid input. Please enter a number.")
    value = None

# Check the user's choice using if-elif-else
if value == 1:
    print("You selected Adventure!")
elif value == 2:
    print("You selected Fight!")
elif value == 3:
    print("You decided to hear rumors in a bar.")
else:
    print("Invalid selection. Please choose a valid option.")
    
diceRoll()
monster()
