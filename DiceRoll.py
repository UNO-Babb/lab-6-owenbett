#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,]
  #Create two dice values ranging from 1 - 6 each
  numRolls = 1
  for count in range(numRolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2

    rolls[total-2] = rolls[total-2] + 1


    print(dice1, dice2, total)
    print(rolls)
    num = 2
    for r in rolls:
      percent = round(r / numRolls * 100, 1)
      print(num, ":", r, percent)
      num = num + 1


  #find the sum total of the two dice
  
  #print statictics for dice rolls


if __name__ == '__main__':
  main()