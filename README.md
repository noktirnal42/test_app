# Calculator Package

A Python calculator package that provides basic and advanced mathematical operations with proper error handling. This package demonstrates test-driven development with comprehensive test coverage and robust error handling for all operations.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Advanced operations (power, square root, absolute value, rounding)
- Comprehensive error handling
- Full test coverage
- Usage examples

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd test_app
   ```

2. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install package in development mode:
   ```bash
   pip install -e .
   ```

## Usage

Basic usage:
```python
from test_app.calculator import Calculator

# Create calculator instance
calc = Calculator(10, 5)

# Basic operations
result = calc.add()        # 15
result = calc.subtract()   # 5
result = calc.multiply()   # 50
result = calc.divide()     # 2.0

# Advanced operations
calc = Calculator(16, 0)
result = calc.square_root()    # 4.0

calc = Calculator(2, 3)
result = calc.power()          # 8

calc = Calculator(-5, 0)
result = calc.absolute_value() # 5

calc = Calculator(3.14159, 2)
result = calc.round_number()   # 3.14
```

See `examples.py` for more detailed examples including error handling.

## Error Handling

The Calculator class includes comprehensive error handling:

- Subtraction: Raises ValueError if first number is smaller than second
- Division: Raises ValueError if dividing by zero
- Power: Raises ValueError if exponent is negative
- Square Root: Raises ValueError if number is negative
- Round: Raises ValueError if decimal places is negative

## Development

### Install development dependencies:
```bash
pip install -r requirements-dev.txt
pip install pytest-cov   # For test coverage reports
```

### Running tests:
```bash
# Run all tests
pytest

# Run tests with detailed output
pytest -v

# Run a specific test file
pytest test_app/tests/test_calculator.py

# Run a specific test class
pytest test_app/tests/test_calculator.py::TestCalculator

# Run a specific test method
pytest test_app/tests/test_calculator.py::TestCalculator::test_add
```

### Test coverage:
```bash
# Generate basic coverage report
pytest --cov=test_app

# Generate detailed HTML coverage report
pytest --cov=test_app --cov-report=html

# Generate XML coverage report (for CI tools)
pytest --cov=test_app --cov-report=xml
```

After generating the HTML coverage report, open `htmlcov/index.html` in your browser to see detailed code coverage information.

## Command Line Interface

The calculator can be used directly from the command line using the `cli.py` script.

### Basic Operations
```bash
./cli.py add 5 3        # 8
./cli.py subtract 10 4  # 6
./cli.py multiply 6 7   # 42
./cli.py divide 20 5    # 4
```

### Advanced Operations
```bash
./cli.py power 2 3         # 8
./cli.py sqrt 16          # 4
./cli.py abs -15         # 15
./cli.py round 3.14159 2  # 3.14
```

### Logarithm Operations
```bash
./cli.py ln 2.718     # 1
./cli.py log10 100    # 2
./cli.py log 8 2      # 3 (log base 2 of 8)
```

### Help and Usage
For detailed help and examples:
```bash
./cli.py -h           # Show general help
./cli.py add -h       # Show help for specific operation
```

All operations include proper error handling and input validation.

## License

MIT License
