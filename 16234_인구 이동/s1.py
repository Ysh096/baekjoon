import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs():
    while queue:
        calc = []
        r, c = queue.popleft()
        calc.append((r, c))
        visited[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 내에 있고 방문하지 않았으면
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if L <= abs(populations[r][c] - populations[nr][nc]) <= R:
                    queue.append((nr, nc))
    return calc

N, L, R = map(int, input().split())
populations = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*N for _ in range(N)] # 방문표시를 할 visited

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

days = 0
flag = True
while flag: # 언제 끝날지 모름
    days += 1
    visited = [[0] * N for _ in range(N)]  # 방문표시를 할 visited
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                queue = deque()
                queue.append((i, j))
                calc = bfs() # 계산할 (행, 열) 값을 가져옴
                if len(calc) == 1:
                    flag = False
                L = len(calc)
                pop_sum = 0
                for k in range(L):
                    r, c = calc[k]
                    pop_sum += populations[r][c]
                avg = pop_sum // L
                for k in range(L):
                    r, c = calc[k]
                    populations[r][c] = avg

print(days)