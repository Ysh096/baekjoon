import sys
sys.stdin = open('input.txt')

# 유클리드 호제법으로 최대공약수 구하기
def gcd(x, y):
    '''
    x가 y보다 클 때 최대공약수 구하기
    '''
    while x % y:
        tmp_y = x % y
        x = y
        y = tmp_y
    return y
# 최소공배수 구하기
def lcm(x, y):
    return x*y // gcd(x, y)

s = input()
t = input()

if len(t) > len(s):
    s, t = t, s
LCM = (lcm(len(s), len(t)))
if s * (LCM // len(s)) == t * (LCM // len(t)):
    print(1)
else:
    print(0)