import sys
# sys.stdin = open('input.txt')

input = sys.stdin.readline
def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x != y:
        p[y] = x

n, m = map(int, input().split())

# 0 a b : 합집합해라, a 집합과 b 집합을 합친다.
# 1 a b : a와 b가 같은 집합에 포함되어 있는가?

# 1. {0}, {1}, ... {n}의 집합 만들기
p = list(range(n+1))
# 2. 하나씩 읽으며 연산 및 프린트하기
for _ in range(m):
    num, a, b = map(int, input().split())
    if num:
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)
