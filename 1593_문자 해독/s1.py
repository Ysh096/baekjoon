import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
W = input()
S = input()

Ws = [0] * 200

for w in W:
    # 확인할 것
    Ws[ord(w)] += 1

Ss = [0] * 200
length = 0
start = 0
result = 0
for m in range(M):
    Ss[ord(S[m])] += 1
    length += 1
    if length == N:
        if Ws == Ss:
            result += 1
        Ss[ord(S[start])] -= 1
        length -= 1
        start += 1
print(result)