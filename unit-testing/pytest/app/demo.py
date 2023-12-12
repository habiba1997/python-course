def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("divide by zero")
    return a / b


def discount_reason_condition():
    return True