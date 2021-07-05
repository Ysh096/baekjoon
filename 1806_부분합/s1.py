import sys
sys.stdin = open('input.txt')

N, S = map(int, input().split())
# 비교 대상 하나를 고른 후 다 해보기? => 너무 오래 걸릴듯
# 투 포인터
numbers = list(map(int, input().split()))
start = 0
end = 1
ans = 0 # 만들 수 없으면 ans = 0
min_L = 1000001
while start < N and end <= N:
    if sum(numbers[start:end]) >= S:
        L = end - start # 길이
        if L < min_L:
            min_L = L
        start += 1
    else:
        end += 1

if min_L == 1000001:
    print(ans)
else:
    print(min_L)