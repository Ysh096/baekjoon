import sys
sys.stdin = open('input.txt')

def perm(i, last, cnt):
    global result
    if result > cnt + (N-i):
        return
    if i == N:
        if cnt > result:
            result = cnt
        return

    visited[i] = 1
    if nums[i] > last:
        perm(i+1, nums[i], cnt+1)
        visited[i] = 0
        perm(i+1, last, cnt)
    else:
        perm(i+1, last, cnt)
        visited[i] = 0



N = int(input())
nums = list(map(int, input().split()))
result = 0
visited = [0]*N

perm(0, 0, 0)
print(result)