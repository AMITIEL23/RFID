# Read - Validate - Execute
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import bcrypt

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
    print("Program Executed Succefully")        


while True:
    read()
    if validate() == True:
        execute()

    repeat = input('Execute again: y/n:')
    if repeat.upper() != 'Y':
        print("Aborting")
        break