import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra():
    dist[0][0] = 0 # 0에서 0으로 가는 경우 0
    heap = []
    heapq.heappush(heap, (dist[0][0], 0, 0))

    while heap:
        w, r, c = heapq.heappop(heap) # 가중치, r, c
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if dist[nr][nc] > dist[r][c] + int(miro[nr][nc]):
                    dist[nr][nc] = dist[r][c] + int(miro[nr][nc])
                    heapq.heappush(heap, (dist[nr][nc], nr, nc))

M, N = map(int, input().split())
miro = [input() for _ in range(N)]
# 0은 빈 방, 1은 벽
# N, M으로 이동할 때 부숴야 하는 벽의 최소 개수
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
dist = [[987654321] * M for _ in range(N)]
dijkstra()

print(dist[N-1][M-1])

