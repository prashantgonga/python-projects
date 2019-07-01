# simple program not using regex to validate if the number is a phone number of not
# we are checking if the total length of the number is 12 including two - (dash)
# eg: 983-123-5467

def isPhoneNumber(text): # this is the format we need 983-123-5467
    if len(text) != 12:
        return False # phone number is not 12 chars long including '-'
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-': # check for '-'
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-': # check for '-'
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# print(isPhoneNumber('983-123-5457'))

message = 'Call me at 983-123-5457 tomorrow or at 983-123-5489 on Monday'
foundNumber = False

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone number')
