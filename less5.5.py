import os
os.system('cls')

def encode_file(my_text):  
    str_code = ''
    count = 1       
    for i in range(len(my_text)):
        if i < len(my_text)-1:
            if my_text[i] == my_text[i + 1]:
                count += 1
            else:
                str_code += str(count) + my_text[i]
                count = 1
        else:
            str_code += str(count) + my_text[i]
    return str_code

def decode_file(strc):
    count = ''
    result = ''
    for i in strc:
        if i.isdigit():
            count += i
        else:
            result += i * int(count)
            count = ''
    return result

text = input("Текст для кодировки: ")
print(f'Текст: \n{text}')
with open('task.txt', 'w') as data:
    data.write(text)

with open('task.txt', 'r') as data:
    my_text = data.read()

strc = encode_file(my_text)
print(f'Закодированный текст: \n{strc}') 

with open('task.txt', 'w') as data:
    data.write(strc)

with open('task.txt', 'r') as data:
    my_text = data.read()

total = decode_file(my_text)
print(f'Текст после дешифровки: \n{total}') 

with open('task.txt', 'w') as data:
    data.write(total)