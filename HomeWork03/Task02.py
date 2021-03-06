# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

some_lst = [randint(0, 10) for _ in range(11)]
result = []
for i in range((len(some_lst) + 1) // 2):
    result.append(some_lst[i] * some_lst[len(some_lst) - 1 - i])

print(some_lst)
print(result)
