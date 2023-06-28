bushes = int(input('Введите количество кустов на грядке: '))
my_list = []
new_list = []
for _ in range(bushes):
    number = (int(input('Введите количество ягод на кустах: ')))
    my_list.append(number)
for elem in range(len(my_list)):
    new_list.append(my_list[elem - 1] + my_list[(elem + 1) % len(my_list)] + my_list[elem])
print("Самое большое количество ягод равно:", max(new_list))
