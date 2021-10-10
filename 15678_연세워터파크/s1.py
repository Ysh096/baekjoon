import sys
sys.stdin = open('input.txt')

# 징검다리 밟기
# 밟은 징검다리에 쓰여진 정수의 합이 가장 큰 사람이 이김

# N개 징검다리, 1부터 N까지 번호가 붙음
# U번 징검다리에서 V번 징검다리로 점프하기 위해서는
# U와 V의 차이가 미리 정해진 값 D 이하여야 한다.
# 어떤 징검다리도 두 번 이상 밟을 수 없다.

# N은 징검다리의 수
# D는 미리 정해진 값
from collections import deque

n, D = map(int, input().split())
stone = list(map(int, input().split()))

dp = [stone[0]]
Q = deque([(0, stone[0])]) # j, f(j)
for i in range(1, n):
    # stone[i] + max dp[j]; i-j <= D
    while Q and Q[0][0] < i-D:
        Q.popleft()
    dp.append(stone[i] + max(0, Q[0][1]))
    while Q and Q[-1][1] < dp[i]:
        Q.pop()
    Q.append((i, dp[i]))
print(max(dp))