class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

math_ops = MathOperations()
#print(math_ops.add(2, 3))      # Error: Only the second definition of add() is recognized
print(math_ops.add(2, 3, 4))   # Output: 9