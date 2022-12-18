# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import functions as gb

while (n := gb.get_int('Введите число: ')) <= 0:
    print('Введенное число должно быть положительным')
print(f'Степени двойки не превосходящие {n}: ', end = '')    
deegree = 1
while n >= deegree:
    print(deegree, end = ' ')
    deegree *= 2