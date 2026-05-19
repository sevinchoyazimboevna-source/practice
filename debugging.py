'''
Packagesw and Debugging:
1 Python Packages and Core Package.
2 Package Manager and External Package.
3 Debugging.
'''
import turtle
print("===========Python Packages and Core Package.============")
# python > package/modul 
# CORE>FILE>EXTERNALL

#CORE PACKAGE

t = turtle.Turtle()
t.shape("turtle") 
t.speed(2)
t.circle(100)

turtle.done()

print("===========")
my_file = open("material/message.txt", "r") #open syntax orqali turli malumotlarni oqishimiz mumkin
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()

#with - context manager - ishimizni yengilashtiradi 
with  open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your file:", your_content)

print("DONE")
