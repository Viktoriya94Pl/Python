dictionary_eng = {'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т': 1,
    'D, G, Д, К, Л, М, П, У': 2,
    'B, C, M, P, Б, Г, Ё, Ь, Я': 3,
    'F, H, V, W, Y, Й, Ы': 4,
    'K, Ж, З, Х, Ц, Ч': 5,
    'J, X, Ш, Э, Ю': 8,
    'Q, Z, Ф, Щ, Ъ': 10}
word = input('Enter the word: ')
summa = 0
for letter in word.upper():
      for key, value in dictionary_eng.items():
         if letter in key:
             summa += dictionary_eng[key]
print(summa)