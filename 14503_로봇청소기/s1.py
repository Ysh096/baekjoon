import sys
sys.stdin = open('input.txt')

def dfs(r, c, heading):
    global cnt
    for k in range(1, 4): # 2. 회전
        nr = r + dr[heading-k]
        nc = c + dc[heading-k]
        if not room[nr][nc]: # 청소할 공간이 있으면
            room[nr][nc] = 1 # 이동 및 청소, 방향은 heading
            cnt += 1
            if heading-k < 0:
                dfs(nr, nc, heading-k+4)
            else:
                dfs(nr, nc, heading-k)
            # room[nr][nc] = 0 # 해당 방향 탐색 이후
            # cnt -= 1
    nr = r + dr[heading - 2] # 뒤 방향
    nc = c + dc[heading - 2]
    if 0 < nr < N-1 and 0 < nc < M-1: # 범위 내에 있을 때
        if room[nr][nc] == 0:
            dfs(nr, nc, heading) # 후진(방향 유지)
        else:
            result.append(cnt)
            return
    else:
        result.append(cnt)
        return


N, M = map(int, input().split()) # 세로 N, 가로 M
r, c, d = map(int, input().split()) # 로봇 좌표 r, c, 방향 d
# d = 0, 1, 2, 3 북 동 남 서

room = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 1
room[r][c] = 1 # 처음 위치 청소
result = []
dfs(r, c, d)
print(result)