def print_info(data):
    print(' ', *data,' ', sep='\n')


def read_file():
    with open('my_file.txt', 'r') as file:
        data = file.readlines()
    return(data)

def write_file():
    insert = input('Внесите новую запись: ')
    with open('my_file.txt', 'a') as file:
        file.writelines("%s\n" % insert)

def delete_info(insert):
    with open('my_file.txt', 'r') as file:
        lines = file.readlines()
    with open('my_file.txt', 'w') as file:
        for elem in lines:
            if insert not in elem:
                file.write(elem)

def search_info(insert):
    with open('my_file.txt') as file:
        lines = file.readlines()
        for line in lines:
            if insert in line:
                print(' ')
                print(*line.split())
                print(' ')


def change_info(old_data, number, new_data):
    user_lst = []
    with open("my_file.txt", "r") as file:
        lines =file.readlines()
        for line in lines:
            if old_data in line:
                user_lst.append(line)
        print(*user_lst)
    with open("my_file.txt", "w") as file:
        for line in lines:
            if user_lst[number - 1] != line:
                file.write(line)
            else:
                file.write(new_data)
    print("Готово!")


def menu():
    data = read_file()
    while True:
        print('1 - Вывести информацию на экран')
        print('2 - Внести новую запись')
        print('3 - Удалить информацию')
        print('4 - Найти информацию')
        print('5 - Изменить данные')
        print('0 - Выход из программы')
        select = int(input('Вставьте нужную вам цифру: '))
        if select == 0:
            break
        elif select == 1:
            print_info(data)
        elif select == 2:
            write_file()
        elif select == 3:
            insert = input('Укажите фамилию, которую хотите удалить:  ')
            delete_info(insert)
        elif select == 4:
            insert = input('Укажите данные (фамилию) для поиска: ')
            search_info(insert)
        elif select == 5:
            old_data = input("Введите данные (фамилию): ")
            number = int(input("Введите строчку, которую хотите заменить: "))
            new_data = input("Введите новый контакт: ") + "\n"
            change_info(old_data, number, new_data)

    
    

if __name__ == '__main__':
    menu()