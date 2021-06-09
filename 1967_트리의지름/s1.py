import sys
sys.stdin = open('input.txt')

# 메모리 초과
import heapq

def dijkstra(i):
    dist[i] = 0
    heap = []
    heapq.heappush(heap, (dist[i], i))

    while heap:
        w, s = heapq.heappop(heap)
        for e in range(n+1):
            if graph[s][e]:
                if dist[e] > dist[s] + graph[s][e]:
                    dist[e] = dist[s] + graph[s][e]
                    heapq.heappush(heap, (dist[e], e))


n = int(input())
edges = []
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n-1):
    s, e, w = map(int, input().split())
    graph[s][e] = w
    graph[e][s] = w

result = []
# 어떤 두 노드 사이의 거리 구하기(다익스트라)
dist = [987654]*(n+1)
dijkstra(1)
# dist에는 1번에서 가장 먼 노드가 주어짐
max_val = 0
max_idx = 1
for idx, val in enumerate(dist[1:]):
    if val > max_val:
        max_idx = idx
        max_val = val

# 두 번째 다익스트라
dist = [987654]*(n+1)
dijkstra(max_idx+1) # dist에서 0번을 빼고 찾은 max_idx 이므로 1 더하기
print(max(dist[1:]))