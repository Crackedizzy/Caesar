# A Caesar Cipher Program
import os.path
import string

def welcome():
    # add your code here
    print("Welcome to Caesar Cipher ")
    print("This program encrypts and decrypts text with the Caesar Cipher.")

def enter_message():
    # add your code here
    mode = input("Would you like to encrypt (e) or decrypt (d): ")
    while mode not in ('e', 'd'):
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
    if mode == "e":
        message = input("What message wold you like to encrypt: ")
        message = message.upper()
        shift = input("What is the shift number: ")
        while not shift.isdigit():
            print("Invalid Shift")
            shift = input("What is the shift number: ")
    else:
        message = input("What message would you like to decrypt: ")
        message = message.upper()
        shift = input("What is the shift number: ")
        while not shift.isdigit():
            print("Invalid Shift")
            shift = input("What is the shift number: ")
    return (mode, message, shift)

def encrypt(message,shift):
    # add your code here
    global encrypted
    encrypted = ""
    message = message.upper()
    for i in message:
        if i  in string.ascii_letters:
            alphanum = ord(i) + int(shift)
            if alphanum > ord('Z'):
                alphanum -= 26
            encrypt = chr(alphanum)
            encrypted += encrypt
            #encrypted = encrypted.upper()
        else:
            encrypted += i
            encrypted = encrypted.replace("\n","")
    return encrypted

def decrypt(message,shift):
    # add your code here
    global decrypted
    decrypted = ""
    message = message.upper()
    for i in message:
        if i.isalpha():
            alphanum = ord(i) - int(shift)
            if alphanum < ord('A'):
                alphanum += 26
            decrypt = chr(alphanum)
            decrypted += decrypt
            #decrypted = decrypted.upper()
        else:
            decrypted += i
            decrypted = decrypted.replace("\n","")
    return decrypted

def process_file(filename, mode, shift):
    global list_messages
    list_messages = []
    # add your code here
    f = open(filename, "r")
    if is_file(filename) is True:
        if mode == "e":
            for message in f:
                encrypt(message,shift)
                list_messages.append(encrypted)
        elif mode == "d":
            for message in f:
                decrypt(message,shift)
                list_messages.append(decrypted)
    else:
        print("File doesnt exist")
    #return list_messages
    f.close()
    return write_messages(list_messages)

def write_messages(list_messages):
    # add your code here
    f = open("results.txt", "w")
    for i in list_messages:
        f.write("%s\n" % i)
    f.close()
    print("Output written to results.txt")

def is_file(filename):
    if os.path.exists(filename):
        return True
    else:
        return False

def message_or_file():
    mode = ''
    filename = None
    message = None
    shift = 0
    # add your code here
    mode = input("Would you like to encrypt (e) or decrypt (d): ")
    while mode not in ('e', 'd'):
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
    read = input("Would you like to read from a file(f) or console(c)?: ")
    while read not in ('f', 'c'):
        read = input("Would you like to read from a file(f) or console(c)?: ")
    if read == "f":
        filename = input("Enter a filename: ")
        while is_file(filename) is False:
            filename = input("Enter a filename: ")
        shift = input("What is the shift number: ")
        while not shift.isdigit():
            print("Invalid Shift")
            shift = input("What is the shift number: ")
        return process_file(filename, mode, shift)
        return write_messages(list_messages)
        return (mode, message, filename, shift)
    elif read == "c":
        if mode == "e":
            message = input("What message would you like to encrypt: ")
            shift = input("What is the shift number: ")
            while not shift.isdigit():
                print("Invalid Shift")
                shift = input("What is the shift number: ")
            print(encrypt(message,shift))
        else:
            message = input("What message would you like to decrypt: ")
            shift = input("What is the shift number: ")
            while not shift.isdigit():
                print("Invalid Shift")
                shift = input("What is the shift number: ")
            print(decrypt(message,shift))
        #return (mode, message, filename, shift)
"""
MAIN DRIVER FUNCTION
----------------------------------------------------------------------------------------------
Requirements:
    • Prompt users to select a mode: encrypt (e) or decrypt (d).
    • Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    • Prompt the user for the message they would like to encrypt/decrypt.
    • encrypt/decrypt the message as appropriate and print the output.
    • Prompt the user whether they would like to encrypt/decrypt another message.
        • Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            • End the program if the user selects no.
            • Proceed directly to step 2 if the user says yes.
    • Your program should be as close as possible to the example shown in the assessment specification.
"""
def main():
    # add your code here
    welcome()
    message_or_file()
    again = input("Would you like to encrypt or decrypt another message? (y/n) :")
    while again not in ("y", "n"):
        again = input("Would you like to encrypt or decrypt another message? (y/n) :")
    if again == "y":
        message_or_file()
        while again != "n":
            again = input("Would you like to encrypt or decrypt another message? (y/n) :")
            if again == "y":
                message_or_file()
            else:
                print("Thanks for using the program, goodbye!")
    else:
        print("Thanks for using the program, goodbye!")

# Program execution begins here
if __name__ == '__main__':
    main()
