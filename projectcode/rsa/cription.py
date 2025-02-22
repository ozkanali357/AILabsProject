'''
This file has tools for RSA encryption and decryption with functions.
We aim to convert messages to integers, perform modular exponentiation
and convert the message back to text.
'''

def encrypt(message, pubkey):
    '''
    As an argument, we put a string message to encrypt and a tuple public key (e, n).
    The function encrypts a message using the RSA public key.
    In return, we get the ciphertext, which is the encrypted message as an integer.
    '''
    e, n = pubkey
    bytemessage = message.encode()
    messageint = int.from_bytes(bytemessage, 'big')
    if messageint >= n:
        raise ValueError("For this key size, the message is long.")
    ciphertext = pow(messageint, e, n)
    return ciphertext

def decrypt(ciphertext, privkey):
    '''
    As an argument, we put the ciphertext as an integer and a tuple private key (d, n).
    The function decrypts a ciphertext using the RSA private key.
    In return, we get the decrypted message as a string.
    '''
    d, n = privkey
    messageint = pow(ciphertext, d, n)
    try:
        message = messageint.to_bytes((messageint.bit_length() + 7) // 8, 'big').decode()
    except UnicodeDecodeError:
        return ("The decryption didn't happen, because the decrypted bytes can't be decoded "
                "as UTF-8.")
    return message
