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


# SET
# set of unique collection without keeping order
# index tushunchasi yok
new_numbers = array("i", [1,4,5,7,8,4 ,7 , 5, 47])
numbs_set = set(new_numbers)
print(numbs_set)
# set matigida doyin gulli qavs paydo boladi
# setlarda ketma ketlik mavjud emas

print(f"numbs: {numbs_set} and type: {type(numbs_set)}")

numbs_set.add(200)
print(numbs_set)

numbs_set.add(7)
print(numbs_set)

print("+==============SPECIFIC OPERATORS WITH SET==================")

# | & - ^ 

a = {10, 20, 50}
b = {20, 40}

result1 = a | b #union  #ikkalasida bor bir hil qiymatni faqat bittasinikini  kaytaradi
result1 = a & b #intersection bir hil qiymatni qayataradi
result1 = a - b #difference
result1 = a ^ b #symetric difference bir hil qaytarimagan qiymatni olmay qolganlarni oladi
print(result1)