import sys
sys.stdin = open('input.txt')

# 1. 그냥 풀어보기 => 메모리 초과
# N, K = map(int, input().split())
#
# people = [i for i in range(1, N+1)]
# visited = [0] * N
#
# val = 1
# idx = 0
# cnt = 0
# while cnt < N:
#     if visited[idx % N] == 1:
#         idx += 1
#         continue
#     if val == K:
#         visited[idx % N] = 1
#         out = (idx % N) + 1
#         cnt += 1
#         idx += 1
#         val = 1
#     else:
#         val += 1
#         idx += 1
#
# print(out)

# 2. 점화식 사용 => RecursionError (최대 재귀 깊이에 걸린듯)
# 점화식 f(n, k) = (f(n-1, k) + k) mod n, with f(1, k) = 0
# 병사 수가 1명이면 생존자 1번
# 병사 수가 2명이면 생존자는 2번
# 병사 수가 3명이면 생존자는 2번
# ...
# N, K = map(int, input().split())
# def josephus(n, k):
#     if n == 1:
#         return 1
#     return ((josephus(n-1, k) + k - 1) % n) + 1
#
# result = josephus(N, K)
# print(result)


# 3. 재귀를 while문으로 풀어봄 => 시간 초과
# N, K = map(int, input().split())
# n = 1
# value = 1
# while n <= N:
#     value = ((value + K - 1) % n) + 1
#     n += 1
# print(value)

# 4. for문(wiki)
N, K = map(int, input().split())
res = 0
for n in range(1, N+1):
    res = (res+K) % n

print(res+1)

