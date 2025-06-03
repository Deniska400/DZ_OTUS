def stop(value):
    if value == '':
        return True

def check_string(value: str):
    while True:
        if value.isalpha():
            value = value.capitalize()
            return value
            break
        elif value == '':
            return ''
            break
        else:
            print('Введите значение повторно')
            value = input()

def check_age(value):
    while True:
        if 17 < int(value) < 61:
            return value
            break
        else:
            print('Введите корректный возраст')
            value = input()

def up_to_8(value):
    if len(value) < 8:
        value = '0' * (8 - len(value)) + str(value)
        return value

def check_id(value):
    while value in storage:
        print('Этот id занят, введите другой')
        value = input()
        if len(value) < 8:
            value = '0' * (8 - len(value)) + str(value)
    return value

def print_dict():
    for key in sorted(storage):
        print(f'{key}:', end=' ')
        for i in sorted(storage[key].items()):
            print(' '.join(i))

storage = {}

while True:
    print('Введите имя:')
    name = input()
    name = check_string(name)
    if stop(name):
        print('Программа завершена')
        break
    print('Введите фамилию:')
    surname = input()
    surname = check_string(surname)
    if stop(surname):
        print('Программа завершена')
        break
    print('Введите возраст:')
    age = input()
    age = check_age(age)

    if stop(age):
        print('Программа завершена')
        break
    print('Введите ID:')
    id_people = input()
    if stop(id_people):
        print('Программа завершена')
        break
    id_people = up_to_8(id_people)
    id_people = check_id(id_people)

    storage[id_people][name] = storage.setdefault(id_people, {}).setdefault(name, '') + str(surname) + ' ' + str(age)

print_dict()
