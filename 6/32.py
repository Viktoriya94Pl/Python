n = int(input('Введите количество элементов: '))
minimum = int(input('Введите минимальное значение: '))
maximum = int(input('Введите максимальное значение: '))
my_list = []
for _ in range(n):
    number = (int(input('Введите значения: ')))
    my_list.append(number)
for i in range(len(my_list)):
    if minimum <= my_list[i] <= maximum:
        print(i)