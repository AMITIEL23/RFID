# Read - Validate - Execute
#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import bcrypt
import random
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

reader = SimpleMFRC522()

def randomhex():
    rn = random.randint(80000000, 950000000)
    hexadecimal = hex(rn)
    return hexadecimal
    
def send_email():
    sender_email = "email@gmail.com"
    password = "password"
    to_email = "amilreciver@gmail.com"

    message = MIMEMultipart("alternative")
    message["Subject"] = 'Your secret number'
    message["From"] = sender_email

    part1 = MIMEText(hexadecimal, "plain")
    message.attach(part1)

    message["To"] = sender_email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, to_email, message.as_string())

def program():
    return print("Hi")

def validate():
    with open('/home/ubuntu/RFID/authorized-rfid-cards.txt', 'r') as file: 
        authorized_cards_text = file.read()
    authorized_cards = authorized_cards_text.split(',')
    for cardID in authorized_cards[0:(len(authorized_cards)-1)]:
        if bcrypt.checkpw(string_id.encode('UTF-8'), cardID.encode('UTF-8')):
            print('Success')
            return True
            break
        else:
            print('Failed')    

while True:
    try:
        print("Place Target: ")
        id, name = reader.read()
        print(name.upper())
        string_id = str(id)
        validate()
        if validate() == True:
            hexadecimal = randomhex()
            send_email()
            hex_password = input('SECRET CODE: ')
            if hex_password == hexadecimal:
                program()

    finally:
        GPIO.cleanup()

    repeat = input('Execute Again y/n: ')
    if repeat.upper() != 'Y':
        print("Aborting")
        break    
