# 메모리 초과
import sys
sys.stdin = open('input.txt')

N = int(input())
k = int(input())
# 인덱스 1부터 시작
# 1~N까지
B = []
for i in range(1, N+1):
    for j in range(1, N+1):
      B.append(i*j)
B.sort()
print(B[k])
