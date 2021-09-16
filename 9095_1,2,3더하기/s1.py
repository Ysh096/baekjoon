import sys
sys.stdin = open('input.txt')

T = int(input())

def dp(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    else:
        return dp(N-1) + dp(N-2) + dp(N-3)

for _ in range(T):
    N = int(input())
    print(dp(N))