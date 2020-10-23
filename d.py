# Read - Validate - Execute
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import bcrypt
import random
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

rfid = SimpleNFRC522()  

def read():
    try:
        print("Scan RFID :")
        id, text = rfid.read()
        return id
    finally:
        GPIO.cleanup()     

def validate():
    with open('C:/Users/SLASH/Desktop/Python/RFID/authorized-rfid-cards.txt', 'r') as file: 
        authorized_cards_text = file.read()
    authorized_cards = []
    authorized_cards = authorized_cards_text.split(',')
    print(authorized_cards)
    for cardID in authorized_cards:
        if bcrypt.checkpw(id.encode('UTF-8'), cardID.encode('UTF-8')):
            return True
            break

def execute():
    def randomhex():
        rn = random.randint(80000000, 950000000)
        hexadecimal = hex(rn)
        return hexadecimal
    
    hexadecimal = randomhex()

    def send_email():
        sender_email = "angelfuentesbr3556@gmail.com"
        password = "SUM41BLINK182"

        message = MIMEMultipart("alternative")
        message["Subject"] = 'Your secret number'
        message["From"] = sender_email

        part1 = MIMEText(hexadecimal, "plain")
        message.attach(part1)

        message["To"] = sender_email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, sender_email, message.as_string())

    while True:
        attempt = 0
        key = input('Introduce the secret key:')
        if key == hexadecimal:
            print("Auth Correct")
            program()
            break

        else:
            if attempt >= 2:
                print("Failed to auth the key")
                break
            print("Access denied")   
            inputagain = input("Input key again y/n:")
            if inputagain.upper() != 'Y':
                break
            else:
                attempt += 1
                return attempt

    def program():
        hi = "hi"   
        print(hi)             

while True:
    read()
    if validate() == True:
        execute()

    repeat = input('Execute again y/n:')
    if repeat.upper() != 'Y':
        print("Aborting")
        break