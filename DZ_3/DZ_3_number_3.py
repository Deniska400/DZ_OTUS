print('Введите число:')
a = int(input())

def check_simple():
    cnt = 0
    for i in range(1, a + 1):
        if a % i == 0:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False

print(check_simple())