import sys
sys.stdin = open('input.txt')

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

print(A)
print(B)
print(C)
print(D)

# 이진탐색으로 어떻게?