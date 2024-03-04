from abc import ABC, abstractmethod
import cmath

class SquareRootCalculator(ABC):
    @abstractmethod
    def calculate_square_root(self, num):
        pass

class DefaultSquareRootCalculator(SquareRootCalculator):
    def calculate_square_root(self, num):
        if num < 0:
            return cmath.sqrt(num)
        else:
            return num ** 0.5

# Example usage
calculator = DefaultSquareRootCalculator()
result = calculator.calculate_square_root(-4)
print("Square root of -2:", result)