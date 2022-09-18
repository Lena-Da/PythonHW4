# Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция. 
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, 
# которая спрашивает ключ, считывает текст и дешифровывает его.


from cgi import test
import checks

step=checks.input_num()

alfavit="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890"
text_shifr=input("Введи текст, который необходимо зашифровать: ")

def secret(step, alfavit):
    result=""
    
    for i in text_shifr:
        letter=alfavit.find(i)
        new_letter=letter+step
        if i in alfavit:
            result+=alfavit[new_letter]
        else:
            result+=i
    print("Зашифрованный текст ", result)
    
    text_res=open("4task_secret_text.txt", "w", encoding="UTF-8")
    text_res.writelines(result)
    text_res.close()

secret(step, alfavit)

def decoding(step):
    input_key=int(input("Введите ключ шифровки: "))
    if input_key == step:
        print (text_shifr)
    else:
        print("Не верный ключ")


decoding(step)
        

