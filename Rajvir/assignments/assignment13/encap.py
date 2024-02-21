class Shape:
    def __init__(self, base, height):
        self.__area = (base*height)/2
        
    def get_area(self):
        return self.__area

triangle= Shape(2, 4)
print(triangle.get_area())