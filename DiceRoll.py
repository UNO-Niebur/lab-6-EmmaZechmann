#DiceRoll.py
#Name: Emma Zechmann
#Date: 3/1/2026
#Assignment:Dice roll 
import random

def main():
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  num_rolls = 1000

  for i in range(num_rolls):
    die1= random.randint(1,6)
    die2= random.randint(1,6)

    total = die1 + die2
    rolls[total-2] +=1

  print("Sum Count")
  for i in range(len(rolls)):
    print(i+2,"", rolls[i])

if __name__ == '__main__':
  main()
