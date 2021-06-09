import sys
sys.stdin = open('input.txt')

N = int(input())

# N = 5x + 3y
# N//5 <= x + y <= N//3
# x = (N-3k) / 2
# y = 5k/2 - N/2
result = -1
flag = False
for k in range(N//5, (N//3)+1):
    x = (N-3*k)//2
    y = 5*k//2 - N//2
    while 0 <= x and 0<= y:
        # 만약 답이라면 5x+3y = N이 나옴
        if 5*x + 3*y == N:
            result = x+y
            flag = True
            break
        else:
            break
    if flag:
        break
print(result)
