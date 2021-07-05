import sys
sys.stdin = open('input.txt')

N, S = map(int, input().split())
numbers = [0] + list(map(int, input().split())) # 합은 0부터 시작
num_sum = [0] * (N+1)
for i in range(1, N+1):
    num_sum[i] = num_sum[i-1] + numbers[i]
# print(num_sum) => [0, 5, 6, 9, 14, 24, 31, 35, 44, 46, 54]

start = 0
end = 1
ans = 0
min_L = 1000001
while end < N+1 and start < N:
    if num_sum[end] - num_sum[start] >= S:
        L = end - start
        start += 1
        if L < min_L:
            min_L = L
    else:
        end += 1
if min_L == 1000001:
    print(ans)
else:
    print(min_L)
