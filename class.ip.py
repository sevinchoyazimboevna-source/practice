print("==========Inheritance============")

#means Meros;
# parent class > child 

class Animal:
    description = "THe class creates animals"

    def __init__(self, voice):
        self._status = "Animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):
    

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")

class Cat(Animal):
    

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        print("Yes, I will love you forewer my Angel!")



class Fish(Animal):
    

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim (self):
        print("Yes, I can swim!")


dog = Dog("Reks", "wow", True)
cat = Cat("Tutu", "Miyau", True)
fish = Fish("Nemo", "Zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("================")
dog.make_voice()
fish.make_voice()

print("===================")
print("+++++++++++++++++++")
print(Animal.description)
print(Cat.description)

print("+++++++++++++++++++")
print(dog.voice, fish.voice)
print("status", cat._status)



print("+++++++++++Polymorphism++++++++++++")
dog.make_voice()
fish.make_voice()

print("++++================")
# fish > Fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
result = a and b and c
print(f"the result : {a}")

# Fish > Animal > object
data = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data:", data, data2)