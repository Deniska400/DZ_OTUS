print('Введите строку текста:')
text = input()
print('Введите ключ кода:')
key = int(input())
text_new = []
big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' # 26 букв
small = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

for i in range(len(text)):
    if text[i] in big:
        letter = big.find(text[i]) # индекс буквы в строке big
        text_new.append(big[letter + key % 27])

    elif text[i] in small:
        if text[i] in small:
            letter = small.find(text[i])  # индекс буквы в строке small
            text_new.append(small[letter + key % 27])
    else:
        text_new.append(text[i])

print(''.join(text_new))