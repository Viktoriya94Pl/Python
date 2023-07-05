first_number = int(input('Введите первый элемент: '))
step = int(input('Введите разность: '))
n = int(input('Введите количество элементов: '))
my_list = []
for i in range(n):
    my_list.append(first_number + i * step)
print(*my_list, sep='\n')