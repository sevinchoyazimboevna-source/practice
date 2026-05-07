'''
FUNCTIONS:
1 DEFINE VS CALL
2 PARAMETR VS ARGUMENT
3 KEYWORD VS DEFAULT ARGUMENTS
4 SCOPE
'''

print("===========DEFINE VA CALL==============")
#built in function > print() type()
#function - reusable block of code!
#instead of block {} in JAVA , Python users indentation!

#DEFINE - parametr
def greet(a):
    print(f"how do you do: {a}")


def greeting(b):
    print("greeting:")
    return f"hi {b}"

#CALL - execute - argument
result1 = greet('Angel') 
print("result1", result1)

result2 = greeting("Mother")
print("result2", result2)

