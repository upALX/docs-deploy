# calculator/calculations.py

def add(a, b) -> float:
    """
    function to sum two float numbers.

        Examples:
            >>> add(4.0, 2.0)
            6.0
            >>> add(4, 2)
            6.0

        Args:
            a (float): first number to sum.
            b (float):  second number to sum.
        Returns:
            float: A number representing the arithmetic sum of `a` and `b`.     
    """
    return float(a + b)

def subtract(a, b) -> float:
    return float(a - b)

def multiply(a, b) -> float:
    return float(a * b)

def divide(a, b) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)