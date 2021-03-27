import sys
sys.stdin = open('input.txt')

# 토끼 or 고양이, 키는 다 다름
# 수빈: 너랑 같은 동물 중에서 너보다 키가 큰 동물은 몇 마리야?

# N: 모든 동물의 수, answers: 각 동물의 대답
N = int(input())
answers = list(map(int, input().split()))

# 조건1: 무조건 0으로 시작해야 함
# 조건2: 답은 무조건 2의 배수
# 조건3: 같은 숫자가 3개 이상 나올 수 없음
# 트리 구조인가?
answers.sort()
possible = True # 가능한 대답인지 아닌지?
i = 0 # idx
cnt = 0 # 각 동물의 수
s = 2
while True:
    if 2*cnt+i+1 >= N:
        if answers[2*cnt+i] - 1 != answers[2*cnt+i-1]:
            possible = False
        break
    if s == 1:
        if answers[2*cnt+i] + 1 != answers[2*cnt+i+1]:
            possible = False
        i += 1
        continue

    if 2*cnt + 1 >= N:
        if 2*cnt > N: # 둘 다 범위를 벗어나는 경우
            break
        else: # 마지막 값이 범위를 벗어나는 경우(마지막에 한 종류만 남은 경우)
            if answers[2*cnt] == cnt:
                cnt += 1
                break

    if answers[2*cnt] == cnt and answers[2*cnt+1] == cnt:
        cnt += 1
    elif answers[2*cnt] == cnt and answers[2*cnt+1] != cnt:
        s = 1


if s == 1 and possible == True:
    answer = (2 ** cnt) * 2
elif s == 2 and possible == True:
    answer = 2 ** cnt
else:
    answer = 0

print(answer)