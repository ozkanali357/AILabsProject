# Implementation Document

## General Structure of the Program

- The primegen.py file has functions for making large prime numbers with the Sieve of Eratosthenes and the Miller-Rabin Primality Test.
- The keygen.py file makes public and private keys with large prime numbers.
- The cription.py file includes functions for encryption and decryption of messages using RSA.
- The clinterface.py file gices a command line interface for key generation, encryption, and decryption.
- The guinterface.py program provides a graphical user interface for key generation, encryption, and decryption.

## Time and Space Complexities

### keygen.py
- Time Complexity: \(O(n^3)\) for key generation, where \(n\) is the number of bits.
- Space Complexity: \(O(n)\).

### primegen.py
- Sieve of Eratosthenes:
- Time Complexity: \(O(n \log \log n)\).
- Space Complexity: \(O(n)\).
- Miller-Rabin Primality Test:
- Time Complexity: \(O(k \cdot \log^3 n)\), \(k\) is the number of iterations.
- Space Complexity: \(O(\log n)\).

### cription.py
- Modular Exponentiation:
- Time Complexity: \(O(\log n)\).
- Space Complexity: \(O(\log n)\).

## Performance and Big O Analysis Comparison

Efficiency of the RSA algorithm relies heavily on prime number generation and modular exponentiation. Although the Sieve of Eratosthenes is an effective way to generate small primes, large primes can be found to a very high precision using the Miller-Rabin test. Modular exponentiation also provides effective encryption and decryption methods.

## Possible Weaknesses and Recommended Improvements

### Weaknesses
- I believe the number of iterations for the Miller-Rabin test can be optimized for better performance.
- I have provided error handling in the code but might have missed some edge cases.
- I can make the GUI more intuitive.

### Future Improvements
- I can use parallel processing to generate prime numbers for better performance.
- I can enhance error handling for more edge cases.
- I can create a more intuitive graphical user interface with more features.

## Used Advanced Language Models

I utilized GitHub Copilot to help make confusing parts of the subject more understandable and decipher code errors.

## References

- RSA Encryption (https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- Miller-Rabin Primality Test (https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
- Modular Exponentiation (https://en.wikipedia.org/wiki/Modular_exponentiation)