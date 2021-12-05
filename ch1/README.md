# Ch1. Multi-Currency Money

## Takeaways

### The Work Cycle
1. Add a little test
2. Run all tests and fail
3. Make a little change
4. Run the tests and succeed
5. Refactor to remove duplication

### Failure is a progress
- Writing a test has the following meaning:
    - Turning an abstract task into a measurable quantity
    - This makes our task much simpler

### Dependency and Duplication
- The code is depending on the tests
    - we want to add tests without changing the code
- the answer is: reduce duplication

### TDD is about being able to take a small step
- Try first! You'll never be able to take a small step if you only take large ones

## Personal Summary
- First, you need to have a mind of a client
    - For a specific functionality or API itself, you need to have in your mind  
    what this functionality has to meet

- After then, even if you have no class, method, or whatever, just write a test
    - Surely there would be compile errors, but you need to write a test first
    - To pass the test, now then you write your classes and methods

- When we pass all the test, then refactor the code
    - reduce duplication: replace constants with variables

- Test itself works as a documentation