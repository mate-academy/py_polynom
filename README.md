# py_polynom

Create a function that, for given coefficients, returns a function for calculating the value of a polynomial of a given degree. The degree of the polynomial is determined by the number of factors.
For instance:

(1, 2, 3) -> 1 * x * x + 2 * x + 3

To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

To run all style checkers and tests use commands:

`pytest `

`flake8 polynom`

`pylint polynom`

`mypy --ignore-missing-imports .`
