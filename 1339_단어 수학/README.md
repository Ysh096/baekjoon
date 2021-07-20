# 1339 단어 수학

정렬까지는 생각함

어떻게 해야할지 몰라서 찾아봄

아이디어를 얻고 나서 풀어봄



각 문자가 10^n 자리에 있음을 이용하여 문자의 자릿수 합이 가장 큰 것부터 9, 8, 7, ... 순서대로 할당하는 방법

```python
N = int(input())
dict = {}
for _ in range(N):
    word = input()
    word_len = len(word)
    for i in range(word_len):
        j = word_len-i-1
        if dict.get(word[i]):
            dict[word[i]] += 10**j
        else:
            dict[word[i]] = 10**j
arr = []
for key, val in dict.items():
    arr.append((key, val))
arr.sort(key=lambda x: -x[1])

result = 0
for k in range(len(arr)):
    result += arr[k][1] * (9-k)

print(result)
```

딕셔너리로 자릿수 덧셈 -> 배열로 나타내기 -> 정렬하기 -> 정렬한 순서대로 값 매기기

좀 과정이 길어졌음

72ms



## 가장 빠른 풀이

```python
n=int(input())
w,r,s=[0]*26,0,9 # w = [0]*26,   r=0,  s=9
for i in range(n):
	ii=input()
	for i in range(len(ii)):
		w[ord(ii[i])-ord('A')]+=10**(len(ii)-i-1)
w.sort(reverse=True)
for i in w:
	r,s=r+i*s,s-1
print(r)
```

같은 방법인데 ord와 미리 만들어놓은 배열을 이용하여 시간 단축 (56ms)