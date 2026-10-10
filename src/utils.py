def _validate_operands(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be numbers.")


def add(a, b):
    _validate_operands(a, b)
    return a + b


def subtract(a, b):
    _validate_operands(a, b)
    return a - b


def multiply(a, b):
    _validate_operands(a, b)
    return a * b


def divide(a, b):
    _validate_operands(a, b)
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Add error handling for invalid inputs
