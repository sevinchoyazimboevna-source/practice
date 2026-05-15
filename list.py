'''
LIST:
1 WORKING WITH LISTS
2 LIST METHODS
3 LAMBDA FUNCTION
4 ENUMARATE, MAP AND FILTER
'''

print("========WORKING WITH LISTS=========")
#literal
person = {"name": "Angel", "age": 19} #dictionary
people = ("Angel", "JAvanna", "CAt") #tuple
groups = ["Mit", "flexy", "devex"] #list
for team in groups:
    print(f"team: {team}")

#constructor 
letter = list("Hello World")
print(f"letter: {letter} and size: {len(letter)}")

print("+++++++++++++++++++++++++")
fruits = ["apple", "orange", "lemon", "liwi"]
a = fruits[0]
b = fruits[0:2]
c = fruits[::3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d) 

print("==========LIST METHODS===========")
#methods> append() insert() pop() remove() clear() sort() // mutable 
# index() //unmutable

letters = ["a", "b", "c"]

letters.append("d") #add behind
print(f"append: {letters}")

letters.insert(0, "z") # add front
print(f"insert: {letters}")

size = len(letters) -1
result1 = letters.pop(size) # - behind
print(f"result1: {result1} and lettera: {letters}")

result2 = letters.pop(0) #pop front
print(f"pop3: {result2} and letter: {letters}")

print("+++++++++++++++++++++++++++++++")
animals = ["cat", "dog", "capybara", "cheburashka", "krokodil"]
print("animals:", animals)

animals.remove("dog")
print("remove:", animals)

del animals[2:4]
print("delete:", animals)

exist = animals.index("cat")
print("index", exist)

animals.clear()
print("clear:", animals)

if "cat" in animals:
    print("yes:", animals.index("cat"))
else:
    print("cat opsoyo:")

print("=================")

gena = [2,4,7,27,12]
gena.sort()
print("numbers:", gena) #tartiblab yozish
gena.sort(reverse=True)
print("reverse:", gena) #balandan pasga


#inmutable sorted

numbs = [2, 17, 27, 39, 7]
new_numbs = sorted(numbs)
print(f"numbs: {numbs} and {new_numbs}")