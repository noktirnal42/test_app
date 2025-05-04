"""
Calculator module providing basic arithmetic operations with error handling.

This module defines a Calculator class that can perform addition, subtraction, 
multiplication, division, power, square root, absolute value, and rounding operations.
"""

import math

class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    
    Attributes:
        first_number (float): The first operand.
        second_number (float): The second operand.
    """
    
    def __init__(self, first_number, second_number):
        """
        Initialize a Calculator with two numbers.
        
        Args:
            first_number (float): The first operand.
            second_number (float): The second operand.
        """
        self.first_number = first_number
        self.second_number = second_number

    def add(self):
        """
        Add the two numbers.
        
        Returns:
            float: The sum of first_number and second_number.
        """
        return self.first_number + self.second_number

    def subtract(self):
        """
        Subtract second_number from first_number.
        
        Returns:
            float: The result of first_number - second_number.
            
        Raises:
            ValueError: If first_number is smaller than second_number.
        """
        if self.first_number < self.second_number:
            raise ValueError("Subtraction error: First number is smaller than the second number")
        return self.first_number - self.second_number

    def multiply(self):
        """
        Multiply the two numbers.
        
        Returns:
            float: The product of first_number and second_number.
        """
        return self.first_number * self.second_number

    def divide(self):
        """
        Divide first_number by second_number.
        
        Returns:
            float: The result of first_number / second_number.
            
        Raises:
            ValueError: If second_number is zero.
        """
        if self.second_number == 0:
            raise ValueError("Division error: Cannot divide by zero")
        return self.first_number / self.second_number

    def power(self):
        """
        Raise first_number to the power of second_number.
        
        Returns:
            float: The result of first_number ** second_number.
            
        Raises:
            ValueError: If second_number is negative.
        """
        if self.second_number < 0:
            raise ValueError("Power error: Negative exponents are not allowed")
        return self.first_number ** self.second_number
    
    def square_root(self):
        """
        Calculate the square root of first_number.
        
        Returns:
            float: The square root of first_number.
            
        Raises:
            ValueError: If first_number is negative.
        """
        if self.first_number < 0:
            raise ValueError("Square root error: Cannot calculate square root of a negative number")
        return math.sqrt(self.first_number)
    
    def absolute_value(self):
        """
        Calculate the absolute value of first_number.
        
        Returns:
            float: The absolute value of first_number.
        """
        return abs(self.first_number)
    
    def round_number(self):
        """
        Round first_number to second_number decimal places.
        
        Returns:
            float: The rounded value of first_number.
            
        Raises:
            ValueError: If second_number is negative.
        """
        if self.second_number < 0:
            raise ValueError("Rounding error: Number of decimal places cannot be negative")
        return round(self.first_number, int(self.second_number))

    def natural_log(self):
        """
        Calculate the natural logarithm (base e) of first_number.
        
        Returns:
            float: The natural logarithm of first_number.
            
        Raises:
            ValueError: If first_number is less than or equal to zero.
        """
        if self.first_number <= 0:
            raise ValueError("Logarithm error: Natural logarithm is not defined for negative or zero inputs")
        return math.log(self.first_number)
    
    def log10(self):
        """
        Calculate the base 10 logarithm of first_number.
        
        Returns:
            float: The base 10 logarithm of first_number.
            
        Raises:
            ValueError: If first_number is less than or equal to zero.
        """
        if self.first_number <= 0:
            raise ValueError("Logarithm error: Base 10 logarithm is not defined for negative or zero inputs")
        return math.log10(self.first_number)
    
    def log(self):
        """
        Calculate the logarithm of first_number with base second_number.
        
        Returns:
            float: The logarithm of first_number with base second_number.
            
        Raises:
            ValueError: If first_number is less than or equal to zero.
            ValueError: If second_number is less than or equal to zero or equal to 1.
        """
        if self.first_number <= 0:
            raise ValueError("Logarithm error: Logarithm is not defined for negative or zero inputs")
        if self.second_number <= 0:
            raise ValueError("Logarithm error: Base must be positive")
        if self.second_number == 1:
            raise ValueError("Logarithm error: Base cannot be 1")
        
        return math.log(self.first_number, self.second_number)

