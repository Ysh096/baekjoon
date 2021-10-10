import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
num = list(map(int, input()))

# 1. 맨 앞 K번째(0, 1, ..., K) 위치까지 확인해서 제일 큰 값을 첫 번째 값으로 한다.
# 처음 시작은 i = 0 <= X <= N-T (여기서 T = N-K로, 구하려는 수의 길이)
# 이 범위에서 가장 큰 값을 찾고 나면 i = max_idx+1, T = T-1


result = []
start = 0
T = N-K
while True:
    max_val = 0
    for i in range(start, N-T+1):
        if num[i] > max_val:
            max_val = num[i]
            max_idx = i
    result.append(max_val) # 앞자리부터 하나씩 최대값을 구함
    if len(result) == N-K:
        break
    start = max_idx+1
    T = T-1

answer = ''
for val in result:
    answer += str(val)
print(answer)