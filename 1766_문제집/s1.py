import sys
import heapq
sys.stdin = open('input.txt')

# 위상정렬 + heap 이용하는 문제라고 함
N, M = map(int, input().split())
heap = []
result = [] # 결과를 담을 배열
problems = [0 for _ in range(N+1)] # N개 문제의 진입차수 (0번째는 무시할 것)
a_to_b = {}
for _ in range(M):
    a, b = map(int, input().split()) # a를 풀고 b를 풀어야 함
    # 필요한 것: a와 연결된 문제들의 정보, b의 진입차수
    # a를 선행 문제로 가지는 b는 진입 차수가 하나 늘어난다.
    # a를 키로, [b1, b2, b3, ...]를 value로 하는 dictionary를 만든다.
    problems[b] += 1
    if a_to_b.get(a):
        a_to_b[a].append(b)
    else:
        a_to_b[a] = [b]

# 풀이법
# 진입 차수가 0인 problem을 heap에 넣는다.
# 하나 꺼낸 후 해당 문제 key와 연결된 b1, b2, b3, ...의 진입 차수를 줄여준다.
# 다시 진입 차수가 0인 문제를 넣어준다.
# heap이 빌 때까지 반복

# 초기 설정: 진입 차수가 0인 problem을 heap에 넣음
for i in range(1, N+1):
    if problems[i] == 0:
        heapq.heappush(heap, i)

while heap:
    a_pop = heapq.heappop(heap)
    if a_to_b.get(a_pop):
        for b in a_to_b[a_pop]:
            problems[b] -= 1
            if problems[b] == 0:
                heapq.heappush(heap, b)

    result.append(a_pop)
print(*result)