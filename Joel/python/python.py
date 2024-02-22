class Car:
    def --init--(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.make} {self.model} started.")
        else:
            print(f"{self.make} {self.model} is already running.")

    def stop(self):
        if self.is_running
            print(f"{self.make} {self.model} is already started.")

    def drive(self):
        if self.is_running:
            print(f"{self.make} {self.model} is being driven.")
        else:
            print(f"{self.make} {self.model} needs to be started.")