from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(shape):
    def _ _init(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def _ _ init _ _(self, radius):
        self.radius = radius

    def calculate_area(Self):
        return 3.14 * self.radius * * 2   