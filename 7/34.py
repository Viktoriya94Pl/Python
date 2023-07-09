def find_vowel(str):
    str = str.split()
    new_list = []
    for word in str:
        summa = 0
        for elem in word:
            if elem in 'а':
                summa += 1
        new_list.append(summa)
    return len(new_list) == new_list.count(new_list[0])

str = 'пара-ра-рам рам-пам-папам па-ра-па-да'

if find_vowel(str):
    print('Парам пам-пам')
else:
    print('Пам парам')