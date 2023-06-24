N = int(input('Enter the length of the list: '))
find_number = int(input('Enter the number you want to count: '))
my_list = []
count = 0
for i in range(N):
    number = (int(input('Enter the number: ')))
    my_list.append(number)
    if find_number == my_list[i]:
        count += 1
print(count)