class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Example usage
if __name__ == "__main__":
    car1 = Car("Toyota", "Camry", 2020)
    car2 = Car("Honda", "Accord", 2021)

    print(car1.display_info())
    print(car2.display_info())