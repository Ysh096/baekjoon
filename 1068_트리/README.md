# 1068 트리



## 1. 내 풀이1(78%에서 틀림)

```python
N = int(input()) # 노드의 개수 N <= 50
data = list(map(int, input().split()))
tree = []
for i in range(N):
    tree.append([data[i]])
target = int(input())

for i in range(N):
    if data[i] != -1:
        tree[data[i]].append(i)

def dfs(target):
    while len(tree[target]) > 1:
        c = tree[target].pop() # 자식노드
        dfs(c)
    tree[target] = -2

dfs(target)

cnt = 0
removed = 0
for i in range(N):
    if type(tree[i]) != int:
        if len(tree[i]) == 1:
            cnt += 1
    else:
        removed += 1

if target != 0 and N-removed == 1:
    print(1)
else:
    print(cnt)
```



## 2. 내 풀이2

```python
N = int(input()) # 노드의 개수 N <= 50
data = list(map(int, input().split()))
tree = []
for i in range(N):
    tree.append([data[i]])
target = int(input())

for i in range(N):
    if data[i] != -1:
        tree[data[i]].append(i)

def dfs(target):
    if type(tree[target]) != int:
        while len(tree[target]) > 1:
            c = tree[target].pop() # 자식노드
            dfs(c)
        tree[target] = -2
# target의 부모 노드에서 찾은 자식 노드로서의 target 위치
if tree[target][0] != -1:
    tree[tree[target][0]].remove(target)
dfs(target)

cnt = 0
removed = 0
for i in range(N):
    if type(tree[i]) != int:
        if len(tree[i]) == 1:
            cnt += 1
    else:
        removed += 1

if target != 0 and N-removed == 1:
    print(1)
else:
    print(cnt)
```

타겟의 자식 노드는 모두 삭제했지만 정작 타겟은 삭제하지 않았음.

부모 노드가 있는 경우 부모 노드를 찾아가 자식 노드로 연결되어 있는 타겟을 제거하고

제거되지 않은(-2가 대입되지 않은) 노드를 찾아 개수를 센다.



## 3. 가장 빠른 풀이

```python
'''input
7
5 0 0 1 -1 4 4 // 4번 노드가 root, 5번, 6번 노드는 4번 노드의 자식
0
'''
import sys
input=sys.stdin.readline

N=int(input())
nodes=[[] for  i in range(N)]
for idx,p in enumerate(map(int,input().split())):
	if p==-1: continue
	nodes[p].append(idx)
# nodes 결과: [[1, 2], [3], [], [], [5, 6], [0], []]
rem=int(input()) # 제거 대상

def remove(rem):
	for i in nodes[rem]:
		remove(i)
	nodes[rem]=None
# nodes 결과: [None, None, None, None, [5, 6], [0], []]

remove(rem)

print(sum([1 if i in([],[rem]) else 0 for i in nodes]))
# nodes의 각 값이 [] 이나 [rem] 이면, 즉 자식 노드가 없거나 자식 노드가 타겟이면 1
# 결과: sum([0, 0, 0, 0, 0, 1, 1])
```

