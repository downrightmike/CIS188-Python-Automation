#CIS188_Mike_Lab7.py
'''This Lab is based on the Practice Project “Strong Password Detection” on page 186 in the textbook. 

In this assignment, you will write a function that uses regular expressions to make sure the password string it is passed is strong.
'''
import re

passwordLength = 10
user = 'bob'
#TestPlan
'''
bob123@abC fail 
abc123@boB fail 
okaysue@abC fail 
okay123andabC fail 
okay123@abc fail 
okay1@abC fail 
123456@!$123  fail 
okay123@abC pass '''

passwordList = [
    'bob123@abC',
    'abc123@boB',
    'okaysue@abC',
    'okay123andabC',
    'okay123@abc',
    'okay1@abC',
    '123456@!$123 ',
    'okay123@abC'
]


tenChar =    re.compile(r'.{' + str(passwordLength) + ',}')
oneNumber =  re.compile(r'\d+')
oneSpecial = re.compile(r'[@]|[$]|[_]')
oneLower =   re.compile(r'[a-z]+')
oneUpper =   re.compile(r'[A-Z]+')
noUsername = re.compile(r'^((?!' + user + ').)*$')

for password in passwordList:
    #Check password against all of our regex and create match objects
  to = tenChar.search(password)
  no = oneNumber.search(password)
  so = oneSpecial.search(password)
  lo = oneLower.search(password)
  uo = oneUpper.search(password)
  ao = noUsername.search(password.lower())
  # Object will be NoneType if no match, so we make sure that None is not there
  if(to is not None and no is not None and so is not None and lo is not None and uo is not None and ao is not None):
    print(password + ' pass ')
  else:
    print(password + ' fail ')
    