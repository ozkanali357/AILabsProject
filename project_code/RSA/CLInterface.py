# This file gives the command line interface for the RSA program.
# Here, we can generate keys, encrypt messages, and decrypt messages. (python3 -m RSA.CLInterface)

from .KeyGen import genkeys
from .Cription import encrypt, decrypt

def main():
    print("RSA Encryption Tool")
    print("1 -> Generate Keys")
    print("2 -> Encrypt Message")
    print("3 -> Decrypt Message")
    choice = input("Chose an option by entering its number: ")

    if choice == "1":
        pubkey, privkey = genkeys()
        print("Public Key (e, n):", pubkey)
        print("Private Key (d, n):", privkey)
    elif choice == "2":
        message = input("Enter message to encrypt: ")
        e = int(input("Enter e (from public key): "))
        n = int(input("Enter n (from public key): "))
        pubkey = (e, n)
        encryptedmessage = encrypt(message, pubkey)
        print("Encrypted Message:", encryptedmessage)
    elif choice == "3":
        encryptedmessage = int(input("Enter encrypted message: "))
        d = int(input("Enter d (from private key): "))
        n = int(input("Enter n (from private key): "))
        privkey = (d, n)
        decryptedmessage = decrypt(encryptedmessage, privkey)
        print("Decrypted Message:", decryptedmessage)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()