import sys
sys.stdin = open('input.txt')

def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    roads = []
    total = 0
    for _ in range(n):
        a, b, z = map(int, input().split())
        roads.append((a, b, z))
        total += z
    roads.sort(key=lambda x:x[2])

    p = list(range(m))
    cnt = 0
    result = 0
    for i in range(n):
        a, b, w = roads[i]
        if find_set(a) != find_set(b): # 싸이클이 형성되지 않는 한
            union(a, b)
            result += w
            cnt += 1
        if cnt == m-1:
            break
    print(total - result)
