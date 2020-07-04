class Calculator():

    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def substract(self, num1, num2):
        return (num1 - num2)

    def multiply(self, num1, num2):
         return (num1 * num2)

    def divide(self, num1, num2):
         return (num1 // num2)

calculator = Calculator()

calculator.add(10,5)
calculator.substract(10,5)
calculator.multiply(10,5)
calculator.divide(10,5)