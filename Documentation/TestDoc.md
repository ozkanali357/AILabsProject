# Testing Document

Apart from the coverage tests, the project also holds a 10/10 pylint code quality on all ProjectCode files. The pylint terminal output is found in the Documentation folder. You can test it with this command: pylint ProjectCode/rsa/*.py

## Coverage Report of the Unit Tests
### Algorithms Coverage Summary (Without Interfaces)
- Overall Coverage: 100%
- Files Covered:
  - primegen.py: 100%
  - keygen.py: 100%
  - cription.py: 100%

## What Has Been Tested and How?

### primegen.py
- eratosieve(limit): Generates small prime numbers up to a given limit using the Sieve of Eratosthenes. It was tested by giving a value and looking at the correctness of the prime numbers made up to it.
- millerrabin(n, k=40): Tests the primality of a number using the Miller-Rabin Primality Test. It was tested with known prime and non-prime numbers. It's additionally composite numbers.
- dobigprime(bits): Creates big prime numbers through the Miller-Rabin Primality Test. It was checked against a known large prime.

### keygen.py
- genkeys(bits=1024): Creates public and private keys for RSA encryption.
- Added unit tests to ensure that the keys produced fulfill RSA properties. Mocking was used to create various situations like producing the same primes and ensuring the public exponent is coprime to Euler's totient function.

### cription.py
- encrypt(message, pubkey): Encrypts a message with the RSA public key.
- decrypt(ciphertext, privkey): Decrypts a ciphertext with the RSA private key.
- Unit tests were written to ensure a message can be successfully encrypted and decrypted. Edge cases, such as invalid UTF-8 sequences, were attempted to ensure errors are properly dealt with.

## What Kind of Inputs Were Used for the Testing?

- Prime Number Generation: Small integers for eratosieve, known prime and composite numbers for millerrabin, and bit lengths for dobigprime.
- Key Generation: Default bit length of 1024 and mock scenarios for edge cases.
- Encryption and Decryption: Example messages, for instance, long strings and special characters, to test the encryption and decryption methods.

## How Can the Tests Be Repeated?

- Ensure you have unittest installed: pip install coverage
- Get into the ProjectCode/Testing folder: export PYTHONPATH=where_the_project_is_downloaded/ProjectCode
- Run the unit tests: cd where_the_project_is_downloaded/ProjectCode/Testing
coverage run --source=./rsa --omit=./rsa/clinterface.py,./rsa/guinterface.py -m unittest discover
- For a covarage report: coverage html
- To view the report: xdg-open htmlcov/index.html

## Presentation of the Empirical Testing Results

### Prime Number Generation
- Sieve of Eratosthenes: Generated primes up to 30 were [2, 3, 5, 7, 11, 13, 17, 19, 23, 29].
- Miller-Rabin Primality Test: Correctly identified primes and composites.
- Large Prime Generation: Successfully generated large primes of specified bit lengths.

### Key Generation
- Generated Keys: Verified that the generated keys satisfy RSA properties.
- Mocked Scenarios: Looked how the code works in edge cases.

### Encryption and Decryption
- Sample Messages: Successfully encrypted and decrypted messages, maintaining data integrity.
- Edge Cases: Properly handled invalid UTF-8 sequences and other edge cases.

### Graphical Representation
The coverage report for the files and the functions are in the Documentation folder.