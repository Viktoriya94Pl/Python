def find_vowel (word):
    vowel = {'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю'}
    return len(list(filter(lambda x: x in vowel, word)))

screamer = input('Введите кричалку: ')

if len(set(map(find_vowel, screamer.split()))) == 1:
    print(set(screamer))
    print('Парам пам-пам')
else:
    print('Пам парам')