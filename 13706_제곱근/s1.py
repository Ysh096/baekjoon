import sys
sys.stdin = open('input.txt')

# V = int(input())
#
# def bin_search(left, right):
#     global ans
#     middle = (left + right) // 2
#     middle_square = middle ** 2
#     if middle_square == V:
#         ans = middle
#         return ans
#     elif middle_square > V:
#         bin_search(left, middle)
#     else:
#         bin_search(middle, right)
#
# left = 0
# right = V
# ans = 0
# bin_search(left, right)
# print(ans)

V = int(input())
def bin_search(left, right):
    while True:
        middle = (left + right) // 2
        if middle ** 2 == V:
            return middle
        elif middle ** 2 > V:
            right = middle
        else:
            left = middle

left = 0
right = V
print(bin_search(0, V))