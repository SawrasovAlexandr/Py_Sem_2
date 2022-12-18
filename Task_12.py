# Задача 12 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

import random
import time

x = random.randint(1, 1000)
y = random.randint(1, 1000)
sum = x + y
prod = x * y
x = y = 0
print(f'Петя загадал два числа от 1 до 1000. Сумма чисел равна {sum}, произведение чисел равно {prod}')
time.sleep(3)
print('Катя задумалась...')
if sum > 1000: 
    begin = sum - 1000
    end = 1000
else: 
    begin = sum // 2
    end = sum
step = 1
if not (sum % 2):
    step = 2
    if (prod % 2):
        begin = begin // 2 * 2 + 1
    else:
        begin = begin // 2 * 2
for i in range(begin, end, step):
    if (sum - i) == (prod / i):
        x = i
        y = sum - x
        break
time.sleep(3)
print(f'...и решила Петину задачу! Он загадал числа: {x} и {y}')
