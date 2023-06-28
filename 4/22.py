n = int(input('Введите количество элементов первого множества: '))
list1 = []
for _ in range(n):
    numbers_list1 = (int(input('Введите числа: ')))
    list1.append(numbers_list1)
    set1 = set(list1)
m = int(input('Введите количество элементов первого множества: '))
list2 = []
for _ in range(m):
    numbers_list2 = (int(input('Введите числа: ')))
    list2.append(numbers_list2)
    set2 = set(list2)
print(set1.union(set2))