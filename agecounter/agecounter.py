# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

from datetime import date
userName = input("Enter your name: ")
inputAge = input("Enter your current age: ")
try :
    userAge = int(inputAge)
except :
    print("Enter numbers only") 
    quit()
currentYear = date.today().year
targetAge = 100 - userAge
print("In the year", targetAge+currentYear, "you'll be 100 years old!")

