import sys
sys.stdin = open('input.txt')

# 문자열의 뒤에 A 추가
# 문자열 뒤집고 뒤에 B를 추가

S = input()
T = input()
# S -> T
# 뒤에만 추가가 가능하다는 점!
def possible(S, T):
    while True:
        if S == T:
            return 1
        elif len(S) == len(T):
            return 0
        c = T[-1]
        T = T[0:-1]
        if c == 'B':
            T = T[::-1]

print(possible(S, T))