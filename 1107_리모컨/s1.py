import sys
sys.stdin = open('input.txt')

# 브루트 포스
# 목적 채널의 앞자리부터 가능한지 확인
# 가능하면 해당 숫자 입력, cnt + 1
# 불가능하면 가장 가까운 숫자 입력, cnt + 1
target = input() # 문자로 받기
M = int(input()) # 고장난 버튼 개수
if M > 0:
    mal_btns = list(map(int, input().split())) # 고장난 버튼 리스트
else:
    mal_btns = []
def pos_num(i, mal_btns, target_num, num, result):
    global flag
    if int(target_num) not in mal_btns:
        num += target_num # 현재 입력한 채널
        result.append(num)
    else: # 해당 버튼이 고장난 경우
        # ex) 5가 고장 => 4 또는 6을 확인
        if int(target_num) < 9 and not flag:
            pos_num(i, mal_btns, str(int(target_num)+1), num, result)
        flag = True

        if int(target_num) > 0 and flag:
            pos_num(i, mal_btns, str(int(target_num)-1), num, result)

    return result

answer = []
sol = []
evr_btns = False
for i in range(len(target)):
    flag = False
    result = []
    if len(mal_btns) != 10:
        result = pos_num(i, mal_btns, target[i], '', result)
        if answer: # answer가 비어있지 않으면
            for j in range(len(answer)):
                for k in range(len(result)):
                    answer.append(answer[j]+result[k])
                    if len(answer[j]+result[k]) == len(target):
                        sol.append(answer[j]+result[k])
        else:
            for j in range(len(result)):
                answer.append(result[j])
                if len(target) == len(result[j]):
                    sol.append(result[j])
    else:
        evr_btns = True

sol = list(set(sol))
min_sol = 99999999
for val in sol:
    diff = abs(int(target) - int(val))
    if diff < min_sol:
        min_sol = diff
        ans_val = val

# 앞에 붙어있는 0의 개수 세기

if not evr_btns:
    if ans_val: # ans_val 이 있을 때
        cnt = 0
        for i in ans_val:
            if i == '0':
                cnt += 1
            else:
                break

        ans = min_sol + len(target) - cnt

    if ans_val == '0':
        print(1 + abs(int(target)))
    else:
        print(min(ans, abs(int(target)-100)))
else: # 모든 버튼이 고장난 경우
    print(abs(int(target) - 100))