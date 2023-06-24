# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input('Enter any three digit number: '))
summa = 0
for i in str(number):
    summa += int (i)
print('The result is: ', summa)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

number = int(input('Enter number of cranes: '))
if(number % 6 == 0 and number % 2 == 0):
    result1 = number // 6
    result2 = result1
    result3 = (result1 + result2) * 2
    print('Pete has:',(result1), 'Sergey has:', (result2), 'Kate has:', (result3))
else:
    print('TRY AGAIN')

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

number = input('Enter the number: ')
sum1 = int(number[0]) + int(number[1]) + int(number[2])
sum2 = int(number[-1]) + int(number[-2]) + int(number[-3])
if sum1 == sum2:
    print('YES')
else:
    print('NO')


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

width = int(input('Enter the width: '))
length = int(input('Enter the length: '))
slices = int(input('How much slices do you need: '))
if slices >= width * length:
    print('Not enough choco')
elif slices % width == 0 or slices % length == 0:
    print("YES")
else:
    print('NO')


