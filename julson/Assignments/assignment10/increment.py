class counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1

    def get_value(self):
        return self.value 
    
counter = counter()

counter.increment()
counter.increment()
counter.increment()

print("Current value of the counter :",counter.get_value())