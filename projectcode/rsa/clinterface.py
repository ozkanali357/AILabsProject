'''
This file gives the command line interface for the RSA program.
Here, we can generate keys, encrypt messages, and decrypt messages.
(Error handling is implemented as well.)
'''

import sys
import os
from pathlib import Path
from typing import Tuple

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from projectcode.rsa.keygen import genkeys
from projectcode.rsa.cription import encrypt, decrypt

def getintinput(prompt: str) -> int:
    '''
    As arguments, we have the prompt message.
    In this function we get integer input from the user.
    We return the valid integer value from the user.
    '''
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("The input can't be empty.")
                continue
            return int(value)
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nThe operation is cancelled.")
            raise

def savekeys(pubkey: Tuple[int, int],
            privkey: Tuple[int, int],
            directory: str = ".") -> None:
    '''
    As arguments, we have the public, private key, and the directory to save the keys.
    This function saves the keys to files.
    We try to save the keys to the directory.
    '''
    try:
        Path(directory).mkdir(parents=True, exist_ok=True)
        with open(f"{directory}/pubkey.txt", "w", encoding="utf-8") as f:
            f.write(f"{pubkey[0]}\n{pubkey[1]}")
        with open(f"{directory}/privkey.txt", "w", encoding="utf-8") as f:
            f.write(f"{privkey[0]}\n{privkey[1]}")
        print(f"The keys are saved to {directory}/pubkey.txt and {directory}/privkey.txt .")
    except PermissionError:
        print(f"Error: There's no permission to write to {directory}.")
        sys.exit(1)

def loadkey(filename: str) -> Tuple[int, int]:
    '''
    As an argument, we have the filename of the key file.
    This function loads the keys from files.
    We return the valid key components.
    '''
    try:
        with open(filename, "r", encoding="utf-8") as f:
            e = int(f.readline().strip())
            n = int(f.readline().strip())
            if e <= 0 or n <= 0:
                raise ValueError("These are invalid key values")
            return (e, n)
    except FileNotFoundError:
        print(f"Error: We couldn't find {filename}. Please generate the keys first.")
        sys.exit(1)
    except (ValueError, IndexError):
        print(f"Error: There's an invalid key format in {filename}")
        sys.exit(1)

def main():
    '''
    We get the menu of options printed.
    This function is the main command line interface for RSA operations.
    '''
    try:
        while True:
            print("\nRSA Encryption and Decryption Project")
            print("Press 1 and 'Enter' for generating keys.")
            print("Press 2 and 'Enter' for encrypting your message.")
            print("Press 3 and 'Enter' for decrypting your message.")
            print("Press 4 and 'Enter' for exiting the project.")

            choice = input("\nPlease choose an option (1,2,3,4): ").strip()

            if choice == "1":
                pubkey, privkey, _, _ = genkeys()
                savekeys(pubkey, privkey)

                print("\nThe keys are generated successfully:")
                print(f"Public Key (e, n):\ne: {pubkey[0]}\nn: {pubkey[1]}")
                print(f"\nPrivate Key (d, n):\nd: {privkey[0]}\nn: {privkey[1]}")

            elif choice == "2":
                message = input("Enter a message to encrypt: ").strip()
                if not message:
                    print("Error: Your message can't be empty.")
                    continue

                pubkey = loadkey("pubkey.txt")
                try:
                    encrypted = encrypt(message, pubkey)
                    print(f"\nYour Encrypted Message:\n{encrypted}")
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == "3":
                try:
                    encrypted = getintinput("Enter your encrypted message: ")
                    privkey = loadkey("privkey.txt")
                    decrypted = decrypt(encrypted, privkey)

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

    except KeyboardInterrupt:
        print("\nThe operation is cancelled by you.")
        sys.exit(0)

# pragma: no cover
if __name__ == "__main__":
    main()
