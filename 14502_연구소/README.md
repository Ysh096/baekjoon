# 14502_연구소



## 방법1. 일일이 확인

```python
import sys
sys.stdin = open('input.txt')
import copy
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0

def bfs():
    global ans
    w = copy.deepcopy(a)
    for i in range(n):
        for j in range(m):
            if w[i][j] == 2:
                q.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if w[nx][ny] == 0:
                    w[nx][ny] = 2
                    q.append([nx, ny])

    cnt = 0
    for i in w:
        cnt += i.count(0)
    ans = max(ans, cnt)

def wall(x):
    if x == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                a[i][j] = 1
                wall(x+1)
                a[i][j] = 0

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = deque()
wall(0)
print(ans)
```

https://chldkato.tistory.com/9 참고

3440ms



## 가장 빠른 풀이

```python
from itertools import combinations

dx,dy = [0,0,1,-1],[1,-1,0,0]
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for ARR in range(N)] # 맵 받아오기
cnt_max = 0


def blocking(list): # list에는 벽을 세울 위치가 숫자로 들어가 있다. ex) (1, 2, 3), ... ,(40, 42, 43)
    global virus_max
    arr_new = [i[:] for i in arr] # 맵의 한 row에 대해
    for i in list:
        a = i//8 # 행 좌표
        b= i%8 # 열 좌표
        arr_new[a][b] = 1
    virus2=virus[:] # 바이러스 위치 복사하여 dfs에 사용
    cnt = 0
    cntt=dfs(arr_new,virus2,cnt)  
    
    if cntt<virus_max:
        virus_max=cntt
    
def dfs(arr_new,vir,cnt):
    global virus_max
    while vir:
        z=vir.pop() # 바이러스 위치 하나 꺼내서
        node_y=z//8
        node_x=z%8 # x, y 좌표 구하고,
        if virus_max<=cnt:
            return 64 # 바이러스 수는 최대 64개로 제한
        for i in range(4):    
            ny = node_y + dy[i]
            nx = node_x + dx[i]
            if 0<=nx<M and 0<=ny<N and arr_new[ny][nx] == 0: # 위아래로 퍼뜨리기
                vir.append(ny*8+nx)  
                arr_new[ny][nx] = 2  
                cnt+=1
        
    return cnt

# 벽을 세울 수 있는 후보군 찾기
possible_block = []
virus=[]
safe_zone=0
virus_max=64
for y in range(N):
    for x in range(M):
        if arr[y][x] == 0:
            possible_block.append(y*8+x)
            safe_zone+=1
        elif arr[y][x]==2:
            virus.append(y*8+x)  
block_3_list = combinations(possible_block,3)

for i in block_3_list: # ex) i = (1, 2, 3), (1, 2, 6), ...
    blocking(i)

print(safe_zone-virus_max-3)
```

