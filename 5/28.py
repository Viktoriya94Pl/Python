def find_sum(a, b):
    if a == 0:
        return b
    return find_sum(a- 1, b + 1)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(find_sum(a, b))