# 3190 뱀



## 내 풀이

```python
import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(input()) # 보드의 크기

board = [[0] * (N+1) for _ in range(N+1)] # 시작은 (1, 1)

K = int(input()) # 사과의 개수

for _ in range(K): # 사과의 위치
    row, col = map(int, input().split())
    board[row][col] = 2 # 사과 놓기

L = int(input()) # 뱀의 방향 변환 횟수
directions = deque()
for _ in range(L):
    X, C = input().split()
    X = int(X)
    directions.append((X, C))

dr = [0, 1, 0, -1] # 우 - 하 - 좌 - 상
dc = [1, 0, -1, 0]

flag = False
r = 1
c = 1
i = 0
cnt = 0
board[r][c] = 1
snake = deque()
snake.append((r, c)) # 뱀이 위치한 좌표
while 0 < r < N+1 and 0 < c < N+1:
    if directions and cnt == directions[0][0]:
        _, dir = directions.popleft()
        if dir == "D":
            i += 1
        else:
            i -= 1
    r = r + dr[i % 4]
    c = c + dc[i % 4]
    cnt += 1
    if not (0 < r < N+1 and 0 < c < N+1):
        break
    if board[r][c] == 1: # 뱀이 자기 몸을 만난 경우
        break
    if board[r][c] == 2: # 사과를 만난 경우
        board[r][c] = 1 # 사과 없애기
        snake.append((r, c))
    else:
        board[r][c] = 1 # 사과가 없으면
        snake.append((r, c))
        remove_r, remove_c = snake.popleft()
        board[remove_r][remove_c] = 0

print(cnt)
```

112ms



런타임 에러가 뜬 이유: `if not (0 < r < N+1 and 0 < c < N+1):` 에서 괄호를 안쳐서

