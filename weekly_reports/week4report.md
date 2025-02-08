# Report for Week 4

## Hours Spent: 12 hours

## What have you done this week?
I mostly worked on refining the project to improve its overall quality, particularly based on given feedback.
- I fixed bug related to error handling, handling huge numbers, UTF-8 encoding in CLInterface.py
- I improved input validations by checking the empty input field, key formats, and limiting message length.
- I improved error handling for KeyboardInterrupt and invalid inputs.
- Implemented directory existence checks and file permissions handling in file operations.
- I did the graphical user interface mainly to solve difficulty of copying/pasting large numbers.
- Added more comments and explanations in the code for better understanding.
- I tested inputs such as large numbers, but also smaller numbers. Based on the feedback provided by the professor, I ensured that Miller-Rabin rejects composites with large factors and accepts known primes of the same magnitude.
- I deleted the tests for the interfaces. I updated the test cases with more appropriate inputs.

## How has the project progressed?
The error handling, input validation, and user experience were the parts of the progress. The test coverage tests all algorithms with inputs.

## What did you learn this week?
- Improved my understanding of error handling and input validation in Python.
- Learned to handle large number and UTF-8 decoding problems in RSA encryption and decryption.
- Learned insights about writing tests on cryptographic algorithms.
- Improved skills in enhancing the user experience, making the code more friendly for users.

## What has been unclear or problematic?
- Handling of large numbers and saving/loading them correctly from/to files was a challenge.
- Testing of complete error handling and input validation had to be carefully implemented.
- Maintaining a balance between explanations and code is a little tricky.

## What next?
- Find and fix any issues that might have remained if the code has met project requirements and standards.
- Doing the documentation and user guide for the project.
- Doing the first code review assignment.

## Questions and Feedback to the Course Assistant:
- Are there any other suggestions on how to improve the code? I'm guessing the Code Review assignment can have suggestions I could apply.