number = int(input())
rim = []

if number // 1000 > 0: # тысячи
    rim += 'M' * (number // 1000)

if number % 1000 // 100 < 4: # сотни
    rim += 'C' * (number % 1000 // 100)
elif number % 1000 // 100 < 4 == 4:
    rim += 'CD'
elif number % 1000 // 100 == 5:
    rim += 'D'
elif number % 1000 // 100 == 6:
    rim += 'DC'
elif 6 < number % 1000 // 100 < 9:
    rim += 'D' + 'C' * (number % 1000 // 100 - 5)
else:
    rim += 'CM'

if number % 100 // 10 < 4: # десятки
    rim += 'X' * (number % 100 // 10)
elif number % 100 // 10 == 4:
    rim += 'XL'
elif number % 100 // 10 == 5:
    rim += 'L'
elif number % 100 // 10 == 6:
    rim += 'LX'
elif 6 < number % 100 // 10 < 9:
    rim += 'L' + 'X' * (number % 100 // 10 - 5)
else:
    rim += 'XC'

if number % 10 < 4: # единицы
    rim += 'I' * (number % 10)
elif number % 10 == 4:
    rim += 'IV'
elif number % 10 == 5:
    rim += 'V'
elif number % 10 == 6:
    rim += 'VI'
elif 6 < number % 10 < 9:
    rim += 'V' + 'I' * (number % 10 - 5)
else:
    rim += 'IX'

print(''.join(rim))