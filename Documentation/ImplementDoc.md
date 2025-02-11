# Implementation Document

## General Structure of the Program

The project is separated into several files, each responsible for different aspects of the RSA encryption and decryption process:

- KeyGen.py file generates public and private keys using large prime numbers.
- PrimeGen.py file includes functions for generating large prime numbers using the Sieve of Eratosthenes and the Miller-Rabin Primality Test.
- Cription.py file includes functions for encryption and decryption of messages using RSA.
- CLInterface.py file offers a command line interface for key generation, encryption, and decryption.
- GUInterface.py file provides a graphical user interface for key generation, encryption, and decryption.

## Time and Space Complexities

### KeyGen.py
- Time Complexity: $O(\n^3)$ for key generation, where n is the number of bits.
- Space Complexity: $O(n)$.

### PrimeGen.py
- Sieve of Eratosthenes:
  - Time Complexity: $O(n \log \log n)$.
  - Space Complexity: $O(n)$.
- Miller-Rabin Primality Test:
  - Time Complexity: $O(k \\cdot \\log^3 n)$, where $k$ is the number of iterations.
  - Space Complexity: $O(\\log n)$.

### Cription.py
- Modular Exponentiation:
- Time Complexity: $O(\log n)$.
 - Space Complexity: $O(\log n)$.

## Performance and Big O Analysis Comparison

Efficiency in the RSA algorithm depends significantly on prime number generation and modular exponentiation. While the Sieve of Eratosthenes is an efficient method of generating small primes, large primes can be generated with high accuracy by using the Miller-Rabin test. Moreover, modular exponentiation ensures efficient encryption and decryption operations.

## Potential Shortcomings and Suggested Improvements

### Shortcomings
1. Efficiency: There is room for improvement in the efficiency of a number of iterations for the Miller-Rabin test.
2. Error Handling: Even though error handling is done, edge cases may be missed out.
3. UI: The GUI can be made more user-friendly.

### Further Improvements
1. Parallel Processing: Do parallel processing for generating prime numbers so that the performance will increase.
2. Improved Error Handling: Increase the error handling to cater for more edge cases.
3. User Interface Improvements: A better graphical user interface, easier to work with, and more features.

## Utilized Advanced Language Models

GitHub Copilot helped explain confusing areas to me in the topic and to decode errors in the code for this assignment.

## References

- RSA Encryption (https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- Miller-Rabin Primality Test (https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
- Modular Exponentiation (https://en.wikipedia.org/wiki/Modular_exponentiation)