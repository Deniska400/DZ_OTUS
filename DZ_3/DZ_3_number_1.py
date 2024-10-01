print('Введите строку')
text = input()

def check_text():
    if text[0] == text.lower()[0]:
        a = text.split('_')
        text_1 = ''
        for i in range(len(a)):
            text_1 += str(a[i]).capitalize()
        print(text_1)
    else:
        text_1 = ''
        a, b = 0, 0
        for i in range(1, len(text)):
            if text[i] == text[i].upper():
                b = i
                text_1 += text[a:b] + ' '
                a = b
        text_1 += text[b::]
        text_1 = text_1.lower()
        text_1 = text_1.split(' ')
        print('_'.join(text_1))

check_text()