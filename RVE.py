# Read - Encrypt - Save
import RPi.GPIO as GPIO
import MFRC522
import signal
import bcrypt
import random
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


continue_reading = True

password_encrypted = '$2b$14$LcUGT.RzazdCY5KtNn15ROJZIlYTGN1eNM3miiUhnGYe5AJUziGWi'

MIFAREReader = MFRC522.MFRC522()

def read():
    try:
        rfid_id = MIFAREReader.MFRC522_SelectTag(uid)
        return rfid_id
    finally:
        GPIO.cleanup()    

rdif_id = read()

def validate():
    with open('C:/Users/SLASH/Desktop/Python/RFID/authorized-rfid-cards.txt', 'r') as file: 
        authorized_cards_text = file.read()
    authorized_cards = authorized_cards_text.split(',')
    for cardID in authorized_cards[0:(len(authorized_cards)-1)]:
        if bcrypt.checkpw(rdif_id.encode('UTF-8'), cardID.encode('UTF-8')):
            print('Success')
            return True
            break
        else:
            print('Failed')
def execute():
    def randomhex():
        rn = random.randint(80000000, 950000000)
        hexadecimal = hex(rn)
        return hexadecimal
    
    hexadecimal = randomhex()

    def send_email():
        sender_email = "boxgroundstation@gmail.com"
        password = "rfidgroundstationbox"
        to_email = "angelfuentesbr3556@gmail.com"

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
        print('Hi')

    while True:
        send_email()
        key = input('Introduce the secret key:')
        if key == hexadecimal:
            print("Auth Correct")
            program()
            break

        else:
            print("Access denied")   
            inputagain = input("Input key again y/n:")
            if inputagain.upper() != 'Y':
                break            

while True:
    while continue_reading:
        if status == MIFAREReader.MI_OK:
            print("Card Detected")
    
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

        if status == MIFAREReader.MI_OK:
            read()
            break

    if validate() == True:
        execute()

    repeat = input('Execute again y/n:')
    if repeat.upper() != 'Y':
        print("Aborting")
        break