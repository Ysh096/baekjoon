import sys
sys.stdin = open('input.txt')

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

# 최소비용
# N = 컴퓨터의 수
N = int(input())

# M = 연결할 수 있는 선의 수
M = int(input())
money = []
for _ in range(M):
    money.append(list(map(int, input().split())))
money.sort(key=lambda x:x[2])

p = list(range(N+1))
result = 0
cnt = 0
for i in range(M):
    s, e, w = money[i]

    if find_set(s) != find_set(e):
        union(s, e)
        cnt += 1
        result += w
    if cnt > N-1:
        break

print(result)