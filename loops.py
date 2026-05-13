'''
LOOPS:
1 FOR
2 BREAK/ELSE
3 WHILE
'''


print("==========for operators================")
#iterable obj > string dict tuple list range map filter
text = "MIT"
numbs = (19, 9, 3, 7)
car_obj = dict(brand="porsche", year=2027)
range_obj = range(5)

for letter in text:
    print(f"text: {letter}")

print("====================")
for number in numbs:
    print(f"number: {number}")

print("===================")
for x in range_obj:
    print(f"element: {x}")

print("=======================")
for key in car_obj:
    print(f"key: {key} => value: {car_obj.get(key)}")


print("==========break/else=============") 

for x in range(1, 20, 3):
    print(f"x: {x}")
    if x > 10:
        print("good")
        break
    else:
        print("successfully")

print("==========While operators================")
numb = 40
while numb > 0:
    numb -= 10
    print(f"equal: {numb}")

print("+++++++++++++++++++++")
count = 0
while True:
    count += 1
    x = int(input("FInd number"))

    if x == 41:
        print(f"you found {count}")
        break
    else:
        print("wrong")