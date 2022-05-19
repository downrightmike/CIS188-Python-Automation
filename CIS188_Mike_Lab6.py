#CIS188_Mike_Lab6.py
'''In this assignment, you will write a series of functions and a program that calls them and displays the results. Each function should accept a given string as a parameter, and return the modified or determined values. These are the tasks required, one for each function:
• Determine and return the number of characters in the given string, not including spaces.

• Determine and return what character is in the 6th position of the given string

• Return the given string in all uppercase.

• Determine and return the last word in the given string, repeated a random number of times.

• Create and return a dictionary that contains key pair values where each word in the given string is the key and the count of how often that word appears is the value.
'''
from random import randint
import re

def charCount(string):
    count = 0
    for char in string:
        if char != ' ':
            count = count + 1
    print('Number of characters is: ', count)

def getSixth(string):
    if(len(string) >= 6):
       print('The sixth character is: ', string[6])
    else:
        print('not long enough for a sixth character')

def toUpper(string):
    print("Here is your string in upper case: ", string.upper())

def lastWord(string):
    # find last word 
    word = string.split()
    print('Last word is: ', word[-1])

    #return it random of times
    value = randint(0, 7)
    repeat = ''
    for i in range(value):
        repeat += word[-1] 
        repeat += ' ' 
    print(repeat)

def twentySlice(string):
    #print('Length of string is: ', len(string))
    if len(string) < 20:
        print('Not long enough for a twenty character slice :( ')
    else:
        max = len(string) - 20
        value = randint(0, max)
        if(value + 20 < len(string)):
            print(string[value:(value + 20)])
        

  

def wordCount(string):
    string = re.sub(r'[^\w\s]', '',string) # remove punctuation marks to make the dictionary clean
    print(string)
    word_counts = {}
    for word in string.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    print('Word      Count')
    for word, count in word_counts.items():
        print(f'{word:<12}{count}')



print(r'Welcome to the String Processing Program!')
string = input('Please enter your favorite quote from a book: ')
print('Here is your string: ', string)

charCount(string)
getSixth(string)
toUpper(string)
lastWord(string)
wordCount(string)
twentySlice(string)