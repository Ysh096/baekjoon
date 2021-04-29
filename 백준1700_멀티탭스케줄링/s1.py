import sys
sys.stdin = open('input.txt')
T = int(input())
for T in range(1, T+1):

    N, K = map(int, input().split())
    elecs = list(map(int, input().split()))

    # 하나의 플러그를 빼는 최소의 횟수를 출력하시오.
    # 기기를 순서대로 읽으며 진행
    socket = [0]*N
    remains = N
    cnt = 0
    for i in range(K):
        if elecs[i] in socket:
            continue
        if remains != 0:
            for j in range(N):
                if not socket[j]:
                    socket[j] = elecs[i]
                    remains -= 1
                    break
        else: # 자리가 없는 경우
            flag = False
            for j in range(N):
                if socket[j] not in elecs[i+1:]:
                    socket[j] = elecs[i] # 바꿔 끼기
                    cnt += 1
                    flag = True
                    break
            if flag:
                continue
            for k in range(K - 1, -1, -1):
                # 콘센트에 꽂힌 기기가 모두 나중에 사용해야 되는 기기라면
                for j in range(N):
                    if socket[j] == elecs[k]:
                        socket[j] = elecs[i]
                        cnt += 1
                        flag = True
                        break

                if flag:
                    break
    print(cnt)


