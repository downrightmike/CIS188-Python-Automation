# CIS188_Mike_Lab_2_Part2.py


"""
'''
Flow Control 
This program asks the user their name, how old they are, and if they like pirates or skeletons. Then, based on the user's age and what party they picked, there are several possible messages displayed to the user.
'''

"""
import random


while (input('Do you want to try to make a bargain? y/n: ') == 'y'):
    #Display 'Please enter your name: '
    #Input username
    print('')
    print('What is your name?')
    myName = input()
    #Display 'Hello, ' + username + '! How old are you?'
    print('It\'s good to meet you ' + myName + ' ! What is your age?')
    myAge = input()
    #Input user_age as an integer
    myAge = int(myAge)
    #Display Do you like pirates or skeletons
    print('Do you like pirates or skeletons?')
    #Input dinner
    myChoice = input()
    myChoice = myChoice.lower()
    ## Check if user is 18 or over
    #If user_age >= 18:
    if myAge >= 18:
        if myChoice == 'pirates':
            print('Y\'arr in good company!')
            print('Be ye needin\' a parrot for this party? y/n:')
            partyParrot = input()
            # outcome 1
            if partyParrot == 'y':
                print('   (')
                print('  `-`-.')
                print('  \'( @ >')
                print('   _) (')
                print('  /    )')
                print(' /_,\'  / ')
                print('   \  / ')
                print('===m""m===')
            elif(partyParrot == 'n'):
                print('brought yer own yes? y/n:')
                myAnswer = input()
                # outcome 2
                if myAnswer == 'y':
                    print('YARR!')
                # outcome 3
                else:
                    print('That\'s not the best way to make frineds')
            else: print('At least yerr honest')
        # outcome 4
        elif myChoice == 'skeletons':
            print('')
            print('     .-.')
            print('    (o.o) / sup?/')
            print('     |=| / ')
            print('    __|__')
            print('  //.=|=.\\\ ')
            print(' // .=|=. \\\ ')
            print(' \\\ .=|=. //')
            print('  \\\(_=_)//')
            print('   (:| |:)')
            print('    || ||')
            print('    () ()')
            print('    || ||')
            print('    || ||')
            print('   ==\' \'==')
            #for loop with random iteration, ends with ...skeletons are hungry...
            list = [1,2,3,4]
            for x in range(random.random() * 10):
                print('Feast on the flesh of the living? y/n:')
                feastOnTheFleshOfTheLiving = input()
                if feastOnTheFleshOfTheLiving == 'y':
                    print('              .7')
                    print('            .\'/')
                    print('           / /')
                    print('          / /')
                    print('         / /')
                    print('        / /')
                    print('       / /')
                    print('      / /')
                    print('     / /         ')
                    print('    / /          ')
                    print('  __|/')
                    print('|f-"Y\|')
                    print('\()7L/')
                    print(' cgD                            __ _')
                    print(' |\(                          .\'  Y \'>,')
                    print('  \\ \\                        / _   _   \\')
                    print('   \\\\\\                       )(_) (_)(|}')
                    print('    \\\\\\                      {  4A   } /')
                    print('    \\\\\\                      \\uLuJJ/\\l')
                    print('      \\\\\\                     |3    p)/')
                    print('       \\\\\\___ __________      /nnm_n//')
                    print('       c7___-__,__-)\\,__)(".  \\_>-<_/D')
                    print('                  //V     \\_"-._.__G G_c__.-__<"/ ( \\')
                    print('                         <"-._>__-,G_.___)\\   \\7\\')
                    print('                        ("-.__.| \\"<.__.-" )   \\ \\')
                    print('                        |"-.__"\\  |"-.__.-".\\   \\ \\')
                    print('                        ("-.__"". \\"-.__.-".|    \\_\\')
                    print('                        \"-.__""|!|"-.__.-".)     \\ \\')
                    print('                         "-.__""\\_|"-.__.-"./      \\ l')
                    print('                          ".__""">G>-.__.-">       .--,_')
                    print('                              ""  G')
                else:
                    print('Perhaps another time then...')
            print()
            print()
            print('...The skeletons are hungry....')
            print('.............')
            print()

        # outcome 5
        else:
            print('The pirates and skeletons have teamed up and they are coming for you ' + myName + '...')
    else: print('Yerr not ta want ta be here for long '+ myName + ', best to run home quick as ya can! The ' + myChoice + ' will be after ya! Off you go! Yah!')