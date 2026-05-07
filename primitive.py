print("===========NUMBER===========")
#IN JAVA, VARIABLE IS A NAME STORAGE LOCATION!
#IN PYHTON , VARIABLE IS NAMED REFERENCE!

count = 100
print("count", count)
counti = type(count)
print("911:", counti)
print(f"the count: {count} and type: {counti}")

result1 = count.bit_count()  #method
result2 = count.numerator  #state
print(result1, result2)


print("===========STRING===========")
#METHODS: upper() lower() title() find() replace()

course = "AI Python Fullstack"
result = type(course)
print(f"result1: {result}")

result = course.title()
print(f"result2: {result}")

result = course.upper()
print(f"result3: {result}")

result = course.replace("Fullstack", "MasterClass")
print(f"result4: {result}")

print("===========BOOLEAN===========")

