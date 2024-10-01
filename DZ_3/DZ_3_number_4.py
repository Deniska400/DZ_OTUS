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
    if stop(age):
        print('Программа завершена')
        break
    print('Введите ID:')
    id_people = input()
    if stop(id_people):
        print('Программа завершена')
        break
print(name, surname)
