# Week 2 Report

## Hours Spent: 15 hours

## What have you done this week?
This week, I focused on implementing the core functionality of the RSA encryption and decryption project. The following components were developed:
- Created `CLInterface.py` to provide a user-friendly interface for key generation, encryption, and decryption. Users can generate keys, encrypt messages, and decrypt them via the CLI.
- Implemented `Cription.py` with functions for encrypting and decrypting messages using RSA. Handled conversion between strings, bytes, and integers for encryption and decryption.
- Developed `KeyGen.py` to generate public and private keys using large prime numbers. Used the Sieve of Eratosthenes to precompute small primes for efficient divisibility checks.
- Built `PrimeGen.py` to generate large prime numbers using the Miller-Rabin primality test. Optimized the Miller-Rabin test by first checking divisibility against precomputed small primes.

## How has the project progressed?
The project is progressing well, with the core functionality now in place. Users can generate keys, encrypt messages, and decrypt them via the CLI.

## What did you learn this week?
- Gained a deeper understanding of how RSA encryption works, including key generation, modular exponentiation, and the mathematical principles behind it.
- Learned about the Sieve of Eratosthenes and the Miller-Rabin primality test for generating large prime numbers.
- Improved my skills in Python, particularly in handling large integers, byte manipulation, and modular arithmetic.
- Learned how to optimize the Miller-Rabin test by precomputing small primes, significantly reducing computation time.

## What has been unclear or problematic?
- Converting between strings, bytes, and integers for encryption and decryption was initially challenging. I had to carefully handle encoding and decoding to ensure accuracy.
- Understanding the probabilistic nature of the Miller-Rabin test and ensuring its accuracy for large prime numbers required additional research.
- Handling edge cases, such as very short messages or invalid user inputs, is still a work in progress.
- Setting up unit tests and configuring test coverage tools (`coverage` and `pylint`) is a new area for me. However, since I the main functionaliy of the code is mostly done, I will focus on the tests much more in week 3.

## What next?
For the upcoming week, I plan to:
- Write unit tests for all functions to ensure correctness and reliability.
- Set up the `coverage` tool to measure test coverage and identify untested parts of the code.
- Integrate `pylint` to enforce coding standards and improve code quality.
- Write detailed documentation for the codebase and usage instructions.