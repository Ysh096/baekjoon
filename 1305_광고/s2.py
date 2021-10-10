import sys
sys.stdin = open('input.txt')

def failure(p):
    tmp = [0] * len(p)

    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = tmp[j-1]

        if p[i] == p[j]:
            j += 1
            tmp[i] = j

    return tmp

l = int(input())
adv = input()

table = failure(adv)
print(l - table[-1])