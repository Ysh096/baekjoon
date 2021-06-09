import sys
sys.stdin = open('input.txt')

def BOJ_5430():
    for _ in range(int(input())):
        p = input().replace('RR', '') # 찾을 값, 바꿀 값
        n = int(input())
        i, j, is_reverse = 0, 0, False

        for f in p:
            if f == "R":
                is_reverse = not is_reverse
            elif f == "D":
                if not is_reverse: # 뒤집어지지 않았으면 i += 1
                    i += 1
                else:
                    j += 1 # 뒤집어져 있으면 j += 1

        dq = input()[1:-1].split(',')[i:n - j]

        if i + j <= n:
            if not is_reverse:
                print('[' + ','.join(dq) + ']')
            else:
                print('[' + ','.join(dq[::-1]) + ']')
        else:
            print("error")


BOJ_5430()