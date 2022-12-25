# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

def dif_max_min(lst: list[float]) -> float:
    new_list = list(map(lambda i: round(i - int(i), 2), lst))
    return max(new_list) - min(new_list)


a = list(map(float, input("Введите числа через пробел: ").split()))

print(dif_max_min(a))