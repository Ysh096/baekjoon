import sys
import heapq
sys.stdin = open('input.txt')

heap = []
N = int(input())
subin = [int(input()) for _ in range(N)]
# 매번 sort를 하면 시간초과가 날 것 같다.

for i in range(N):
    heapq.heappush(heap, subin[i])
    heapq.heapify(heap)
    print(heap)