# In main file
# import script1
# print(script1.sum(1, 3))

from Dice import diceRoll
def monster():
  roll = diceRoll()
  if roll == 1:
    print("Your fighting an Ogre")
  elif roll == 2:
    print("Your fighting an Putty Patrol")
  elif roll == 3:
    print("Your fighting an Kracken")
  elif roll == 4:
    print("Your fighting an Zombie")  
  elif roll == 5:
    print("Your fighting an Black Knight")
  elif roll == 6:
    print("Your fighting an King")
  return roll
