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

N, K, M = map(int, input().split())
friends = [i for i in range(1, N+1)]

target = friends[M-1]
tmp_friends = []
idx = 0
val = 1
cnt = 0 # 몇 번째로 퇴장?
while True:
    if val == K:
        cnt += 1
        if idx-1 == target:
            break
        idx += 1
        val = 1
    else: # val == 1
        tmp_friends.append(friends[idx])
        idx += 1
        val += 1
    if idx == N:
        friends = tmp_friends
        N = len(friends)
        idx = 0
print(cnt)