
# возвращает True если строка number является числом, иначе False
def is_number(number):
    digit = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    temp = list(number)
    if temp[0] in ('+','-'): temp.pop(0)
    if temp == []: return False
    for i in range(0, len(temp) - 1):
        if temp[i] == '.':
            temp.pop(i)
            break
    if len(temp) == 1:
        if not (temp[0] in digit): return False
    else:
        for i in range(0, len(temp)):
            if  not (temp[i] in digit): return False
    return True

# принимает ввод с клавиатуры и проверяет является ли введенное выражение числом, если не является 
# просит повторить ввод, если является преобразует в int или float и возвращает значение   
def get_number(text):
    while not is_number(temp := input(text)): 
        print('Введенное выражение не является числом. Повторите ввод: ')
    if float(temp) == int(float(temp)):
        return int(float(temp))
    else: return float(temp)

# принимает ввод с клавиатуры и проверяет является ли введенное выражение числом, если не является 
# просит повторить ввод, если является преобразует в int и возвращает значение
def get_int(text):
    while not is_number(temp := input(text)):
        print('Введенное выражение не является целым числом. Повторите ввод: ')
    return int(float(temp))

# принимает ввод с клавиатуры и проверяет является ли введенное выражение числом, если не является 
# просит повторить ввод, если является преобразует float и возвращает значение
def get_float(text):
    while not is_number(temp := input(text)): 
        print('Введенное выражение не является действительным числом. Повторите ввод: ')
    return float(temp)

