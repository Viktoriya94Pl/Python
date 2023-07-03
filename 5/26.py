def find_pow(number, pow):
    if pow == 1:
        return number
    return (number) * find_pow(number, pow - 1)


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(find_pow(a, b))