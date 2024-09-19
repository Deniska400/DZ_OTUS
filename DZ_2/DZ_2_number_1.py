print('Введите целое число:')
n = int(input())

while n >=10:
    n_copy = n
    n_new = 0
    while n_copy > 0:
        n_new += n_copy % 10
        n_copy = n_copy // 10
    n = n_new

print(n_new)
