row = [[0,1,1,0], [1, 0, 0, 0], [0,1,0,0]]
print('Введите количество билетов:')
quantity = int(input())
cnt = 0

for i in range(len(row)):
    if cnt == quantity:
        break
    else:
        cnt = 0
    for j in range(len(row[i])):
        if row[i][j] == 0:
            cnt += 1
        else:
            cnt = 0
        if cnt == quantity:
            print(i)
            break
if cnt != quantity:
    print('False')