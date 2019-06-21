import random

characters = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^()}{/<>'
print('Required Password Length: ')
passwordLength = int(input())
password = ''

for i in range(passwordLength):
    password += random.choice(characters)
print(password)

