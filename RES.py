# Read - Encrypt - Save
import RPi.GPIO as GPIO
import MFRC522
import signal
import bcrypt

continue_reading = True

password_encrypted = '$2b$14$LcUGT.RzazdCY5KtNn15ROJZIlYTGN1eNM3miiUhnGYe5AJUziGWi'

MIFAREReader = MFRC522.MFRC522()
       

def read():
    try:
        rfid_id = MIFAREReader.MFRC522_SelectTag(uid)
        return rfid_id
    finally:
        GPIO.cleanup()     

def encrypt():
    encrypted_rfid_id = bcrypt.hashpw(rfid_id.encode('UTF-8'), bcrypt.gensalt())
    encrypted_rfid_id = encrypted_rfid_id.decode('UTF-8')
    return encrypted_rfid_id

def save():
    with open('C:/Users/SLASH/Desktop/Python/RFID/authorized-rfid-cards.txt', 'a') as file: 
        file.write(encrypted_rfid_id + ',')        

rfid_id = read()
encrypted_rfid_id = encrypt()

while True:
    password = input('Password: ')
    if bcrypt.checkpw(password.encode('UTF-8'), password_encrypted.encode('UTF-8')):
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        while continue_reading:
            if status == MIFAREReader.MI_OK:
                print("Card Detected")
        
            (status,uid) = MIFAREReader.MFRC522_Anticoll()

            if status == MIFAREReader.MI_OK:
                read()
                break
                            
            encrypt()
            save()
            print('Succefully Saved')
            repeat = input('Encrypt more IDs: y/n: ')
            if repeat.upper() != 'Y':
                print('Aborting')
                break
    else:
        print('Incorrect Password')    