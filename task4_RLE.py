# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from pathlib import Path


path_1 = 'RLE_input.txt'
path_2 = 'RLE_output.txt'

def read_file(path):
    out_string = ''
    res_txt = open(path, 'r')
    out_string = res_txt.read()
    res_txt.close()
    return out_string

def write_file(path, input_string:str):
    res_txt = open(path, 'w')
    res_txt.write(input_string)
    res_txt.close()

def unzip_str(input_str:str):
    unzipped_str = ""
    count = ""
    for char in input_str: 
        if char.isdigit():
            count += char
        else:    
            unzipped_str += char * int(count)
            count = ""

    return unzipped_str

def zip_str(input_str:str): 
    zipped_str = ""
    i = 0
    while i < len(input_str):
        count = 1 
        while i  < len(input_str) - 1 and input_str[i] == input_str[i + 1]:
            count += 1
            i += 1
 
        zipped_str += str(count) + input_str[i]
        i += 1
 
    return zipped_str


# Сжатие данных:
write_file(path_2, zip_str(read_file(path_1)))

# Восстановление данных:
# write_file(path_1, unzip_str(read_file(path_2)))
