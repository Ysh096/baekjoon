import sys
sys.stdin = open('input.txt')

N = int(input())
P = list(map(int, input().split()))

P.sort()
# 그냥 누적합 구하기
sum = 0
tmp_sum = 0
i = 0
while i < N:
    tmp_sum += P[i]
    sum += tmp_sum
    i += 1
print(sum)