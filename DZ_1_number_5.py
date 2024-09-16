a = input()
b = list(a)

if b[0] == '-': # Если есть минус
    b.remove('-')

if '.' in b: # проверяем наличие точки
    b.remove('.')

if ''.join(b).isdigit() and float(a) > 0:
    print('True и положительное')
elif ''.join(b).isdigit() and float(a) < 0:
    print('True и отрицательное')
else:
    print('False')
