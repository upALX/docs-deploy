# calculator/calculations.py
from typing import Union

def add(a: Union[float, int], b: Union[float, int]) -> float:
    """sum two float numbers.

        Examples:
            >>> add(4.0, 2.0)
            6.0
            >>> add(4, 2)
            6.0

        Args:
            a: first number to sum.
            b:  second number to sum.
        
        Returns:
            float: A number representing the arithmetic sum of `a` and `b`.

    """
    return float(a + b)

def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    """ subtract two numbers.
    
    Examples:
        >>> subtract(4.0, 1.0)
        3.0
        >>> subtract(4, 1)
        3.0

    Args:
        a: first number to subtract.
        b:  second number to subtract.
    Returns:
        float: A number representing the arithmetic subtract of `a` and `b`. 

    """
    return float(a - b)

def multiply(a: Union[float, int], b) -> float:
    """multiply two numbers.
    
        Examples:
            >>> multiply(4.0, 1.0)
            3.0
            >>> multiply(4, 1)
            3.0

        Args:
            a: first number to multiply.
            b:  second number to multiply.
        Returns:
            float: A number representing the arithmetic multiply of `a` and `b`. 

    """
   
    return float(a * b)

def divide(a, b) -> float:
    """ divide two numbers
    
        Examples:
            >>> divide(4.0, 1.0)
            3.0
            >>> divide(4, 1)
            3.0

        Args:
            a: first number to divide.
            b:  second number to divide.
        Returns:
            float: A number representing the arithmetic divide of `a` and `b`. 

    """
     
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)