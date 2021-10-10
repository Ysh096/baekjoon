import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
# K개의 글자를 가르칠 때, 학생들이 읽을 수 있는 단어 개수의 최댓값은?
# 0 <= K <= 26
# 1) 배워야 하는 글자의 수가 적은 단어를 찾기
# 2) 글자에는 겹치는 단어가 많은 순으로 우선순위 부여

# 처음에 최소 5개의 글자를 알아야 하므로 5개 미만으로 가르치는 경우 답은 0이다.

def teach(K):
    if K < 5:
        return 0
    else:
        pass

# 배열 미리 만들어서 배워야 하는 글자에 1을 채워넣기
alpha = [0] * 26
for val in 'antic':
    alpha[ord(val)-97] = 1
dict = {}
ans = []
for i in range(N):
    cnt = 0
    temp = list(set(list(input())))
    L = len(temp)
    learn = []
    for k in range(len(temp)):
        if not alpha[ord(temp[k])-97]: # 만약 antic에 포함된 글자면 무시하고, 포함되어 있지 않으면
            cnt += 1
            learn.append(temp[k])
            if dict.get(temp[k]):
                dict[temp[k]] += 1
            else:
                dict[temp[k]] = 1
    if cnt > K-5:
        continue
    else:

        ans.append((learn, cnt))
print(ans) # 순서대로, ([더 배워야 하는 글자들], 배워야 하는 개수)
