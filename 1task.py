# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

import checks

num=checks.input_num()

def result(num):
    """
    Функция ищет простые множители введенного числа
    """

    for i in range(2, num+1):
        if num%i == 0:
            count=1
            for j in range(2,(i//2+1)):
                if(i%j == 0):
                    count=0
                    break
            if(count==1):
                print(i)
result(num)