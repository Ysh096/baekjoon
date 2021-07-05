import sys
sys.stdin = open('input.txt')

N = int(input()) # 탑의 수

towers = list(map(int, input().split()))

# 맨 오른쪽부터 순서대로 스택에 쌓는다.
# 새로운 탑의 높이를 마지막 원소와 비교하여 새로운 탑이 더 크면 꺼낸다.
ans = [0] * N
stack = []
L = len(towers)
stack.append((L-1, towers[-1])) # 초기값(가장 오른쪽 탑의 번호와 높이)
for i in range(L-2, -1, -1): # 역순
    while stack[-1][1] < towers[i]:
        idx, tall = stack.pop()
        ans[idx] = i+1
        if len(stack) == 0:
          break
    stack.append((i, towers[i]))

print(*ans)