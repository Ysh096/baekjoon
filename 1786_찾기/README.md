# 1786 찾기(KMP)



## 내 풀이(틀림, 시간아까움)

```python
import sys
sys.stdin = open('input.txt')

# 검색 기능 구현
# 패턴 P가 텍스트 T에서 어느 위치에 몇 번 나타나는가?
def pi(pattern):
    L = len(pattern)
    array = [0] * L
    if L == 0:
        return array
    i = 0
    j = 1
    cnt = 0
    while j < L:
        if pattern[i] == pattern[j]:
            cnt += 1
            array[j] = cnt
            i += 1
            j += 1
        else:
            i = 0
            j += 1
            cnt = 0
    return array

def KMP(text, pattern):
    result = []
    array = pi(pattern)
    i = 0 # text를 돌기 위함
    j = 0 # pattern을 돌기 위함
    while i < len(text):
        if text[i] == pattern[j]:
            if j == len(pattern)-1:
                result.append(i-j+1)
                i += 1
                j = 0
                continue
            i += 1
            j += 1
        else:
            if j != 0:
                j = array[j-1]
            else:
                i += 1
    return result

T = input()
P = input()

result = KMP(T, P)
print(len(result))
print(*result)
```

반례를 못 찾겠다.



## 다른 사람 풀이

```python
import sys
sys.stdin = open('input.txt')

def makeTable(P):
    lp=len(P)
    Table=[0]*lp
    i=0
    for j in range(1,lp):
        while i>0 and P[i]!=P[j]:
            i=Table[i-1]
        if P[i]==P[j]:
            i+=1
            Table[j]=i
    return Table
def KMP(P,T):
    ans=[]
    lt=len(T)
    lp=len(P)
    table=makeTable(P)
    i=0
    for j in range(lt):
        while i>0 and P[i]!=T[j]:
            i=table[i-1]
        if P[i]==T[j]:
            if i==lp-1:
                ans.append(j-lp+2)
                i=table[i]
            else:
                i+=1
    return ans


text=input().rstrip()
pattern=input().rstrip()
ans=KMP(pattern,text)
print(len(ans))
print(*ans)
```

