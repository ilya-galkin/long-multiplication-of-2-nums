# Python 3.8.5

import re

def mul(num_1, num_2):

    ''' Функция для перемножения больших чисел, оперирующая текстовыми строками.
    Основана на алгоритме перемножения "в столбик".
    На вход принимает 2 положительных или отрицательных целых числа любой длины.'''

    # Очищаем input от всех знаков, кроме цифр. 

    n_1 = ''.join(re.findall(r'\d', num_1))
    n_2 = ''.join(re.findall(r'\d', num_2))

    n_1_len = len(n_1)
    n_2_len = len(n_2)

    # Реализуем алгоритм "столбика", записываем лист с получившимися суммами. 

    list_to_add = []
    place = 0
    for n_2_digit in range(n_2_len -1, -1, -1):
        q = ''
        carry = 0
        for n_1_digit in range(n_1_len- 1, -1, -1):
            num2 = int(n_2[n_2_digit])
            num1 = int(n_1[n_1_digit])
            x = (num2 * num1) + carry
            if n_1_digit == 0:
                q = str(x) + q
            else:
                if x > 9:
                    q = str(x % 10) + q
                    carry = x // 10
                else:
                    q = str(x % 10) + q
                    carry = 0
                    num = x % 10
        list_to_add.append(q + '0' * place)
        place += 1

    # Проверяем на наличие отрицательных чисел и возвращаем ответ.

    if (num_1[0] == '-' and num_2[0] != '-') or (num_1[0] != '-' and num_2[0] == '-'): 
        return '-' + add(list_to_add)
    else:
        return add(list_to_add)

def add(list_of_nums):

    ''' Функция для сложения больших чисел, оперирующая текстовыми строками.
    Основана на алгоритме сложения "в столбик".
    На вход принимает список положительных чисел в текстовом формате.'''

    # Уравниваем длины текстовых строк, добавляя нули перед числами.

    lengths = []
    for num in list_of_nums:
        lengths.append(len(num))
    max_lenght = max(lengths)
    nums_with_zeros = []
    for num in list_of_nums:
        while len(num) < max_lenght:
            num = '0' + num
        nums_with_zeros.append(num)

    # Трансформируем данные - добавляем списками цифры одного разряда.

    set_of_nums = []
    for i in range(max_lenght):
        nums_to_sum = []
        for num in nums_with_zeros:
            nums_to_sum.append(int(num[-1 - i]))
        set_of_nums.append(nums_to_sum)

    # Складываем числа в "столбик", сохраняя результат в текстовую строку.

    q = ''
    carry = 0
    for set in set_of_nums:
        subsum = sum(set) + carry
        res = int(subsum % 10)
        carry = (subsum - res) / 10
        q = str(res) + q

    return q


# Пример работы функции.

example_number_1 = 99 ** 99
example_number_2 = 99 ** 99
answer = mul(str(example_number_1), str(example_number_2))

print(answer)
print(type(answer))
print(int(answer) == example_number_1 * example_number_2)