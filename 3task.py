# В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, 
# которые имеют средний балл более «4».

text_read=open("3task_name.txt", "r", encoding="UTF-8")
res_name=""

for line in text_read:
    lines=line.strip().split()
    if int(lines[2])>4:
        lines[0] = lines[0].upper()
    res_name=res_name + lines[0] + " " + lines[1] + " " + lines[2]+ " \n"

    text_res=open("3task_text_res.txt", "w", encoding="UTF-8") 
    text_res.writelines(res_name)
    text_res.close()

text_read.close()
