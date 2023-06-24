N = int(input('Enter the length of the list: '))
my_list = []
for _ in range(N):
    number = (int(input('Enter thr numbers: ')))
    my_list.append(number)
X = int(input('Enter the number you want to compare: '))
closest = my_list[0]
diff = abs (X - my_list[0])
for elem in my_list:
     if abs(X - elem) < diff:
          closest = elem
print(closest)