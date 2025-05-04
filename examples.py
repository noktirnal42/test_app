#!/usr/bin/env python3
"""
Comprehensive examples for the Scientific Calculator.

This file provides two types of examples:

1. Command Line Interface (CLI) Usage:
   - Basic arithmetic operations (add, subtract, multiply, divide)
   - Advanced operations (power, sqrt, abs, round)
   - Logarithm operations (ln, log10, custom base)
   - Trigonometric functions (in both radians and degrees)
   - Unit conversions (degrees/radians, temperature)

2. Calculator Class Usage:
   - Demonstration of the Calculator class API
   - All calculator methods with proper instantiation
   - Error handling for boundary cases and invalid inputs
   - Proper usage patterns with explanations

Each section includes multiple examples with expected outputs and explanations.
All examples can be run directly to observe the behavior of the calculator.
"""

print("Example usage of the Scientific Calculator CLI:\n")

# Basic Operations
print("# Basic Operations")
print("./cli.py add 5 3                   # Result: 8")
print("./cli.py subtract 10 4             # Result: 6")
print("./cli.py multiply 6 7              # Result: 42")
print("./cli.py divide 20 5               # Result: 4")
print()

# Advanced Operations
print("# Advanced Operations")
print("./cli.py power 2 3                 # Result: 8")
print("./cli.py sqrt 16                   # Result: 4")
print("./cli.py abs -15                   # Result: 15")
print("./cli.py round 3.14159 2           # Result: 3.14")
print()

# Logarithm Operations
print("# Logarithm Operations")
print("./cli.py ln 2.718                  # Result: 1")
print("./cli.py log10 100                 # Result: 2")
print("./cli.py log 8 2                   # Result: 3 (log base 2 of 8)")
print()

# Trigonometric Functions (in radians)
print("# Trigonometric Functions (in radians)")
print("./cli.py trig sin 1.57079          # Result: 1 (sin(π/2))")
print("./cli.py trig cos 3.14159          # Result: -1 (cos(π))")
print("./cli.py trig tan 0.785398         # Result: 1 (tan(π/4))")
print()

# Trigonometric Functions (in degrees)
print("# Trigonometric Functions (in degrees)")
print("./cli.py trig sin 90 --degrees     # Result: 1 (sin(90°))")
print("./cli.py trig cos 180 --degrees    # Result: -1 (cos(180°))")
print("./cli.py trig tan 45 --degrees     # Result: 1 (tan(45°))")
print()

# Unit Conversions
print("# Unit Conversions")
print("./cli.py convert 90 deg rad        # Result: 1.5708 (90° to radians)")
print("./cli.py convert 1.5708 rad deg    # Result: 90 (1.5708 radians to degrees)")
print("./cli.py convert 100 c f           # Result: 212 (100°C to °F)")
print("./cli.py convert 32 f c            # Result: 0 (32°F to °C)")
print()

# Error Handling Examples
print("# Error Handling Examples")
print("./cli.py divide 10 0               # Error: Division error: Cannot divide by zero")
print("./cli.py sqrt -4                   # Error: Square root error: Cannot calculate square root of a negative number")
print("./cli.py trig tan 90 --degrees     # Error: Tangent is undefined at 90 degrees")
print()

# Tips and Tricks
print("# Tips and Tricks")
print("1. For trigonometric functions, use --degrees flag if your input is in degrees")
print("2. Values are displayed with full precision by default")
print("3. The calculator handles negative angles and angles > 360°")
print("4. For tan function, be careful with angles close to 90° or 270° (undefined)")
print("5. Use the -h flag to see help for any operation (e.g., ./cli.py trig -h)")
print()



import math

from test_app.calculator import Calculator

def demonstrate_basic_operations():
    """Demonstrate basic arithmetic operations."""
    print("Basic Operations Examples:")
    print("-" * 50)
    
    # Addition
    calc = Calculator(5, 3)
    result = calc.add()
    print(f"Addition: {calc.first_number} + {calc.second_number} = {result}")
    
    # Subtraction with error handling
    try:
        calc = Calculator(8, 3)
        result = calc.subtract()
        print(f"Subtraction: {calc.first_number} - {calc.second_number} = {result}")
        
        # This will raise an error
        calc = Calculator(3, 8)
        result = calc.subtract()
    except ValueError as e:
        print(f"Subtraction Error Demo: {e}")
    
    # Multiplication
    calc = Calculator(4, 5)
    result = calc.multiply()
    print(f"Multiplication: {calc.first_number} × {calc.second_number} = {result}")
    
    # Division with error handling
    try:
        calc = Calculator(10, 2)
        result = calc.divide()
        print(f"Division: {calc.first_number} ÷ {calc.second_number} = {result}")
        
        # This will raise an error
        calc = Calculator(10, 0)
        result = calc.divide()
    except ValueError as e:
        print(f"Division Error Demo: {e}")

def demonstrate_advanced_operations():
    """Demonstrate advanced mathematical operations."""
    print("\nAdvanced Operations Examples:")
    print("-" * 50)
    
    # Power operation
    try:
        calc = Calculator(2, 3)
        result = calc.power()
        print(f"Power: {calc.first_number} ^ {calc.second_number} = {result}")
        
        # This will raise an error
        calc = Calculator(2, -3)
        result = calc.power()
    except ValueError as e:
        print(f"Power Error Demo: {e}")
    
    # Square root
    try:
        calc = Calculator(16, 0)
        result = calc.square_root()
        print(f"Square Root: √{calc.first_number} = {result}")
        
        # This will raise an error
        calc = Calculator(-4, 0)
        result = calc.square_root()
    except ValueError as e:
        print(f"Square Root Error Demo: {e}")
    
    # Absolute value
    calc = Calculator(-5, 0)
    result = calc.absolute_value()
    print(f"Absolute Value: |{calc.first_number}| = {result}")
    
    # Rounding
    try:
        calc = Calculator(3.14159, 2)
        result = calc.round_number()
        print(f"Round: {calc.first_number} to {calc.second_number} decimal places = {result}")
        
        # This will raise an error
        calc = Calculator(3.14159, -2)
        result = calc.round_number()
    except ValueError as e:
        print(f"Round Error Demo: {e}")


def demonstrate_logarithm_operations():
    """Demonstrate logarithm operations."""
    print("\nLogarithm Operations Examples:")
    print("-" * 50)
    
    # Natural logarithm
    try:
        calc = Calculator(math.e, 0)  # e is Euler's number
        result = calc.natural_log()
        print(f"Natural Log: ln({calc.first_number:.4f}) = {result:.4f}")
        
        # This will raise an error
        calc = Calculator(0, 0)
        result = calc.natural_log()
    except ValueError as e:
        print(f"Natural Log Error Demo: {e}")
    
    # Base 10 logarithm
    try:
        calc = Calculator(100, 0)
        result = calc.log10()
        print(f"Log base 10: log₁₀({calc.first_number}) = {result}")
        
        # This will raise an error
        calc = Calculator(-10, 0)
        result = calc.log10()
    except ValueError as e:
        print(f"Log10 Error Demo: {e}")
    
    # Custom base logarithm
    try:
        calc = Calculator(8, 2)  # log base 2 of 8
        result = calc.log()
        print(f"Log base {calc.second_number}: log₂({calc.first_number}) = {result}")
        
        # This will raise an error
        calc = Calculator(10, 1)  # base 1 is invalid
        result = calc.log()
    except ValueError as e:
        print(f"Custom Log Error Demo: {e}")


if __name__ == "__main__":
    demonstrate_basic_operations()
    demonstrate_advanced_operations()
    demonstrate_logarithm_operations()

