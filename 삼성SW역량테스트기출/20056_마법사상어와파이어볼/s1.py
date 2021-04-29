import sys
sys.stdin = open('input.txt')

# 1. 모든 파이어볼이 자신의 방향 d_i로 속력 s_i칸 만큼 이동(겹치기 가능)
# 2. 이동이 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는
#   1. 파이어볼이 모두 하나로 합쳐진다.
#   2. 파이어볼은 4개의 파이어볼로 나누어진다.
#   3. 나누어진 파이어볼의 질량, 속력, 방향은
#       1. 질량: 합쳐진 파이어볼 질량의 합/5
#       2. 속력: 합쳐진 파이어볼 속력의 합/합쳐진 파이어볼의 개수
#       3. 합쳐지는 파이어볼의 방향이 모두 홀수 or 모두 짝수면 방향은 0, 2, 4, 6, 그 외에는 1, 3, 5, 7
#   4. 질량이 0인 파이어볼은 소멸
# 마법사 상어가 K번 이동 명령을 한 후 남아있는 파이어볼 질량의 합은?

# 주의: 1행, 1열부터 시작해서 N행, N열에서 끝남
dr = [-1, -1, 0, 1, 1, 1, 0, -1] # 방향은 위부터 시작해서 시계방향
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def move(ball):
    new_ball = []
    r, c, m, s, d = ball[0], ball[1], ball[2], ball[3], ball[4]
    # r:0, c:1, 질량m:2, 속력s:3, 방향d:4
    # 방향 d로 속력 s만큼 이동
    # 1 <= r <= N, 1<= c <= N
    # 만약 N = 4 라면, 1<=r<=4 이고, r이 5가 되면 1로, 6이 되면 2로, ... %N 위치로 이동!
    # 만약 N = 4 라면, 1<=r<=4 이고, r이 0이 되면 4로, -1이 되면 3으로, ... ... -4면 4로, -8이면 4로, ...
    # 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12
    # 4  3  2  1  4  3  2  1  4  3  2   1   4 ...
    # N - (abs(값)%N)
    nr = r + s*dr[d] # new row
    nc = c + s*dc[d] # new col

    # 벽을 뚫는 경우 위치 재계산
    if nr > N:
        nr = nr % N
    elif nr < 1:
        nr = N - (abs(nr) % N)
    if nc > N:
        nc = nc % N
    elif nc < 1:
        nc = N - (abs(nc) % N)
    new_ball.append([nr, nc, m, s, d])
    return new_ball

def divide_balls(new_balls):
    # new_balls에서 위치가 같은 것 표시하기
    new_dict = {}
    for idx, ball in enumerate(new_balls):
        r, c = ball[0], ball[1]
        if new_dict.get((r, c)):
            new_dict[(r, c)].append(idx)
        else:
            new_dict[(r, c)] = [idx]
    # new_dict에는 파이어볼의 idx가 담겨있다. 겹치면 겹치는 만큼 담겨있음!
    divided = []
    for key, val in new_dict.items():
        if len(val) == 1:
            divided.append(new_balls[val[0]])
        else:
            # 파이어볼이 겹치는 경우
            nr, nc, m, s = key[0], key[1], 0, 0
            dd = new_balls[val[0]][-1] % 2
            flag = True
            for i in val: # 각 인덱스별 값을 다 더해준다.
                m += new_balls[i][2]
                s += new_balls[i][3]
                d = new_balls[i][-1]
                if d % 2 != dd:
                    flag = False
            m = m // 5
            s = s // len(val)
            if m == 0:
                continue
            if flag:
                for j in range(0, 8, 2):
                    divided.append([nr, nc, m, s, j])
            else:
                for j in range(1, 9, 2):
                    divided.append([nr, nc, m, s, j])
    return divided
N, M, K = map(int, input().split())
balls = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    balls.append([r, c, m, s, d])

for _ in range(K):
    new_balls = []
    for ball in balls:
        new_balls.extend(move(ball))
    balls = new_balls
    balls = divide_balls(balls)
    print(balls)
    result = 0
for i in range(len(balls)):
    result += balls[i][2]
print(result)