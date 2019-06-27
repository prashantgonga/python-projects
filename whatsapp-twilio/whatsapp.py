# Working with Twilio Whatsapp API
# pip install twilio

from twilio.rest import Client

account_sid = "" # Enter your twilio account sid (can be found on your twilio console)
auth_token = "" # Enter your auth_token (can be found on your twilio console), don't share this with anyone

client = Client(account_sid, auth_token)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'

to_whatsapp_number='whatsapp:000000000' # Replace the 0's with your WhatsApp number

print('Enter your message text:')
messageText = input()

client.messages.create(body=messageText,
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
