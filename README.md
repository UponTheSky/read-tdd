# read-tdd
- Read Test-Driven Development By Example written by Kent Beck
- This repository is for summary and actual test-writing of his messages. 
- Many part of this book is written in Java, but for our own situation, we'll use Python for exercise

## Requirements
- Good to have your own virtual environment
    - there are tons of libraries for this for Python
    - but in my case I prefer [miniconda](https://docs.conda.io/en/latest/miniconda.html) for its easy usability

- Clone this repo, but you don't need to install any extra library
    - as you can see, we'll use [Unittest](https://docs.python.org/3/library/unittest.html) since it is what Django uses
    - however, as we read through the chapters of the book, this requirements above might change

## Use Unittest Library
- Basically, we follow [the official docs](https://docs.python.org/3/library/unittest.html)

## Code Documentation
- The README.md part is for summarizing the book contents
- The ~.py files are the examples used in the book: this would follow [the Numpy style](https://numpydoc.readthedocs.io/en/latest/format.html)
- THe test_~.py files are for the test: this would just follow the format of the book

## Linting, Prettier
- Linting: Possibly Pylint
    - https://code.visualstudio.com/docs/python/linting#_pylint
- Prettier: Possibly [black](https://github.com/psf/black)
