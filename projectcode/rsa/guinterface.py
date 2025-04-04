'''
This file contains the graphical user interface for the RSA encryption and decryption project.
It has key generation, message encryption, and message decryption functionalities.
'''

import sys
from pathlib import Path
from typing import Tuple
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from projectcode.rsa.keygen import genkeys
from projectcode.rsa.cription import encrypt, decrypt

def savekeys(pubkey: Tuple[int, int],
            privkey: Tuple[int, int],
            directory: str = ".") -> None:
    '''
    If the directory doesn't exist, we create it.
    We write the public and private keys to different files.
    This function saves the RSA keys to files.
    '''
    Path(directory).mkdir(parents=True, exist_ok=True)
    try:
        with open(f"{directory}/pubkey.txt", "w", encoding="utf-8") as f:
            f.write(f"{pubkey[0]}\n{pubkey[1]}")
        with open(f"{directory}/privkey.txt", "w", encoding="utf-8") as f:
            f.write(f"{privkey[0]}\n{privkey[1]}")
    except PermissionError as exc:
        raise PermissionError(f"There's no permission to write to {directory}") from exc

def loadkey(filename: str) -> Tuple[int, int]:
    '''
    This function loads the RSA valid integer keys from a file.
    '''
    try:
        with open(filename, "r", encoding="utf-8") as f:
            line1 = f.readline().strip()
            line2 = f.readline().strip()
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            f"We couldn't find {filename}. Please generate your keys first."
            ) from exc
    try:
        e = int(line1)
        n = int(line2)
    except ValueError as exc:
        raise ValueError(f"There's an invalid key format in {filename}") from exc
    if e <= 0 or n <= 0:
        raise ValueError("These are invalid key values.")
    return (e, n)

class RSAGUI:
    '''
    Here, this class starts the GUI and puts the window and tabs.
    '''
    def __init__(self, root: tk.Tk) -> None:
        '''
        The tabs are made for key generation, encryption, and decryption.
        '''
        self.root = root
        self.root.title("RSA Encryption Project")
        self.root.geometry("800x600")
        self.tabcontrol = ttk.Notebook(root)
        self.tabs = {
            'key': ttk.Frame(self.tabcontrol),
            'encrypt': ttk.Frame(self.tabcontrol),
            'decrypt': ttk.Frame(self.tabcontrol)
        }
        self.tabcontrol.add(self.tabs['key'], text='Key Generation')
        self.tabcontrol.add(self.tabs['encrypt'], text='Encryption')
        self.tabcontrol.add(self.tabs['decrypt'], text='Decryption')
        self.tabcontrol.pack(expand=1, fill="both")
        self.textboxes = {}
        self.setkeytab()
        self.setencrypttab()
        self.setdecrypttab()

    def setkeytab(self) -> None:
        '''
        The key generation tab is put here, 
        and there is a button to make keys and show them with text boxes.
        '''
        ttk.Label(self.tabs['key'], text="RSA Key Generation", font=('Arial', 14)).pack(pady=10)
        keyframe = ttk.Frame(self.tabs['key'])
        keyframe.pack(pady=10, padx=10)
        ttk.Button(keyframe, text="Generate New Keys", command=self.generatekeys).pack(pady=10)
        self.textboxes['pubkey'] = scrolledtext.ScrolledText(keyframe, width=60, height=5)
        self.textboxes['pubkey'].pack(pady=5)
        self.textboxes['privkey'] = scrolledtext.ScrolledText(keyframe, width=60, height=5)
        self.textboxes['privkey'].pack(pady=5)
        self.ctrlall(self.textboxes['pubkey'])
        self.ctrlall(self.textboxes['privkey'])

    def setencrypttab(self) -> None:
        '''
        The encryption tab is put here with a button to encrypt
        and there are text boxes for the message and the encrypted message.
        '''
        ttk.Label(self.tabs['encrypt'], text="Message Encryption", font=('Arial', 14)).pack(pady=10)
        encryptframe = ttk.Frame(self.tabs['encrypt'])
        encryptframe.pack(pady=10, padx=10)
        ttk.Label(encryptframe, text="Enter Message:").pack()
        self.textboxes['message'] = scrolledtext.ScrolledText(encryptframe, width=50, height=4)
        self.textboxes['message'].pack(pady=5)
        ttk.Button(encryptframe, text="Encrypt", command=self.encryptmessage).pack(pady=10)
        ttk.Label(encryptframe, text="Encrypted Message:").pack()
        self.textboxes['encrypted'] = scrolledtext.ScrolledText(
            encryptframe, width=50, height=4
            )
        self.textboxes['encrypted'].pack(pady=5)
        self.ctrlall(self.textboxes['message'])
        self.ctrlall(self.textboxes['encrypted'])

    def setdecrypttab(self) -> None:
        '''
        The decryption tab is put here, with a button to decrypt
        and there are text boxes for the encrypted message and the decrypted message.
        '''
        ttk.Label(self.tabs['decrypt'], text="Message Decryption", font=('Arial', 14)).pack(pady=10)
        decryptframe = ttk.Frame(self.tabs['decrypt'])
        decryptframe.pack(pady=10, padx=10)
        ttk.Label(decryptframe, text="Enter Encrypted Message:").pack()
        self.textboxes['encrypted_input'] = scrolledtext.ScrolledText(
            decryptframe, width=50, height=4
            )
        self.textboxes['encrypted_input'].pack(pady=5)
        ttk.Button(decryptframe, text="Decrypt", command=self.decryptmessage).pack(pady=10)
        ttk.Label(decryptframe, text="Decrypted Message:").pack()
        self.textboxes['decrypted'] = scrolledtext.ScrolledText(
            decryptframe, width=50, height=4
            )
        self.textboxes['decrypted'].pack(pady=5)
        self.ctrlall(self.textboxes['encrypted_input'])
        self.ctrlall(self.textboxes['decrypted'])

    def ctrlall(self, textbox: scrolledtext.ScrolledText) -> None:
        '''
        You can select the text in the boxes with Ctrl+A.
        '''
        def gettext(event):
            textbox.tag_add(tk.SEL, "1.0", tk.END)
            textbox.mark_set(tk.INSERT, "1.0")
            textbox.see(tk.INSERT)
            return 'break'
        textbox.bind("<Control-a>", gettext)
        textbox.bind("<Control-A>", gettext)

    def generatekeys(self) -> None:
        '''
        This function generates the RSA keys and shows them in the text boxes.
        '''
        try:
            pubkey, privkey, _, _ = genkeys()
            savekeys(pubkey, privkey)
            self.textboxes['pubkey'].delete(1.0, tk.END)
            self.textboxes['privkey'].delete(1.0, tk.END)
            self.textboxes['pubkey'].insert(
                tk.END, f"Public Key (e, n):\ne: {pubkey[0]}\nn: {pubkey[1]}"
            )
            self.textboxes['privkey'].insert(
                tk.END, f"Private Key (d, n):\nd: {privkey[0]}\nn: {privkey[1]}"
            )
            messagebox.showinfo("Success", "Your keys are generated and saved successfully!")
        except (PermissionError, ValueError) as e:
            messagebox.showerror("Error", str(e))

    def encryptmessage(self) -> None:
        '''
        This function encrypts the message by using the public key
        and shows the encrypted message in the text box.
        '''
        try:
            message = self.textboxes['message'].get(1.0, tk.END).strip()
            if not message:
                messagebox.showwarning("Warning", "Please enter a message.")
                return
            pubkey = loadkey("pubkey.txt")
            try:
                encrypted = encrypt(message, pubkey)
                self.textboxes['encrypted'].delete(1.0, tk.END)
                self.textboxes['encrypted'].insert(tk.END, str(encrypted))
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        except (PermissionError, ValueError) as e:
            messagebox.showerror("Error", str(e))

    def decryptmessage(self) -> None:
        '''
        This function decrypts the encrypted message by using the private key
        and shows the decrypted message in the text box.
        '''
        try:
            encrypted = self.textboxes['encrypted_input'].get(1.0, tk.END).strip()
            if not encrypted:
                messagebox.showwarning("Warning", "Please enter an encrypted message.")
                return
            privkey = loadkey("privkey.txt")
            decrypted = decrypt(int(encrypted), privkey)
            self.textboxes['decrypted'].delete(1.0, tk.END)
            self.textboxes['decrypted'].insert(tk.END, decrypted)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def main() -> None:
    '''Main function to start the GUI application.'''
    root = tk.Tk()
    RSAGUI(root)
    root.mainloop()

# pragma: no cover
if __name__ == "__main__":
    main()
