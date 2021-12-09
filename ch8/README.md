# Ch8. Makin' Objects

## Takeaways
- reduce duplicates(refactoring): `times()`
- but what if we just move upwards `times()` method to `Money` class?
    - then what's the difference btw `Dollar` and `Franc`?
    - we use the __factory__ method

- first, review the tests

- decoupling the tests from the exeistence of the subclass:   
free to change inheritance without affecting any model code

