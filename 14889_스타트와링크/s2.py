import sys
sys.stdin = open('input.txt')

def divide_team(idx, k, n, r): # 팀을 구성하는 모든 조합 생성
    if idx == r:
        all_combi.append(list(one_team))
        return

    for i in range(k, n-r+idx+1):
        one_team[idx] = i
        divide_team(idx+1, i+1, n, r)


N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]

one_team = [0] * (N//2)
all_combi = []
divide_team(0, 0, N, N//2) # 팀 조합 만들기

# print(all_combi) [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
# 팀이 나뉘어진 조합을 보면 앞뒤로 짝이 맞음 순서대로 구해지기 때문
all_N = len(all_combi) # 팀나누기
start = all_combi[:all_N//2] # 스타트
link = all_combi[all_N//2:][::-1] # 링크

# 최소값 찾기
min_val = 999999
for t in range(all_N//2):
    start_synergy, link_synergy = 0, 0
    for i in range(N//2 - 1):
        for j in range(i, N//2):
            start_synergy += people[start[t][i]][start[t][j]] +people[start[t][j]][start[t][i]]
            link_synergy += people[link[t][i]][link[t][j]] + people[link[t][j]][link[t][i]]

    val = abs(start_synergy-link_synergy)
    if val < min_val:
        min_val = val

print(min_val)