'''
TUPLES:
1 WHAT IS TUPLE: TYPE VS LIST
2 UNPACKING ARGUMENT
3 ZIP
'''
print("===========WHAT IS TUPLE: TYPE VS LIST=============")
#java/php/nodejs array => python list

#literal
numbs = [3,4,7,1]
print(numbs)

#constructer
letter = list("Hello World")
fruits = ["apple", "banana", "kiwi"]
print("before:", fruits)

#tuplle ni ichidaki qiymatni ozgartirib bolmidi
#Tuple
animals = ("cat", "dog", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])

print("===========UNPACKING ARGUMENT==========")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, z, a) = groups
print(f"x: {x} and y: {y}")

people = "Angel"
animals = "Cat"

print(people)
print(animals)

# *args/tuple
def calculate(*args):
    print("args>", args)
    total = 1
    for x in args:
        total *= x
    print(f"type(args): {type(args)}")
    print(f"total value: {total}")
    return total

calculate(1, 7, 12, 1)
print("+++++++++++++++++++++++++")
calculate(0, 7, 3, 19)
print("++++++++++++++++++++")
calculate(5, 7)


#**kwargs > dictionary orqali qurilgan
def introduce(**kwargs):
 print(f"type: {type(kwargs)}")
 print(f" Hi im {kwargs["name"]} and im {kwargs["age"]} years old")
 pass

#call
introduce(name="Angel", age=19)
introduce(name="Javanna", age=20, single=True)


def greeting(*args, **kwargs):
   print("*args>", args)
   print("**kwargs>", kwargs)

#call
greeting("HI", "ASSALOMU ALAYKUM VA RAHMATULLOHU VA BARAKATUH", True, 19, 17)
 