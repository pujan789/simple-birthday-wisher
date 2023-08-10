import pandas
import smtplib
import datetime as dt
import random as ra

# CONSTANTS
MY_EMAIL = "enter your email"
MY_PASSWORD = 'enter your password'

# 1. Update the birthdays.csv
birthday = False
ready_to_send = False

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
data = pandas.read_csv('birthdays.csv')
matching_birthdays = data[(data.month == now.month) & (data.day == now.day)]

if not matching_birthdays.empty:
    birthday = True
    birthday_person = matching_birthdays.iloc[0]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
path = ''
if birthday:
    print('It\'s a birthday!')
    choose = ra.randint(1, 3)
    if choose == 1:
        path = 'letter_templates/letter_1.txt'
    elif choose == 2:
        path = 'letter_templates/letter_2.txt'
    elif choose == 3:
        path = 'letter_templates/letter_3.txt'

    with open(path) as file:
        content = file.read()
        ready_to_send = content.replace('[NAME]', f"{birthday_person['name']}")

# 4. Send the letter generated in step 3 to that person's email address.
if ready_to_send:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{ready_to_send}"
        )
        print("Birthday email sent!")
