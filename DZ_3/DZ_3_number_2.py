print('Введите дату:')
data = input().split('.')

def check_year():
    return bool(not int(data[2]) % 4 and int(data[2]) % 100 or not int(data[2]) % 400)

def check_months():
    if int(data[1]) in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif int(data[1]) in (4, 6, 9, 11):
        return 30
    else:
        if check_year():
            return 29
        else:
            return 28

def check_data():
    if int(data[0]) <= check_months() and int(data[1]) < 13:
        print(True)
    else:
        print(False)

check_data()