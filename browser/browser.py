#open URL's on chrome in a specific order and also open installed softwares on Windows

import webbrowser
import subprocess #open windows applications (.exe)


gmail = 'https://mail.google.com/mail/u/1/#inbox'
googleCalendar = 'https://calendar.google.com'
hubspot = 'https://app.hubspot.com'
trello = 'https://trello.com'
whatsApp = 'https://web.whatsapp.com'


# Open URL in a new tab, opens default browser on the computer.
webbrowser.open_new_tab(gmail)
webbrowser.open_new_tab(googleCalendar)
webbrowser.open_new_tab(hubspot)
webbrowser.open_new_tab(trello)
webbrowser.open_new_tab(whatsApp)


#subprocess.Popen() is used to open windows apps
subprocess.Popen('calc.exe')
subprocess.Popen('notepad.exe')
subprocess.Popen('C:/Users/Prashant/AppData/Local/Programs/Microsoft VS Code/code.exe')
subprocess.Popen('C:/Users/Prashant/AppData/Local/slack/app-3.4.0/slack.exe')
subprocess.Popen('C:/Users/Prashant/AppData/Local/Amazon/Kindle/application/Kindle.exe')
