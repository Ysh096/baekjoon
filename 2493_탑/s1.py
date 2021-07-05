# 500,000개의 이중 루프 => 시간초과

import sys
sys.stdin = open('input.txt')

N = int(input())
towers = list(map(int, input().split()))
answer = [0]*N
for i in range(len(towers)-1, 0, -1):
    for j in range(i-1, 0, -1):
        if towers[i] < towers[j]:
            answer[i] = j+1
            break

print(*answer)