# 9935 문자열 폭발



## 내 풀이(실패)

```python
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
```

골치아파서 포기



## 2. 스택

1) 한 글자씩 스택

2) 현재 스택한 글자가 문자열의 마지막 글자와 일치하면 스택에 폭발문자열이 있는지 확인

3) 있으면 pop하기

```python
text = input()
check = input()

check_len = len(check)

stack = []
for w in text:
    stack.append(w)
    if w == check[-1]:
        if ''.join(stack[-check_len:]) == check:
            for _ in range(check_len):
                stack.pop()
if stack == []:
    print("FRULA")
else:
    print(''.join(stack))
```

524ms