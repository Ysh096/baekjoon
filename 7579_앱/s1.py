import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
# 현재 활성화 되어 있는 앱이 사용 중인 메모리의 바이트 수
ms = list(map(int, input().split()))
# 각 앱을 비활성화 했을 경우의 비용
cs = list(map(int, input().split()))

# 앱을 비활성화 했을 경우의 비용을 최소화하여 M 바이트 메모리를 확보
# 느낌은 오는데 풀이를 어떻게 했는지 기억이 잘 안난다. 0-1 배낭문제
# https://claude-u.tistory.com/445
max_cost = sum(cs)
result = [[0] * (max_cost+1) for _ in range(2)]
cnt = 0
ans = -99
while cnt < N:
    for i in range(2):
        if i == 0:
            result[0][:] = result[1][:]
            continue
        for j in range(max_cost+1):
            if j < cs[cnt]:
                pass
            else:
                result[1][j] += ms[cnt]
                if result[1][j] >= M:
                    ans = j
                    break
    if ans >= 0:
        break
    cnt += 1
print(result)
print(ans)
