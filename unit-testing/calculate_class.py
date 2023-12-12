class Calculate:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except Exception as e:
            raise ValueError("Division by zero")
