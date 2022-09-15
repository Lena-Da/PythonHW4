# Функции для импорта


def input_num():
    """
    Функция проверяет ввод положительного целого числа
    """

    try:
        num=int(input("Введи число: "))
        if num < 0:
            print ("Введи число больше 0")
        return num
    except ValueError:
        print("Ввели не число, попробуй еще")
        return input_num()