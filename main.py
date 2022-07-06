from collections import Counter
import numpy


# задание 1


line = [1, 1, 4, 4, 7, 12, 10]
counter = dict(Counter(line))
max_repeat = 0
max_list = []
for i in counter:
    if counter[i] == 1:
        continue
    else:
        if counter[i] > max_repeat:
            max_list = []
            max_repeat = counter[i]
            max_list.append(i)
        if counter[i] == max_repeat:
            max_repeat = counter[i]
            max_list.append(i)
max_list = set(max_list)
print(max_list)

# задание 2

menu = '___МЕНЮ___\n1)ввести данные\n2)вывести все введенные данные\n3)выход'
storage = {}
while True:
    print(menu)
    a = input()
    if a == '1':
        print('Введите название товара')
        name = input()
        print('Введите колличество товара')
        qty = input()
        print('Введите стоимость товара')
        price = input()
        storage[name] = [f'колличество:{qty}', f'стоимость:{price}']
    if a == '2':
        print('СПИСОК ТОВАРОВ')
        for key in storage:
            print(key, '->', storage[key])

    if a == '3':
        print('Выхожу')
        break

# задание 2*


line = list(input())
# line = [0, 1, 0, 0, 0, 1, 0]
length = 0
start = 0
maxlength = 0
max_key = 0
index_of_final_length = 0

for i in range(len(line)):
    if line[i] == 0:
        start = i
        length += 1
    else:
        if maxlength < length:
            maxlength = length
            index_of_final_length = i
            start = 0
            length = 0
print(int(numpy.mean([index_of_final_length - maxlength, index_of_final_length-1])))
