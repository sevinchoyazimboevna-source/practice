'''
OPERATORS AND CONDITIONS:
1 OPERATORS
2 CONDITIONS
3 LOGICAL OPERATORS
'''

print("========Operators============")
# + - > >= < <= * / // % += -= ** == ===

a = 19
b = 5
print(a/b)
result = a // b
left = a % b
print(f"the result: {result} and left: {left}")

# a = a + 100
a += 100
print("a:", a)

print("b", b**2)
print("b", b**3)

print("="*10)

c = dict(name="Angel", age=19)
d = dict(name="Angel", age=19)
e = c
print("c==d", c == d) #only value
print(id(c), id(d), id(e))

data = c is d
print("v", data)
print("c", c is e)

#is reference uchun


print("=============CONDITIONS================")  #truthy vs falsy
x = 50

if x > 50:
    print("case A")
elif x > 10:
    print("case B")
else:
    print("case C")

print("=============Logical operator================")

age = 20
# person = None

# if age > 18:
#     print("adult")
# else:
#     print("child")
# print("person", person)

#Ternary
person = "adult" if age > 17 else "minor"
print(person)

print("++++++++++++++++++++")

is_student = True
is_admin = False
is_guest = True
is_parent = True


if  is_student:
    print("executed")

if  not is_student:
    print("welcomeee")
elif is_admin:
    print("Please go to this office!")
elif is_guest:
    print("Welcome home and be quite and dont touch my personal things and my toys just seat and eat")

# "or" da bir true bolsa true ni oladi agar "and" bolsa bitsa false bolsa falsni aladi





