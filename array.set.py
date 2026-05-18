'''
ARRAY SET
1 ARRAY
2 SET
3 SPECIFIC OPERATORS WITH SET
'''

from array import array
numbers = array("i", [1,4,5,7,8,47])

# ARRAY agar raqamlardan ega bolgan ketma 
# ketlikni hosil qilmoqchi bolsak listslar
#  orqali hosil qilish
print(numbers)

# integer hamda float
numbers.append(100)
numbers.insert(0, 14)
print("numbers", numbers)

numbers.remove(5)
numbers.pop()
print(numbers)

del numbers[0:2]
print(numbers)

# katta son bolsa array mashinani kamroq kuchlantirish uchun
# list esa ososnroq sonlar uchun

