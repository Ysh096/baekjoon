# 20055_컨베이어벨트 위의 로봇

주어진 그대로 구현하는 문제!

시간 초과는 걱정하지 않아도 될 정도로 넉넉한 듯

잘 풀어놓고 한 가지를 잘못 이해하여 고민한 케이스다.

- 회전할 때 뿐만 아니라 로봇이 직접 움직일 때에도 로봇이 내리는 자리에 위치하면 내릴 수 있다!

이거 때문에 삼십분정도 더 쓴 것 같다. 시험이었다면 필패했을듯..

내가 푼 답안은 약간 지저분하지만 일단 올린다.

```python
import sys
sys.stdin = open('input.txt')

# 올라가는 부분 = 인덱스 0
# 내려가는 부분 = 인덱스 N-1
def rotation(As, visit):
    last = As.pop()
    v_last = visit.pop()
    As = [last] + As
    visit = [v_last] + visit
    return (As, visit)

def move(As, visit):
    global cnt
    for i in range(N-1, 0, -1):
        if visit[N - 1]:  # N에 로봇이 있으면
            visit[N - 1] = 0  # 내린다.
        if not visit[i] and As[i]: # i자리에 로봇이 없고 내구도가 남았으면
            if visit[i-1]:
                visit[i-1] = 0
                visit[i] = 1
                As[i] -= 1
                if As[i] == 0:
                    cnt += 1
    if not visit[0] and As[0]:
        visit[0] = 1 # 0 자리에 로봇 올리기
        As[0] -= 1 # 내구도 1 감소
        if As[0] == 0:
            cnt += 1
    return (As, visit)
# 로봇이 이동하려면
# 1) 이동하려는 칸에 로봇이 없으며
# 2) 그 칸의 내구도가 1 이상 남아야 한다.

N, K = map(int, input().split())
As = list(map(int, input().split()))
visit = [0] * len(As)
step = 0 # 몇 단계인지
cnt = 0 # 내구도가 다 닳은 칸의 수

while cnt < K:
    As, visit = rotation(As, visit)
    As, visit = move(As, visit)
    step += 1

print(step)
```



### 다른 사람의 답안

```python
from collections import deque
import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline
n,k = map(int,input().split())
A = deque(map(int,input().split()))
ans =1

#robot이 들어온 순서대로 현재 자신의 위치를 담고있는다
robot =deque([0]*(n*2))

while(True):
    #1
    A.rotate(1)
    robot.rotate(1)
    robot[n-1]=0 #내려가는 위치에 로봇 삭제

    #2
    for i in range(n-2,-1,-1):
        if(robot[i]!=0 and robot[i+1]==0 and A[i+1]>=1):
            A[i+1]-=1
            robot[i+1]=robot[i]
            robot[i]=0
    robot[n-1]=0

    #3
    if(robot[0]==0 and A[0]>0):
        A[0]-=1
        robot[0]=1

    #4
    cnt=0
    for i in range(len(A)):
        if(A[i]==0):
            cnt+=1

    if(cnt>=k):
        print(ans)
        break

    ans+=1

    print(A)
```

