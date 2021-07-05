from math import inf
import sys
sys.stdin = open('input.txt')
def sol(ht) :
    ht.insert(0, inf) # 맨 앞에 inf 추가
    st = [0] # 벽 역할
    res = []
    for i in range(1, len(ht)) :
        while ht[st[-1]] <= ht[i] :
            st.pop()
        res.append(st[-1]) # 답
        st.append(i)
    ht.pop(0)
    return res

n = int(input())
ht = [int(x) for x in input().split()]
res = sol(ht)
print(' '.join(str(x) for x in res))