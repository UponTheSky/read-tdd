# Ch19. Set the Table

## Takeaways

### How to write a test(3A)?
- Arrange - create some objects(common)
- Act - stimulate them(unique)
- Assert - check the result(unique)

- question: how often do we need to Arrange(generate objects)?
    - performance: want to reduce duplicates
    - isolation: a test may change a commonly used object

- Test coupling is extremely dangerous
    - if not necessary, go with isolation

- A test can be omitted or simplifed iff there are other reliable tests

- if we create independent test objects, then we may simplify our tests
