# This is a guess the number game
# A player has only 6 attempts to guess the computer generated number

import random

print('Hello, what is your name?')
playerName = input('')

print('Well, ' + playerName + ', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess')

    try :
        playerGuess = int(input())

        if playerGuess < secretNumber:
            print('Guess is too low')
        elif playerGuess > secretNumber:
            print('Guess is too high')
        else:
            break
    except:
        print('Enter only numbers')

if playerGuess == secretNumber:
   print('Good job ' + playerName + ' You guessed the correct number in', (str(guessesTaken)), 'attempts' )
else:
    print('No, the number I was thinking of was ', secretNumber)
    


