##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random as ra
import os
from twilio.rest import Client

# 1. Update the birthdays.csv
birthday = False
ready_to_send_ = False

#CONSTANTS
my_email = "gamingfury317@gmail.com"
password = 'sagarjadu770'
account_sid = 'ACa1e28a301d9c47c99dfbcf1889aa8913'
auth_token = '86480bd03f5720a1c453a676af844cd5'


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
data = pandas.read_csv('birthdays.csv')
month = now.month
day = now.day
coloum = data[data.month == now.month]

if not coloum.empty:
    day_of_birthday_month = coloum.month.item()
    birthday_day = coloum.day.item()

    birthday = True
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
choose = ra.randint(1,3)
if choose == 1 and birthday:
    path = 'letter_templates/letter_1.txt'

elif choose == 2 and birthday:
    path = 'letter_templates/letter_2.txt'
elif choose == 3 and birthday:
    path = 'letter_templates/letter_3.txt'
if birthday:
    print('its birthday')
    with open(path) as file:
        content = file.read()
        ready_to_send = content.replace('[NAME]',f"{coloum.name.item()}")
        print(ready_to_send)
        ready_to_send_ = True

# 4. Send the letter generated in step 3 to that person's email address.
if birthday and ready_to_send_:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"{ready_to_send}",
        from_='+17622269097',
        to='+919428393969'
    )
