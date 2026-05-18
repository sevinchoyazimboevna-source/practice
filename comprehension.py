'''
COMPREHENSION:
1 WHAT IS COMPREHENSION
2 SET AND DICTIONARY COMP
'''

print("++++++++++++WHAT IS COMPREHENSION+++++++++++++")
#comprehension acts like spread operator:

'''
Comprehension general syntax:
a) *iterable
b) <expression> for item in iterable
c0 <expression> for item in iterable <condition>
'''
#comprehension spread operatori imkoniyatini bizga pyhtonda taqdim etadi

#list comp.
numbers = [1, 2, 4, 7, 1 ,3 ,7,27]
list_numbers = [*numbers] #a version
print(list_numbers)

print("+===2====")

numbers = [1, 2, 4, 7, 1 ,3 ,7,27]
list_numbers = numbers #a version
print(list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))  

print("===========================")

people = [("ANGEL",20), ("KEUN PARK", 37)]
list_people = [person[0] for person in people] #b version

print(list_people)

print("========================")

cars = [
    ("PORSCHE CABRIOLET", 72),
    ("AUDI", 77),
    ("PORSCHE TYCAN",78 ),
    ("PANGE ROVER", 74),
    ("BMW", 57),
    ("MERCI", 58)
]

list_cars = [car[0] for car in cars if car[1] > 70] #c version
print(list_cars)