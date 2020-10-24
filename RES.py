# Read - Encrypt - Save
#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import bcrypt

reader = SimpleMFRC522()

password_encrypted = '$2b$14$LcUGT.RzazdCY5KtNn15ROJZIlYTGN1eNM3miiUhnGYe5AJUziGWi'

password = input('Password: ')

if bcrypt.checkpw(password.encode('UTF-8'), password_encrypted.encode('UTF-8')):
    while True:
        try:
            name = input('NAME: ')
            print("Place Target:")
            reader.write(name)
            print("Success")
            id = reader.read()
            string_id = ""
            for number in id:
                string_id += number
            encrypted_rfid_id = bcrypt.hashpw(string_id.encode('UTF-8'), bcrypt.gensalt())
            encrypted_rfid_id = encrypted_rfid_id.decode('UTF-8')
            with open('/home/ubuntu/RFID/authorized-rfid-cards.txt', 'a') as file: 
                file.write(encrypted_rfid_id + ',')

        finally:
            GPIO.cleanup()

        repeat = input('Encrypt More IDs y/n: ')    
        if repeat.upper() != 'Y':
            print("Aborting")
            break
else:
    print("Incorrect Password")        
