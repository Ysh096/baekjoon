import sys
sys.stdin = open('input.txt')

# 하나의 집합에 있으면 가능하지 않을까?
def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

# 도시의 수 N
N = int(input())

# 여행 계획에 속한 도시들의 수 M
M = int(input())

graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    data_i = list(map(int, input().split()))
    for j in range(0, N):
        graph[i][j+1] = data_i[j]
p = list(range(N+1))

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j]:
            union(i, j)

plan = list(map(int, input().split()))

trip_set = find_set(plan[0])
flag = True
for i in range(1, M):
    if find_set(plan[i]) != trip_set:
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')
