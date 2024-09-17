print('Введите количество дней, оставшихся до отпуска:')
day = int(input())

if day >= 7 and day % 7 < 6:
    print(day // 7 * 2)
elif day > 7 and day % 7 == 6:
    print(day // 7 * 2 + 1)
elif 5 < day < 7:
    print(day - 5)
else:
    print(0)
