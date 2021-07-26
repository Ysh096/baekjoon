import sys
sys.stdin = open('input.txt')

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
