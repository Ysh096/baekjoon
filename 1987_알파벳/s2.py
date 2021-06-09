import sys
sys.stdin = open('input.txt')

# 세로 R칸, 가로 C칸
# 상하좌우 인접 칸으로 이동 가능, 이동한 칸의 알파벳은 새로운 알파벳이어야 함
# 좌측 상단에서 시작한 말이 최대 몇 칸을 지나는가?(시작점 포함)
# R과 C는 최대 20으로, 그렇게 크지는 않다.
# 백트래킹을 어떻게 할지??
def dfs(r, c, cnt):
    global max_cnt
    global flag
    if max_cnt < cnt:
        max_cnt = cnt
    if max_cnt == 26:
        flag = True
        return
    if flag:
        return
    for k in range(4):
        # 새로 방문하고자 하는 좌표
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < R and 0 <= nc < C:
            if not visited[nr][nc] and not alpha[ord(board[nr][nc])]:
                alpha[ord(board[nr][nc])] = 1  # 방문 처리
                visited[nr][nc] = 1
                dfs(nr, nc, cnt+1)
                alpha[ord(board[nr][nc])] = 0  # 방문 처리 풀기
                visited[nr][nc] = 0

R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
alpha = [0]*200 # A~Z까지 방문한 알파벳을 기록할 배열

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 초기화
max_cnt = 0
visited[0][0] = 1
alpha[ord(board[0][0])] = 1
flag = False
dfs(0, 0, 1)
print(max_cnt)