print('Введите пятизначное число')
number = input()

while len(number) != 5:
    print('Введите пятизначное число')
    number = input()

print(number[0], number[3:0:-1], number[4], sep='')
