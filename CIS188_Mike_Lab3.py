# CIS188_Mike_Lab3.py
'''This Lab is based on the Practice Project “The Collatz Sequence” on page 76 in the textbook. 
In this lab you will write a function named collatz() that has one parameter named number. If the number is even, then collatz() should print number / 2 and return this value. If the number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1.
'''
def collatz(number):
    if(number % 2 == 0):
        print(number /2)
        return number /2
    elif(number == 1):
        return 1
    else:
        print( 3 * number + 1)
        return 3 * number +1

print("Welcome to the Collatz Sequence calculator.")
print()
print("Please enter a positive number: ")
for guessesTaken in range(1, 7):
    guess = int(input())
    if(collatz(guess) > 1):
        print('Guess again.')
    else:
        break # This condition is the correct guess!
if collatz(guess) == 1:
    print('Good job! You guessed the number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was 1.')

