print('Введите данные:')
s = input()
cnt = 0
s_1 = s[0]
s_new = []

for i in range(len(s)):
    if s[i] == s_1:
        cnt += 1
        s_1 = s[i]
    else:
        s_new += str(cnt) + s[i - 1]
        cnt = 1
        s_1 = s[i]
s_new += str(cnt) + s[-1]
print(''.join(s_new))