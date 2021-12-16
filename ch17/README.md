# Ch17. Money Retrospective

# What's Next?
- coding, implementation: those never finish
- but then why TDD?: 
    - at least you need to have a solid brick on which you can put on another brick
    - important for a big system

- what tests should be added?
    - a test that should not work: may reveal a limit of your code

- recheck your design
    - naming, DRY

# Metaphor
- `Expression`: better design, cleaner code

# JUnit Usage
- very short time interval between the test runnings

# Code Metrics
- > there are roughly as many lines and functinos in the test and functional code
- although we're keeping the DRY rule, the number of lines of the test and the code would be almost the same
- use polymorphism rather than control flows

# Process
1. Add a little test
2. Run all tests and fail
3. Make a change
4. Run the tests and succeed
5. Refactor to remove duplication

- how many changes does it take to compile, run, and refactor for a single test writing?
    - compile and run: relatively small
    - refactoring: a (probably)skewed bell curve

# Test Quality
- TDD tests cannot replace other types of testing
- However, since we're quite sure the quality of our code at the system level,
we can encourage those high-level tests to concentrate on their own works

- state coverage: 100%
- defect insertion: change the meaning of a line of code and a test should break
