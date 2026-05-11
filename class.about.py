'''
CLASS:
1 WHAT IS CLASS
2 ORDINARY VS STATIC PROPERTIES
3 SPECIAL METHODS
'''

print("=========== WHAT IS CLASS=============")
#class- blue print creating!
#structure > state, constructer, method

class Person():
    # state
    message = "Class State Property"

    # constructor state property
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method

    def introduce(self):
        print(f"{self.name} is {self.age}")

    @classmethod
    def explain(args):
        print("static method property executed")


person1 = Person("Angel", 19)
person2 = Person("Dina", 20)
person3 = Person("Kevin", 22)

print(person1.name)  # ordinary state
person1.introduce()  # ordinary method

print(person2.name)
person2.introduce()


print("========= ordinary and static properties ===========")
# static state

print(Person.message)


# static method  class decoraters bilan hosil qilinadi
Person.explain()

print("========= special/magic methods ===========")

# Python's most common used special methods:
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __len__


class Car:
    # state
    description = "This class makes cars"

    # constructor

    def __new__(clc, *args):
        print("* __new__ *")
        return super().__new__(clc)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def start(self):
        print(f"{self.name} started engine")

    def stop(self):
        print(f"{self.name} stopped engine")

    def __str__(self):
        return f"This: {self.name} and was produced in {self.year}"

    def __call__(self, *args, **kwds):
        print("Object is called as a function")
        return True


my_car = Car("porsche", 2025)
my_car.start()
my_car.stop()

your_car = Car("Tayota", 2026)

print(your_car)
your_car()  # execute a sa function we use __call__ method

response = your_car()
print(response)