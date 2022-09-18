# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool

str_input="AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool"
str_output=""

file_input=open("5task_input.txt", "a")
file_input.writelines(str_input)
file_input.close()

i=0
while i<len(str_input):
    count=1
    while i+1<len(str_input) and str_input[i] == str_input[i+1]:
        count+=1
        i+=1
    str_output+=str(count)+str_input[i]
    i+=1
print(str_output)

file_output=open("5task_output.txt", "a")
file_output.writelines(str_output)
file_output.close()
