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


