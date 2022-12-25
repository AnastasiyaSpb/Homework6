# Реализуйте алгоритм перемешивания списка.

import random

a = int(input("Введите количество элементов в списке: "))
list = [random.randint(1, 20) for i in range(a)]
list2 = []

while len(list2) != len(list):
    k = random.choice(list)
    if k not in list2:
        list2.append(k)

print(list)
print(list2)