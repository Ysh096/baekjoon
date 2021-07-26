import sys
sys.stdin = open('input.txt')
input=sys.stdin.readline

N=int(input())
nodes=[[] for  i in range(N)]
for idx,p in enumerate(map(int,input().split())):
	if p==-1: continue
	nodes[p].append(idx)

rem=int(input())

def remove(rem):
	for i in nodes[rem]:
		remove(i)
	nodes[rem]=None


remove(rem)

print(sum([1 if i in([],[rem]) else 0 for i in nodes]))
