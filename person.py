class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Ravi", 18)
person2 = Person("Raj", 20)

person1.greet()
person2.greet()
