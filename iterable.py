print("==========ITERABLE OBJECTS & RANGE==========")

range_obj = range(3)
print("range_obj:", range_obj)

for letter in "MIT":
    print(f"the letter: {letter}")
for ele in range_obj:
    print(f"the element: {ele}")

print("============DICTIONARY==============")
#this is json obj
person = {"name": "Angel", "age": 19, "single": True}
person_obj = dict(name="Angel", age=19, single=True)
print(f"person: {person}")
print(f"person_obj: {person_obj}")

#method get
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 77.000)
print(f"name: {name}, hobby: {hobby}, balance: {balance}")

del person_obj["single"]
for key in person_obj:
    print(f"key: {key}, > value {person_obj.get(key)}")