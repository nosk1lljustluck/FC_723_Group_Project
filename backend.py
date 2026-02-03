# Backend logic for calculator (uses eval)

import math


class CalculatorBackend:
    """
    Backend class:
    - Stores expression
    - Evaluates expression using eval
    - Provides sqrt/square and trig functions (degrees)
    """

    #initialize constructor method to store expression
    def __init__(self):
        self.expression = ""


    # Basic expression handlings

    def add_token(self, token: str) -> str:
        """Add a token (digit/operator) to the expression."""
        self.expression += token
        return self.expression

    def clear(self) :
        """Clear the expression."""
        self.expression = ""
        return self.expression

    def set_expression(self, value):
        """Replace expression with a new value (usually a result)."""
        self.expression = value
        return self.expression

    def evaluate(self):
        """
        Evaluate the current expression with basic operators.
        """
        expr = self.expression.replace("×", "*").replace("÷", "/")
        #replace x with * and ÷ with / for eval to be able to calculate it

        return eval(expr)

    #Scientific operations 

    def sqrt_of(self, value):
        """Square root"""
        return math.sqrt(value)

    def square_of(self, value):
        """Square (x²)"""
        return value ** 2

    def trig(self, func, value):
        """
        Trigonometry:
        sin/cos/tan use degrees input
        asin/acos/atan output degrees
        """
        if func == "sin":
            return math.sin(math.radians(value))
        if func == "cos":
            return math.cos(math.radians(value))
        if func == "tan":
            return math.tan(math.radians(value))
        if func == "asin":
            return math.degrees(math.asin(value))
        if func == "acos":
            return math.degrees(math.acos(value))
        if func == "atan":
            return math.degrees(math.atan(value))

        #raise error if any other trif function is used
        raise ValueError("Unsupported trig function")
