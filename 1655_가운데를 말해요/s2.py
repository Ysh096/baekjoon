import sys
sys.stdin = open('input.txt')
import heapq

n = int(sys.stdin.readline())
left, right = [], []

for _ in range(n):
    num = int(sys.stdin.readline())

    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if right and -left[0] > right[0]:
        heapq.heappush(left, -heapq.heappop(right))
        heapq.heappush(right, -heapq.heappop(left))

    print(-left[0])