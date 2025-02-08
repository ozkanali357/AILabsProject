# This file gives the command line interface for the RSA program.
# Here, we can generate keys, encrypt messages, and decrypt messages. (Error handling is implemented as well.)

import sys
import os
from pathlib import Path
from typing import Tuple

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # This is for correct parent directory to path addition, allowing correct import of modules.

from RSA.KeyGen import genkeys
from RSA.Cription import encrypt, decrypt

def getintinput(prompt: str) -> int: # In this function we get integer input from the user.
    while True:
        try:
            value = input(prompt).strip() # As arguments, we have the prompt message.
            if not value:
                print("The input can't be empty.")
                continue
            return int(value) # We return the valid integer value from the user.
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nThe operation is cancelled.")
            raise # If the user cancels the input, then we get a Keyboard Interrupt.

def savekeys(pubkey: Tuple[int, int], # This function saves the keys to files.
            privkey: Tuple[int, int], 
            directory: str = ".") -> None: # As arguments, we have the public key, private key, and the directory to save the keys.
    try: # We try to save the keys to the directory.
        Path(directory).mkdir(parents=True, exist_ok=True) # If the directory doesn't exist to save the keys, we create it.
        with open(f"{directory}/pubkey.txt", "w") as f:
            f.write(f"{pubkey[0]}\n{pubkey[1]}")
        with open(f"{directory}/privkey.txt", "w") as f:
            f.write(f"{privkey[0]}\n{privkey[1]}")
        print(f"The keys are saved to {directory}/pubkey.txt and {directory}/privkey.txt .")
    except PermissionError: # If we don't have permission to write to the directory, we raise an error.
        print(f"Error: There's no permission to write to {directory}.")
        sys.exit(1)

def loadkey(filename: str) -> Tuple[int, int]: # This function loads the keys from files.
    try: # As an argument, we have the filename of the key file.
        with open(filename, "r") as f: # We read and validate key components
            e = int(f.readline().strip())
            n = int(f.readline().strip())
            if e <= 0 or n <= 0:
                raise ValueError("These are invalid key values")
            return (e, n) # We return the key components.
    except FileNotFoundError:
        print(f"Error: We couldn't find {filename}. Please generate the keys first.") # If the file doesn't exist, we raise an error.
        sys.exit(1)
    except (ValueError, IndexError):
        print(f"Error: There's an invalid key format in {filename}") # If the key format is invalid, we raise an error.
        sys.exit(1)

def main(): # This function is the main command line interface for RSA operations.
    try:
        while True: # We get the menu of options printed.
            print("\nRSA Encryption and Decryption Project")
            print("Press 1 for generating keys.")
            print("Press 2 for encrypting your message.")
            print("Press 3 for decrypting your message.")
            print("Press 4 for exiting the project.")

            choice = input("\nPlease choose an option (1,2,3,4): ").strip()

            if choice == "1": # 1 is selected by the user if they want to generate keys.
                pubkey, privkey, _, _ = genkeys()
                savekeys(pubkey, privkey)
                
                print("\nThe keys are generated successfully:") # The generated keys are printed.
                print(f"Public Key (e, n):\ne: {pubkey[0]}\nn: {pubkey[1]}")
                print(f"\nPrivate Key (d, n):\nd: {privkey[0]}\nn: {privkey[1]}")

            elif choice == "2": # 2 is selected by the user if they want to encrypt a message.
                message = input("Enter a message to encrypt: ").strip()
                if not message: # This check is for an empty message.
                    print("Error: Your message can't be empty.")
                    continue
                    
                pubkey = loadkey("pubkey.txt") # We load the public key.
                encrypted = encrypt(message, pubkey)
                print(f"\nYour Encrypted Message:\n{encrypted}") # The encrypted message is printed.

            elif choice == "3": # 3 is selected by the user if they want to decrypt a message.
                try:
                    encrypted = getintinput("Enter your encrypted message: ")
                    privkey = loadkey("privkey.txt")
                    decrypted = decrypt(encrypted, privkey)
                    
                    if isinstance(decrypted, str): # If the decryption is successful, we print the decrypted message.
                        print(f"\nYour Decrypted Message: {decrypted}")
                    else:
                        print("Error: The decryption process failed.")
                except UnicodeDecodeError:
                    print("Error: We couldn't decrypt the message. "
                          "It may be corrupted or using wrong key.")

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

    except KeyboardInterrupt: # If the user cancels the operation, we print a message and exit.
        print("\nThe operation is cancelled by you.")
        sys.exit(0)

if __name__ == "__main__": # pragma: no cover
    main()