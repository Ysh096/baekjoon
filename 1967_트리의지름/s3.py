# 배열로 인접리스트 만들기
import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra(i):
    dist[i] = 0 # 자기 자신으로 향하는 거리
    heap = []
    heapq.heappush(heap, (dist[i], i)) # 초기화

    while heap:
        w, j = heapq.heappop(heap)
        for k in range(len(adj_list[j])): # 인접 리스트의 배열 길이만큼 순회
            w_new, j_new = adj_list[j][k]
            if dist[j_new] > dist[j] + w_new:
                dist[j_new] = dist[j] + w_new
                heapq.heappush(heap, (dist[j_new], j_new))


n = int(input()) # 노드의 개수

# 딕셔너리로 인접리스트 만들기
adj_list = [[] for _ in range(10001)]
# 주어지는 정보: (부모 노드, 자식 노드, 가중치)
for _ in range(n-1):
    p, c, w = map(int, input().split())
    adj_list[p].append((w, c))
    adj_list[c].append((w, p)) # 반대 방향

# print(adj_list)
# adj_list = [[], [(3, 2), (2, 3)], [(3, 1), (5, 4), ...]
dist = [987654321]*(n+1)
dijkstra(1) # 첫 번째 다익스트라
print(dist)
max_val = 0
max_idx = 0
dist[0] = 987654321 # 987654321을 배제
for idx, val in enumerate(dist[1:]):
    if val > max_val:
        max_idx = idx
        max_val = val
dist = [987654321]*(n+1) # 배열 다시 만들기
dijkstra(max_idx+1)
print(dist)
print(max(dist[1:]))