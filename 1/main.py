# number = int(input('Enter any three digit number: '))
# summa = 0
# for i in str(number):
#     summa += int (i)
# print('The result is: ', summa)

# number = int(input('Enter number of cranes: '))
# if(number % 6 == 0 and number % 2 == 0):
#     result1 = number / 6
#     result2 = result1
#     result3 = (result1 + result2) * 2
#     print('Pete has:',round(result1), 'Sergey has:', round(result2), 'Kate has:', round(result3))
# else:
#     print('TRY AGAIN')

# number = input('Enter the number: ')
# sum1 = int(number[0]) + int(number[1]) + int(number[2])
# sum2 = int(number[-1]) + int(number[-2]) + int(number[-3])
# if sum1 == sum2:
#     print('YES')
# else:
#     print('NO')

width = int(input('Enter the width: '))
length = int(input('Enter the length: '))
slices = int(input('How much slices do you need: '))
if slices >= width * length:
    print('Not enough choco')
elif slices % width == 00 or slices % length == 00:
    print("YES")
else:
    print('NO')


