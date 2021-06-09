import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for tc in range(T):
    n = int(sys.stdin.readline()) # 전화번호의 수
    nums = []
    for _ in range(n): # n^2번 계산하라고 낸 문제는 아님
        nums.append(sys.stdin.readline()[:-1])
    nums.sort()
    # print(nums)
    # 정렬을 하면 길이가 아니라 오로지 다음에 오는 수만 따져서 정렬
    flag = False
    for i in range(n-1):
        if nums[i] == nums[i+1][:len(nums[i])]:
            flag = True
            break
    if flag:
        print('NO')
    else:
        print('YES')

# pypy3 444ms