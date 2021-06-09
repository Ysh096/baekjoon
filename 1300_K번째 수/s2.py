import sys
sys.stdin = open('input.txt')
N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2 # mid로 K번째 위치의 값을 찾아나감
    tmp = 0
    for i in range(1, N+1) :
        # 각 행별로 mid보다 작은 값의 개수를 구해서 더함
        tmp += min(mid // i, N) # 최대 N개
    if tmp >= K: # tmp가 목표 위치보다 크거나 같으면
        ans = mid # 일단 답을 mid로 저장하고
        end = mid - 1 # 오른쪽 범위를 줄여서 start > end가 될 때 까지 루프
    else:
        start = mid + 1 # tmp가 목표 위치에 도달하지 못했으면
        # mid라는 숫자는 K번째보다 앞에 있으므로 mid+1 숫자값부터 다시 확인한다.
print(ans)