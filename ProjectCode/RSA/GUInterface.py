# This file contains the graphical user interface for the RSA encryption and decryption project.
# It has key generation, message encryption, and message decryption functionalities.

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from pathlib import Path
import sys
import os
from typing import Tuple

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # For correct parent directory

from RSA.KeyGen import genkeys
from RSA.Cription import encrypt, decrypt

def savekeys(pubkey: Tuple[int, int],  # This function saves the RSA keys to files.
            privkey: Tuple[int, int],
            directory: str = ".") -> None:
    Path(directory).mkdir(parents=True, exist_ok=True) # If the directory doesn't exist, we create it.
    try: # We write the public and private keys to different files.
        with open(f"{directory}/pubkey.txt", "w") as f:
            f.write(f"{pubkey[0]}\n{pubkey[1]}")
        with open(f"{directory}/privkey.txt", "w") as f:
            f.write(f"{privkey[0]}\n{privkey[1]}")
    except PermissionError:  # We get an error if there's no permission.
        raise Exception(f"There's no permission to write to {directory}")

def loadkey(filename: str) -> Tuple[int, int]: # This function loads the RSA keys from a file.
    try:
        with open(filename, "r") as f: # We read the keys from the file.
            line1 = f.readline().strip() # The code reads the key parts from the file.
            line2 = f.readline().strip()
    except FileNotFoundError: # We check if the file exists.
        raise Exception(f"We couldn't find {filename}. Please generate your keys first.")
    try:
        e = int(line1)
        n = int(line2)
    except ValueError: # We check if the keys are integers.
        raise Exception(f"There's an invalid key format in {filename}")
    if e <= 0 or n <= 0: # We check if the keys are valid.
        raise ValueError("These are invalid key values.")
    return (e, n)

class RSAGUI: # Here, this class starts the GUI and puts the window and tabs.
    def __init__(self, root: tk.Tk) -> None: # The tabs are made for key generation, encryption, and decryption.
        self.root = root
        self.root.title("RSA Encryption Project")
        self.root.geometry("800x600")
        self.tabcontrol = ttk.Notebook(root)
        self.keytab = ttk.Frame(self.tabcontrol)
        self.encrypttab = ttk.Frame(self.tabcontrol)
        self.decrypttab = ttk.Frame(self.tabcontrol)
        self.tabcontrol.add(self.keytab, text='Key Generation')
        self.tabcontrol.add(self.encrypttab, text='Encryption')
        self.tabcontrol.add(self.decrypttab, text='Decryption')
        self.tabcontrol.pack(expand=1, fill="both")
        self.setkeytab()
        self.setencrypttab()
        self.setdecrypttab()

    def setkeytab(self) -> None: # The key generation tab is put here, and there is a button to make keys and show them with text boxes.
        ttk.Label(self.keytab, text="RSA Key Generation", font=('Arial', 14)).pack(pady=10)
        keyframe = ttk.Frame(self.keytab)
        keyframe.pack(pady=10, padx=10)
        ttk.Button(keyframe, text="Generate New Keys", command=self.generatekeys).pack(pady=10)
        self.pubkeydisplay = scrolledtext.ScrolledText(keyframe, width=60, height=5)
        self.pubkeydisplay.pack(pady=5)
        self.privkeydisplay = scrolledtext.ScrolledText(keyframe, width=60, height=5)
        self.privkeydisplay.pack(pady=5)

    def setencrypttab(self) -> None: # The encryption tab is put here with a button to encrypt and there are text boxes for the message and the encrypted message.
        ttk.Label(self.encrypttab, text="Message Encryption", font=('Arial', 14)).pack(pady=10)
        encryptframe = ttk.Frame(self.encrypttab)
        encryptframe.pack(pady=10, padx=10)
        ttk.Label(encryptframe, text="Enter Message:").pack()
        self.messageinput = scrolledtext.ScrolledText(encryptframe, width=50, height=4)
        self.messageinput.pack(pady=5)
        ttk.Button(encryptframe, text="Encrypt", command=self.encryptmessage).pack(pady=10)
        ttk.Label(encryptframe, text="Encrypted Message:").pack()
        self.encrypteddisplay = scrolledtext.ScrolledText(encryptframe, width=50, height=4)
        self.encrypteddisplay.pack(pady=5)

    def setdecrypttab(self) -> None: # The decryption tab is put here, with a button to decrypt and there are text boxes for the encrypted message and the decrypted message.
        ttk.Label(self.decrypttab, text="Message Decryption", font=('Arial', 14)).pack(pady=10)
        decryptframe = ttk.Frame(self.decrypttab)
        decryptframe.pack(pady=10, padx=10)
        ttk.Label(decryptframe, text="Enter Encrypted Message:").pack()
        self.encryptedinput = scrolledtext.ScrolledText(decryptframe, width=50, height=4)
        self.encryptedinput.pack(pady=5)
        ttk.Button(decryptframe, text="Decrypt", command=self.decryptmessage).pack(pady=10)
        ttk.Label(decryptframe, text="Decrypted Message:").pack()
        self.decrypteddisplay = scrolledtext.ScrolledText(decryptframe, width=50, height=4)
        self.decrypteddisplay.pack(pady=5)

    def generatekeys(self) -> None: # This function generates the RSA keys and shows them in the text boxes.
        try:
            pubkey, privkey, _, _ = genkeys()
            savekeys(pubkey, privkey)
            self.pubkeydisplay.delete(1.0, tk.END)
            self.privkeydisplay.delete(1.0, tk.END)
            self.pubkeydisplay.insert(tk.END, f"Public Key (e, n):\ne: {pubkey[0]}\nn: {pubkey[1]}")
            self.privkeydisplay.insert(tk.END, f"Private Key (d, n):\nd: {privkey[0]}\nn: {privkey[1]}")
            messagebox.showinfo("Success", "Your keys are generated and saved successfully!")
        except Exception as e: # An error message is shown if there is a problem with key generation.
            messagebox.showerror("Error", str(e))

    def encryptmessage(self) -> None: # This function encrypts the message by using the public key and shows the encrypted message in the text box.
        try:
            message = self.messageinput.get(1.0, tk.END).strip()
            if not message:
                messagebox.showwarning("Warning", "Please enter a message.")
                return
            pubkey = loadkey("pubkey.txt")
            encrypted = encrypt(message, pubkey)
            self.encrypteddisplay.delete(1.0, tk.END)
            self.encrypteddisplay.insert(tk.END, str(encrypted))
        except Exception as e: # An error message is shown if there is a problem with encryption.
            messagebox.showerror("Error", str(e))

    def decryptmessage(self) -> None: # This function decrypts the encrypted message by using the private key and shows the decrypted message in the text box.
        try:
            encrypted = self.encryptedinput.get(1.0, tk.END).strip()
            if not encrypted:
                messagebox.showwarning("Warning", "Please enter an encrypted message.")
                return
            privkey = loadkey("privkey.txt")
            decrypted = decrypt(int(encrypted), privkey)
            self.decrypteddisplay.delete(1.0, tk.END)
            self.decrypteddisplay.insert(tk.END, decrypted)
        except Exception as e: # An error message is shown if there is a problem with decryption.
            messagebox.showerror("Error", str(e))

def main() -> None:
    root = tk.Tk()
    app = RSAGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()  # pragma: no cover