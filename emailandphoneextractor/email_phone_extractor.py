# A simple scrapper build using regex which would fetch email addresses and phone numbers from a pdf

import re
import pyperclip

# Create a regex for phone numner

phoneRegex = re.compile(r'''(

# Phone number formats that we will collect 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, x12345

((\d\d\d)|(\(\d\d\d\)))?        # area code (optional)
(\s|-)                           # first seperator
\d\d\d                           # first 3 digits
-                                # second seperator
\d\d\d\d                         # last 4 digits
(((ext(\.)?\s) | x)              # extension word part(optional)
(\d{2,5}))?                      # extension number part(optional)

)''', re.VERBOSE)

# Create a regex for email address

emailRegex = re.compile(r'''

# Email format some.+_thing@something.com

[a-zA-Z0-9_.+]+                  # name part
@                                # @ symbol
[a-zA-Z0-9_.+]+                  # domain name

''', re.VERBOSE)


# Get the text off the clipboard

text = pyperclip.paste()

# Extract the email and phone numbers

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email and phone numbers to the clipboard

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
