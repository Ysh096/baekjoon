import sys
sys.stdin = open('input.txt')

N = int(input())
towers = list(map(int, input().split()))
answer = [0]*N
L = len(towers)
i = L-1 # 포인터
j = L-2 # 포인터2
tmp = towers[i]
while i >= 0:
    if tmp <= towers[j]:
        for k in range(j+1, i+1):
            answer[k] = j+1
        i -= 1
        j -= 1
        tmp = towers[i]
    elif tmp > towers[j]:
        j -= 1

        if j == -1:
            answer[i] = 0
            i -= 1
            j = i-1
            tmp = towers[i]

print(*answer)