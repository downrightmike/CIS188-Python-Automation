#CIS188_Mike_Lab4.py
'''This Lab is based on the Practice Project “Coin Flip Streaks” on page 107 in the textbook.   
In this lab we’ll try doing an experiment. If you flip a coin 100 times and write down an “H” for each heads and “T” for each tails, you’ll create a list that looks like “T T T T H H H H T T.” If you ask a human to make up 100 random coin flips, you’ll probably end up with alternating head-tail results like “H T H T H H T H T T,” which looks random (to humans), but isn’t mathematically random. A human will almost never write down a streak of six heads or six tails in a row, even though it is highly likely to happen in truly random coin flips. Humans are predictably bad at being random.
'''

from random import randint

numberOfStreaks = 0
list = []
for coin in range(10000):
    # create a list of 100 tails or heads
    value = randint(0, 1)
    #print(value)
    list = list + [value]
# code to check for streaks of 6
ones_list = []
zero_list = []
last = randint(0, 1) #What was the last number in the list? Starting with random 0 or 1
for thing in list:  
  #print(thing)
  # check if current and last thing are both 1
  if( thing  == 1 and last == 1):
    ones_list.append(thing)
    last = 1
    # if we have reached a streak, increment
    if(len(ones_list) == 6):
      numberOfStreaks = numberOfStreaks + 1
  elif(thing == 0 and last ==0):
    zero_list.append(thing)
    last = 0
    if(len(zero_list) == 6):
      numberOfStreaks = numberOfStreaks + 1
  # we wipe the arrays if the current and last thing are not the same, so no streak.
  else:
    ones_list.clear()
    zero_list.clear()

print("Count of streaks", numberOfStreaks)

# Display
print('Chance of streak: %s%%' % ((numberOfStreaks / 10000)  * 100))