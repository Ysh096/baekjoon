import sys
sys.stdin = open('input.txt')
N = int(input())
answer = [999999999 for _ in range(-1, N)]
answer[1] = 0

for i in range(2, N+1):
    val_one = 999999999
    val_two = 999999999
    val_thr = 999999999
    val_one = answer[i-1] + 1
    if i % 2 == 0:
        val_two = answer[int(i/2)] + 1
    if i % 3 == 0:
        val_thr = answer[int(i/3)] + 1
    val = min(val_one, val_two, val_thr)
    answer[i] = val
print(answer[-1])