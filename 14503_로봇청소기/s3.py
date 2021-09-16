# 실패!
import sys
sys.stdin = open('input.txt')

# 1. 현재 위치 청소
# 2. 왼쪽 방향부터 탐색

def cleaner(r, c, d, cnt):
    global answer
    global flag
    # 동, 서 바꾸기
    k = d
    if d == 1:
        k = 3
    elif d == 3:
        k = 1
    if cnt == 4:
        # 뒤쪽이 벽인지 확인
        nr = r + dr[d-2]
        nc = c + dc[d-2]
        if board[nr][nc] == 1: # 벽이면
            flag = True
            return
        else:
            cleaner(nr, nc, d, 0)
    if flag:
        return
    if board[r][c] != 2 and not board[r][c] == 1:
        board[r][c] = 2 # 청소표시
        answer += 1
    nr = r + dr[(d+1)%4]
    nc = c + dc[(d+1)%4]
    if board[nr][nc] == 0: # 왼쪽 방향에 청소하지 않은 공간이 있다면
        cleaner(nr, nc, (d+1)%4, 0)
    elif board[nr][nc]: # 청소할 공간이 없다면
        cleaner(r, c, (d+1)%4, cnt+1)

N, M = map(int, input().split())
# d가 0이면 북쪽, 1이면 동쪽, 2면 남쪽, 3이면 서쪽
r, c, d = map(int, input().split())
flag = False
board = [list(map(int, input().split())) for _ in range(N)]
# 0 => 3 => 2 => 1 => 0 => 3 => 2 => 1 => 0 ...
# 방향
dr = [-1, 0, 1, 0] # 북 서 남 동
dc = [0, -1, 0, 1]
answer = 0
cleaner(r, c, d, 0)

print(answer)