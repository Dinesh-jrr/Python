def welcome():
    print(" Welcome to the Caesar Cipher \n This program encrypts and decrypts text with the caesar cipher")
   
    
def enter_message():
    messages=["encrypt" , "decrypt"]
    message=None
    while message not in messages:
        message=input("Would you like to encrypt(e) or decrypt(d):").lower()

    message_operation=input("What message would you like to encrypt or decrypt:").upper()
    return messages , message_operation
enter_message()

def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char.upper()) - 65 +shift) % 26 +65)
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    return encrypted_message
encrypt()

def decrypt(message, shift):
 decrypted_message =""
 for char in message:
     if char.isalpha():
         shifted_char = chr((ord(char.upper()) - 65 - shift) % 26 +65)
         decrypted_message += shifted_char
     else:
        decrypted_message += char
 return decrypted_message
decrypt()
     

 
def process_file(filename, mode):
    messages = []
    
    with open(filename, "r") as file:
        for line in file:
            if mode == "encrypt":
                message = encrypt(line.strip())
            elif mode == "decrypt":
                message = decrypt (line.strip())
            else:
                raise ValueError ("Invalid mode:must be "encrypt" or "decrypt" ")
            messages.append(message)
    return messages
process_file()


import os
def is_file(file.txt):
    try: 
        with open(file.txt, "r"):
            pass
    except FileNotFoundError:
        return False
    return True
is_file()

def write_messages(messages):
    with open("file.txt", "w") as file:
        for message in messages:
            file.write(message + "\n")
write_messages() 

def message_or_file():
    
    valid_modes=["e" , "d"]
    mode =None
    message = None
    filename = None
    
    while not mode:
        mode_input = input("Enter mode e/d:")
        if mode_input.lower() in valid_modes:
            mode = mode_input.lower()
        else:
            print("Invalid mode.Please enter "e" for encryption or "d" for decryption.")
    while not message and not filename:
        input_method = input("Enter input method (file/console):")
        if input_method.lower() == "file":
            while not filename:
                filename_input = input("Enter filename:")
                if is_file(filename_input):
                    filename = filename_input
                else:
                    print("File doesnot exist.Please enter a valid filename.")
        elif input_method.lower()== "console":
            message_input = input ("Enter message:")
            message = message_input.upper()
        else:
            print("Invalid input method.Please enter "file" or "console"".)


    return mode, message, filename







