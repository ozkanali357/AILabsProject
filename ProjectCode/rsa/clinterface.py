'''
This file gives the command line interface for the RSA program.
Here, we can generate keys, encrypt messages, and decrypt messages.
(Error handling is implemented as well.)
'''

import sys
import os
from pathlib import Path
from typing import Tuple
from rsa.keygen import genkeys
from rsa.cription import encrypt, decrypt

# This is for correct parent directory to path addition, allowing correct import of modules.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# As arguments, we have the prompt message.
def getintinput(prompt: str) -> int:
    '''
    In this function we get integer input from the user.
    '''
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("The input can't be empty.")
                continue
# We return the valid integer value from the user.
            return int(value)
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nThe operation is cancelled.")
# If the user cancels the input, then we get a Keyboard Interrupt.
            raise

# As arguments, we have the public key, private key, and the directory to save the keys.
def savekeys(pubkey: Tuple[int, int],
            privkey: Tuple[int, int],
            directory: str = ".") -> None:
    '''
    This function saves the keys to files.
    '''
# We try to save the keys to the directory.
    try:
# If the directory doesn't exist to save the keys, we create it.
        Path(directory).mkdir(parents=True, exist_ok=True)
        with open(f"{directory}/pubkey.txt", "w", encoding="utf-8") as f:
            f.write(f"{pubkey[0]}\n{pubkey[1]}")
        with open(f"{directory}/privkey.txt", "w", encoding="utf-8") as f:
            f.write(f"{privkey[0]}\n{privkey[1]}")
        print(f"The keys are saved to {directory}/pubkey.txt and {directory}/privkey.txt .")
# If we don't have permission to write to the directory, we raise an error.
    except PermissionError:
        print(f"Error: There's no permission to write to {directory}.")
        sys.exit(1)

# As an argument, we have the filename of the key file.
def loadkey(filename: str) -> Tuple[int, int]:
    '''
    This function loads the keys from files.
    '''
    try:
# We read and validate key components
        with open(filename, "r", encoding="utf-8") as f:
            e = int(f.readline().strip())
            n = int(f.readline().strip())
            if e <= 0 or n <= 0:
                raise ValueError("These are invalid key values")
# We return the key components.
            return (e, n)
    except FileNotFoundError:
# If the file doesn't exist, we raise an error.
        print(f"Error: We couldn't find {filename}. Please generate the keys first.")
        sys.exit(1)
    except (ValueError, IndexError):
# If the key format is invalid, we raise an error.
        print(f"Error: There's an invalid key format in {filename}")
        sys.exit(1)

def main():
    '''This function is the main command line interface for RSA operations.'''
    try:
# We get the menu of options printed.
        while True:
            print("\nRSA Encryption and Decryption Project")
            print("Press 1 and 'Enter' for generating keys.")
            print("Press 2 and 'Enter' for encrypting your message.")
            print("Press 3 and 'Enter' for decrypting your message.")
            print("Press 4 and 'Enter' for exiting the project.")

            choice = input("\nPlease choose an option (1,2,3,4): ").strip()

# 1 is selected by the user if they want to generate keys.
            if choice == "1":
                pubkey, privkey, _, _ = genkeys()
                savekeys(pubkey, privkey)

# The generated keys are printed.
                print("\nThe keys are generated successfully:")
                print(f"Public Key (e, n):\ne: {pubkey[0]}\nn: {pubkey[1]}")
                print(f"\nPrivate Key (d, n):\nd: {privkey[0]}\nn: {privkey[1]}")

# 2 is selected by the user if they want to encrypt a message.
            elif choice == "2":
                message = input("Enter a message to encrypt: ").strip()
# This check is for an empty message.
                if not message:
                    print("Error: Your message can't be empty.")
                    continue

# We load the public key.
                pubkey = loadkey("pubkey.txt")
                encrypted = encrypt(message, pubkey)
# The encrypted message is printed.
                print(f"\nYour Encrypted Message:\n{encrypted}")

# 3 is selected by the user if they want to decrypt a message.
            elif choice == "3":
                try:
                    encrypted = getintinput("Enter your encrypted message: ")
                    privkey = loadkey("privkey.txt")
                    decrypted = decrypt(encrypted, privkey)

# If the decryption is successful, we print the decrypted message.
                    if isinstance(decrypted, str):
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

# If the user cancels the operation, we print a message and exit.
    except KeyboardInterrupt:
        print("\nThe operation is cancelled by you.")
        sys.exit(0)

# pragma: no cover
if __name__ == "__main__":
    main()
