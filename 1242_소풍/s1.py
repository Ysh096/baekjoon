import sys
sys.stdin = open('input.txt')
# from collections import deque
#
# N, K, M = map(int, input().split())
# friends = [i for i in range(1, N+1)]
#
# dq = deque(friends)
# num = 1
# cnt = 0
# while True:
#     if num == K:
#         exit = dq.popleft()
#         num = 1
#         cnt += 1
#         if exit == M:
#             break
#     elif num != K:
#         dq.append(dq.popleft())
#         num += 1
#
# print(cnt)

# N, K, M = map(int, input().split())
# friends = [i for i in range(1, N+1)]
#
# idx = 0
# val = 1
# cnt = 0
# tmp_list = []
# while True:
#     if val == K:
#         cnt += 1
#         if friends[idx % N] == M:
#             break
#         idx += 1
#         val = 1
#
#     else:
#         tmp_list.append(friends[idx % N])
#         idx += 1
#         val += 1
#     if idx % N == 0:
#         N = len(tmp_list)
#         friends = tmp_list
#         tmp_list = []
#         idx = 0

# print(cnt)

#
# N, K, M = map(int, input().split())
# friends = [i for i in range(1, N+1)]
#
# target_idx = M-1
# val = 1
# idx = 0
# cnt = 0
# while True:
#     if val == K:
#         friends[idx % N] = 0
#         cnt += 1
#         if idx % N == target_idx:
#             break
#         val = 1
#         idx += 1
#     else:
#         idx += 1
#         val += 1
# print(cnt)

# 어떻게 해야 가장 효율적일까?
# 1. len()을 쓰지 말자
# N, K, M = map(int, input().split())
# start = 1 # 시작 지점이자 val=K일 때 없앨 위치
# value = 1
# cnt = 0
# # M이 목표의 위치
# while True:
#     if value == K:
#         if start == M:
#             cnt += 1
#             break
#         elif start < M:
#             M -= 1
#             cnt += 1
#         else:
#             cnt += 1
#         N -= 1
#         value = 1
#     else:
#         start += 1
#         value += 1
#     if start > N:
#         start = start % N
# print(cnt)

# 이게 무슨  풀이일까?
N, K, M = map(int,input().split())
original_N = N
while True:
    mod = K % N
    if mod == 0:
        mod = N
    if mod == M:
        break
    elif mod < M:
        M = M - mod
    else:
        M = M - mod + N
    N -= 1
print(original_N - N + 1)