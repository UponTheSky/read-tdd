# Ch13. Make it

## Takeaways
- ugly parts: public fields(`augend, addend`), two levels of references
    - first, we need to express `Sum` as `Money`, while the currencies are preserved
    - and then, `Bank` would simply return it
    - > anytime we are checking classes explicitly, we should be using polymorphism instead