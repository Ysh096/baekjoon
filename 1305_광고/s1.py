import sys
sys.stdin = open('input.txt')

# KMP 알고리즘의 pi배열을 이용
L = int(input())
adv = input()
# 반복되는 부분을 찾아서 그만큼 전체 길이에서 빼준다.
# https://bowbowbow.tistory.com/6 이거 보고 했다가 실패
# 실패함수는 좀 다른거였음
pi_list = [0] * L
i = 0
cnt = 0
while i < L:
    if i-cnt <= (0 + cnt):
        i += 1
        cnt = 0
    else:
        if adv[i-cnt] == adv[0+cnt]:
            pi_list[i] += 1
            cnt += 1
        else:
            i += 1
            cnt = 0
print(pi_list)
print(L - pi_list[-1])