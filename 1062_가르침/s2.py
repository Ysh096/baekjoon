import sys
import itertools
sys.stdin = open('input.txt')
# n, m 입력
n, m = map(int, sys.stdin.readline().split())

# words : 각 단어의 비트마스킹한 정수를 저장
words = [0] * n
ans = 0
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    # word 배열에 단어를 저장할 것, 단어가 총 세 개라면 word 배열에는 세 개의 단어가 저장됨
    # word 배열의 각 단어는 단어의 알파벳을 비트 형태로 저장한 결과로, 다음과 같다.
    # 만약 a라면 첫 번째 위치를 1로 바꿈(1)
    # 만약 b라면 두 번째 위치를 1로 바꿈(10)
    # 만약 c라면 세 번째 위치를 1로 바꿈(100)
    # ex) antarctica => 1, 8192(2의 13승, 14번째 위치), 524288(2의 19승, 20번째 위치), ...
    # 이미 그 위치가 1이라면 1로 그대로 유지, 따라서 같은 글자라면 words 원소의 값이 변화하지 않음
    for x in temp:
        words[i] |= (1 << (ord(x) - ord('a')))
    # 이제 words[i]에는 i번째 단어를 비트로 표현한 값이 들어있게 된다.

# 만일 m이 5미만이면 필수 글자를 다 배울 수 없기 때문에 한 단어도 읽지 못한다
if m < 5:
    print(0)
else:
    # candidiate : 필수 글자를 제외한 알파벳
    # need : 필수 알파벳
    candidiate = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y',
                  'z']
    need = ['a', 'c', 't', 'i', 'n']
    for i in list(itertools.combinations(candidiate, m - 5)): # 배울 수 있는 글자에서 필수 다섯 개를 제외한 모든 가능한 배움 조합
        each = 0
        res = 0
        # 각 조합에 대한 비트마스킹
        for j in need:
            each |= (1 << (ord(j) - ord('a'))) # 필수 글자를 비트로 표현한 것
        for j in i:
            each |= (1 << (ord(j) - ord('a'))) # 각 조합을 비트로 표현한 것

        # 단어와 각 조합의 비교
        for j in words: # 각 단어에 대해
            if each & j == j: # 단어 j와 each의 비트가 모두 일치하면
                res += 1 # 결과에 하나 추가

        # 최대값 갱신
        if ans < res:
            ans = res
    print(ans)