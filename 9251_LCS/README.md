# 9251_LCS

최장공통부분수열 구하기 알고리즘



현재 위치에서의 문자가 같을 때

LCS("ABCD", "AEBD") = 1 + LCS("ABC", "AEB")

현재 위치에서 문자가 다를 때

LCS("ABC", "AEB") = MAX(LCS("AB", "AEB"), LCS("ABC", "AE"))

이를 코드로 표현한 것이 아래다.



## 정석 풀이

```python
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
```





## 가장 빠른 풀이

```python
a=input()
b=input()
T=[0]*300
row=0
X=0
al = len(a)
bl = len(b)
for i in range(al):
    T[ord(a[i])]+=(2**i) # 알파벳의 인덱스 위치에 2**i를 더함
for i in range(al):
    if(a[i]==b[0]):
        row+=(2**i)
        break
for i in range(1, bl):
    X = T[ord(b[i])]|row
    row=X&((X-(row*2+1))^X)

cnt = 0
while(row):
    cnt+=(row%2)
    row//=2

print(cnt)
```

?? 뭐하는거지

10배 빠름

