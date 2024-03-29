# 7453 합이 0인 네 정수

풀이가 떠오르지 않아 그냥 찾아봤다.



## 다른 사람 풀이

```python
import sys
sys.stdin = open('input.txt')
number = int(sys.stdin.readline())
a_list, b_list, c_list, d_list = [], [], [], []
for _ in range(number):
    a, b, c, d = map(int,sys.stdin.readline().split())
    a_list.append(a); b_list.append(b); c_list.append(c); d_list.append(d)

a_b_dict = dict()
for a in a_list:
    for b in b_list:
        a_b_dict[a+b] = a_b_dict.get(a+b, 0) + 1

count = 0
for c in c_list:
    for d in d_list:
        count += a_b_dict.get(-(c+d),0)

print(count)
```

매우 단순하게도 가능한 a+b 조합을 다 찾아 저장한 후 c+d 조합이 -(a+b)이 되는 경우 count를 하나 해주는 식이었다. O(N^2) 으로 10000ms 정도 걸렸다.



## 가장 빠른 풀이

```python
import sys

input = sys.stdin.readline


def main(n):
    a.sort()
    b.sort()
    ab = [i + j for i in a for j in b] # 가능한 a + b의 조합
    ab.sort() # 오름차순 정렬, [-99, -95, -90, -90, -86, -83, ...]
    ab.append((1 << 29) + 2) # 최대값보다 2 큰 값을 추가?? 왜 한건지 잘 모름
    c.sort(reverse=True)
    d.sort(reverse=True)
    cd = [i + j for i in c for j in d]
    cd.sort(reverse=True) # 내림차순 정렬, [133, 119, 118, 104, 101, 87, 86, 72, ...]
    cd.append((1 << 29) + 1) # 최대값보다 1 큰 값 추가??
    i = j = 0
    k = n * n # 배열 크기의 제곱
    res = 0
    while (i < k and j < k):
        m = ab[i] + cd[j]
        if (m > 0): # ab + cd > 0 => 다음 cd값을 찾음
            j += 1
        elif (m < 0): # ab + cd < 0 => 다음 ab값을 찾음
            i += 1
        else:
            u, v = ab[i], cd[j] 
            p = i
            q = j
            while (u == ab[i]): i += 1 # 같은 수가 몇 번 나오는지 확인(인덱스 + 1로 표시)
            while (v == cd[j]): j += 1
            res += (i - p) * (j - q)
            # 5번 값이 3번 나오고, 12번 값이 4번 나왔다면 총 12개의 쌍이 만들어진다.
            # 계산: (8 - 5) * (16 - 12)

    return res


if __name__ == '__main__':
    n = int(input())
    a, b, c, d = [], [], [], []
    for _ in range(n):
        v, w, x, y = map(int, input().split())
        a.append(v)
        b.append(w)
        c.append(x)
        d.append(y)
    print(main(n))
```

