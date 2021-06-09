# keyError
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
adj_list = {}
# 주어지는 정보: (부모 노드, 자식 노드, 가중치)
for _ in range(n-1):
    p, c, w = map(int, input().split())
    if adj_list.get(p):
        adj_list[p].append((w, c))
        if adj_list.get(c):
            adj_list[c].append((w, p)) # 반대 방향
        else:
            adj_list[c] = [(w, p)]
    else:
        adj_list[p] = [(w, c)]
        if adj_list.get(c):
            adj_list[c].append((w, p)) # 반대 방향
        else:
            adj_list[c] = [(w, p)]
# adj_list = {1: [(3, 2), (2, 3)], 2: [(3, 1), (5, 4)], ...}
dist = [987654321]*(n+1)
dijkstra(1) # 첫 번째 다익스트라

max_val = 0
max_idx = 1
for idx, val in enumerate(dist[1:]):
    if val > max_val:
        max_idx = idx
        max_val = val
dist = [987654321]*(n+1) # 배열 다시 만들기
dijkstra(max_idx+1)
print(max(dist[1:]))