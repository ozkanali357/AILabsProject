# Specification Document

## Project Title: RSA Encryption

### Programming Language:

- **Primary Language:** Python
- **Proficient Languages:**
  - Python (the preferred one)
  - R
  - JavaScript
  - HTML/CSS
  - SQL
  - Kotlin
  - Swift
  - TypeScript
  - Go

### Algorithms and Data Structures:

#### Algorithms:
- RSA Encryption
- Miller-Rabin Primality Test
- Modular Exponentiation

#### Data Structures:
- Nothing specific beyond basic data types like integers, strings, lists.

### Problem Statement:

The project would implement RSA encryption to secure data. This would showcase the importance of encryption in today's world and the ways in which one can make sure that data is kept secure.

### Inputs and Usage:

#### Inputs:
- Plaintext message that needs to be encrypted
- Public and private keys for RSA encryption/decryption

#### Usage:
- The program should take a plaintext message and then encrypt it with RSA encryption.
- It should also decrypt an encrypted message using the corresponding private key.

  (As far as I understand, the RSA encryption has both encryption and decryption. I am not sure if I should both enrypt it with the public key and decrypt it with the private key to show that the encrypted data can be turned to its original version. Maybe I could put it in the testing document/code. Another concern that I have is if the decription part makes the project ambitious or unmanagable.)

### Desired Time and Space Complexities:

#### RSA Encryption:
- Time Complexity: $O(n^3)$ for key generation, where $n$ is in bits
- Space Complexity: $O(n)$

#### Miller-Rabin Primality Test:
- Time Complexity: $O(k \cdot \log^3 n)$ where $k$ is the number of iterations
- Space Complexity: $O(\log n)$

#### Modular Exponentiation:
- Time Complexity: $O(\log n)$
- Space Complexity: $O(\log n)$

### References:

- [RSA Encryption](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [Miller-Rabin Primality Test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
- [Modular Exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation)

### Other Information:

- Study Program: Bachelor of Science (In the Computer and Data Science Study Track)
- Documentation Language: English
