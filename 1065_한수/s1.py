# 각 자리의 등차수열의 개수 구하기
import sys
sys.stdin = open('input.txt')
N = int(input())
cnt = 0
# 1 <= N <= 1000
if N < 100:
    result = N
else:
    # N이 100보다 큰 경우
    for n in range(100, N+1):
        nums = []
        while n > 0:
            v, r = divmod(n, 10)
            nums.append(r)
            n = v
        flag = True
        val = nums[0] - nums[1]
        for i in range(len(nums)-1):
            if (nums[i] - nums[i+1]) != val:
                flag = False
        if flag:
            cnt += 1
    result = 99 + cnt
print(result)
