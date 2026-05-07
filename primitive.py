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