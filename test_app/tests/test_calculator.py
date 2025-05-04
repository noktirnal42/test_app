"""
Test suite for the Calculator class.

This module contains tests for all calculator operations including
error cases and edge cases.
"""

import math

import pytest

from test_app.calculator import Calculator

class TestCalculator:
    """Test cases for the Calculator class."""
    
    def test_add(self):
        """Test the add method with positive and negative numbers."""
        # Test with positive numbers
        calc = Calculator(5, 3)
        assert calc.add() == 8
        
        # Test with negative numbers
        calc = Calculator(-5, -3)
        assert calc.add() == -8
        
        # Test with mixed numbers
        calc = Calculator(-5, 8)
        assert calc.add() == 3
        
        # Test with zero
        calc = Calculator(0, 10)
        assert calc.add() == 10
    
    def test_subtract(self):
        """Test the subtract method with valid inputs."""
        # Test normal subtraction
        calc = Calculator(8, 3)
        assert calc.subtract() == 5
        
        # Test with zero
        calc = Calculator(10, 0)
        assert calc.subtract() == 10
    
    def test_subtract_error(self):
        """Test that subtract raises ValueError when first number is smaller."""
        # Test error case
        calc = Calculator(3, 8)
        with pytest.raises(ValueError, match="Subtraction error"):
            calc.subtract()
    
    def test_multiply(self):
        """Test the multiply method with various inputs."""
        # Test with positive numbers
        calc = Calculator(4, 5)
        assert calc.multiply() == 20
        
        # Test with negative numbers
        calc = Calculator(-4, 5)
        assert calc.multiply() == -20
        
        # Test with zero
        calc = Calculator(0, 5)
        assert calc.multiply() == 0
    
    def test_divide(self):
        """Test the divide method with valid inputs."""
        # Test normal division
        calc = Calculator(10, 2)
        assert calc.divide() == 5
        
        # Test with negative numbers
        calc = Calculator(-10, 2)
        assert calc.divide() == -5
        
        # Test that returns float for non-integer division
        calc = Calculator(5, 2)
        assert calc.divide() == 2.5
    
    def test_divide_error(self):
        """Test that divide raises ValueError when dividing by zero."""
        # Test division by zero
        calc = Calculator(10, 0)
        with pytest.raises(ValueError, match="Division error"):
            calc.divide()
    
    def test_power(self):
        """Test the power method with valid inputs."""
        # Test with positive base and exponent
        calc = Calculator(2, 3)
        assert calc.power() == 8
        
        # Test with base of 1
        calc = Calculator(1, 5)
        assert calc.power() == 1
        
        # Test with exponent of 0
        calc = Calculator(5, 0)
        assert calc.power() == 1
        
        # Test with exponent of 1
        calc = Calculator(5, 1)
        assert calc.power() == 5
        
        # Test with fractional result
        calc = Calculator(4, 0.5)
        assert calc.power() == 2.0
    
    def test_power_error(self):
        """Test that power raises ValueError when exponent is negative."""
        # Test with negative exponent
        calc = Calculator(2, -3)
        with pytest.raises(ValueError, match="Power error"):
            calc.power()

    def test_square_root(self):
        """Test the square_root method with valid inputs."""
        # Test with perfect square
        calc = Calculator(9, 0)
        assert calc.square_root() == 3.0
        
        # Test with non-perfect square
        calc = Calculator(2, 0)
        assert calc.square_root() == pytest.approx(1.4142, 0.0001)
        
        # Test with zero
        calc = Calculator(0, 0)
        assert calc.square_root() == 0.0
    
    def test_square_root_error(self):
        """Test that square_root raises ValueError for negative numbers."""
        calc = Calculator(-4, 0)
        with pytest.raises(ValueError, match="Square root error"):
            calc.square_root()
    
    def test_absolute_value(self):
        """Test the absolute_value method."""
        # Test with positive number
        calc = Calculator(5, 0)
        assert calc.absolute_value() == 5
        
        # Test with negative number
        calc = Calculator(-5, 0)
        assert calc.absolute_value() == 5
        
        # Test with zero
        calc = Calculator(0, 0)
        assert calc.absolute_value() == 0
    
    def test_round_number(self):
        """Test the round_number method with valid inputs."""
        # Round to 2 decimal places
        calc = Calculator(3.14159, 2)
        assert calc.round_number() == 3.14
        
        # Round to 0 decimal places (integer)
        calc = Calculator(3.7, 0)
        assert calc.round_number() == 4.0
        
        # Round to 3 decimal places
        calc = Calculator(1.2345678, 3)
        assert calc.round_number() == 1.235
    
    def test_round_number_error(self):
        """Test that round_number raises ValueError for negative decimal places."""
        calc = Calculator(3.14, -2)
        with pytest.raises(ValueError, match="Rounding error"):
            calc.round_number()
    
    def test_natural_log(self):
        """Test the natural_log method with valid inputs."""
        # Test with e (result should be 1)
        calc = Calculator(math.e, 0)
        assert calc.natural_log() == pytest.approx(1.0, 0.0001)
        
        # Test with 1 (result should be 0)
        calc = Calculator(1, 0)
        assert calc.natural_log() == 0.0
        
        # Test with another value
        calc = Calculator(10, 0)
        assert calc.natural_log() == pytest.approx(2.3026, 0.0001)
    
    def test_natural_log_error(self):
        """Test that natural_log raises ValueError for invalid inputs."""
        # Test with zero
        calc = Calculator(0, 0)
        with pytest.raises(ValueError, match="Logarithm error"):
            calc.natural_log()
        
        # Test with negative number
        calc = Calculator(-5, 0)
        with pytest.raises(ValueError, match="Logarithm error"):
            calc.natural_log()
    
    def test_log10(self):
        """Test the log10 method with valid inputs."""
        # Test with 10 (result should be 1)
        calc = Calculator(10, 0)
        assert calc.log10() == 1.0
        
        # Test with 100 (result should be 2)
        calc = Calculator(100, 0)
        assert calc.log10() == 2.0
        
        # Test with 1 (result should be 0)
        calc = Calculator(1, 0)
        assert calc.log10() == 0.0
        
        # Test with another value
        calc = Calculator(5, 0)
        assert calc.log10() == pytest.approx(0.699, 0.001)
    
    def test_log10_error(self):
        """Test that log10 raises ValueError for invalid inputs."""
        # Test with zero
        calc = Calculator(0, 0)
        with pytest.raises(ValueError, match="Logarithm error"):
            calc.log10()
        
        # Test with negative number
        calc = Calculator(-5, 0)
        with pytest.raises(ValueError, match="Logarithm error"):
            calc.log10()
    
    def test_log(self):
        """Test the log method with valid inputs."""
        # Test with custom base (2)
        calc = Calculator(8, 2)
        assert calc.log() == 3.0
        
        # Test with custom base (3)
        calc = Calculator(27, 3)
        assert calc.log() == 3.0
        
        # Test with base 10
        calc = Calculator(100, 10)
        assert calc.log() == 2.0
        
        # Test with 1 as first_number (should be 0 for any base)
        calc = Calculator(1, 5)
        assert calc.log() == 0.0
    
    def test_log_error(self):
        """Test that log raises ValueError for invalid inputs."""
        # Test with zero as first_number
        calc = Calculator(0, 10)
        with pytest.raises(ValueError, match="Logarithm error"):
            calc.log()
        
        # Test with negative first_number
        calc = Calculator(-5, 10)
        with pytest.raises(ValueError, match="Logarithm error"):
            calc.log()
        
        # Test with zero as base
        calc = Calculator(10, 0)
        with pytest.raises(ValueError, match="Logarithm error"):
            calc.log()
        
        # Test with negative base
        calc = Calculator(10, -2)
        with pytest.raises(ValueError, match="Logarithm error"):
            calc.log()
        
        # Test with base 1 (undefined)
        calc = Calculator(10, 1)
        with pytest.raises(ValueError, match="Logarithm error"):
            calc.log()

