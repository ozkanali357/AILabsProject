# User Guide

## Running the Program
The program can be executed in editors like VSCode using the run button. Hovewer, I've also explained other methods below.

You can additionally find the code explanations under the codecomment folder.

### Command Line Interface (CLI)

- Open a terminal and move to where the project is.
cd where_the_project_is_located/ProjectCode

- Run the clinterface.py.
python rsa/clinterface.py

### Graphical User Interface (GUI)
- Open a terminal and move to where the project is.
cd where_the_project_is_located/ProjectCode

- Run the clinterface.py.
python rsa/guinterface.py

## Running the Different Features of the Program

### Key Generation

#### CLI
- Generate Keys: Follow CLI's instruction to generate a new RSA key pair. The keys will be stored to pubkey.txt and privkey.txt.
python rsa/clinterface.py
- Follow CLI's instruction to generate keys.

#### GUI
- Open the Key Generation Tab: Click on the "Key Generation" tab in GUI.

- Generate Keys: Click on the "Generate New Keys" button. The keys that get created will be displayed in the text boxes and stored to pubkey.txt and privkey.txt.

### Encryption

#### CLI
- Encrypt a Message: Follow CLI's instruction to input a message and encrypt it using the public key.
python rsa/clinterface.py
Follow CLI's instruction to encrypt a message.

#### GUI
- Open the Encryption Tab: Click on the "Encryption" tab in GUI.

- Input Message: Input message to be encrypted in given text box.

- Encrypt Message: Click on the "Encrypt" button. The encrypted message will be displayed in the text box.

### Decryption
#### CLI
- Decrypt a Message: Follow CLI's instruction to input a message that is encrypted and decrypt it using the private key.
python rsa/clinterface.py
Follow CLI's instruction to decrypt a message.

#### GUI
- Open the Decryption Tab: Click on the "Decryption" tab in GUI.

- Enter Encrypted Message: Enter the encrypted message in the given text box.

- Decrypt Message: Click on the "Decrypt" button. The decrypted message appears in the text box.

### Formats Inputs the Program Accepts
#### Key Generation
- Bit Length: The program accepts an integer input of used bit length during key generation. The default is 1024 bits.
#### Encryption
- Message: The program accepts a string message to be encrypted. The message can be letters, numbers, or special characters.
#### Decryption
- Encrypted Message: The program accepts an integer input of the encrypted message. The encrypted message must be in the same format provided by the encryption function.