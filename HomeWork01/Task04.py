# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).


quadrant = int(input('Введите номер квадранта (1-4): '))

if quadrant == 1:
    print('Диапазон: X>0, Y>0')
elif quadrant == 2:
    print('Диапазон: X<0, Y>0')
elif quadrant == 3:
    print('Диапазон: X<0, Y<0')
elif quadrant == 4:
    print('Диапазон: X>0, Y<0')
else:
    print('Неверный ввод.')
