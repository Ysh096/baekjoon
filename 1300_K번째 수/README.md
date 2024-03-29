## 1300_K번째 수

못 풀어서 다른 사람 풀이 가져왔습니다.

```python
import sys
sys.stdin = open('input.txt')
N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2 # mid로 K번째 위치의 값을 찾아나감
    tmp = 0
    for i in range(1, N+1) :
        # 각 행별로 mid보다 작은 값의 개수를 구해서 더함
        tmp += min(mid // i, N) # 최대 N개
    if tmp >= K: # tmp가 목표 위치보다 크거나 같으면
        ans = mid # 일단 답을 mid로 저장하고
        end = mid - 1 # 오른쪽 범위를 줄여서 start > end가 될 때 까지 루프
    else:
        start = mid + 1 # tmp가 목표 위치에 도달하지 못했으면
        # mid라는 숫자는 K번째보다 앞에 있으므로 mid+1 숫자값부터 다시 확인한다.
print(ans)
```

도대체 어떻게 푸는 건가 고민을 많이 해봤는데 모르겠어서 다른 사람 답을 봤다.

내 생각과는 반대로 푸는 문제였다. K번째 위치에 어떤 값이 있는지 찾는 것이 아니라, 중심값 mid(시작점과 끝점의 중심점)을 정해두고 그 값보다 작거나 같은 숫자의 개수를 세서, 그 수가 K값보다 작으면 K번째 까지는  mid보다 작은 숫자만 나타난다는 소리기 때문에 이분법으로 탐색하는 범위를 mid+1에서 K까지로 바꿔주고, K값보다 큰 값이 나오면 탐색 범위를 start에서 mid+1 까지로 한정시키는 방법이었다.

과정을 적어보면 다음과 같다.

```
# N = 3, K = 7 인 경우
mid = (1 + K) // 2  <= 답은 K이하임, K를 지난 위치에 K보다 큰 값이 올 수 없음
# mid값은 위치를 나타내는게 아니라 값(value)을 나타낸다.

1) start = 1, end = 7, mid = 4
# 행별 i*j 값                      누적
1 2 3  => min(mid // 1, 3) = 3     3
2 4 6  => min(mid // 2, 3) = 2     5
3 6 9  => min(mid // 3, 3) = 1     6

따라서 4 이하의(4 포함임에 주의) 숫자 개수는 6개이고, 7번째 숫자가 무엇인지 알 수 없으므로
start를 바꾼다.
								  누적
2) start = 5, end = 7, mid = 6
1 2 3  => min(mid // 1, 3) = 3     3
2 4 6  => min(mid // 2, 3) = 3     6
3 6 9  => min(mid // 3, 3) = 2     8

ans = 6 으로 일단 저장

따라서 6 이하의 숫자 개수는 8개이고, 7번째 숫자가 무엇인지 아직 알 수 없지만 7보다 숫자 개수가 더 크므로 end를 하나 줄여 범위를 줄인다.

3) start = 5, end = 6, mid = 5
1 2 3  => min(mid // 1, 3) = 3     3
2 4 6  => min(mid // 2, 3) = 2     5
3 6 9  => min(mid // 3, 3) = 1     6

이제 5 이하의 숫자 개수는 6이고, 7번째 숫자가 무엇인지는 알 수 없으므로 start를 바꾼다.

4) start = 6, end = 6, mid = 6
1 2 3  => min(mid // 1, 3) = 3     3
2 4 6  => min(mid // 2, 3) = 3     6
3 6 9  => min(mid // 3, 3) = 2     8

ans = 6 으로 일단 저장
이제 6 이하의 숫자 개수는 8이고, 7보다 숫자 개수가 더 크므로 end를 하나 줄여 범위를 줄인다.

5) start = 6, end = 5, mid = 5
=> while문 종료, ans = 6
```



