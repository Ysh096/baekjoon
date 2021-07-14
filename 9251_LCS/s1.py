import sys
sys.stdin = open('input.txt')
string_a = ' '+input()
string_b = ' '+input()
dp = [[0] * len(string_b) for _ in range(len(string_a))]

for i in range(1, len(string_a)):
    for j in range(1, len(string_b)):
        if string_a[i] == string_b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
print(dp)
# X[i] == Y[j]일 때
# LCS(Xi, Yj) = LCS(Xi - 1, Yj - 1) + 1
#
# X[i] != Y[j]일 때
# LCS(Xi, Yj) = LCS(Xi - 1, Yj - 1)
# LCS(Xi, Yj) = max(LCS(Xi - 1, Yj), LCS(Xi, Yj - 1))

# 다시, 현재 위치에서의 문자가 같을 때
# LCS("ABCD", "AEBD") = 1 + LCS("ABC", "AEB")

# 현재 위치에서 문자가 다를 때
# LCS("ABC", "AEB") = MAX(LCS("AB", "AEB"), LCS("ABC", "AE"))
