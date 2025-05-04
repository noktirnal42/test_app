#!/usr/bin/env python3
"""
Command-line interface for the Calculator class.

This module provides a CLI interface to access all Calculator functionality
including basic operations, advanced math functions, and logarithms.
"""

import argparse
import math
import sys
from typing import Optional, Tuple

from test_app.calculator import Calculator

def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Calculator CLI - Perform mathematical operations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Basic Operations:
    %(prog)s add 5 3
    %(prog)s subtract 10 4
    %(prog)s multiply 6 7
    %(prog)s divide 20 5

  Advanced Operations:
    %(prog)s power 2 3
    %(prog)s sqrt 16
    %(prog)s abs -15
    %(prog)s round 3.14159 2

  Logarithm Operations:
    %(prog)s ln 2.718
    %(prog)s log10 100
    %(prog)s log 8 2  # log base 2 of 8
        """
    )

    # Create subparsers for different operation types
    subparsers = parser.add_subparsers(dest='operation', help='Operation to perform')

    # Basic Operations
    add_parser = subparsers.add_parser('add', help='Add two numbers')
    add_parser.add_argument('x', type=float, help='First number')
    add_parser.add_argument('y', type=float, help='Second number')

    subtract_parser = subparsers.add_parser('subtract', help='Subtract second number from first')
    subtract_parser.add_argument('x', type=float, help='First number')
    subtract_parser.add_argument('y', type=float, help='Second number')

    multiply_parser = subparsers.add_parser('multiply', help='Multiply two numbers')
    multiply_parser.add_argument('x', type=float, help='First number')
    multiply_parser.add_argument('y', type=float, help='Second number')

    divide_parser = subparsers.add_parser('divide', help='Divide first number by second')
    divide_parser.add_argument('x', type=float, help='First number')
    divide_parser.add_argument('y', type=float, help='Second number')

    # Advanced Operations
    power_parser = subparsers.add_parser('power', help='Raise first number to power of second')
    power_parser.add_argument('x', type=float, help='Base number')
    power_parser.add_argument('y', type=float, help='Exponent')

    sqrt_parser = subparsers.add_parser('sqrt', help='Calculate square root')
    sqrt_parser.add_argument('x', type=float, help='Number to find square root of')

    abs_parser = subparsers.add_parser('abs', help='Calculate absolute value')
    abs_parser.add_argument('x', type=float, help='Number to find absolute value of')

    round_parser = subparsers.add_parser('round', help='Round a number')
    round_parser.add_argument('x', type=float, help='Number to round')
    round_parser.add_argument('y', type=int, help='Number of decimal places')

    # Logarithm Operations
    ln_parser = subparsers.add_parser('ln', help='Calculate natural logarithm')
    ln_parser.add_argument('x', type=float, help='Number to calculate natural log of')

    log10_parser = subparsers.add_parser('log10', help='Calculate base-10 logarithm')
    log10_parser.add_argument('x', type=float, help='Number to calculate log10 of')

    log_parser = subparsers.add_parser('log', help='Calculate logarithm with custom base')
    log_parser.add_argument('x', type=float, help='Number to calculate log of')
    log_parser.add_argument('y', type=float, help='Base of logarithm')

    return parser.parse_args()

def format_result(result: float) -> str:
    """Format the result for display."""
    # Remove trailing zeros for whole numbers
    if result.is_integer():
        return str(int(result))
    # Format floating point numbers nicely
    return f"{result:.6g}"

def main() -> None:
    """Main entry point for the calculator CLI."""
    args = parse_args()
    
    if not args.operation:
        print("Error: No operation specified. Use -h for help.", file=sys.stderr)
        sys.exit(1)

    try:
        # Create calculator with appropriate arguments
        if args.operation in ['sqrt', 'abs', 'ln', 'log10']:
            calc = Calculator(args.x, 0)  # Second argument not used
        else:
            calc = Calculator(args.x, args.y)

        # Execute requested operation
        result = None
        if args.operation == 'add':
            result = calc.add()
        elif args.operation == 'subtract':
            result = calc.subtract()
        elif args.operation == 'multiply':
            result = calc.multiply()
        elif args.operation == 'divide':
            result = calc.divide()
        elif args.operation == 'power':
            result = calc.power()
        elif args.operation == 'sqrt':
            result = calc.square_root()
        elif args.operation == 'abs':
            result = calc.absolute_value()
        elif args.operation == 'round':
            result = calc.round_number()
        elif args.operation == 'ln':
            result = calc.natural_log()
        elif args.operation == 'log10':
            result = calc.log10()
        elif args.operation == 'log':
            result = calc.log()

        print(format_result(result))

    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

