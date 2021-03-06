import os
import tkinter as tk
import sys
from cryptography.fernet import Fernet
from tkinter import filedialog

def encrypt(to_encrypt, key):
    text_to_encrypt = file.read()
    encrypted_text = f_key.encrypt(text_to_encrypt.encode())

    new_file = open(f"[ENCRYPTED]{filename.split('/')[-1]}", "w+")
    new_file.write(encrypted_text.decode())

    print("File Encrypted and saved in this directory!")

def decrypt(to_decrypt, key):
    text_to_decrypt = file.read()
    decrypted_text = f_key.decrypt(text_to_decrypt.encode())

    new_name = f"[DECRYPTED]{(filename.split('/')[-1]).replace('[ENCRYPTED]', '')}"

    new_file = open(new_name, "w+")
    new_file.write(decrypted_text.decode())

    print("File decrypted and saved in this directory!")


key = ""

tk.Tk().withdraw()

while True:
    response = input("Do you have a key (y/n): ").lower()

    if response == 'n':
        key = Fernet.generate_key()
        print(f"This is your key, keep it safe: {key.decode()}")
        break
    elif response == 'y':
        key = input("Enter your key: ")
        break
    else:
        print("Invalid answer")


try:
    f_key = Fernet(key)
except Exception as e:
    print("\nYour key isn't valid")
    print(f"Exception: {e}\n")

    sys.exit()

filename = filedialog.askopenfilename()

if not filename:
    print("You must pick a file.")
    sys.exit()

file = open(filename, 'r')

while True:
    response = input("Encrypt or decrypt (e/d): ").lower()
    if response == 'e':
        encrypt(file, f_key)
        break
    elif response == 'd':
        decrypt(file, f_key)
        break
    else:
        print("Invalid answer")
