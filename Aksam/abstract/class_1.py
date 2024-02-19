class ABC:
    def __init__(self, name, size):
        self.name = name
        self.size  = size
    
    def size(self):
        print(f"Your size is {self.size}")

slick = ABC("Cyrus", 40)