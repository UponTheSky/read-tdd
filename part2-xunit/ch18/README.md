# Ch18. First Steps to xUnit

## Takeaways
- objective: create a test framework, but how to do it under the context of TDD
without any testing framework?

- step by step: accomplish the list items in the page 91

- refactoring tip: generalize your code by replacing a constant with a variable
(`test_method` => `getattr(self, self.name`))

- remark: we used here a pluggable selector(`getattr`)