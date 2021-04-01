import sys
sys.stdin = open('input.txt')

# 백준 특강: 조건을 먼저 찾자.
# 1 0 2 0 1 의 경우.. 0 0 1 1 2 를 구성하는 방법의 수
# 토 고 토 고
# 토 고 고 토
# 고 토 토 고
# 고 토 고 토
# 네 가지 경우에 마지막은 토끼 or 고양이로 두 가지 경우가 있으므로 총 여덟 가지 경우가 가능
# 제한 조건 찾기
# 1) 0은 반드시 필요하다.
# 2) 동일한 숫자는 세 개 이상 나올 수 없다.
# 3) 앞선 수의 개수보다 더 많은 수는 나올 수 없다. ex) 0 1 1 불가능
# 조건 2는 맨 처음에 오는 수인 0에만 적용하면 나머지는 조건 3에 의해 걸러진다.
# 조합의 수는 같은 수가 2개인 경우에 *2, 하나인 경우에도 *2를 해주면 된다.

# 틀린 이유1: 숫자가 한 번 나오면 cnt를 하나 늘리고 break를 걸었는데, 이렇게 하면
# 0 0 1 2 3 3 같이 숫자가 한 번 나온 후 다음 동물이 두 종류가 되는 경우를 거를 수 없었다.

# 틀린 이유2
# for i in range(40):
#     if cnt_list[i + 1] > cnt_list[i]:
# 이 부분에서 range(N)을 사용했더니 틀렸다. 대답이 0에서 40까지라서 cnt_list[N]만으로는
# 틀린 경우인데도 끝까지 확인을 못 할수 있겠다는 생각이 든다.
# 예를 들어 N 범위에서는 정상적으로 cnt값이 구해지지만 N 범위 밖에 어떤 값을 가지는 경우.. 실패
N = int(input())
answers = list(map(int, input().split()))
cnt_list = [0] * 41

for answer in answers:
    cnt_list[answer] += 1

def comb(cnt_list):
    cnt = 0
    is_one_exist = False
    # 조건1, 조건2
    if cnt_list[0] == 0 or cnt_list[0] > 2:
        return 0
    for i in range(40):
        # 조건3
        if cnt_list[i+1] > cnt_list[i]:
            return 0
        # 두 마리가 대답한 경우
        if cnt_list[i] == 2:
            cnt += 1
        # 한 마리만 대답한 경우
        elif cnt_list[i] == 1:
            is_one_exist = True

    if is_one_exist:
        return cnt+1
    else:
        return cnt

ex = comb(cnt_list)
if ex == 0:
    print(0)
else:
    print(2**ex)