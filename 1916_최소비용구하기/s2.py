import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra():
    heap = []
    dist[s] = 0 # s에서 s로 가는 비용은 0
    heapq.heappush(heap, (0, s))

    while heap:
        cost, start = heapq.heappop(heap)
        for j in range(1, N+1):
            if graph[start][j] > -1:
                if dist[j] > graph[start][j] + cost:
                    dist[j] = graph[start][j] + cost
                    heapq.heappush(heap, (dist[j], j))

N = int(input())
M = int(input())

graph = [[-1 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    start, end, w = map(int, input().split())
    if graph[start][end] > -1:
        if graph[start][end] > w:
            graph[start][end] = w
    else:
        graph[start][end] = w
s, e = map(int, input().split()) # target start, end point
dist = [987654321] * (N+1)

dijkstra()

print(dist[e])
