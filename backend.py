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
        Use round function as there is a precision error in trig functions.
        """
        if func == "sin":
            return round(math.sin(math.radians(value)), 2)
        if func == "cos":
            return round(math.cos(math.radians(value)), 2)
        if func == "tan":
            return round(math.tan(math.radians(value)), 2)
        if func == "asin":
            return round(math.degrees(math.asin(value)), 2)
        if func == "acos":
            return round(math.degrees(math.acos(value)), 2)
        if func == "atan":
            return round(math.degrees(math.atan(value)), 2)

        #raise error if any other trif function is used
        raise ValueError("Unsupported trig function")
