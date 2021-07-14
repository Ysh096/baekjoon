# 16236 아기상어

현재 위치에서 거리가 가장 가까운 물고기를 알아야 함 => BFS로 일일이 탐색

거리가 가까운 물고기가 많으면 가장 위, 가장 위인 물고기가 많으면 가장 왼쪽에 있는 물고기를 먹는다.



## 가장 빠른 풀이

```python
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs():
    global shark_eat, fish_count, shark_size
    start = [(shark_x, shark_y)] # 시작 지점
    queue =[]
    times = 0

    while start:
        p = start.pop() # 현재 시작 지점 기준으로 새롭게 설정
        visitied = [[0]*N for _ in range(N)] # 방문표시를 할 배열
        visitied[p[0]][p[1]] = 1 # 내 위치 방문표시
        size = 1
        queue.append(p)
        if fish_count == 0: # 남은 물고기가 없으면
            break # 종료
        while queue:
            for _ in range(size):
                q = queue.pop(0)
                for i in range(4):
                    nx = q[0] + dx[i]
                    ny = q[1] + dy[i]
                    if 0 <= nx < N and 0 <= ny < N and visitied[nx][ny] == 0 and (sea[nx][ny] == shark_size or sea[nx][ny] == 0): # 조건에 맞는 물고기를 찾으면
                        queue.append((nx, ny)) # 큐에 넣기
                        visitied[nx][ny] = visitied[q[0]][q[1]]+1 # bfs 방문표시
                    elif 0 <=nx < N and 0 <= ny < N and sea[nx][ny] != 0 and shark_size > sea[nx][ny] and visitied[nx][ny] == 0:
                        start.append((nx, ny))
                        visitied[nx][ny] = visitied[q[0]][q[1]] + 1
            if len(start):
                sx, sy = start[0][0], start[0][1]
                for x, y in start:
                    if x < sx:
                        sx = x
                        sy = y
                    elif x == sx and y < sy:
                        sx = x
                        sy = y
                shark_eat += 1
                if shark_eat == shark_size:
                    shark_size += 1
                    shark_eat = 0
                sea[p[0]][p[1]] = 0
                sea[sx][sy] = 9
                queue = []
                fish_count -= 1
                times += visitied[sx][sy]-1
                start = [(sx,sy)]
                break
            size = len(queue)

    return times


N = int(input())

sea = [list(map(int, input().split())) for _ in range(N)]
shark_x = shark_y = 0
fish_count = 0
fish_cnt =[]
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9: # 상어 위치
            shark_x, shark_y = i, j
        elif sea[i][j] != 0: # 물고기가 있으면
            fish_count += 1 # 물고기 수 +1

shark_size = 2
shark_eat = 0

result = bfs()
print(result)
```



