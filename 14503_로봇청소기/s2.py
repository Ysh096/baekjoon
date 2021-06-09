import sys
sys.stdin = open('input.txt')

def dfs(r, c, d, cnt):
    global max_cnt
    global flag
    if flag:
        return
    if cnt > max_cnt:
        max_cnt = cnt

    room[r][c] = 2 # 1. 현재 위치를 청소한다.
    for k in list(range(d+1, d+5)):
        k = k % 4
        nr = r + dr[k]
        nc = c + dc[k]
        if room[nr][nc] == 0: # 2_a. 청소하지 않은 공간이 존재
            dfs(nr, nc, k, cnt+1) # 그 방향으로 회전 + 전진
    # 모두 청소가 되어있거나 벽인 경우,
    # 만약 뒤쪽 방향이 벽이 아니라면
    # d의 반대 방향으로 이동, 바라보는 방향은 유지
    nr = r + dr[(d+2) % 4]
    nc = c + dc[(d+2) % 4]
    if room[nr][nc] != 1:
        dfs(nr, nc, d, cnt)
    else:
        flag = True
        return

N, M = map(int, input().split())
r, c, d = map(int, input().split())
# 0: 북, 1: 동, 2: 남, 3: 서
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

flag = False
room = [list(map(int, input().split())) for _ in range(N)]
max_cnt = 0
if d == 1:
    d = 3
elif d == 3:
    d = 1
dfs(r, c, d, 1)
print(max_cnt)