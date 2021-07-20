import sys
sys.stdin = open('input.txt')

text = input()
text_len = len(text)

check = input()
check_len = len(check)

result = ''
removed = [0] * 10000000

i = 0
cnt = 0
while (i + check_len) < text_len:
    tmp = ''
    start = i
    while len(tmp) < check_len:
        if not removed[i]:
            tmp += text[i]
            i += 1
        else:
            i += 1
    end = i
    if tmp == check:
        for j in range(start, end):
            removed[j] = 1
        if i != 0:
            i = start - 1
        else:
            i = end
    else:
        result += tmp

if result == '':
    print('FRULA')
else:
    print(result)