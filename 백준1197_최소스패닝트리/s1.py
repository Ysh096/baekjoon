import sys
sys.stdin = open('input.txt')

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x != y:
        p[y] = x

sets = []
V, E = map(int, input().split())
p = list(range(V+1))
for _ in range(E):
    a, b, c = map(int, input().split())
    sets.append((a, b, c))
sets.sort(key = lambda x:x[2])

result = 0
cnt = 0
for i in range(E):
    a, b, c = sets[i]
    if find_set(a) != find_set(b):
        union(a, b)
        result += c
        cnt += 1
    if cnt > V-1:
        break

print(result)

