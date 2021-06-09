import sys
sys.stdin = open('input.txt')

from itertools import combinations
# 인원 수, 1부터 시작
N = int(input())

S = [list(map(int, input().split())) for _ in range(N)]

member = list(range(N))
combs = list(combinations(member, N//2)) # 두 명씩 짝지은 것
# print(combs)

result = 9999999
for i in range(len(combs)//2): # 조합은 절반만 보면 됨
    start = 0
    link = 0
    for j in range(N): # 0, 1, 2, 3을 돌며 숫자가 조합에 들어 있는 경우 start 팀에 추가
        if j in combs[i]:
            for k in range(N):
                if k in combs[i]:
                    start = start + S[j][k]
        else:
            for k in range(N):
                if k not in combs[i]:
                    link = link + S[j][k]
    if result > abs(start-link):
        result = abs(start-link)
print(result)
