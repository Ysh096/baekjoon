# 암호는 L개의 알파벳 소문자들로 구성
# 최소 한 개의 모음(a, e, i, o u)과 최소 두 개의 자음으로 구성
# 암호는 알파벳 순서대로 구성됨
# C개의 문자들이 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램
import sys
from itertools import combinations
sys.stdin = open('input.txt')

L, C = map(int, input().split())
chars = list(input().split())
consonants = []
vowels = []
for i in range(C):
    if chars[i] in 'aeiou':
        vowels.append(chars[i])
    else:
        consonants.append(chars[i])
total_vowels = len(vowels)
total_consonants = len(consonants)
# 이제 모음에서 하나를, 자음에서 두 개를 뽑는다.
vs = list(combinations(vowels, 1))
cs = list(combinations(consonants, 2))
remains_cnt = L-3 # 남은 뽑을 개수
answer = []
# 삼중 for문..
for v in vs:
    for c in cs:
        remains = []
        for k in range(C):
            if chars[k] not in v+c: # 이미 뽑은 문자가 아니라면
                remains.append(chars[k]) # 골라줄 문자를 따로 모아줌
        rs = list(combinations(remains, remains_cnt))
        for r in rs:
            result = v+c+r # 가능한 조합 만들기
            result = sorted(list(result)) # 정렬
            result = ''.join(result)
            answer.append(result)
answer = sorted(list(set(answer)))
for ans in answer:
    print(ans)

