class Car:
    car_count = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.car_count += 1

    @classmethod
    def total_cars(cls):
        return cls.car_count

    @staticmethod
    def car_info():
        print("Cars are a popular means of transportation.")


car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Focus")


print("Total cars created:", Car.total_cars())
Car.car_info()
