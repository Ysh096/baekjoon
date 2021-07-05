import sys
sys.stdin = open('input.txt')

# 검색 기능 구현
# 패턴 P가 텍스트 T에서 어느 위치에 몇 번 나타나는가?
def pi(pattern):
    L = len(pattern)
    array = [0] * L
    if L == 0:
        return array
    i = 0
    j = 1
    cnt = 0
    while j < L:
        if pattern[i] == pattern[j]:
            cnt += 1
            array[j] = cnt
            i += 1
            j += 1
        else:
            i = 0
            j += 1
            cnt = 0
    return array

def KMP(text, pattern):
    result = []
    array = pi(pattern)
    j = 0
    for i in range(len(text)):
        if text[i] == pattern[j]:
            if j == len(pattern)-1:
                result.append(i-j+1)
                j = array[j]
            j += 1
        else:
            if j != 0:
                j = array[j-1]

    return result

T = input()
P = input()

result = KMP(T, P)
print(len(result))
print(*result)