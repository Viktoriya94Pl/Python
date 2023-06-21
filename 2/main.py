
number = int(input("Enter the number of coins: "))
count = 0
for i in range(number):
    coins = int(input())
    if coins <= 0:
        count += 1
print(count)

summa = int(input("Sum is: "))
product = int(input("Product is: "))
for i in range(summa):
    for j in range(product):
        if summa == i + j and product == i * j:
            print(i, j)

n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1