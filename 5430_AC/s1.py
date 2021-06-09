import sys
sys.stdin = open('input.txt')

from collections import deque
T = int(input())

for tc in range(1, T+1):
    p = input()
    n = int(input())
    data = input()
    data = data[1:-1] # 앞뒤 괄호 제거
    data = data.split(',')

    if data[0] != '':
        data = list(map(int, data))
    elif data[0] == '': # 맨 처음 비어있으면
        data.pop()

    data = deque(data)
    reverse = False
    error = False
    for i in range(len(p)):
        if p[i] == 'R':
            # 진짜 뒤집는거보단 인덱스 바꾸기
            if reverse == False:
                reverse = True
            else:
                reverse = False
        elif p[i] == 'D' and data:
            if reverse: # 거꾸로 된 상태라면
                data.pop()
            else: # 원래대로면
                data.popleft()
        else: # 데이터가 비어 있고 D면
            error = True
            break

    if error:
        print('error')
    else:
        data = list(data)
        if reverse == True:
            data = data[::-1]
        data = list(map(str, data))
        data = ','.join(data)
        result = '[' + data + ']'
        print(result)

# 원인1. 빈 배열에 대해 D가 아니라 R일 때도 error가 발생하도록 만들었음