import random

numbers = [1, 2, 3, 4, 5]
print('Оригинальный список: ', numbers)
for i in range(len(numbers)):
    j = random.randint(0, len(numbers) - 1)
    element = numbers.pop(j)
    numbers.append(element)
print("Перемешанный список: ", numbers)