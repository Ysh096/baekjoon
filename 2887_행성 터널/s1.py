import sys

sys.stdin = open('input.txt')

def find_set(x):
    if p[x] != x:
         p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

N = int(input())

locations = []
for i in range(N):
    x, y, z = map(int, input().split())
    locations.append((x, y, z, i)) # 순서까지 매겨서 위치 추가

# x의 최소 비용
locations.sort()
tunnel = [] # 통로
for i in range(N-1):
    tunnel.append((abs(locations[i][0] - locations[i+1][0]), locations[i][3], locations[i+1][3]))
# y의 최소 비용
locations.sort(key=lambda x: x[1])
for i in range(N-1):
    tunnel.append((abs(locations[i][1] - locations[i+1][1]), locations[i][3], locations[i+1][3]))
# z의 최소 비용
locations.sort(key=lambda x: x[2])
for i in range(N-1):
    tunnel.append((abs(locations[i][2] - locations[i+1][2]), locations[i][3], locations[i+1][3]))

p = [i for i in range(N)]

tunnel.sort()
# print(tunnel)
cnt = 0
i = 0
ans = 0
while cnt < N-1:
    if find_set(tunnel[i][1]) != find_set(tunnel[i][2]): # 부모가 같지 않으면
        union(tunnel[i][1], tunnel[i][2])
        ans += tunnel[i][0]
        cnt += 1
        i += 1
    else:
        i += 1
print(ans)

