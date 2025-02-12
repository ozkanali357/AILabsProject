# Implementation Document

## Overall Structure of the Program

- The large prime generation methods via Sieve of Eratosthenes and Miller-Rabin Primality Test are in file primegen.py.
- The file keygen.py is used to generate keys via large prime numbers.
- The file cription.py has methods to message encryption and decryption via RSA.
- The file clinterface.py is a command line interface to generate keys, encrypt, and decrypt.
- The file guinterface.py is a graphical user interface to generate keys, encrypt, and decrypt.

## Time and Space Complexities

### keygen.py
- Time Complexity: \(O(n^3)\) to generate keys, \(n\) is number of bits.
- Space Complexity: \(O(n)\).

### primegen.py
- Sieve of Eratosthenes:
- Time Complexity: \(O(n \log \log n)\).
- Space Complexity: \(O(n)\).
- Miller-Rabin Primality Test:
- Time Complexity: \(O(k \cdot \log^3 n)\), \(k\) is iteration count.
- Space Complexity: \(O(\log n)\).

### cription.py
- Modular Exponentiation:
- Time Complexity: \(O(\log n)\).
- Space Complexity: \(O(\log n)\).

## Comparison of Efficiency of RSA Algorithm using Big O Analysis

The generation of large primes and modular exponentiation highly impact the efficiency of RSA algorithm. Although Sieve of Eratosthenes is a wonderful method to generate small primes, large primes can be generated to high precision via Miller-Rabin test. Modular exponentiation also results in efficient methods of encryption and decryption.

## Potential Weaknesses and Recommended Improvements

### Weaknesses
- I feel that I can set the number of Miller-Rabin test iterations to be more efficient.
- I've added error handling in my program but possibly not to all possibilities.
- I can also make my GUI more intuitive to use.

### Improvements in the Future
- I can apply parallel processing to generate primes to get a better response.
- I can also enhance error handling to more possibilities.
- I can design a more intuitive graphical user interface that is stronger.

## Used Advanced Language Models

I used GitHub Copilot to help to make hard to read parts of the subject more readable and to decode bugs in code.

## References

- RSA Encryption (https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- Miller-Rabin Primality Test (https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test