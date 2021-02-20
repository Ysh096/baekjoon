import sys
sys.stdin = open('input.txt', 'r')

#대칭인 구간을 찾는 함수
def find_sym(switches, Z, N):
    i = 1
    while Z-i >= 0 and Z+i <= N-1:
        if switches[Z-i] == switches[Z+i]:
            i += 1
        else:
            return i-1
    return i-1
#스위치 개수
N = int(input())

#스위치 초기 배열
switches = list(map(int, input().split()))

#학생 수
T = int(input())
for tc in range(T):
    S, Z =  map(int, input().split()) #성별 S, 학생이 받은 수 Z
    if S == 1: #남학생이라면
        #횟수
        t = N//Z
        for i in range(1, t+1):
            idx = Z*i - 1
            if switches[idx] == 1:
                switches[idx] = 0
            else:
                switches[idx] = 1 #스위치 상태 바꾸기

    else: #여학생이라면
        Z = Z-1 #스위치 번호 = 인덱스로 맞춰주기(Z는 0부터 시작)
        idx = find_sym(switches, Z, N) #Z를 중심으로 대칭인 양 옆 범위 idx 찾기
        for i in range(Z-idx, Z+idx+1):
            if switches[i] == 1:
                switches[i] = 0
            else:
                switches[i] = 1

for idx, val in enumerate(switches):
    if idx > 0 and idx % 20 == 0:
        print()
    print('{} '.format(val), end = '')