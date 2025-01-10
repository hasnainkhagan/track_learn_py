def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts second number from the first."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """Divides the first number by the second. Handles division by zero."""
    if b == 0:
        return "Division by zero is not allowed."
    return a / b
