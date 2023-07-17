#  Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных


def print_info(temp):
    for line in temp:
        print(line.strip())


def read_file():
    with open('my_file.txt', 'r', encoding='utf-8') as file:
        temp = file.readlines()
    return temp


def write_file(data):
    with open('my_file.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)


def append_data(data):
    new_data = input('Введите данные для добавления: ')
    data.append(new_data + '\n')
    return data


def find_data_by_name(data, name):
    found_indices = []
    for i, line in enumerate(data):
        if name.lower() in line.lower():
            found_indices.append(i)
    return found_indices


def print_found_records(data, found_indices):
    if found_indices:
        print('Найденные записи:')
        for idx in found_indices:
            print(f'{idx + 1}. {data[idx].strip()}')
    else:
        print('Записей с указанным именем или фамилией не найдено.')


def edit_data(data):
    name_to_edit = input('Введите имя или фамилию для редактирования: ')
    found_indices = find_data_by_name(data, name_to_edit)

    print_found_records(data, found_indices)

    line_number = int(input('Введите номер записи для редактирования: '))
    if 1 <= line_number <= len(data):
        new_data = input('Введите новые данные: ')
        data[line_number - 1] = new_data + '\n'
        print('Запись успешно отредактирована.')
    else:
        print('Некорректный номер записи.')

def delete_data(data):
    name_to_delete = input('Введите имя или фамилию для удаления: ')
    found_indices = find_data_by_name(data, name_to_delete)
    
    print_found_records(data, found_indices)

    line_number = int(input('Введите номер записи для удаления: '))
    if 1 <= line_number <= len(data):
        deleted_record = data.pop(line_number - 1)
        print(f'Запись "{deleted_record.strip()}" успешно удалена.')
    else:
        print('Некорректный номер записи.')
  

def menu():
    data = read_file()
    while True:
        print('Выберите действие: ')
        print('1 - вывести инфо на экран')
        print('2 - добавить данные')
        print('3 - изменить данные')
        print('4 - удалить данные')
        print('0 - выход из программы')
        n = int(input('ваш выбор: '))
        if n == 0:
            break
        elif n == 1:
            print_info(data)
        elif n == 2:
            data = append_data(data)
        elif n == 3:
            edit_data(data)
        elif n == 4:
            delete_data(data)
        else:
            print('Некорректный выбор. Попробуйте еще раз.')

    write_file(data)

if __name__ == '__main__':
    menu()

