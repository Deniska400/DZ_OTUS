a = {}

while True:
    print('Введите предмет:')
    lesson = input()
    if lesson == '':
        print('Оценки внесены')
        break
    print('Введите фамилию ученика:')
    name = input()
    print('Введите оценку:')
    gross = input()
    a[lesson][name] = a.setdefault(lesson, {}).setdefault(name, '') + str(gross) + ' '
for key in sorted(a):
    print(f'{key}:')
    for i in sorted(a[key].items()):
        print(' '.join(i))