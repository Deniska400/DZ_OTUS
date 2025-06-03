print('Введите длину плитки шоколада:')
length = int(input())
print('Введите ширину плитки шоколада:')
width = int(input())
print('Введите размер куска:')
size = int(input())

if size <= length * width and (size % length == 0 or size % width == 0):
    print(True)
else:
    print(False)
