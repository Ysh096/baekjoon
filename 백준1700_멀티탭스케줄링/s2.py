import sys
sys.stdin = open('input.txt')

T = int(input())
for T in range(1, T+1):

    N, K = input().split()
    N = int(N)
    K = int(K)
    multap = [0] * N
    li = list(map(int, input().split()))
    res = swap = num = max_I = 0

    for i in li:
        if i in multap:
            pass
        elif 0 in multap:
            multap[multap.index(0)] = i
        else:
            for j in multap:
                if j not in li[num:]:
                    swap = j
                    break
                elif li[num:].index(j) > max_I:
                    max_I = li[num:].index(j)
                    swap = j
            multap[multap.index(swap)] = i
            max_I = swap = 0
            res += 1
        num += 1
    print(res)