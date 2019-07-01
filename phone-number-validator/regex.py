import re # need to import this module to use regex

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # (r'\d\d\d') here r is to initialize the validation and \d\d\d is the pattern of the phone number \d means digits 
print(phoneNumberRegex.findall('Call me at 983-123-5457 tomorrow or at 983-123-5489 on Monday')) # findall method will patten-match all phone numbers in a given text 
