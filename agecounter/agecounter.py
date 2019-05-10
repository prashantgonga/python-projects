# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

userName = input("Enter your name: ")
inputAge = input("Enter your current age: ")
if inputAge is not int :
    print("Invalid input, enter a number")
    continue : 
   
userAge = int(inputAge)
