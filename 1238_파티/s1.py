import sys
sys.stdin = open('input.txt')

import heapq

# 단방향 도로들 -> 다익스트라 힌트
def dijkstra(i):
    dist[i] = 0
    heap = []
    heapq.heappush(heap, (dist[i], i))
    while heap:
        t, s = heapq.heappop(heap)
        for j in range(1, N+1):
            if graph[s][j]:
                if dist[j] > dist[s] + graph[s][j]:
                    dist[j] = dist[s] + graph[s][j]
                    heapq.heappush(heap, (dist[j], j))

N, M, X = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s][e] = t

result = []
# 다익스트라 배열 만들기
for i in range(1, N+1):
    # i = 학생의 번호
    dist = [987654321 for _ in range(N+1)]
    dijkstra(i)
    # 갈 때
    result.append(dist[X])

# 돌아올 때
dist = [987654321 for _ in range(N + 1)]
dijkstra(X)

# 갈 때 + 돌아올 때
for i in range(1, len(dist)):
    result[i-1] += dist[i]

print(max(result))