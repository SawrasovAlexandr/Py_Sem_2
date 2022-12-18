# Задача №11
# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

# Input:     5
# Output:  6

#0 1 1 2 3 5 8 13 21 34 55 89 

import functions as gb

while (a := gb.get_int('Введите число: ')) <= 1:
    print('Введенное число должно быть строго больше 1!')
fibonaci = [0, 1, 1]
counter = 3
while fibonaci[2] < a:
    fibonaci.append(fibonaci[2] + fibonaci[1])
    fibonaci.pop(0)
    counter += 1
    if a == fibonaci[2]: break
else: counter = -1
print(f'Позиция введенного числа в ряду Фибоначи: {counter}')