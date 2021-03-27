import sys
sys.stdin = open('input.txt')

# B가 짝수면 2로 나누고 1이면 1을 없애주기
A, B = map(int, input().split())
cnt = 0
while True:
    if A == B:
        print(cnt+1)
        break
    if A > B:
        print(-1)
        break
    if B % 2 == 0:
        B = B // 2
    elif B % 10 == 1:
        B = B // 10
    else: # 2로 나눌수도 없고 끝이 1도 아니면
        print(-1)
        break
    cnt += 1
