import sys
sys.stdin = open('input.txt')

# 처음 시도한 방법, 그냥 그대로 구현하려고 했음 => 시간초과

# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# # 0 <= p < q < r < N
# cnt = 0
# for p in range(0, N-2):
#     for q in range(p+1, N-1):
#         for r in range(q+1, N):
#             if A[p] * A[q] * A[r] % K == 0:
#                 cnt += 1
#
# print(cnt)

# 생각해보니 p, q, r 값이 뭔지는 중요하지 x, 그냥 서로 다른 값이기만 하면 됨
# 배열에서 중복없이 3개를 뽑아 곱하고 K로 나눠보기
# => 시간 초과
import itertools
N, K = map(int, input().split())
A = list(map(int, input().split()))
combs = itertools.combinations(A, 3)
cnt = 0
for comb in combs:
    if comb[0] * comb[1] * comb[2] % K == 0:
        print(comb[0], comb[1], comb[2])
        cnt += 1
print(cnt)

xyz = Ka
