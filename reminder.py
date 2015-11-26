#!/bin/python
import smtplib
from email.mime.text import MIMEText
import datetime

##
## Major U.S. Carriers
##
# AT&T
# 10digitphonenumber@txt.att.net
# Boost Mobile
# 10digitphonenumber@myboostmobile.com
# Metro PCS
# 10digitphonenumber@mymetropcs.com
# Nextel
# 10digitphonenumber@messaging.nextel.com
# Sprint
# 10digitphonenumber@messaging.sprintpcs.com
# T-Mobile
# 10digitphonenumber@tmomail.net
# Tracfone
# 10digitphonenumber@txt.att.net
# Sprint
# 10digitphonenumber@messaging.sprintpcs.com
# Verizon
# 10digitphonenumber@vtext.com
# Virgin Mobile
# 10digitphonenumber@vmobl.com

# Configuration
# Note: If you have two-step authentication on your Gmail account,
# you'll need to set up an application password and use that password here.
username = 'username@gmail.com'
password = 'application_password_here'
relatives = {
             "Tom" : "5552225555@txt.att.net", # index 0
             "Joe" : "5552225555@txt.att.net", # index 1
             "Bob" : "5552225555@vtext.com",  # index 2
             "Carol" : "5552225555@vtext.com", # index 3
             "Missy" : "5552225555@messaging.sprintpcs.com" # index 4
             }
schedule = {
        1 : relatives[0], 2 : relatives[1], 3 : relatives[2], 4 : relatives[3], 5 : relatives[4], 6 : relatives[5],
        7 : relatives[0], 8 : relatives[1], 9 : relatives[2], 10 : relatives[3], 11 : relatives[4], 12 : relatives[5],
        13 : relatives[0], 14 : relatives[1], 15 : relatives[2], 16 : relatives[3], 17 : relatives[4], 18 : relatives[5],
        19 : relatives[0], 20 : relatives[1], 21 : relatives[2], 22 : relatives[3], 23 : relatives[4], 24 : relatives[5],
        25 : relatives[0], 26 : relatives[1], 27 : relatives[2], 28 : relatives[3], 29 : relatives[4], 30 : relatives[5],
        31 : relatives[0]
        }
subject = "Reminder to Call Grandma Today!"
sender = "username@gmail.com"
msg_body = "Today is your turn to call Grandma.  Don't forget!  Love, John"
# End Configuration

# Select a relative based on today's date
today = datetime.datetime.now() # today's date, i.e. 25
recipient = schedule[today]

# Generate Message
msg = MIMEText(msg_body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient

# Send Email
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
