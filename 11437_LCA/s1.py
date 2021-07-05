import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(int(1e5))
n = int(input())

parent = [0] * (n+1) # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지의 깊이
c = [0] * (n+1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n+1)] # 그래프 정보

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 깊이 구하기
def dfs(x, depth):



    c[x] = True
    d[x] = depth
    for y in graph[x]: # 처음엔 2, 3
        if c[y]: # y의 깊이를 구했는지 확인
            continue # 구했으면 넘어가기
        parent[y] = x
        dfs(y, depth+1)

# a와 b의 공통 조상 찾기
def lca(a, b):
    while d[a] != d[b]: # 두 노드의 깊이가 같지 않을 때
        if d[a] > d[b]: # a의 깊이가 더 깊다면
            a = parent[a] # a의 위치를 한 칸 위로(부모로)
        else:
            b = parent[b] # b가 더 깊으면 b를 부모 노드로
    # 위의 while문을 거치면 동일 깊이에 두 노드가 위치한다.

    while a != b: # 두 노드가 같아질 때까지
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0)

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
