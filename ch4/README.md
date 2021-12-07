# Ch1. Multi-Currency Money

## Takeaways

### Value Object Pattern
- the values of the instance vars of the object never change once they have been set in the constructor
- aliasing problems: when two instances have the same value, a change in one affects another(a bug)
- all operations must return a new object
- value objects should implement `equals()`

### Triangulation: the third way of implementation
- a rule: we only generalize code when we have two examples or more
- briefly ignore the duplication between test and model code
- Mr.Beck says it is useful when he's not sure of how to refactor:
    it provides a chance to think about the problem from a slightly different direction

### Test Strategy
- fake implmentation: return a constant, and gradually replace it with variables until you have the real code
- write the real code first, if you are obvious in what you're doing

## Personal Summary
