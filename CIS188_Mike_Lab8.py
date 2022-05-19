#CIS188_Mike_Lab8.py
'''This is based on the Practice Project “Sandwich Maker” on pages 198-199 in the textbook. 

In this assignment, you will write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input'''

import pyinputplus as pyip
#def calcCosts 
def calcCosts(bread, meat, cheeseYn, mayo, mustard, lettuce, tomato):
    # Costs
  breadCost = 1.1
  meatCost = 0.65
  cheeseCost = 0.22
  mayoCost = 0.1
  mustardCost = 0.8 # Best mustard you've ever had ;)
  lettuceCost = 0.1
  tomatoCost = 0.2

  # decide the values needed, zero out costs not being charged
  if(not cheeseYn):
    cheeseCost =0
  if(not mayo):
    mayo = 0
  if(not mustard):
    mustard = 0
  if (not lettuce):
    lettuce = 0
  if(not tomato):
    tomato = 0
  return breadCost + meatCost + cheeseCost + mayoCost + mustardCost + lettuceCost + tomatoCost

def printSammich(bread, meat, cheeseYn, cheese, mayo, mustard, lettuce, tomato, many, singleCost):
  total = many * singleCost    
  # decide the values needed
  print(f'Number of samwiches: {many}')
  if(cheeseYn):
    print(f'Cheese: {cheese}')
  if( mayo):
    print('Mayo: Yes')
  if( mustard):
    print('Mustard: Yes')
  if ( lettuce):
    print('Lettuce: Yes')
  if( tomato):
    print('Tomatoes: Yes')
  print(f'On {bread} bread')
  print(f'\nOrder total: ${total:.2f}')
    

# main loop
bread = pyip.inputMenu(['white', 'wheat','sourdough'])
meat = pyip.inputMenu(['chicken','turkey','ham','tofu'])
cheeseYn = pyip.inputYesNo('Would you like cheese? ')
if cheeseYn :
  cheese = pyip.inputMenu(['cheddar', 'Swiss',  'mozzarella'])
mayo = pyip.inputYesNo('Would you like mayo? ')
mustard = pyip.inputYesNo('Would you like mustard? ')
lettuce = pyip.inputYesNo('Would you like lettuce? ')
tomato = pyip.inputYesNo('Would you like tomato? ')
many = pyip.inputInt('How many sammiches? ', min=1)

#Calculat bill
singleCost = calcCosts(bread, meat, cheeseYn, mayo, mustard, lettuce, tomato)

# Print out things nicely
printSammich(bread, meat, cheeseYn, cheese, mayo, mustard, lettuce, tomato, many, singleCost)

