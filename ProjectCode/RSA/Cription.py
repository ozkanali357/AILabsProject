# This file has tools for RSA encryption and decryption with functions.
# We aim to conver messages to integers, perform modular exponentiation and convert the message back to text.

# The function encrypts a message using the RSA public key.
def encrypt(message, pubkey): # As an argument, we put a string message to encrypt and a tuple public key (e, n).
    e, n = pubkey # The tuple public key is unpacked to its components (the public exponent e and the modulus n).
    messageint = int.from_bytes(message.encode(), 'big') # The string message is encoded into bytes (message.encode()). Then, the method int.from_bytes() converts the bytes to an integer. We use big endian byte order, so the most significant byte is at the beginning.
    ciphertext = pow(messageint, e, n) # We do the encryption with the RSA formula: ciphertext = message^e mod n.
    return ciphertext # In return, we get the ciphertext, which is the encrypted message as an integer.

# The function decrypts a ciphertext using the RSA private key.
def decrypt(ciphertext, privkey): # As an argument, we put the ciphertext as an integer and a tuple private key (d, n).
    d, n = privkey # The tuple private key is unpacked to its components (the private exponent d and the modulus n).
    messageint = pow(ciphertext, d, n) # We do the decryption with the RSA formula: message = ciphertext^d mod n.
    try:
        message = messageint.to_bytes((messageint.bit_length() + 7) // 8, 'big').decode() # The integer message is converted to bytes with the method int.tobytes(). Then, the bytes are decoded to a string. We use big endian byte order, so the most significant byte is at the beginning. The number of bytes is calculated with the formula (messageint.bit_length() + 7) // 8 to see if there are enough bytes to represent the integer.
    except UnicodeDecodeError: # Here, we catch the exception if the encrypted message isn't a valid UFT-8 sequence and the decrypted bytes can't be decoded as UFT-8 (Unicode Transformation Format - 8-bit.).
        return "The decryption didn't happen, because the decrypted bytes can't be decoded as UTF-8."
    return message # In return, we get the decrypted message as a string.