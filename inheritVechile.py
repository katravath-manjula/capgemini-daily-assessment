# 6. Implement a multi-level inheritance example where `Vehicle` is a base class, `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.
class Vehicle:
    def __init__(self, model, color):
        print("This is a vehicle")

class Car(Vehicle):
    def __init__(self, model, color):
        super().__init__(model, color)
        print("This is a car")

class Bike(Vehicle):
    def __init__(self, model, color):
        super().__init__(model, color)
        self.model = model
        self.color = color

    def showB(self):
        print(f"Bike model: {self.model}, color: {self.color}")

    def display_car_info(self):
        print("This is a Bike.")

class ElectricalCar(Car):
    def __init__(self, model, color, year):
        super().__init__(model, color)
        self.year = year
        self.model = model
        self.color = color

    def showFerrari(self):
        print(f"Car model: {self.model}, color: {self.color}, manufactured in year: {self.year}")

    def display_electric_car_details(self):
        print("This is an electric car.")


ob = ElectricalCar("Tesla Model ", "Green", 2023)
ob.showFerrari()
ob2=Bike("maruthi","red")
ob2.showB()
print()
