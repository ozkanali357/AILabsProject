# Week 2 Report

## Hours Spent: 15 hours

## What have you done this week?
Core Implementation of the RSA encryption and decryption project was done this week. The following components were developed:
- Created CLInterface.py that provides a user-friendly interface for key generation, encryption, and decryption.
- Implemented Cription.py that contains functions to encrypt and decrypt messages using RSA. Handled the conversion of strings to bytes and further to integers and vice-versa in encryption and decryption, respectively.
- Wrote KeyGen.py to generate public and private keys using large prime numbers. Precomputed small primes by using the Sieve of Eratosthenes for efficient divisibility checks.
- Built PrimeGen.py to generate large prime numbers using the Miller-Rabin primality test. Optimized the Miller-Rabin test by first performing divisibility against precomputed small primes.

## How has the project progressed?
The project is coming on well; the core functionality is now in place. Users can generate keys, encrypt messages, and decrypt them via the CLI.

## What did you learn this week?
- How RSA encryption works-including key generation, modular exponentiation, and the mathematics behind it.
- Learned about the Sieve of Eratosthenes and Miller-Rabin for large prime number generation.
- Improved my skills in Python, like working with large integers, byte manipulations and modular arithmetic.
- Pre-computation of small primes in the Miller-Rabin test, optimized it and reduced computation time.

## What has been unclear or problematic?
- String to bytes to integer back to string conversions at the time of encryption and decryption were quite confusing. I had to really pay closer attention while encoding and decoding.
- The probabilistic nature of the Miller-Rabin test called for more research to ensure it would return correctly for large prime numbers. 
- Cases such as very short messages or invalid user input are yet to be handled.
- Unit tests and setting up test coverage tools is something quite new for me, so regarding the tests, I will focus way more on them in week 3 since the main functionality of the code is mostly done.

## What next?
During the next week I'm going to:
- Write unit tests for all functions on correctness to make them reliable.
- Configure the coverage tool to measure test coverage and locate untested parts of the code. 
- Add pylint for maintaining standards of coding for improved quality. 
- Provide documentation for all codebases on how to use them.