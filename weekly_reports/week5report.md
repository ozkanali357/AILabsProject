# Week 5 Report

## Hours Spent: 12 hours

## What did you do this week?
- Added more comments to be readable.
- Renamed class names to PascalCase naming conventions and file names to snake_case naming conventions.
- Removed trailing whitespaces and divided up lengthy lines for readability.
- Used different commenting conventions for function and details to be readable.
- Improved import system to allow files to be easily runnable.
- Completed peer review 1.
- Written testing document, implementation document, and user guide.
- Made project code get a 10/10 code quality using pylint.

### Peer Review
I cloned the project repository to my laptop. It is the same topic as my project but I went over the project's topic and what it is all about. I went over the project's code and tests in detail to be familiar with every class and method. I tried to run the project and its tests to find bugs. I provided in-depth feedback. This was in the form of improvement proposals, bugs found, and constructive notes. I put up the feedback as a GitHub Issue and referenced it in Labtool.

## How did the project move forward?
The project progressed well this week. The code is of better quality, and documentation is done correctly.

## What did you learn this week?
- Greater knowledge of readability of code and quality.
- Learnt to use pylint for coding conventions and improving code quality.
- Experienced in making in-depth documentation, such as testing documentation, implementation documentation, and user manuals.
- Experienced in performing peer review and providing constructive criticism.

## What was unclear or difficult?
- Ensuring documentation and comments maintain a balance of detail to be informative without using too many words.
- All edge cases handled in the tests and ensuring that the code is pylint compliant.

## Next steps to be done:
- Work towards making the code better and documentation based on any input provided.
- Prepare to submit the project in its final state.

## Questions to Ask/Feedback to TA:
- Would you have advice on improving readability of the code?
- Are there other tests or edge cases you would recommend that I include?

## After the Peer Review Updates
- I added the ctrl a to the gui from the feedback.
- I added a dependency management (Poetry)
- I made it easier for the users to download coverage
- I made the public exponent e fixed when even the condition gcd(e, phi) = 1 isn't met. The program regenerates the prime numbers p and q now.
- I made a difference checker between the generated primes for the case if they are too close.
- I made the generated prime numbers 1024 bits long by setting the most significant bit.
- I put errors in the interfaces if the written messages are too long.
- I changed the formatting of the naming of some files and folders.