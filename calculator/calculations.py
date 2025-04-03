# calculator/calculations.py

def add(a, b) -> float:

    return float(a + b)

def subtract(a, b) -> float:
    return float(a - b)

def multiply(a, b) -> float:
    return float(a * b)

def divide(a, b) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)